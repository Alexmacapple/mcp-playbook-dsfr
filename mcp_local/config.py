"""
Configuration du serveur MCP DSFR.
Centralise tous les paramètres (S de SOLID).
Support des variables d'environnement pour production.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()


class MCPConfig:
    """Configuration centralisée du serveur MCP avec support des env vars."""
    
    # Environnement
    ENV = os.getenv('ENV', 'development')
    IS_PRODUCTION = ENV == 'production'
    
    # Métadonnées du serveur
    SERVER_NAME = "mcp-playbook-dsfr"
    SERVER_VERSION = "2.0.0"
    SERVER_DESCRIPTION = "MCP Production Playbook for French Design System (DSFR) v1.14.1"
    
    # Chemins (configurables via env)
    BASE_DIR = Path(__file__).parent.parent
    GABARITS_DIR = Path(os.getenv('GABARITS_DIR', str(BASE_DIR / "gabarits")))
    DATA_DIR = Path(os.getenv('DATA_DIR', str(BASE_DIR / "data")))
    
    # Limites et performances (configurables)
    MAX_CACHE_SIZE = int(os.getenv('MAX_CACHE_SIZE', '256'))
    MAX_COMPONENTS_IN_LIST = int(os.getenv('MAX_COMPONENTS_IN_LIST', '20'))
    MAX_HTML_SIZE = int(os.getenv('MAX_HTML_SIZE', '1000000'))  # 1MB par défaut
    
    # Validation (configurables)
    DEFAULT_RGAA_LEVEL = os.getenv('DEFAULT_RGAA_LEVEL', 'AA')
    VALIDATE_ON_GENERATE = os.getenv('VALIDATE_ON_GENERATE', 'false').lower() == 'true'
    
    # Sécurité (nouvelles variables)
    ENABLE_HTML_SANITIZATION = os.getenv('ENABLE_HTML_SANITIZATION', 'true').lower() == 'true'
    MAX_REQUEST_SIZE = int(os.getenv('MAX_REQUEST_SIZE', '5000000'))  # 5MB
    RATE_LIMIT_PER_MINUTE = int(os.getenv('RATE_LIMIT_PER_MINUTE', '60'))
    
    # Logging (configurables)
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO').upper()
    DEBUG = os.getenv('DEBUG', 'false').lower() == 'true'
    LOG_FILE = BASE_DIR / "mcp.log" if not IS_PRODUCTION else None
    PRETTY_LOGS = os.getenv('PRETTY_LOGS', 'true').lower() == 'true' and not IS_PRODUCTION
    
    # Monitoring (optionnel)
    ENABLE_METRICS = os.getenv('ENABLE_METRICS', 'false').lower() == 'true'
    METRICS_PORT = int(os.getenv('METRICS_PORT', '9090'))
    
    @classmethod
    def to_dict(cls) -> dict:
        """Export config as dict for debugging."""
        return {
            "env": cls.ENV,
            "is_production": cls.IS_PRODUCTION,
            "server_name": cls.SERVER_NAME,
            "server_version": cls.SERVER_VERSION,
            "base_dir": str(cls.BASE_DIR),
            "gabarits_dir": str(cls.GABARITS_DIR),
            "debug": cls.DEBUG,
            "log_level": cls.LOG_LEVEL,
            "security": {
                "sanitization_enabled": cls.ENABLE_HTML_SANITIZATION,
                "rate_limit": cls.RATE_LIMIT_PER_MINUTE,
                "max_request_size": cls.MAX_REQUEST_SIZE
            },
            "metrics_enabled": cls.ENABLE_METRICS
        }
    
    @classmethod
    def validate(cls) -> bool:
        """
        Valide la configuration.
        
        Returns:
            True si config valide
            
        Raises:
            ValueError: Si configuration invalide
        """
        # Vérifier les chemins requis
        if not cls.GABARITS_DIR.exists():
            raise ValueError(f"Gabarits directory not found: {cls.GABARITS_DIR}")
        
        # Vérifier les valeurs
        if cls.MAX_CACHE_SIZE < 1:
            raise ValueError("MAX_CACHE_SIZE must be at least 1")
        
        if cls.DEFAULT_RGAA_LEVEL not in ['A', 'AA', 'AAA']:
            raise ValueError(f"Invalid RGAA level: {cls.DEFAULT_RGAA_LEVEL}")
        
        return True