"""
Module de sécurité pour MCP DSFR.
Validation, sanitization et protection contre les attaques.
"""

import re
import html
from typing import Dict, Any, Optional, List
from dataclasses import dataclass
from datetime import datetime, timedelta
import bleach
from pydantic import BaseModel, Field, validator
import hashlib
import secrets


class SecurityConfig:
    """Configuration de sécurité centralisée."""
    
    # HTML Sanitization
    ALLOWED_TAGS = [
        'div', 'span', 'p', 'a', 'button', 'input', 'label', 'form',
        'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
        'ul', 'ol', 'li', 'nav', 'header', 'footer', 'main', 'article',
        'section', 'aside', 'figure', 'figcaption', 'img', 'svg',
        'table', 'thead', 'tbody', 'tr', 'td', 'th',
        'select', 'option', 'textarea', 'fieldset', 'legend',
        'strong', 'em', 'code', 'pre', 'blockquote'
    ]
    
    ALLOWED_ATTRIBUTES = {
        '*': ['class', 'id', 'data-*', 'aria-*', 'role'],
        'a': ['href', 'title', 'target', 'rel'],
        'img': ['src', 'alt', 'width', 'height'],
        'input': ['type', 'name', 'value', 'placeholder', 'required', 'disabled'],
        'button': ['type', 'disabled'],
        'form': ['action', 'method'],
        'label': ['for'],
        'select': ['name', 'required', 'multiple'],
        'option': ['value', 'selected'],
        'textarea': ['name', 'rows', 'cols', 'placeholder']
    }
    
    # Tailles maximales
    MAX_HTML_SIZE = 1_000_000  # 1MB
    MAX_STRING_LENGTH = 10_000
    MAX_ARRAY_SIZE = 1000
    
    # Rate limiting
    RATE_LIMIT_WINDOW = 60  # secondes
    RATE_LIMIT_MAX_REQUESTS = 60


@dataclass
class RateLimitEntry:
    """Entrée de rate limiting."""
    count: int
    window_start: datetime
    

