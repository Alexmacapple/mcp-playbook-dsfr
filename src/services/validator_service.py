"""
Service de validation DSFR et RGAA.
Responsabilité unique : valider la conformité (S de SOLID).
"""

import re
from typing import Dict, List, Any, Optional, Tuple
from src.errors.validation import ValidationError, RGAAViolationError, HTMLParseError, CSSClassError


class ValidatorService:
    """
    Service de validation pour les composants DSFR.
    
    Vérifie :
    - Conformité HTML
    - Classes CSS DSFR
    - Accessibilité RGAA
    """
    
    def __init__(self):
        """Initialise le validateur avec les règles de base."""
        self.required_classes = {
            'button': ['fr-btn'],
            'alert': ['fr-alert'],
            'card': ['fr-card'],
            'input': ['fr-input'],
            'modal': ['fr-modal']
        }
        
        self.aria_requirements = {
            'button': ['aria-label', 'aria-labelledby'],  # Au moins un
            'modal': ['aria-modal', 'role'],
            'accordion': ['aria-expanded', 'aria-controls']
        }
    
    def validate(self, html: str, component_type: Optional[str] = None) -> Dict[str, Any]:
        """
        Valide un composant HTML.
        
        Args:
            html: HTML à valider
            component_type: Type de composant (pour validation spécifique)
            
        Returns:
            Dictionnaire avec valid, errors, warnings
        """
        errors = []
        warnings = []
        
        # 1. Validation HTML basique
        html_errors = self._validate_html_structure(html)
        errors.extend(html_errors)
        
        # 2. Validation classes CSS si type connu
        if component_type:
            css_errors = self._validate_css_classes(html, component_type)
            errors.extend(css_errors)
        
        # 3. Validation RGAA
        rgaa_violations = self._validate_rgaa(html, component_type)
        if rgaa_violations:
            warnings.extend(rgaa_violations)
        
        return {
            'valid': len(errors) == 0,
            'errors': errors,
            'warnings': warnings,
            'score': self._calculate_score(errors, warnings)
        }
    
    def _validate_html_structure(self, html: str) -> List[str]:
        """Valide la structure HTML basique."""
        errors = []
        
        # Vérifier les balises fermées
        open_tags = re.findall(r'<([a-z]+)[^>]*>', html, re.IGNORECASE)
        close_tags = re.findall(r'</([a-z]+)>', html, re.IGNORECASE)
        
        # Ignorer les balises auto-fermantes
        self_closing = ['img', 'input', 'br', 'hr', 'meta', 'link']
        open_tags = [t for t in open_tags if t.lower() not in self_closing]
        
        if len(open_tags) != len(close_tags):
            errors.append("Balises non équilibrées")
        
        return errors
    
    def _validate_css_classes(self, html: str, component_type: str) -> List[str]:
        """Vérifie les classes CSS requises."""
        errors = []
        
        if component_type in self.required_classes:
            for required_class in self.required_classes[component_type]:
                if required_class not in html:
                    errors.append(f"Classe CSS manquante: {required_class}")
        
        return errors
    
    def _validate_rgaa(self, html: str, component_type: Optional[str]) -> List[str]:
        """Valide l'accessibilité RGAA."""
        warnings = []
        
        # Vérifier les images sans alt
        if '<img' in html and 'alt=' not in html:
            warnings.append("Image sans attribut alt (RGAA 1.1)")
        
        # Vérifier les labels pour les inputs
        if '<input' in html:
            inputs = re.findall(r'<input[^>]*id="([^"]+)"', html)
            labels = re.findall(r'<label[^>]*for="([^"]+)"', html)
            
            for input_id in inputs:
                if input_id not in labels:
                    warnings.append(f"Input sans label associé: {input_id} (RGAA 11.1)")
        
        # Vérifier ARIA si type connu
        if component_type and component_type in self.aria_requirements:
            for aria_attr in self.aria_requirements[component_type]:
                if aria_attr not in html:
                    warnings.append(f"Attribut ARIA recommandé manquant: {aria_attr}")
        
        return warnings
    
    def _calculate_score(self, errors: List[str], warnings: List[str]) -> float:
        """
        Calcule un score de conformité.
        
        Returns:
            Score entre 0 et 100
        """
        if errors:
            return max(0, 50 - len(errors) * 10)
        elif warnings:
            return max(70, 100 - len(warnings) * 5)
        else:
            return 100.0


# Singleton
_validator_instance: Optional[ValidatorService] = None

def get_validator() -> ValidatorService:
    """Récupère l'instance unique du validateur."""
    global _validator_instance
    if _validator_instance is None:
        _validator_instance = ValidatorService()
    return _validator_instance