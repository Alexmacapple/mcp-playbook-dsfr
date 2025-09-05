"""
Erreurs de validation HTML et RGAA.
Séparation des responsabilités: validation syntaxique vs accessibilité.
"""

from typing import List, Dict, Any
from .base import DSFRError


class ValidationError(DSFRError):
    """Erreur générique de validation."""
    
    def __init__(self, message: str, errors: List[str]):
        """
        Initialise l'erreur de validation.
        
        Args:
            message: Message principal
            errors: Liste des erreurs détectées
        """
        super().__init__(
            message=message,
            code='VALIDATION_ERROR',
            details={
                'errors': errors,
                'error_count': len(errors)
            }
        )


class RGAAViolationError(DSFRError):
    """Erreur de non-conformité RGAA (accessibilité)."""
    
    def __init__(self, violations: List[Dict[str, Any]]):
        """
        Initialise l'erreur RGAA.
        
        Args:
            violations: Liste des violations RGAA détectées
        """
        # Compte les violations par niveau
        levels = {'A': 0, 'AA': 0, 'AAA': 0}
        for v in violations:
            level = v.get('level', 'AA')
            levels[level] = levels.get(level, 0) + 1
        
        message = f"RGAA compliance issues found: {len(violations)} violation(s)"
        if levels['A'] > 0:
            message += f" ({levels['A']} level A)"
        if levels['AA'] > 0:
            message += f" ({levels['AA']} level AA)"
        
        super().__init__(
            message=message,
            code='RGAA_VIOLATION',
            details={
                'violations': violations,
                'violation_count': len(violations),
                'levels': levels
            }
        )


class HTMLParseError(DSFRError):
    """Erreur lors du parsing HTML."""
    
    def __init__(self, html_snippet: str, error_detail: str):
        """
        Initialise l'erreur de parsing HTML.
        
        Args:
            html_snippet: Extrait du HTML problématique
            error_detail: Description de l'erreur
        """
        # Limite le snippet pour éviter des messages trop longs (KISS)
        if len(html_snippet) > 100:
            html_snippet = html_snippet[:100] + '...'
        
        message = f"Failed to parse HTML: {error_detail}"
        
        super().__init__(
            message=message,
            code='HTML_PARSE_ERROR',
            details={
                'html_snippet': html_snippet,
                'error_detail': error_detail
            }
        )


class CSSClassError(DSFRError):
    """Erreur de classes CSS DSFR manquantes ou incorrectes."""
    
    def __init__(self, component: str, missing_classes: List[str], found_classes: List[str]):
        """
        Initialise l'erreur de classes CSS.
        
        Args:
            component: Nom du composant
            missing_classes: Classes CSS requises manquantes
            found_classes: Classes CSS trouvées
        """
        message = f"Missing required CSS classes for component '{component}': {', '.join(missing_classes)}"
        
        super().__init__(
            message=message,
            code='CSS_CLASS_ERROR',
            details={
                'component': component,
                'missing_classes': missing_classes,
                'found_classes': found_classes
            }
        )