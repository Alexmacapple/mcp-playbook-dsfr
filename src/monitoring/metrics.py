"""
Syst\u00e8me de monitoring et m\u00e9triques pour MCP DSFR.
Collecte des m\u00e9triques de performance et d'utilisation.
"""

import time
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, Optional
from collections import defaultdict, deque
from functools import wraps


class MetricsCollector:
    """
    Collecteur de m\u00e9triques pour le monitoring.
    Pattern Singleton pour instance unique.
    """
    
    _instance: Optional['MetricsCollector'] = None
    
    def __new__(cls) -> 'MetricsCollector':
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        """Initialise le collecteur de m\u00e9triques."""
        if not hasattr(self, '_initialized'):
            self.metrics = {
                'components_generated': 0,
                'total_requests': 0,
                'errors': 0,
                'cache_hits': 0,
                'cache_misses': 0,
                'kb_usage': 0,
                'registry_usage': 0
            }
            
            # Latences (garder les 1000 derni\u00e8res)
            self.latencies = deque(maxlen=1000)
            
            # Compteurs par composant
            self.component_counts = defaultdict(int)
            
            # Compteurs par outil MCP
            self.tool_counts = defaultdict(int)
            
            # Erreurs par type
            self.error_types = defaultdict(int)
            
            # Timestamp de d\u00e9marrage
            self.start_time = time.time()
            
            # Fichier de logs m\u00e9triques
            self.metrics_file = Path('logs/metrics.jsonl')
            self.metrics_file.parent.mkdir(exist_ok=True)
            
            self._initialized = True
    
    def track_request(self, tool: str, duration: float, success: bool = True):
        """
        Enregistre une requ\u00eate.
        
        Args:
            tool: Nom de l'outil MCP utilis\u00e9
            duration: Dur\u00e9e en millisecondes
            success: Si la requ\u00eate a r\u00e9ussi
        """
        self.metrics['total_requests'] += 1
        self.tool_counts[tool] += 1
        self.latencies.append(duration)
        
        if not success:
            self.metrics['errors'] += 1
        
        # Log asynchrone
        self._log_metric({
            'timestamp': datetime.utcnow().isoformat(),
            'tool': tool,
            'duration_ms': duration,
            'success': success
        })
    
    def track_component_generation(self, component: str, variant: str = None, 
                                  from_kb: bool = False):
        """
        Enregistre la g\u00e9n\u00e9ration d'un composant.
        
        Args:
            component: Nom du composant
            variant: Variante utilis\u00e9e
            from_kb: Si g\u00e9n\u00e9r\u00e9 depuis la Knowledge Base
        """
        self.metrics['components_generated'] += 1
        self.component_counts[component] += 1
        
        if from_kb:
            self.metrics['kb_usage'] += 1
        else:
            self.metrics['registry_usage'] += 1
    
    def track_cache(self, hit: bool):
        """
        Enregistre un acc\u00e8s cache.
        
        Args:
            hit: True si cache hit, False si cache miss
        """
        if hit:
            self.metrics['cache_hits'] += 1
        else:
            self.metrics['cache_misses'] += 1
    
    def track_error(self, error_type: str, error_msg: str = None):
        """
        Enregistre une erreur.
        
        Args:
            error_type: Type d'erreur
            error_msg: Message d'erreur optionnel
        """
        self.metrics['errors'] += 1
        self.error_types[error_type] += 1
        
        self._log_metric({
            'timestamp': datetime.utcnow().isoformat(),
            'type': 'error',
            'error_type': error_type,
            'message': error_msg
        })
    
    def get_metrics(self) -> Dict[str, Any]:
        """
        R\u00e9cup\u00e8re toutes les m\u00e9triques.
        
        Returns:
            Dictionnaire des m\u00e9triques actuelles
        """
        uptime = time.time() - self.start_time
        
        # Calculer les percentiles de latence
        latencies_sorted = sorted(self.latencies) if self.latencies else [0]
        
        return {
            'uptime_seconds': uptime,
            'metrics': self.metrics,
            'latency': {
                'p50': self._percentile(latencies_sorted, 50),
                'p95': self._percentile(latencies_sorted, 95),
                'p99': self._percentile(latencies_sorted, 99),
                'avg': sum(self.latencies) / len(self.latencies) if self.latencies else 0
            },
            'components': dict(self.component_counts),
            'tools': dict(self.tool_counts),
            'errors': dict(self.error_types),
            'performance': {
                'requests_per_minute': (self.metrics['total_requests'] / uptime) * 60 if uptime > 0 else 0,
                'components_per_minute': (self.metrics['components_generated'] / uptime) * 60 if uptime > 0 else 0,
                'error_rate': (self.metrics['errors'] / self.metrics['total_requests']) if self.metrics['total_requests'] > 0 else 0,
                'cache_hit_rate': (self.metrics['cache_hits'] / (self.metrics['cache_hits'] + self.metrics['cache_misses'])) if (self.metrics['cache_hits'] + self.metrics['cache_misses']) > 0 else 0,
                'kb_vs_registry_ratio': (self.metrics['kb_usage'] / self.metrics['registry_usage']) if self.metrics['registry_usage'] > 0 else float('inf')
            }
        }
    
    def get_health_status(self) -> Dict[str, Any]:
        """
        R\u00e9cup\u00e8re le statut de sant\u00e9 du syst\u00e8me.
        
        Returns:
            Status avec alertes \u00e9ventuelles
        """
        metrics = self.get_metrics()
        alerts = []
        status = 'healthy'
        
        # V\u00e9rifier les seuils
        if metrics['performance']['error_rate'] > 0.01:  # >1% d'erreurs
            alerts.append('High error rate')
            status = 'degraded'
        
        if metrics['latency']['p95'] > 100:  # P95 > 100ms
            alerts.append('High latency')
            status = 'degraded' if status == 'healthy' else status
        
        if metrics['performance']['error_rate'] > 0.05:  # >5% d'erreurs
            status = 'unhealthy'
        
        # V\u00e9rifier la m\u00e9moire (simplifi\u00e9)
        import psutil
        memory_percent = psutil.virtual_memory().percent if hasattr(psutil, 'virtual_memory') else 0
        if memory_percent > 80:
            alerts.append(f'High memory usage: {memory_percent}%')
            status = 'degraded' if status == 'healthy' else status
        
        return {
            'status': status,
            'alerts': alerts,
            'uptime': metrics['uptime_seconds'],
            'total_requests': metrics['metrics']['total_requests'],
            'error_rate': f"{metrics['performance']['error_rate']*100:.2f}%",
            'p95_latency': f"{metrics['latency']['p95']:.2f}ms"
        }
    
    def _percentile(self, sorted_list: list, percentile: int) -> float:
        """Calcule un percentile."""
        if not sorted_list:
            return 0
        index = int(len(sorted_list) * percentile / 100)
        return sorted_list[min(index, len(sorted_list) - 1)]
    
    def _log_metric(self, metric: Dict[str, Any]):
        """Enregistre une m\u00e9trique dans le fichier de logs."""
        try:
            with open(self.metrics_file, 'a') as f:
                f.write(json.dumps(metric) + '\n')
        except Exception:
            pass  # Ignorer les erreurs de log

    def reset(self):
        """R\u00e9initialise toutes les m\u00e9triques."""
        self.__init__()


def track_performance(func):
    """
    D\u00e9corateur pour tracker la performance d'une fonction.
    
    Usage:
        @track_performance
        def my_function():
            ...
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        collector = get_metrics_collector()
        start = time.time()
        success = True
        
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            success = False
            collector.track_error(type(e).__name__, str(e))
            raise
        finally:
            duration = (time.time() - start) * 1000  # En ms
            tool_name = func.__name__
            collector.track_request(tool_name, duration, success)
    
    return wrapper


# Singleton helper
_collector_instance: Optional[MetricsCollector] = None

def get_metrics_collector() -> MetricsCollector:
    """
    R\u00e9cup\u00e8re l'instance unique du collecteur de m\u00e9triques.
    
    Returns:
        Instance de MetricsCollector
    """
    global _collector_instance
    if _collector_instance is None:
        _collector_instance = MetricsCollector()
    return _collector_instance


# Export pour utilisation facile
def get_metrics() -> Dict[str, Any]:
    """R\u00e9cup\u00e8re les m\u00e9triques actuelles."""
    return get_metrics_collector().get_metrics()


def get_health() -> Dict[str, Any]:
    """R\u00e9cup\u00e8re le statut de sant\u00e9."""
    return get_metrics_collector().get_health_status()