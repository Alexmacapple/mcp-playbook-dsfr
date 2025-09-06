"""
Module de sécurité simplifié pour MCP DSFR.
Validation et sanitization des entrées HTML.
"""

import re
import html
from typing import Dict, Any, Optional, List
import bleach


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


class InputValidator:
    """
    Validateur d'entrées pour prévenir les injections.
    Version simplifiée sans Pydantic.
    """
    
    @staticmethod
    def validate_component_name(component: str) -> str:
        """
        Valide un nom de composant.
        
        Args:
            component: Nom du composant
            
        Returns:
            Nom validé
            
        Raises:
            ValueError: Si nom invalide
        """
        if not component:
            raise ValueError("Component name is required")
        
        if len(component) > 50:
            raise ValueError("Component name too long")
        
        if not re.match(r'^[a-z_]+$', component):
            raise ValueError("Invalid component name format")
        
        return component
    
    @staticmethod
    def validate_variant(variant: Optional[str]) -> Optional[str]:
        """
        Valide une variante de composant.
        
        Args:
            variant: Nom de la variante
            
        Returns:
            Variante validée ou None
            
        Raises:
            ValueError: Si variante invalide
        """
        if not variant:
            return None
        
        if len(variant) > 50:
            raise ValueError("Variant name too long")
        
        if not re.match(r'^[a-z_-]+$', variant):
            raise ValueError("Invalid variant format")
        
        return variant
    
    @staticmethod
    def validate_html_input(html: str) -> str:
        """
        Valide du HTML pour sécurité basique.
        
        Args:
            html: HTML à valider
            
        Returns:
            HTML validé
            
        Raises:
            ValueError: Si HTML dangereux
        """
        if not html:
            raise ValueError("HTML content is required")
        
        if len(html) > SecurityConfig.MAX_HTML_SIZE:
            raise ValueError("HTML content too large")
        
        # Détection de patterns dangereux
        dangerous_patterns = [
            r'<script[^>]*>.*?</script>',
            r'javascript:',
            r'on\w+\s*=',  # Event handlers
            r'data:text/html',
            r'vbscript:'
        ]
        
        for pattern in dangerous_patterns:
            if re.search(pattern, html, re.IGNORECASE):
                raise ValueError(f"HTML contains potentially dangerous content")
        
        return html


class HTMLSanitizer:
    """
    Sanitizer HTML pour nettoyer le contenu dangereux.
    Préserve les classes DSFR.
    """
    
    @staticmethod
    def sanitize(html_content: str, preserve_dsfr: bool = True) -> str:
        """
        Nettoie le HTML en préservant les structures DSFR.
        
        Args:
            html_content: HTML à nettoyer
            preserve_dsfr: Préserver les classes fr-*
            
        Returns:
            HTML nettoyé et sécurisé
        """
        # Nettoyer avec Bleach
        cleaned = bleach.clean(
            html_content,
            tags=SecurityConfig.ALLOWED_TAGS,
            attributes=SecurityConfig.ALLOWED_ATTRIBUTES,
            strip=True,
            strip_comments=True
        )
        
        # Préserver les classes DSFR si demandé
        if preserve_dsfr:
            # Garder seulement les classes fr-*
            cleaned = re.sub(
                r'class="([^"]*)"',
                lambda m: f'class="{" ".join([c for c in m.group(1).split() if c.startswith("fr-")])}"',
                cleaned
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


# Fonctions utilitaires exportées
def validate_and_sanitize_html(html: str, preserve_dsfr: bool = True) -> str:
    """
    Valide et nettoie du HTML en une seule opération.
    
    Args:
        html: HTML à traiter
        preserve_dsfr: Préserver les classes DSFR
        
    Returns:
        HTML validé et nettoyé
        
    Raises:
        ValueError: Si HTML invalide ou dangereux
    """
    # Valider
    validated = InputValidator.validate_html_input(html)
    
    # Sanitizer
    sanitized = HTMLSanitizer.sanitize(validated, preserve_dsfr)
    
    return sanitized


def validate_component_request(component: str, 
                              variant: Optional[str] = None,
                              options: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Valide une requête de génération de composant.
    
    Args:
        component: Nom du composant
        variant: Variante optionnelle
        options: Options du composant
        
    Returns:
        Données validées
        
    Raises:
        ValueError: Si données invalides
    """
    # Valider le nom du composant
    component = InputValidator.validate_component_name(component)
    
    # Valider la variante si présente
    variant = InputValidator.validate_variant(variant)
    
    # Valider les options (limite de taille)
    if options and len(str(options)) > SecurityConfig.MAX_STRING_LENGTH:
        raise ValueError("Options too large")
    
    return {
        'component': component,
        'variant': variant,
        'options': options or {}
    }