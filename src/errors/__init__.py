"""
Système de gestion d'erreurs structuré pour DSFR MCP
Suit le principe de responsabilité unique (S de SOLID)
"""

from .base import DSFRError
from .components import (
    ComponentNotFoundError,
    InvalidVariantError,
    MissingPropertyError
)
from .validation import (
    ValidationError,
    RGAAViolationError,
    HTMLParseError
)

__all__ = [
    'DSFRError',
    'ComponentNotFoundError',
    'InvalidVariantError',
    'MissingPropertyError',
    'ValidationError',
    'RGAAViolationError',
    'HTMLParseError'
]