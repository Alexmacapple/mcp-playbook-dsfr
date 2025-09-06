"""
MCP DSFR - Model Context Protocol pour le Design System de l'État Français
Version 2.0 - Architecture Clean Code

Principes:
- SOLID: Single Responsibility, Open/Closed, Liskov, Interface Segregation, Dependency Inversion
- DRY: Don't Repeat Yourself
- KISS: Keep It Stupid Simple
- YAGNI: You Ain't Gonna Need It

Architecture:
    mcp/          # Core MCP server
    src/          # Business logic
    gabarits/     # HTML templates
    data/         # Static data
    tests/        # Unit tests
"""

__version__ = "2.0.0"
__author__ = "MCP DSFR Team"

# Exports principaux pour utilisation simple (KISS)
# from .dsfr_server import DSFRMCPServer  # Commenté car utilise une ancienne API
from .server import app

__all__ = ['app']