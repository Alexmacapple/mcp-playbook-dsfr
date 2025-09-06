#!/usr/bin/env python3
"""
Test des nouveaux outils design : couleurs, icônes et recherche.
"""

import sys
from pathlib import Path

# Ajouter le chemin pour les imports
sys.path.insert(0, str(Path(__file__).parent))

from src.services import get_design_service
from src.data import get_registry


def test_design_tools():
    """Test les outils design."""
    design = get_design_service()
    registry = get_registry()
    
    print("=" * 80)
    print("🎨 TEST DES OUTILS DESIGN DSFR")
    print("=" * 80)
    
    # Test 1: Couleurs
    print("\n📝 TEST 1: Palette de couleurs")
    print("-" * 40)
    
    # Toutes les couleurs
    colors = design.get_colors()
    print(f"Catégories de couleurs: {list(colors.keys())}")
    
    # Couleurs primaires
    primary = design.get_colors("primary")
    print(f"\nCouleurs primaires ({len(primary)} couleurs):")
    for i, (name, value) in enumerate(primary.items()):
        if i < 3:
            print(f"  • {name}: {value}")
    
    # Test 2: Icônes
    print("\n" + "=" * 80)
    print("🎯 TEST 2: Bibliothèque d'icônes")
    print("-" * 40)
    
    # Toutes les icônes
    all_icons = design.get_icons()
    print(f"Total d'icônes: {len(all_icons)}")
    
    # Recherche d'icônes
    search_icons = design.get_icons(search="search")
    print(f"\nIcônes contenant 'search': {len(search_icons)}")
    for name, data in list(search_icons.items())[:3]:
        print(f"  • {name}: {data['class']}")
    
    # Icônes par catégorie
    nav_icons = design.get_icons(category="navigation")
    print(f"\nIcônes de navigation: {len(nav_icons)}")
    
    # Test 3: Recherche de composants
    print("\n" + "=" * 80)
    print("🔍 TEST 3: Recherche de composants")
    print("-" * 40)
    
    # Simuler une recherche
    all_components = registry.list_components()
    query = "button"
    query_lower = query.lower()
    
    # Recherche exacte
    exact = [c for c in all_components if query_lower == c.lower()]
    print(f"\nRecherche '{query}':")
    print(f"  • Correspondances exactes: {len(exact)}")
    
    # Recherche partielle
    partial = [c for c in all_components if query_lower in c.lower() and c not in exact]
    print(f"  • Correspondances partielles: {len(partial)}")
    if partial:
        print(f"    Exemples: {', '.join(partial[:3])}")
    
    # Test 4: Thème personnalisé
    print("\n" + "=" * 80)
    print("🎨 TEST 4: Création de thème")
    print("-" * 40)
    
    theme = design.create_theme("mon-theme", {
        "colors": {
            "primary": {
                "custom-blue": "#0055ff"
            }
        }
    })
    
    print(f"Thème créé: {theme['name']}")
    print(f"Basé sur: {theme['base']}")
    print(f"Couleur custom ajoutée: {theme['colors']['primary'].get('custom-blue')}")
    
    print("\n" + "=" * 80)
    print("✅ TESTS TERMINÉS AVEC SUCCÈS")
    print("=" * 80)


if __name__ == "__main__":
    test_design_tools()