class InputValidator:
    """
    Validateur d'entrées pour prévenir les injections.
    Utilise Pydantic pour validation stricte.
    """
    
    class ComponentRequest(BaseModel):
        """Modèle pour requête de génération de composant."""
        component: str = Field(..., min_length=1, max_length=50, regex=r'^[a-z_]+$')
        variant: Optional[str] = Field(None, max_length=50, regex=r'^[a-z_-]+$')
        options: Optional[Dict[str, Any]] = Field(default_factory=dict)
        
        @validator('options')
        def validate_options(cls, v):
            """Valide les options."""
            if len(str(v)) > SecurityConfig.MAX_STRING_LENGTH:
                raise ValueError("Options trop volumineuses")
            return v
    
    class HTMLInput(BaseModel):
        """Modèle pour HTML à valider."""
        html: str = Field(..., min_length=1, max_length=SecurityConfig.MAX_HTML_SIZE)
        component_type: Optional[str] = Field(None, max_length=50)
        
        @validator('html')
        def validate_html_safety(cls, v):
            """Vérifie la sécurité basique du HTML."""
            # Détection de scripts malveillants
            dangerous_patterns = [
                r'<script[^>]*>.*?</script>',
                r'javascript:',
                r'on\w+\s*=',  # Event handlers
                r'data:text/html',
                r'vbscript:',
                r'<iframe',
                r'<object',
                r'<embed'
            ]
            
            for pattern in dangerous_patterns:
                if re.search(pattern, v, re.IGNORECASE):
                    raise ValueError(f"HTML contient du contenu potentiellement dangereux: {pattern}")
            
            return v
    
    @classmethod
    def validate_component_request(cls, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Valide une requête de génération de composant.
        
        Args:
            data: Données à valider
            
        Returns:
            Données validées et nettoyées
            
        Raises:
            ValueError: Si validation échoue
        """
        request = cls.ComponentRequest(**data)
        return request.dict()
    
    @classmethod
    def validate_html_input(cls, html: str, component_type: Optional[str] = None) -> str:
        """
        Valide et nettoie du HTML.
        
        Args:
            html: HTML à valider
            component_type: Type de composant optionnel
            
        Returns:
            HTML validé
            
        Raises:
            ValueError: Si HTML dangereux
        """
        input_model = cls.HTMLInput(html=html, component_type=component_type)
        return input_model.html


class HTMLSanitizer:
    """
    Sanitizer HTML pour nettoyer le contenu dangereux.
    Préserve les classes DSFR.
    """
    
    @staticmethod
    def sanitize(html_content: str, 
                 preserve_dsfr: bool = True,
                 custom_allowed_tags: Optional[List[str]] = None) -> str:
        """
        Nettoie le HTML en préservant les structures DSFR.
        
        Args:
            html_content: HTML à nettoyer
            preserve_dsfr: Préserver les classes fr-*
            custom_allowed_tags: Tags additionnels autorisés
            
        Returns:
            HTML nettoyé et sécurisé
        """
        # Tags autorisés
        allowed_tags = SecurityConfig.ALLOWED_TAGS.copy()
        if custom_allowed_tags:
            allowed_tags.extend(custom_allowed_tags)
        
        # Attributs autorisés
        allowed_attributes = SecurityConfig.ALLOWED_ATTRIBUTES.copy()
        
        # Préserver les classes DSFR
        if preserve_dsfr:
            def filter_dsfr_classes(tag, name, value):
                """Filtre pour préserver les classes DSFR."""
                if name == 'class':
                    # Garder seulement les classes fr-*
                    classes = value.split()
                    dsfr_classes = [c for c in classes if c.startswith('fr-')]
                    return ' '.join(dsfr_classes) if dsfr_classes else None
                return value
            
            # Nettoyer avec Bleach
            cleaned = bleach.clean(
                html_content,
                tags=allowed_tags,
                attributes=allowed_attributes,
                strip=True,
                strip_comments=True
            )
            
            # Appliquer le filtre DSFR
            # Note: Bleach ne supporte pas directement les filtres custom,
            # donc on fait un post-processing
            if preserve_dsfr:
                # Garder seulement les classes fr-*
                cleaned = re.sub(
                    r'class="([^"]*)"',
                    lambda m: f'class="{" ".join([c for c in m.group(1).split() if c.startswith("fr-")])}"',
                    cleaned
                )
        else:
            cleaned = bleach.clean(
                html_content,
                tags=allowed_tags,
                attributes=allowed_attributes,
                strip=True,
                strip_comments=True
            )
        
        return cleaned
    
    @staticmethod
    def escape_user_content(content: str) -> str:
        """
        Échappe le contenu utilisateur pour affichage sûr.
        
        Args:
            content: Contenu à échapper
            
        Returns:
            Contenu échappé
        """
        return html.escape(content, quote=True)


class RateLimiter:
    """
    Rate limiter simple pour prévenir les abus.
    """
    
    def __init__(self, 
                 max_requests: int = SecurityConfig.RATE_LIMIT_MAX_REQUESTS,
                 window_seconds: int = SecurityConfig.RATE_LIMIT_WINDOW):
        """
        Initialise le rate limiter.
        
        Args:
            max_requests: Nombre max de requêtes par fenêtre
            window_seconds: Taille de la fenêtre en secondes
        """
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.clients: Dict[str, RateLimitEntry] = {}
    
    def check_rate_limit(self, client_id: str) -> bool:
        """
        Vérifie si le client a dépassé la limite.
        
        Args:
            client_id: Identifiant du client
            
        Returns:
            True si dans les limites, False sinon
        """
        now = datetime.now()
        
        if client_id not in self.clients:
            self.clients[client_id] = RateLimitEntry(count=1, window_start=now)
            return True
        
        entry = self.clients[client_id]
        
        # Vérifier si nouvelle fenêtre
        if (now - entry.window_start).total_seconds() > self.window_seconds:
            entry.count = 1
            entry.window_start = now
            return True
        
        # Incrémenter et vérifier limite
        entry.count += 1
        return entry.count <= self.max_requests
    
    def get_client_id(self, request_data: Dict[str, Any]) -> str:
        """
        Génère un ID client depuis les données de requête.
        
        Args:
            request_data: Données de la requête
            
        Returns:
            ID client hashé
        """
        # Créer un hash depuis les données pertinentes
        # En production, utiliser IP + User-Agent + Session
        data_str = str(request_data)
        return hashlib.sha256(data_str.encode()).hexdigest()[:16]


class CSRFProtection:
    """
    Protection CSRF pour formulaires.
    """
    
    @staticmethod
    def generate_token() -> str:
        """
        Génère un token CSRF sécurisé.
        
        Returns:
            Token CSRF
        """
        return secrets.token_urlsafe(32)
    
    @staticmethod
    def validate_token(token: str, expected: str) -> bool:
        """
        Valide un token CSRF.
        
        Args:
            token: Token reçu
            expected: Token attendu
            
        Returns:
            True si valide
        """
        return secrets.compare_digest(token, expected)
    
    @staticmethod
    def add_csrf_field(html: str, token: str) -> str:
        """
        Ajoute un champ CSRF à un formulaire HTML.
        
        Args:
            html: HTML du formulaire
            token: Token CSRF
            
        Returns:
            HTML avec champ CSRF
        """
        csrf_field = f'<input type="hidden" name="csrf_token" value="{token}">'
        
        # Insérer après <form>
        return re.sub(
            r'(<form[^>]*>)',
            rf'\1\n{csrf_field}',
            html,
            count=1
        )


# Instance globale du rate limiter
rate_limiter = RateLimiter()

# Fonctions utilitaires exportées
def validate_and_sanitize_html(html: str, 
                              component_type: Optional[str] = None) -> str:
    """
    Valide et nettoie du HTML en une seule opération.
    
    Args:
        html: HTML à traiter
        component_type: Type de composant
        
    Returns:
        HTML validé et nettoyé
        
    Raises:
        ValueError: Si HTML invalide ou dangereux
    """
    # Valider
    validated = InputValidator.validate_html_input(html, component_type)
    
    # Sanitizer
    sanitized = HTMLSanitizer.sanitize(validated, preserve_dsfr=True)
    
    return sanitized


def check_request_safety(request_data: Dict[str, Any], 
                         client_id: Optional[str] = None) -> bool:
    """
    Vérifie la sécurité globale d'une requête.
    
    Args:
        request_data: Données de la requête
        client_id: ID du client (optionnel)
        
    Returns:
        True si requête sûre
    """
    # Rate limiting
    if client_id:
        if not rate_limiter.check_rate_limit(client_id):
            return False
    
    # Taille de requête
    if len(str(request_data)) > SecurityConfig.MAX_STRING_LENGTH * 10:
        return False
    
    return True