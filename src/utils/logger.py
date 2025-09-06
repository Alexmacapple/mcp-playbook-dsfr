"""
Système de logging centralisé pour MCP DSFR.
Utilise structlog pour des logs structurés et traçables.
"""

import sys
import logging
from pathlib import Path
from typing import Any, Dict, Optional
import structlog
from structlog.stdlib import LoggerFactory
from pythonjsonlogger import jsonlogger
import os


class DSFRLogger:
    """
    Logger centralisé pour le serveur MCP DSFR.
    Singleton pattern pour une instance unique.
    """
    
    _instance: Optional['DSFRLogger'] = None
    _configured: bool = False
    
    def __new__(cls) -> 'DSFRLogger':
        """Singleton pattern."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        """Initialise le logger si pas déjà fait."""
        if not self._configured:
            self.configure()
            self._configured = True
    
    def configure(self):
        """Configure structlog avec les bonnes options."""
        # Niveau de log selon l'environnement
        log_level = os.getenv('LOG_LEVEL', 'INFO').upper()
        
        # Format de log selon l'environnement
        is_production = os.getenv('ENV', 'development') == 'production'
        
        # Configuration du handler
        if is_production:
            # JSON en production pour parsing facile
            handler = logging.StreamHandler(sys.stdout)
            formatter = jsonlogger.JsonFormatter(
                fmt='%(timestamp)s %(level)s %(name)s %(message)s',
                rename_fields={'timestamp': '@timestamp'}
            )
            handler.setFormatter(formatter)
        else:
            # Format lisible en dev
            handler = logging.StreamHandler(sys.stdout)
            handler.setFormatter(
                logging.Formatter(
                    '%(asctime)s [%(levelname)s] %(name)s - %(message)s'
                )
            )
        
        # Configuration root logger
        logging.root.handlers = [handler]
        logging.root.setLevel(getattr(logging, log_level))
        
        # Configuration structlog
        structlog.configure(
            processors=[
                structlog.stdlib.filter_by_level,
                structlog.stdlib.add_logger_name,
                structlog.stdlib.add_log_level,
                structlog.stdlib.PositionalArgumentsFormatter(),
                structlog.processors.TimeStamper(fmt="iso"),
                structlog.processors.StackInfoRenderer(),
                structlog.processors.format_exc_info,
                structlog.processors.UnicodeDecoder(),
                structlog.processors.dict_tracebacks,
                structlog.dev.ConsoleRenderer() if not is_production else structlog.processors.JSONRenderer(),
            ],
            context_class=dict,
            logger_factory=LoggerFactory(),
            cache_logger_on_first_use=True,
        )
        
        # Logger par défaut
        self.logger = structlog.get_logger('mcp.dsfr')
        
    def get_logger(self, name: str = 'mcp.dsfr') -> structlog.BoundLogger:
        """
        Retourne un logger avec le nom spécifié.
        
        Args:
            name: Nom du logger (ex: 'mcp.dsfr.generator')
            
        Returns:
            Logger configuré
        """
        return structlog.get_logger(name)
    
    def log_mcp_call(self, tool: str, params: Dict[str, Any], duration_ms: float = 0):
        """
        Log un appel MCP pour monitoring.
        
        Args:
            tool: Nom de l'outil MCP appelé
            params: Paramètres de l'appel
            duration_ms: Durée d'exécution en ms
        """
        self.logger.info(
            "mcp_call",
            tool=tool,
            params=params,
            duration_ms=duration_ms,
            event_type="mcp_call"
        )
    
    def log_error(self, error: Exception, context: Optional[Dict[str, Any]] = None):
        """
        Log une erreur avec contexte.
        
        Args:
            error: L'exception à logger
            context: Contexte additionnel
        """
        self.logger.error(
            "error_occurred",
            error_type=type(error).__name__,
            error_message=str(error),
            context=context or {},
            event_type="error",
            exc_info=True
        )
    
    def log_audit(self, 
                  component: str, 
                  rgaa_level: str, 
                  score: float,
                  issues: int = 0):
        """
        Log un audit RGAA pour métriques.
        
        Args:
            component: Type de composant audité
            rgaa_level: Niveau RGAA (A, AA, AAA)
            score: Score de conformité (0-100)
            issues: Nombre de problèmes trouvés
        """
        self.logger.info(
            "rgaa_audit",
            component=component,
            rgaa_level=rgaa_level,
            score=score,
            issues=issues,
            event_type="audit"
        )
    
    def log_performance(self, 
                       operation: str,
                       duration_ms: float,
                       metadata: Optional[Dict[str, Any]] = None):
        """
        Log les métriques de performance.
        
        Args:
            operation: Nom de l'opération
            duration_ms: Durée en millisecondes
            metadata: Métadonnées additionnelles
        """
        self.logger.info(
            "performance",
            operation=operation,
            duration_ms=duration_ms,
            metadata=metadata or {},
            event_type="performance"
        )


# Instance singleton globale
logger_instance = DSFRLogger()
get_logger = logger_instance.get_logger
log_mcp_call = logger_instance.log_mcp_call
log_error = logger_instance.log_error
log_audit = logger_instance.log_audit
log_performance = logger_instance.log_performance