"""
Système de logging simplifié pour MCP DSFR.
Utilise le logging Python standard (principe KISS).
"""

import sys
import logging
import os
from typing import Dict, Any, Optional


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
        """Configure le logging Python standard."""
        # Niveau de log selon l'environnement
        log_level = os.getenv('LOG_LEVEL', 'INFO').upper()
        
        # Format selon l'environnement
        is_production = os.getenv('ENV', 'development') == 'production'
        
        # Format simple et clair
        if is_production:
            log_format = '%(asctime)s - %(levelname)s - %(name)s - %(message)s'
        else:
            log_format = '%(asctime)s [%(levelname)8s] %(name)s - %(message)s'
        
        # Configuration du logger
        logging.basicConfig(
            level=getattr(logging, log_level),
            format=log_format,
            datefmt='%Y-%m-%d %H:%M:%S',
            stream=sys.stdout
        )
        
        # Logger par défaut
        self.logger = logging.getLogger('mcp.dsfr')
        
    def get_logger(self, name: str = 'mcp.dsfr') -> logging.Logger:
        """
        Retourne un logger avec le nom spécifié.
        
        Args:
            name: Nom du logger (ex: 'mcp.dsfr.generator')
            
        Returns:
            Logger configuré
        """
        return logging.getLogger(name)
    
    def log_mcp_call(self, tool: str, params: Dict[str, Any], duration_ms: float = 0):
        """
        Log un appel MCP pour monitoring.
        
        Args:
            tool: Nom de l'outil MCP appelé
            params: Paramètres de l'appel
            duration_ms: Durée d'exécution en ms
        """
        self.logger.info(
            f"MCP call: {tool} | Duration: {duration_ms:.2f}ms | Params: {params}"
        )
    
    def log_error(self, error: Exception, context: Optional[Dict[str, Any]] = None):
        """
        Log une erreur avec contexte.
        
        Args:
            error: L'exception à logger
            context: Contexte additionnel
        """
        self.logger.error(
            f"Error: {type(error).__name__}: {str(error)} | Context: {context or {}}",
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
            f"RGAA Audit: {component} | Level: {rgaa_level} | Score: {score:.1f}% | Issues: {issues}"
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
        if duration_ms > 1000:  # Log seulement les opérations lentes
            self.logger.warning(
                f"Slow operation: {operation} took {duration_ms:.2f}ms | {metadata or {}}"
            )
        elif self.logger.isEnabledFor(logging.DEBUG):
            self.logger.debug(
                f"Performance: {operation} took {duration_ms:.2f}ms"
            )


# Instance singleton globale
logger_instance = DSFRLogger()
get_logger = logger_instance.get_logger
log_mcp_call = logger_instance.log_mcp_call
log_error = logger_instance.log_error
log_audit = logger_instance.log_audit
log_performance = logger_instance.log_performance