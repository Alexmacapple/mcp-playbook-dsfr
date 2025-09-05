"""
Erreurs spécifiques aux composants DSFR.
Chaque erreur a une responsabilité unique (S de SOLID).
"""

from typing import List, Optional, Any
from .base import DSFRError


class ComponentNotFoundError(DSFRError):
    """Erreur levée quand un composant n'existe pas."""
    
    def __init__(self, component: str, available: Optional[List[str]] = None):
        """
        Initialise l'erreur composant non trouvé.
        
        Args:
            component: Nom du composant recherché
            available: Liste des composants disponibles (optionnel)
        """
        message = f"Component '{component}' not found"
        if available:
            # Limite à 5 suggestions pour garder le message lisible (KISS)
            suggestions = available[:5]
            message += f". Available: {', '.join(suggestions)}"
            if len(available) > 5:
                message += f" (and {len(available) - 5} more)"
        
        super().__init__(
            message=message,
            code='COMPONENT_NOT_FOUND',
            details={
                'component': component,
                'available': available or []
            }
        )


class InvalidVariantError(DSFRError):
    """Erreur levée quand une variante n'est pas valide."""
    
    def __init__(self, component: str, variant: str, valid_variants: Optional[List[str]] = None):
        """
        Initialise l'erreur de variante invalide.
        
        Args:
            component: Nom du composant
            variant: Variante demandée
            valid_variants: Variantes valides (optionnel)
        """
        message = f"Invalid variant '{variant}' for component '{component}'"
        if valid_variants:
            message += f". Valid variants: {', '.join(valid_variants)}"
        
        super().__init__(
            message=message,
            code='INVALID_VARIANT',
            details={
                'component': component,
                'variant': variant,
                'valid_variants': valid_variants or []
            }
        )


class MissingPropertyError(DSFRError):
    """Erreur levée quand une propriété requise est manquante."""
    
    def __init__(self, component: str, missing_properties: List[str]):
        """
        Initialise l'erreur de propriété manquante.
        
        Args:
            component: Nom du composant
            missing_properties: Liste des propriétés manquantes
        """
        props_str = ', '.join(missing_properties)
        message = f"Missing required properties for component '{component}': {props_str}"
        
        super().__init__(
            message=message,
            code='MISSING_PROPERTY',
            details={
                'component': component,
                'missing_properties': missing_properties
            }
        )


class InvalidPropertyError(DSFRError):
    """Erreur levée quand une propriété a une valeur invalide."""
    
    def __init__(self, component: str, property_name: str, 
                 invalid_value: Any, expected_type: Optional[str] = None):
        """
        Initialise l'erreur de propriété invalide.
        
        Args:
            component: Nom du composant
            property_name: Nom de la propriété
            invalid_value: Valeur invalide fournie
            expected_type: Type attendu (optionnel)
        """
        message = f"Invalid value for property '{property_name}' in component '{component}'"
        if expected_type:
            message += f". Expected {expected_type}, got {type(invalid_value).__name__}"
        
        super().__init__(
            message=message,
            code='INVALID_PROPERTY',
            details={
                'component': component,
                'property': property_name,
                'invalid_value': str(invalid_value),
                'expected_type': expected_type
            }
        )