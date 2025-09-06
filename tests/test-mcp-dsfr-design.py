#!/usr/bin/env python3
"""
Test des outils design : couleurs, icônes et recherche.
Version 2.0 - Aligné avec MCP DSFR - Sans émojis
"""

import sys
from pathlib import Path

# Ajouter le chemin pour les imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.services import get_design_service
from src.data import get_registry


def test_design_tools():
    """Test les outils design et génère un rapport."""
    
    # Créer le rapport de test
    output_dir = Path(__file__).parent / "resultats-test"
    output_dir.mkdir(parents=True, exist_ok=True)
    report_path = output_dir / "test_design_tools_report.txt"
    
    report = []
    report.append("=" * 80)
    report.append("TEST DES OUTILS DESIGN DSFR")
    report.append("=" * 80)
    report.append("Date: 2025-01-06")
    report.append("Version: 2.0\n")
    
    tests_passed = 0
    tests_failed = 0
    
    try:
        design = get_design_service()
        registry = get_registry()
        
        # Test 1: Couleurs
        report.append("\nTEST 1: Palette de couleurs")
        report.append("-" * 40)
        
        try:
            # Toutes les couleurs
            colors = design.get_colors()
            report.append(f"Catégories de couleurs: {list(colors.keys())}")
            
            # Couleurs primaires
            primary = design.get_colors("primary")
            report.append(f"\nCouleurs primaires ({len(primary)} couleurs):")
            for i, (name, value) in enumerate(primary.items()):
                if i < 3:
                    report.append(f"  - {name}: {value}")
            
            # Vérifications
            if len(colors) > 0 and len(primary) > 0:
                report.append("[OK] Test des couleurs réussi")
                tests_passed += 1
            else:
                report.append("[ERREUR] Aucune couleur trouvée")
                tests_failed += 1
                
        except Exception as e:
            report.append(f"[ERREUR] Test des couleurs: {str(e)}")
            tests_failed += 1
        
        # Test 2: Icônes
        report.append("\n" + "=" * 80)
        report.append("TEST 2: Bibliothèque d'icônes")
        report.append("-" * 40)
        
        try:
            # Toutes les icônes
            all_icons = design.get_icons()
            report.append(f"Total d'icônes: {len(all_icons)}")
            
            # Recherche d'icônes
            search_icons = design.get_icons(search="search")
            report.append(f"\nIcônes contenant 'search': {len(search_icons)}")
            for name, data in list(search_icons.items())[:3]:
                report.append(f"  - {name}: {data['class']}")
            
            # Icônes par catégorie
            nav_icons = design.get_icons(category="navigation")
            report.append(f"\nIcônes de navigation: {len(nav_icons)}")
            
            # Vérifications
            if len(all_icons) > 0:
                report.append("[OK] Test des icônes réussi")
                tests_passed += 1
            else:
                report.append("[ERREUR] Aucune icône trouvée")
                tests_failed += 1
                
        except Exception as e:
            report.append(f"[ERREUR] Test des icônes: {str(e)}")
            tests_failed += 1
        
        # Test 3: Recherche de composants
        report.append("\n" + "=" * 80)
        report.append("TEST 3: Recherche de composants")
        report.append("-" * 40)
        
        try:
            # Simuler une recherche
            all_components = registry.list_components()
            query = "button"
            query_lower = query.lower()
            
            # Recherche exacte
            exact = [c for c in all_components if query_lower == c.lower()]
            report.append(f"\nRecherche '{query}':")
            report.append(f"  - Correspondances exactes: {len(exact)}")
            
            # Recherche partielle
            partial = [c for c in all_components if query_lower in c.lower() and c not in exact]
            report.append(f"  - Correspondances partielles: {len(partial)}")
            if partial:
                report.append(f"    Exemples: {', '.join(partial[:3])}")
            
            # Vérifications
            if len(all_components) > 0:
                report.append("[OK] Test de recherche réussi")
                tests_passed += 1
            else:
                report.append("[ERREUR] Aucun composant dans le registre")
                tests_failed += 1
                
        except Exception as e:
            report.append(f"[ERREUR] Test de recherche: {str(e)}")
            tests_failed += 1
        
        # Test 4: Thème personnalisé
        report.append("\n" + "=" * 80)
        report.append("TEST 4: Création de thème")
        report.append("-" * 40)
        
        try:
            theme = design.create_theme("mon-theme", {
                "colors": {
                    "primary": {
                        "custom-blue": "#0055ff"
                    }
                }
            })
            
            report.append(f"Thème créé: {theme['name']}")
            report.append(f"Basé sur: {theme['base']}")
            report.append(f"Couleur custom ajoutée: {theme['colors']['primary'].get('custom-blue')}")
            
            # Vérifications
            if theme['name'] == "mon-theme" and theme['colors']['primary'].get('custom-blue') == "#0055ff":
                report.append("[OK] Test de création de thème réussi")
                tests_passed += 1
            else:
                report.append("[ERREUR] Thème mal créé")
                tests_failed += 1
                
        except Exception as e:
            report.append(f"[ERREUR] Test de création de thème: {str(e)}")
            tests_failed += 1
        
        # Test 5: Tokens de design
        report.append("\n" + "=" * 80)
        report.append("TEST 5: Tokens de design")
        report.append("-" * 40)
        
        try:
            # Espacements
            spacing = design.get_spacing()
            report.append(f"Tokens d'espacement: {len(spacing)} valeurs")
            for key in list(spacing.keys())[:3]:
                report.append(f"  - {key}: {spacing[key]}")
            
            # Typographie
            typography = design.get_typography()
            report.append(f"\nTokens de typographie: {len(typography)} catégories")
            
            # Vérifications
            if len(spacing) > 0 and len(typography) > 0:
                report.append("[OK] Test des tokens réussi")
                tests_passed += 1
            else:
                report.append("[ERREUR] Tokens manquants")
                tests_failed += 1
                
        except Exception as e:
            report.append(f"[ERREUR] Test des tokens: {str(e)}")
            tests_failed += 1
        
        # Test 6: Export CSS
        report.append("\n" + "=" * 80)
        report.append("TEST 6: Export CSS des tokens")
        report.append("-" * 40)
        
        try:
            css = design.export_css_variables()
            
            # Vérifier la structure CSS
            if ":root" in css and "--" in css:
                report.append("[OK] Export CSS généré correctement")
                report.append(f"    Taille: {len(css)} caractères")
                
                # Compter les variables
                var_count = css.count("--")
                report.append(f"    Variables CSS: ~{var_count}")
                tests_passed += 1
            else:
                report.append("[ERREUR] CSS mal formé")
                tests_failed += 1
                
        except Exception as e:
            report.append(f"[ERREUR] Test d'export CSS: {str(e)}")
            tests_failed += 1
        
    except Exception as e:
        report.append(f"\n[ERREUR CRITIQUE] Impossible d'initialiser les services: {str(e)}")
        tests_failed += 1
    
    # Résumé final
    report.append("\n" + "=" * 80)
    total_tests = tests_passed + tests_failed
    
    if total_tests > 0:
        success_rate = (tests_passed / total_tests) * 100
        report.append(f"RESULTATS: {tests_passed}/{total_tests} tests passés ({success_rate:.0f}%)")
    else:
        report.append("RESULTATS: Aucun test exécuté")
    
    if tests_failed == 0 and tests_passed > 0:
        report.append("STATUT: TOUS LES TESTS PASSES")
    elif tests_passed > 0:
        report.append("STATUT: TESTS PARTIELLEMENT PASSES")
    else:
        report.append("STATUT: ECHEC COMPLET")
    
    report.append("=" * 80)
    
    # Sauvegarder le rapport
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(report))
    
    # Afficher le rapport
    print('\n'.join(report))
    print(f"\nRapport sauvegardé dans: {report_path}")
    
    return tests_failed == 0

def main():
    """Point d'entrée principal."""
    success = test_design_tools()
    return 0 if success else 1

if __name__ == "__main__":
    exit(main())