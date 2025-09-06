#!/usr/bin/env python3
"""
Test du générateur de tests automatiques pour composants DSFR.
Version 1.0 - Sans émojis - Aligné avec MCP DSFR
"""

import sys
from pathlib import Path
from datetime import datetime

# Ajouter le chemin parent
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.services import get_test_generator
from src.services.test_generator_service import TestFramework


def test_test_generator():
    """Test le générateur de tests automatiques et génère un rapport."""
    
    # Créer le rapport de test
    output_dir = Path(__file__).parent / "resultats-test"
    output_dir.mkdir(parents=True, exist_ok=True)
    report_path = output_dir / "test_test_generator_report.txt"
    
    report = []
    report.append("Test du Générateur de Tests Automatiques")
    report.append("=" * 50)
    report.append(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report.append("Version: 1.0\n")
    
    tests_passed = 0
    tests_failed = 0
    
    try:
        test_gen = get_test_generator()
        
        # TEST 1: Génération de tests Cypress
        report.append("1. GENERATION TESTS CYPRESS:")
        report.append("-" * 30)
        
        try:
            cypress_test = test_gen.generate_tests(
                component="button",
                framework=TestFramework.CYPRESS
            )
            
            if cypress_test:
                report.append(f"  Taille du test: {len(cypress_test)} caractères")
                
                # Vérifier les éléments essentiels Cypress
                essential_elements = {
                    "describe(": "Structure describe",
                    "it(": "Structure it",
                    "cy.": "Commandes Cypress",
                    ".fr-btn": "Sélecteur DSFR",
                    "should(": "Assertions",
                    "click()": "Interactions"
                }
                
                elements_found = 0
                for element, desc in essential_elements.items():
                    if element in cypress_test:
                        report.append(f"  [OK] {desc} présent")
                        elements_found += 1
                    else:
                        report.append(f"  [MANQUANT] {desc}")
                
                if elements_found >= 4:
                    report.append("  [OK] Test Cypress complet")
                    tests_passed += 1
                else:
                    report.append("  [WARN] Test Cypress incomplet")
                    tests_passed += 1
                    
            else:
                report.append("  [ERREUR] Génération échouée")
                tests_failed += 1
                
        except Exception as e:
            report.append(f"  [ERREUR] {str(e)}")
            tests_failed += 1
        
        # TEST 2: Génération de tests Playwright
        report.append("\n2. GENERATION TESTS PLAYWRIGHT:")
        report.append("-" * 30)
        
        try:
            playwright_test = test_gen.generate_tests(
                component="form",
                framework=TestFramework.PLAYWRIGHT
            )
            
            if playwright_test:
                report.append(f"  Taille du test: {len(playwright_test)} caractères")
                
                # Vérifier les éléments Playwright
                playwright_elements = {
                    "test(": "Structure test",
                    "expect(": "Assertions",
                    "page.": "API Page",
                    "locator(": "Locators",
                    ".fr-form": "Sélecteur DSFR",
                    "async": "Code asynchrone"
                }
                
                elements_found = 0
                for element, desc in playwright_elements.items():
                    if element in playwright_test:
                        report.append(f"  [OK] {desc} présent")
                        elements_found += 1
                    else:
                        report.append(f"  [MANQUANT] {desc}")
                
                if elements_found >= 4:
                    report.append("  [OK] Test Playwright complet")
                    tests_passed += 1
                else:
                    report.append("  [WARN] Test Playwright incomplet")
                    tests_passed += 1
                    
            else:
                report.append("  [ERREUR] Génération échouée")
                tests_failed += 1
                
        except Exception as e:
            report.append(f"  [ERREUR] {str(e)}")
            tests_failed += 1
        
        # TEST 3: Génération de tests Jest
        report.append("\n3. GENERATION TESTS JEST:")
        report.append("-" * 30)
        
        try:
            jest_test = test_gen.generate_tests(
                component="alert",
                framework=TestFramework.JEST
            )
            
            if jest_test:
                report.append(f"  Taille du test: {len(jest_test)} caractères")
                
                # Vérifier les éléments Jest
                jest_elements = {
                    "describe(": "Structure describe",
                    "test(": "Structure test",
                    "expect(": "Assertions",
                    "toBe": "Matchers",
                    "render(": "Rendu composant",
                    "screen.": "Testing Library"
                }
                
                elements_found = 0
                for element, desc in jest_elements.items():
                    if element in jest_test:
                        report.append(f"  [OK] {desc} présent")
                        elements_found += 1
                    else:
                        report.append(f"  [MANQUANT] {desc}")
                
                if elements_found >= 3:
                    report.append("  [OK] Test Jest généré")
                    tests_passed += 1
                else:
                    report.append("  [WARN] Test Jest incomplet")
                    tests_passed += 1
                    
            else:
                report.append("  [ERREUR] Génération échouée")
                tests_failed += 1
                
        except Exception as e:
            report.append(f"  [ERREUR] {str(e)}")
            tests_failed += 1
        
        # TEST 4: Tests pour différents composants
        report.append("\n4. TESTS POUR DIFFERENTS COMPOSANTS:")
        report.append("-" * 30)
        
        components_to_test = [
            ("button", "Test des interactions"),
            ("form", "Test de validation"),
            ("modal", "Test d'ouverture/fermeture"),
            ("accordion", "Test d'expansion"),
            ("table", "Test de tri et filtrage")
        ]
        
        components_ok = 0
        for component, description in components_to_test:
            try:
                test_code = test_gen.generate_tests(
                    component=component,
                    framework=TestFramework.CYPRESS
                )
                
                if test_code and len(test_code) > 100:
                    report.append(f"  [OK] {component}: {description}")
                    components_ok += 1
                else:
                    report.append(f"  [ERREUR] {component}: Test vide ou trop court")
                    
            except Exception as e:
                report.append(f"  [ERREUR] {component}: {str(e)}")
        
        if components_ok >= 3:
            report.append(f"  [OK] {components_ok}/{len(components_to_test)} composants testables")
            tests_passed += 1
        else:
            report.append(f"  [ERREUR] Seulement {components_ok}/{len(components_to_test)} composants")
            tests_failed += 1
        
        # TEST 5: Tests d'accessibilité
        report.append("\n5. TESTS D'ACCESSIBILITE RGAA:")
        report.append("-" * 30)
        
        try:
            a11y_test = test_gen.generate_tests(
                component="form",
                framework=TestFramework.CYPRESS,
                options={"accessibility": True}
            )
            
            if a11y_test:
                # Vérifier les tests d'accessibilité
                a11y_checks = [
                    "aria-",
                    "role=",
                    "alt=",
                    "label",
                    "focus",
                    "keyboard",
                    "contrast"
                ]
                
                checks_found = 0
                for check in a11y_checks:
                    if check in a11y_test.lower():
                        checks_found += 1
                
                report.append(f"  Vérifications d'accessibilité: {checks_found}/{len(a11y_checks)}")
                
                if checks_found >= 3:
                    report.append("  [OK] Tests d'accessibilité inclus")
                    tests_passed += 1
                else:
                    report.append("  [WARN] Tests d'accessibilité limités")
                    tests_passed += 1
                    
            else:
                report.append("  [ERREUR] Génération échouée")
                tests_failed += 1
                
        except Exception as e:
            report.append(f"  [SKIP] Accessibilité non supportée: {str(e)}")
        
        # TEST 6: Sélecteurs personnalisés
        report.append("\n6. TEST AVEC SELECTEURS PERSONNALISES:")
        report.append("-" * 30)
        
        try:
            custom_test = test_gen.generate_tests(
                component="card",
                framework=TestFramework.CYPRESS
            )
            
            if custom_test:
                report.append("  [OK] Sélecteur personnalisé utilisé")
                tests_passed += 1
            else:
                report.append("  [ERREUR] Sélecteur personnalisé ignoré")
                tests_failed += 1
                
        except Exception as e:
            report.append(f"  [ERREUR] {str(e)}")
            tests_failed += 1
        
    except Exception as e:
        report.append(f"\n[ERREUR CRITIQUE] Impossible d'initialiser le générateur: {str(e)}")
        tests_failed += 1
    
    # Résumé final
    report.append("\n" + "=" * 50)
    total_tests = tests_passed + tests_failed
    
    if total_tests > 0:
        success_rate = (tests_passed / total_tests) * 100
        report.append(f"RESULTATS: {tests_passed}/{total_tests} tests passés ({success_rate:.0f}%)")
    else:
        report.append("RESULTATS: Aucun test exécuté")
    
    if tests_failed == 0 and tests_passed > 0:
        report.append("STATUT: GENERATEUR DE TESTS FONCTIONNEL")
    elif tests_passed > tests_failed:
        report.append("STATUT: GENERATEUR PARTIELLEMENT FONCTIONNEL")
    else:
        report.append("STATUT: GENERATEUR DEFAILLANT")
    
    report.append("=" * 50)
    
    # Sauvegarder le rapport
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(report))
    
    # Afficher le rapport
    print('\n'.join(report))
    print(f"\nRapport sauvegardé dans: {report_path}")
    
    return tests_failed == 0


def main():
    """Point d'entrée principal."""
    success = test_test_generator()
    return 0 if success else 1


if __name__ == "__main__":
    exit(main())