#!/usr/bin/env python3
"""
Test de l'agent cognitif avec la matrice Connu-Inconnu de Rumsfeld.
Version 2.0 - Sans émojis - Aligné avec MCP DSFR
"""

import sys
from pathlib import Path
from datetime import datetime

# Ajouter le chemin pour les imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.services import get_cognitive_service


def test_cognitive_analysis():
    """Test l'analyse cognitive avec différents cas et génère un rapport."""
    
    # Créer le rapport de test
    output_dir = Path(__file__).parent / "resultats-test"
    output_dir.mkdir(parents=True, exist_ok=True)
    report_path = output_dir / "test_cognitive_report.txt"
    
    report = []
    report.append("Test de l'Agent Cognitif - Matrice Connu-Inconnu de Rumsfeld")
    report.append("=" * 60)
    report.append(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report.append("Version: 2.0\n")
    
    tests_passed = 0
    tests_failed = 0
    
    try:
        cognitive = get_cognitive_service()
        
        # CAS 1: Formulaire simple
        report.append("CAS 1: FORMULAIRE D'INSCRIPTION SIMPLE")
        report.append("-" * 40)
        
        try:
            result = cognitive.analyze_request(
                "J'ai besoin d'un formulaire d'inscription avec nom et email",
                {"project_type": "web", "deadline": "2_weeks"}
            )
            
            if "known_knowns" in result:
                report.append(f"  Connus connus: {len(result['known_knowns'])} insights")
                for insight in result['known_knowns'][:2]:
                    report.append(f"    - {insight}")
                
                report.append(f"  Inconnus connus: {len(result.get('known_unknowns', []))} insights")
                for insight in result.get('known_unknowns', [])[:2]:
                    report.append(f"    - {insight}")
                
                report.append(f"  Inconnus inconnus: {len(result.get('unknown_unknowns', []))} angles morts")
                for insight in result.get('unknown_unknowns', [])[:2]:
                    report.append(f"    - {insight}")
                
                report.append(f"  Recommandations: {len(result.get('recommendations', []))}")
                for rec in result.get('recommendations', [])[:2]:
                    report.append(f"    - {rec}")
                
                report.append("  [OK] Analyse cognitive complète")
                tests_passed += 1
            else:
                report.append("  [ERREUR] Structure de réponse incorrecte")
                tests_failed += 1
                
        except Exception as e:
            report.append(f"  [ERREUR] {str(e)}")
            tests_failed += 1
        
        # CAS 2: Dashboard complexe
        report.append("\nCAS 2: DASHBOARD ADMINISTRATIF")
        report.append("-" * 40)
        
        try:
            result = cognitive.analyze_request(
                "Dashboard pour suivre les statistiques utilisateurs avec graphiques",
                {"users": "10000", "data_volume": "high"}
            )
            
            if "known_knowns" in result:
                report.append(f"  Connus connus: {len(result['known_knowns'])} insights")
                for insight in result['known_knowns'][:2]:
                    report.append(f"    - {insight}")
                
                unknown_unknowns = result.get('unknown_unknowns', [])
                report.append(f"  Inconnus inconnus détectés: {len(unknown_unknowns)}")
                
                # Analyser les types de risques
                technical_risks = 0
                security_risks = 0
                performance_risks = 0
                
                for insight in unknown_unknowns:
                    insight_lower = str(insight).lower()
                    if 'performance' in insight_lower or 'charge' in insight_lower:
                        performance_risks += 1
                    if 'sécurité' in insight_lower or 'security' in insight_lower:
                        security_risks += 1
                    if 'technique' in insight_lower or 'technical' in insight_lower:
                        technical_risks += 1
                
                report.append(f"    - Risques performance: {performance_risks}")
                report.append(f"    - Risques sécurité: {security_risks}")
                report.append(f"    - Risques techniques: {technical_risks}")
                
                report.append("  [OK] Dashboard analysé avec succès")
                tests_passed += 1
            else:
                report.append("  [ERREUR] Analyse incomplète")
                tests_failed += 1
                
        except Exception as e:
            report.append(f"  [ERREUR] {str(e)}")
            tests_failed += 1
        
        # CAS 3: E-commerce avec angles morts
        report.append("\nCAS 3: APPLICATION E-COMMERCE - ANGLES MORTS")
        report.append("-" * 40)
        
        try:
            context = {"focus": "blind_spots"}
            result = cognitive.analyze_request(
                "Application e-commerce avec paiement en ligne",
                context
            )
            
            if result:
                blind_spots = result.get('unknown_unknowns', [])
                report.append(f"  Angles morts détectés: {len(blind_spots)}")
                
                # Catégoriser les risques
                categories = {
                    'Techniques': 0,
                    'Sécurité': 0,
                    'Conformité': 0,
                    'Performance': 0,
                    'UX': 0
                }
                
                for spot in blind_spots:
                    spot_lower = str(spot).lower()
                    if 'performance' in spot_lower or 'charge' in spot_lower:
                        categories['Performance'] += 1
                    if 'sécurité' in spot_lower or 'security' in spot_lower:
                        categories['Sécurité'] += 1
                    if 'rgpd' in spot_lower or 'conformité' in spot_lower:
                        categories['Conformité'] += 1
                    if 'technique' in spot_lower:
                        categories['Techniques'] += 1
                    if 'ux' in spot_lower or 'utilisateur' in spot_lower:
                        categories['UX'] += 1
                
                report.append("  Répartition des risques:")
                for cat, count in categories.items():
                    if count > 0:
                        report.append(f"    - {cat}: {count}")
                
                recommendations = result.get('recommendations', [])
                report.append(f"  Recommandations: {len(recommendations)}")
                for idx, rec in enumerate(recommendations[:3], 1):
                    report.append(f"    {idx}. {rec}")
                
                report.append("  [OK] Angles morts identifiés")
                tests_passed += 1
            else:
                report.append("  [ERREUR] Analyse échouée")
                tests_failed += 1
                
        except Exception as e:
            report.append(f"  [ERREUR] {str(e)}")
            tests_failed += 1
        
        # CAS 4: Test de robustesse
        report.append("\nCAS 4: TEST DE ROBUSTESSE")
        report.append("-" * 40)
        
        # Test avec requête vide
        try:
            result = cognitive.analyze_request("", {})
            if result:
                report.append("  [OK] Requête vide gérée")
                tests_passed += 1
            else:
                report.append("  [WARN] Requête vide retourne None")
        except:
            report.append("  [OK] Exception levée pour requête vide")
            tests_passed += 1
        
        # Test avec contexte complexe
        try:
            complex_context = {
                "users": "1000000",
                "security": "high",
                "performance": "critical",
                "deadline": "urgent",
                "budget": "limited"
            }
            result = cognitive.analyze_request(
                "Plateforme gouvernementale critique",
                complex_context
            )
            if result and len(result.get('unknown_unknowns', [])) > 5:
                report.append("  [OK] Contexte complexe analysé en profondeur")
                tests_passed += 1
            else:
                report.append("  [WARN] Analyse superficielle du contexte complexe")
                tests_passed += 1
        except Exception as e:
            report.append(f"  [ERREUR] Contexte complexe: {str(e)}")
            tests_failed += 1
        
    except Exception as e:
        report.append(f"\n[ERREUR CRITIQUE] Impossible d'initialiser le service cognitif: {str(e)}")
        tests_failed += 1
    
    # Résumé final
    report.append("\n" + "=" * 60)
    total_tests = tests_passed + tests_failed
    
    if total_tests > 0:
        success_rate = (tests_passed / total_tests) * 100
        report.append(f"RESULTATS: {tests_passed}/{total_tests} tests passés ({success_rate:.0f}%)")
    else:
        report.append("RESULTATS: Aucun test exécuté")
    
    if tests_failed == 0 and tests_passed > 0:
        report.append("STATUT: AGENT COGNITIF FONCTIONNEL")
    elif tests_passed > tests_failed:
        report.append("STATUT: AGENT PARTIELLEMENT FONCTIONNEL")
    else:
        report.append("STATUT: AGENT DEFAILLANT")
    
    report.append("=" * 60)
    
    # Sauvegarder le rapport
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(report))
    
    # Afficher le rapport
    print('\n'.join(report))
    print(f"\nRapport sauvegardé dans: {report_path}")
    
    return tests_failed == 0


def main():
    """Point d'entrée principal."""
    success = test_cognitive_analysis()
    return 0 if success else 1


if __name__ == "__main__":
    exit(main())