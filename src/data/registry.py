"""
Registre centralisé des composants DSFR.
Implémente le pattern Singleton pour garantir une source unique de vérité (DRY).
"""

import os
import json
from pathlib import Path
from typing import Dict, List, Optional, Any
from functools import lru_cache


class ComponentRegistry:
    """
    Registre centralisé de tous les composants DSFR.
    
    Pattern Singleton : Une seule instance pour toute l'application.
    Charge les templates HTML depuis le dossier gabarits/.
    
    Attributes:
        components: Dictionnaire des composants et leurs variantes
        metadata: Métadonnées sur chaque composant
    """
    
    _instance: Optional['ComponentRegistry'] = None
    _initialized: bool = False
    
    def __new__(cls) -> 'ComponentRegistry':
        """
        Singleton pattern : garantit une instance unique.
        Principe S de SOLID : Une seule responsabilité = gérer le registre.
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        """Initialise le registre une seule fois."""
        if not self._initialized:
            self.base_path = Path(__file__).parent.parent.parent / 'gabarits'
            self.components: Dict[str, Dict[str, Any]] = {}
            self.metadata: Dict[str, Any] = {}
            self._load_components()
            ComponentRegistry._initialized = True
    
    def _load_components(self) -> None:
        """
        Charge tous les composants depuis gabarits/.
        KISS : Scan simple du système de fichiers.
        """
        if not self.base_path.exists():
            raise FileNotFoundError(f"Gabarits directory not found: {self.base_path}")
        
        # Charger le fichier de bibliothèque s'il existe
        library_file = self.base_path / 'dsfr_complete_library.json'
        if library_file.exists():
            self._load_from_library(library_file)
        else:
            self._scan_gabarits_directory()
        
        # Charger les métadonnées additionnelles
        self._load_metadata()
    
    def _load_from_library(self, library_file: Path) -> None:
        """
        Charge les composants depuis le fichier JSON de bibliothèque.
        DRY : Réutilise la bibliothèque existante.
        """
        with open(library_file, 'r', encoding='utf-8') as f:
            library = json.load(f)
        
        # Restructurer pour notre format interne
        for comp_name, comp_data in library.get('components', {}).items():
            self.components[comp_name] = {
                'path': str(self.base_path / comp_name),
                'variants': {}
            }
            
            # Charger chaque variante
            for variant in comp_data.get('variants', []):
                variant_file = self.base_path / comp_name / f"{comp_name}_{variant}.html"
                if variant_file.exists():
                    with open(variant_file, 'r', encoding='utf-8') as f:
                        # Skip les commentaires du début
                        lines = f.readlines()
                        html = ''.join(lines[3:]) if len(lines) > 3 else ''.join(lines)
                        self.components[comp_name]['variants'][variant] = {
                            'html': html.strip(),
                            'file': str(variant_file)
                        }
    
    def _scan_gabarits_directory(self) -> None:
        """
        Scan le dossier gabarits/ pour découvrir les composants.
        Fallback si pas de bibliothèque JSON.
        """
        for component_dir in sorted(self.base_path.iterdir()):
            if not component_dir.is_dir():
                continue
            
            component_name = component_dir.name
            self.components[component_name] = {
                'path': str(component_dir),
                'variants': {}
            }
            
            # Scanner les variantes HTML
            for variant_file in sorted(component_dir.glob('*.html')):
                variant_name = variant_file.stem.replace(f"{component_name}_", "")
                
                with open(variant_file, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    html = ''.join(lines[3:]) if len(lines) > 3 else ''.join(lines)
                
                self.components[component_name]['variants'][variant_name] = {
                    'html': html.strip(),
                    'file': str(variant_file)
                }
    
    def _load_metadata(self) -> None:
        """
        Charge les métadonnées des composants (descriptions, RGAA, etc).
        YAGNI : Pour l'instant, métadonnées basiques.
        """
        # Métadonnées de base pour chaque composant
        self.metadata = {
            'button': {
                'description': 'Bouton DSFR avec différentes variantes',
                'rgaa_level': 'AA',
                'required_props': ['label'],
                'optional_props': ['icon', 'disabled', 'size']
            },
            'form': {
                'description': 'Formulaire complet avec validation',
                'rgaa_level': 'AA',
                'required_props': [],
                'optional_props': ['fields', 'action', 'method']
            },
            'alert': {
                'description': 'Message d\'alerte ou d\'information',
                'rgaa_level': 'AA',
                'required_props': ['message'],
                'optional_props': ['title', 'type', 'closable']
            },
            # Ajouter d'autres métadonnées au fur et à mesure (YAGNI)
        }
    
    @lru_cache(maxsize=128)
    def get_component(self, name: str) -> Optional[Dict[str, Any]]:
        """
        Récupère un composant par son nom.
        Cache LRU pour performance (KISS).
        
        Args:
            name: Nom du composant
            
        Returns:
            Dictionnaire avec les variantes et métadonnées
        """
        return self.components.get(name)
    
    def get_variant_html(self, component: str, variant: str = 'basic') -> Optional[str]:
        """
        Récupère le HTML d'une variante spécifique.
        
        Args:
            component: Nom du composant
            variant: Nom de la variante (défaut: 'basic')
            
        Returns:
            HTML de la variante ou None si non trouvé
        """
        comp = self.get_component(component)
        if not comp:
            return None
        
        variant_data = comp.get('variants', {}).get(variant)
        if variant_data:
            return variant_data.get('html')
        
        # Fallback sur la première variante disponible (KISS)
        variants = comp.get('variants', {})
        if variants:
            first_variant = list(variants.values())[0]
            return first_variant.get('html')
        
        return None
    
    def list_components(self) -> List[str]:
        """
        Liste tous les composants disponibles.
        
        Returns:
            Liste triée des noms de composants
        """
        return sorted(self.components.keys())
    
    def list_variants(self, component: str) -> List[str]:
        """
        Liste les variantes d'un composant.
        
        Args:
            component: Nom du composant
            
        Returns:
            Liste des variantes disponibles
        """
        comp = self.get_component(component)
        if not comp:
            return []
        return list(comp.get('variants', {}).keys())
    
    def get_metadata(self, component: str) -> Dict[str, Any]:
        """
        Récupère les métadonnées d'un composant.
        
        Args:
            component: Nom du composant
            
        Returns:
            Dictionnaire de métadonnées
        """
        return self.metadata.get(component, {
            'description': f'Composant DSFR {component}',
            'rgaa_level': 'AA'
        })
    
    def get_stats(self) -> Dict[str, int]:
        """
        Statistiques sur le registre.
        
        Returns:
            Nombre de composants et variantes
        """
        total_variants = sum(
            len(comp.get('variants', {})) 
            for comp in self.components.values()
        )
        
        return {
            'components': len(self.components),
            'variants': total_variants,
            'cached_items': self.get_component.cache_info().currsize
        }


# Helper function pour accès simple (KISS)
_registry: Optional[ComponentRegistry] = None

def get_registry() -> ComponentRegistry:
    """
    Récupère l'instance unique du registre.
    Pattern Singleton avec helper function.
    
    Returns:
        Instance de ComponentRegistry
        
    Example:
        >>> registry = get_registry()
        >>> button_html = registry.get_variant_html('button', 'primary')
    """
    global _registry
    if _registry is None:
        _registry = ComponentRegistry()
    return _registry