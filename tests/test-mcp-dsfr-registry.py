#!/usr/bin/env python3
"""
Test du registre de composants.
Version 2.0 - Aligné avec MCP DSFR - Sans émojis
"""

import time
from pathlib import Path
import sys

# Ajouter le chemin parent
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.data import get_registry


def test_registry():
    """Test le registre de composants et génère un rapport."""
    
    # Créer le rapport de test
    output_dir = Path(__file__).parent / "resultats-test"
    output_dir.mkdir(parents=True, exist_ok=True)
    report_path = output_dir / "test_registry_report.txt"
    
    report = []
    report.append("Test du Registre de Composants DSFR")
    report.append("=" * 50)
    report.append("Date: 2025-01-06")
    report.append("Version: 2.0\n")
    
    tests_passed = 0
    tests_failed = 0
    
    try:
        # Obtenir le registre (Singleton)
        registry = get_registry()
        
        # 1. Test des statistiques
        report.append("\n1. STATISTIQUES:")
        report.append("-" * 30)
        
        try:
            stats = registry.get_stats()
            report.append(f"   - Composants: {stats['components']}")
            report.append(f"   - Variantes: {stats['variants']}")
            report.append(f"   - Items en cache: {stats['cached_items']}")
            
            if stats['components'] > 0:
                report.append("   [OK] Statistiques récupérées")
                tests_passed += 1
            else:
                report.append("   [ERREUR] Aucun composant trouvé")
                tests_failed += 1
        except Exception as e:
            report.append(f"   [ERREUR] {str(e)}")
            tests_failed += 1
        
        # 2. Test de la liste des composants
        report.append("\n2. COMPOSANTS DISPONIBLES:")
        report.append("-" * 30)
        
        try:
            components = registry.list_components()
            report.append(f"   Total: {len(components)} composants")
            
            if len(components) > 0:
                examples = components[:10]
                report.append(f"   Exemples: {', '.join(examples)}")
                report.append("   [OK] Liste des composants récupérée")
                tests_passed += 1
            else:
                report.append("   [ERREUR] Liste vide")
                tests_failed += 1
        except Exception as e:
            report.append(f"   [ERREUR] {str(e)}")
            tests_failed += 1
        
        # 3. Test de récupération d'un composant
        report.append("\n3. TEST DE RECUPERATION:")
        report.append("-" * 30)
        
        # Test button
        try:
            button_html = registry.get_variant_html('button', 'primary')
            if button_html:
                report.append(f"   Button primary: {len(button_html)} caractères")
                report.append(f"      Contient 'fr-btn': {'fr-btn' in button_html}")
                report.append("   [OK] Button récupéré")
                tests_passed += 1
            else:
                report.append("   [ERREUR] Button primary non trouvé")
                tests_failed += 1
        except Exception as e:
            report.append(f"   [ERREUR] Button: {str(e)}")
            tests_failed += 1
        
        # Test alert
        try:
            alert_html = registry.get_variant_html('alert', 'info')
            if alert_html:
                report.append(f"   Alert info: {len(alert_html)} caractères")
                report.append(f"      Contient 'fr-alert': {'fr-alert' in alert_html}")
                report.append("   [OK] Alert récupéré")
                tests_passed += 1
            else:
                report.append("   [ERREUR] Alert info non trouvé")
                tests_failed += 1
        except Exception as e:
            report.append(f"   [ERREUR] Alert: {str(e)}")
            tests_failed += 1
        
        # 4. Test des variantes
        report.append("\n4. TEST DES VARIANTES:")
        report.append("-" * 30)
        
        variants_ok = 0
        for comp in ['button', 'alert', 'badge', 'form']:
            try:
                variants = registry.list_variants(comp)
                if variants:
                    report.append(f"   - {comp}: {len(variants)} variantes")
                    if len(variants) > 3:
                        report.append(f"     Exemples: {', '.join(variants[:3])}...")
                    else:
                        report.append(f"     Toutes: {', '.join(variants)}")
                    variants_ok += 1
            except:
                report.append(f"   - {comp}: Non trouvé")
        
        if variants_ok >= 3:
            report.append("   [OK] Variantes récupérées")
            tests_passed += 1
        else:
            report.append("   [ERREUR] Peu de variantes trouvées")
            tests_failed += 1
        
        # 5. Test des métadonnées
        report.append("\n5. TEST DES METADONNEES:")
        report.append("-" * 30)
        
        metadata_ok = 0
        for comp in ['button', 'form', 'alert']:
            try:
                metadata = registry.get_metadata(comp)
                if metadata:
                    desc = metadata.get('description', 'N/A')
                    report.append(f"   - {comp}: {desc[:50]}...")
                    metadata_ok += 1
            except:
                report.append(f"   - {comp}: Métadonnées non disponibles")
        
        if metadata_ok >= 2:
            report.append("   [OK] Métadonnées accessibles")
            tests_passed += 1
        else:
            report.append("   [WARN] Métadonnées partielles")
        
        # 6. Test du Singleton
        report.append("\n6. TEST DU SINGLETON:")
        report.append("-" * 30)
        
        try:
            registry2 = get_registry()
            is_same = registry is registry2
            report.append(f"   Même instance: {is_same}")
            
            if is_same:
                report.append("   [OK] Pattern Singleton respecté")
                tests_passed += 1
            else:
                report.append("   [ERREUR] Instances différentes")
                tests_failed += 1
        except Exception as e:
            report.append(f"   [ERREUR] {str(e)}")
            tests_failed += 1
        
        # 7. Test de performance (cache)
        report.append("\n7. TEST DE PERFORMANCE:")
        report.append("-" * 30)
        
        try:
            # Premier appel (sans cache ou cache froid)
            start = time.time()
            for _ in range(100):
                registry.get_component('button')
            time1 = time.time() - start
            
            # Deuxième appel (avec cache chaud)
            start = time.time()
            for _ in range(100):
                registry.get_component('button')
            time2 = time.time() - start
            
            report.append(f"   Premier appel: {time1*1000:.2f}ms")
            report.append(f"   Avec cache: {time2*1000:.2f}ms")
            
            if time2 < time1:
                improvement = time1/time2 if time2 > 0 else 1
                report.append(f"   Amélioration: {improvement:.1f}x plus rapide")
                report.append("   [OK] Cache fonctionnel")
                tests_passed += 1
            else:
                report.append("   [WARN] Cache non optimal")
        except Exception as e:
            report.append(f"   [ERREUR] {str(e)}")
            tests_failed += 1
        
        # 8. Test de robustesse
        report.append("\n8. TEST DE ROBUSTESSE:")
        report.append("-" * 30)
        
        errors_handled = 0
        
        # Test composant inexistant
        try:
            result = registry.get_variant_html('composant_inexistant', 'variant')
            if result is None or result == "":
                report.append("   [OK] Composant inexistant géré")
                errors_handled += 1
        except:
            report.append("   [OK] Exception levée pour composant inexistant")
            errors_handled += 1
        
        # Test variante inexistante
        try:
            result = registry.get_variant_html('button', 'variante_inexistante')
            if result is None or result == "" or "default" in str(result).lower():
                report.append("   [OK] Variante inexistante gérée")
                errors_handled += 1
        except:
            report.append("   [OK] Exception levée pour variante inexistante")
            errors_handled += 1
        
        if errors_handled >= 2:
            report.append("   [OK] Gestion d'erreurs robuste")
            tests_passed += 1
        else:
            report.append("   [ERREUR] Gestion d'erreurs insuffisante")
            tests_failed += 1
        
    except Exception as e:
        report.append(f"\n[ERREUR CRITIQUE] Impossible d'initialiser le registre: {str(e)}")
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
        report.append("STATUT: REGISTRE FONCTIONNEL ET OPTIMISE")
    elif tests_passed > tests_failed:
        report.append("STATUT: REGISTRE PARTIELLEMENT FONCTIONNEL")
    else:
        report.append("STATUT: REGISTRE DEFAILLANT")
    
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
    success = test_registry()
    return 0 if success else 1


if __name__ == "__main__":
    exit(main())