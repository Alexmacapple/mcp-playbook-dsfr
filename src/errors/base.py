"""
Classes d'erreur de base pour DSFR MCP
Principe L de SOLID: Les sous-classes doivent être interchangeables
"""

from typing import Dict, Any, Optional


class DSFRError(Exception):
    """
    Classe de base pour toutes les erreurs DSFR.
    
    Attributes:
        message: Message d'erreur lisible
        code: Code d'erreur unique pour identification
        details: Détails supplémentaires sur l'erreur
    """
    
    def __init__(self, message: str, code: str, details: Optional[Dict[str, Any]] = None):
        """
        Initialise une erreur DSFR.
        
        Args:
            message: Message d'erreur explicite
            code: Code d'erreur unique (ex: 'COMPONENT_NOT_FOUND')
            details: Informations contextuelles supplémentaires
        """
        super().__init__(message)
        self.message = message
        self.code = code
        self.details = details or {}
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Sérialise l'erreur pour transmission MCP.
        
        Returns:
            Dictionnaire avec error, message et details
        """
        return {
            'error': self.code,
            'message': self.message,
            'details': self.details
        }
    
    def __str__(self) -> str:
        """Représentation string de l'erreur."""
        if self.details:
            details_str = ', '.join(f"{k}={v}" for k, v in self.details.items())
            return f"[{self.code}] {self.message} ({details_str})"
        return f"[{self.code}] {self.message}"
    
    def __repr__(self) -> str:
        """Représentation développeur de l'erreur."""
        return f"{self.__class__.__name__}(message={self.message!r}, code={self.code!r}, details={self.details!r})"


def is_dsfr_error(error: Any) -> bool:
    """
    Vérifie si une erreur est une erreur DSFR.
    
    Args:
        error: L'objet à vérifier
        
    Returns:
        True si c'est une DSFRError, False sinon
        
    Example:
        >>> try:
        ...     raise ComponentNotFoundError('button')
        ... except Exception as e:
        ...     if is_dsfr_error(e):
        ...         print(f"Erreur DSFR: {e.code}")
    """
    return isinstance(error, DSFRError)