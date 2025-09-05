"""
Module de données pour DSFR MCP.
Gère le registre des composants et les métadonnées.
"""

from .registry import ComponentRegistry, get_registry

__all__ = ['ComponentRegistry', 'get_registry']