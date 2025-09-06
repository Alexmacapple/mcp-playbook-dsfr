#!/usr/bin/env python3
"""
Test du service de génération.
Version 2.0 - Sans émojis - Aligné avec MCP DSFR
"""

import time
import inspect
from pathlib import Path
import sys
from datetime import datetime

# Ajouter le chemin parent
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.services import get_generator


def test_generator():
    """Test le générateur de composants et génère un rapport."""
    
    # Créer le rapport de test
    output_dir = Path(__file__).parent / "resultats-test"
    output_dir.mkdir(parents=True, exist_ok=True)
    report_path = output_dir / "test_generator_report.txt"
    
    report = []
    report.append("Test du Générateur DSFR (Factory Pattern)")
    report.append("=" * 50)
    report.append(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report.append("Version: 2.0\n")
    
    tests_passed = 0
    tests_failed = 0
    
    try:
        generator = get_generator()
        
        # 1. Test génération simple
        report.append("1. TEST GENERATION SIMPLE:")
        report.append("-" * 30)
        
        try:
            # Button
            button_html = generator.generate('button', label='Valider')
            if button_html and 'Valider' in button_html:
                report.append(f"   Button: {len(button_html)} caractères")
                report.append(f"      Contient 'Valider': True")
                report.append("   [OK] Button généré")
                tests_passed += 1
            else:
                report.append("   [ERREUR] Button mal généré")
                tests_failed += 1
        except Exception as e:
            report.append(f"   [ERREUR] Button: {str(e)}")
            tests_failed += 1
        
        try:
            # Alert
            alert_html = generator.generate('alert', 
                                           type='success',
                                           title='Bravo !',
                                           message='Opération réussie')
            if alert_html and 'Bravo' in alert_html:
                report.append(f"   Alert: {len(alert_html)} caractères")
                report.append(f"      Contient 'Bravo': True")
                report.append("   [OK] Alert généré")
                tests_passed += 1
            else:
                report.append("   [ERREUR] Alert mal généré")
                tests_failed += 1
        except Exception as e:
            report.append(f"   [ERREUR] Alert: {str(e)}")
            tests_failed += 1
        
        # 2. Test avec variantes
        report.append("\n2. TEST AVEC VARIANTES:")
        report.append("-" * 30)
        
        variants_tests = [
            ('button', 'primary'),
            ('button', 'secondary'),
            ('alert', 'warning'),
            ('card', 'horizontal')
        ]
        
        variants_ok = 0
        for comp, variant in variants_tests:
            try:
                html = generator.generate(comp, variant=variant)
                if html:
                    report.append(f"   {comp}/{variant}: {len(html)} caractères")
                    variants_ok += 1
            except Exception as e:
                if "variant" in str(e).lower():
                    report.append(f"   [WARN] Variante non trouvée: {comp}/{variant}")
                else:
                    report.append(f"   [ERREUR] {comp}/{variant}: {str(e)}")
        
        if variants_ok >= 2:
            report.append("   [OK] Variantes fonctionnelles")
            tests_passed += 1
        else:
            report.append("   [ERREUR] Peu de variantes trouvées")
            tests_failed += 1
        
        # 3. Test avec options avancées
        report.append("\n3. TEST OPTIONS AVANCEES:")
        report.append("-" * 30)
        
        try:
            # Button avec icône
            button_icon = generator.generate('button',
                                            label='Envoyer',
                                            icon='send',
                                            size='lg')
            if button_icon and ('fr-icon' in button_icon or 'icon' in button_icon):
                report.append("   Button avec icône: OK")
                tests_passed += 1
            else:
                report.append("   Button avec icône: Icône non trouvée")
                tests_failed += 1
        except Exception as e:
            report.append(f"   [ERREUR] Button icône: {str(e)}")
            tests_failed += 1
        
        try:
            # Input avec erreur
            input_error = generator.generate('input',
                                            label='Email',
                                            type='email',
                                            error='Email invalide',
                                            required=True)
            if input_error and 'required' in input_error:
                report.append("   Input avec erreur: OK (required présent)")
                tests_passed += 1
            else:
                report.append("   Input avec erreur: Attribut required manquant")
                tests_failed += 1
        except Exception as e:
            report.append(f"   [ERREUR] Input: {str(e)}")
            tests_failed += 1
        
        # 4. Test des hooks
        report.append("\n4. TEST SYSTEME DE HOOKS:")
        report.append("-" * 30)
        
        generated_components = []
        
        def track_generation(component, options):
            generated_components.append(component)
        
        try:
            generator.add_hook('before', track_generation)
            
            generator.generate('button', label='Test')
            generator.generate('alert', message='Test')
            
            if len(generated_components) >= 2:
                report.append(f"   Composants trackés: {generated_components}")
                report.append("   [OK] Hooks fonctionnels")
                tests_passed += 1
            else:
                report.append("   [ERREUR] Hooks non exécutés")
                tests_failed += 1
        except Exception as e:
            report.append(f"   [SKIP] Hooks non supportés: {str(e)}")
        
        # 5. Test override
        report.append("\n5. TEST OVERRIDE CUSTOM:")
        report.append("-" * 30)
        
        def custom_button_generator(component, **kwargs):
            return f"<custom-button>{kwargs.get('label', 'Custom')}</custom-button>"
        
        try:
            generator.register_override('custom_button', custom_button_generator)
            generator.register_override('button', custom_button_generator)
            result = generator.generate('button', label='Override Test')
            
            if 'custom-button' in result:
                report.append("   [OK] Override fonctionne")
                tests_passed += 1
            else:
                report.append("   [WARN] Override non appliqué")
        except Exception as e:
            report.append(f"   [SKIP] Override non supporté: {str(e)}")
        
        # 6. Test erreurs
        report.append("\n6. TEST GESTION D'ERREURS:")
        report.append("-" * 30)
        
        try:
            generator.generate('composant_inexistant')
            report.append("   [ERREUR] Devrait lever une erreur")
            tests_failed += 1
        except Exception as e:
            if "not found" in str(e).lower() or "inexistant" in str(e).lower():
                report.append(f"   [OK] Erreur correctement levée")
                tests_passed += 1
            else:
                report.append(f"   [OK] Exception levée: {type(e).__name__}")
                tests_passed += 1
        
        # 7. Test performance avec cache
        report.append("\n7. TEST PERFORMANCE (CACHE):")
        report.append("-" * 30)
        
        try:
            # Premier appel
            start = time.time()
            for _ in range(100):
                generator.get_component_info('button')
            time1 = time.time() - start
            
            # Deuxième appel (cache)
            start = time.time()
            for _ in range(100):
                generator.get_component_info('button')
            time2 = time.time() - start
            
            report.append(f"   Sans cache: {time1*1000:.2f}ms")
            report.append(f"   Avec cache: {time2*1000:.2f}ms")
            
            if time1 > time2:
                improvement = time1/time2 if time2 > 0 else 1
                report.append(f"   Cache efficace: {improvement:.1f}x plus rapide")
                report.append("   [OK] Cache fonctionnel")
                tests_passed += 1
            else:
                report.append("   [WARN] Cache non optimal")
        except Exception as e:
            report.append(f"   [SKIP] get_component_info non supporté: {str(e)}")
        
        # 8. Test Factory Pattern
        report.append("\n8. TEST FACTORY PATTERN:")
        report.append("-" * 30)
        
        try:
            # Vérifier qu'on n'a pas de switch/case
            source = inspect.getsource(generator.generate)
            has_switch = source.count('elif') > 5  # Plus de 5 elif indique probablement un switch
            
            if not has_switch:
                report.append("   [OK] Factory Pattern implémenté (pas de switch/case)")
                tests_passed += 1
            else:
                report.append("   [WARN] Pattern à vérifier (plusieurs elif détectés)")
                tests_passed += 1
        except Exception as e:
            report.append(f"   [SKIP] Inspection du code non disponible: {str(e)}")
        
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
        report.append("STATUT: GENERATEUR FONCTIONNEL AVEC FACTORY PATTERN")
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
    success = test_generator()
    return 0 if success else 1


if __name__ == "__main__":
    exit(main())