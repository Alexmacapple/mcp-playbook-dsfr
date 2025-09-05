"""
Configuration du serveur MCP DSFR.
Centralise tous les paramètres (S de SOLID).
"""

from pathlib import Path


class MCPConfig:
    """Configuration centralisée du serveur MCP."""
    
    # Métadonnées du serveur
    SERVER_NAME = "mcp-playbook-dsfr"
    SERVER_VERSION = "2.0.0"
    SERVER_DESCRIPTION = "MCP Production Playbook for French Design System (DSFR) v1.14.1"
    
    # Chemins
    BASE_DIR = Path(__file__).parent.parent
    GABARITS_DIR = BASE_DIR / "gabarits"
    DATA_DIR = BASE_DIR / "data"
    
    # Limites et performances
    MAX_CACHE_SIZE = 256
    MAX_COMPONENTS_IN_LIST = 20
    MAX_HTML_SIZE = 1_000_000  # 1MB max pour validation
    
    # Validation
    DEFAULT_RGAA_LEVEL = "AA"
    VALIDATE_ON_GENERATE = False  # KISS : Pas de validation auto par défaut
    
    # Logging
    DEBUG = False
    LOG_FILE = BASE_DIR / "mcp.log"
    
    @classmethod
    def to_dict(cls) -> dict:
        """Export config as dict for debugging."""
        return {
            "server_name": cls.SERVER_NAME,
            "server_version": cls.SERVER_VERSION,
            "base_dir": str(cls.BASE_DIR),
            "gabarits_dir": str(cls.GABARITS_DIR),
            "debug": cls.DEBUG
        }