#!/usr/bin/env python3
"""
Tests d'intégration pour le serveur MCP DSFR.
Version 2.0 - Sans dépendances externes - Sans émojis
"""

import json
from pathlib import Path
import sys

# Ajouter le chemin parent
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.services import get_generator, get_validator, get_audit_service, get_cognitive_service
from src.data import get_registry


class TestMCPIntegration:
    """Tests d'intégration des services MCP."""
    
    def __init__(self):
        self.generator = get_generator()
        self.validator = get_validator()
        self.audit = get_audit_service()
        self.cognitive = get_cognitive_service()
        self.registry = get_registry()
        self.report = []
        self.tests_passed = 0
        self.tests_failed = 0
    
    def test_generate_component_flow(self):
        """Test le flow complet de génération de composant."""
        self.report.append("\nTEST: Génération de composant")
        self.report.append("-" * 40)
        
        try:
            # Générer un bouton
            html = self.generator.generate(
                "button",
                variant="primary",
                label="Test Button",
                icon="save-line"
            )
            
            # Vérifications
            if html and "fr-btn" in html and "Test Button" in html:
                self.report.append("[OK] Bouton généré correctement")
                self.report.append(f"    Taille HTML: {len(html)} caractères")
                self.tests_passed += 1
            else:
                self.report.append("[ERREUR] Génération incorrecte")
                self.tests_failed += 1
                
        except Exception as e:
            self.report.append(f"[ERREUR] {str(e)}")
            self.tests_failed += 1
    
    def test_validate_html_flow(self):
        """Test le flow de validation HTML/RGAA."""
        self.report.append("\nTEST: Validation HTML")
        self.report.append("-" * 40)
        
        try:
            # HTML à valider
            test_html = """
            <button class="fr-btn fr-btn--primary">
                <span class="fr-icon-save-line fr-icon--left"></span>
                Sauvegarder
            </button>
            """
            
            result = self.validator.validate(test_html)
            
            if result and "score" in result:
                self.report.append(f"[OK] Validation effectuée")
                self.report.append(f"    Score: {result['score']}/100")
                self.report.append(f"    Erreurs: {len(result.get('errors', []))}")
                self.report.append(f"    Avertissements: {len(result.get('warnings', []))}")
                self.tests_passed += 1
            else:
                self.report.append("[ERREUR] Validation échouée")
                self.tests_failed += 1
                
        except Exception as e:
            self.report.append(f"[ERREUR] {str(e)}")
            self.tests_failed += 1
    
    def test_list_components_flow(self):
        """Test la liste des composants disponibles."""
        self.report.append("\nTEST: Liste des composants")
        self.report.append("-" * 40)
        
        try:
            components = self.registry.list_components()
            
            if components and len(components) > 0:
                self.report.append(f"[OK] {len(components)} composants disponibles")
                # Afficher quelques exemples
                examples = components[:5]
                self.report.append(f"    Exemples: {', '.join(examples)}")
                self.tests_passed += 1
            else:
                self.report.append("[ERREUR] Aucun composant trouvé")
                self.tests_failed += 1
                
        except Exception as e:
            self.report.append(f"[ERREUR] {str(e)}")
            self.tests_failed += 1
    
    def test_cognitive_analysis_flow(self):
        """Test l'analyse cognitive Rumsfeld."""
        self.report.append("\nTEST: Analyse cognitive")
        self.report.append("-" * 40)
        
        try:
            result = self.cognitive.analyze_request(
                "Je veux créer un formulaire de contact simple"
            )
            
            if result and all(k in result for k in ["known_knowns", "known_unknowns", "unknown_knowns", "unknown_unknowns"]):
                self.report.append("[OK] Analyse cognitive complète")
                self.report.append(f"    Known knowns: {len(result['known_knowns'])}")
                self.report.append(f"    Known unknowns: {len(result['known_unknowns'])}")
                self.report.append(f"    Unknown knowns: {len(result['unknown_knowns'])}")
                self.report.append(f"    Unknown unknowns: {len(result['unknown_unknowns'])}")
                self.tests_passed += 1
            else:
                self.report.append("[ERREUR] Analyse incomplète")
                self.tests_failed += 1
                
        except Exception as e:
            self.report.append(f"[ERREUR] {str(e)}")
            self.tests_failed += 1
    
    def test_accessibility_audit_flow(self):
        """Test l'audit d'accessibilité RGAA."""
        self.report.append("\nTEST: Audit d'accessibilité")
        self.report.append("-" * 40)
        
        try:
            test_html = """
            <div class="fr-card">
                <img src="test.jpg" alt="">
                <div class="fr-card__body">
                    <h3>Titre sans niveau</h3>
                    <p style="color: #666">Texte avec faible contraste</p>
                </div>
            </div>
            """
            
            result = self.audit.audit(test_html, level="AA")
            
            if result and "score" in result:
                self.report.append(f"[OK] Audit effectué")
                self.report.append(f"    Score: {result['score']}/100")
                self.report.append(f"    Niveau: {result.get('level', 'AA')}")
                
                # Afficher quelques problèmes détectés
                if result.get('errors'):
                    self.report.append(f"    Erreurs critiques: {len(result['errors'])}")
                    for error in result['errors'][:2]:
                        self.report.append(f"      - {error}")
                
                self.tests_passed += 1
            else:
                self.report.append("[ERREUR] Audit échoué")
                self.tests_failed += 1
                
        except Exception as e:
            self.report.append(f"[ERREUR] {str(e)}")
            self.tests_failed += 1
    
    def test_component_variants_flow(self):
        """Test la récupération des variantes de composants."""
        self.report.append("\nTEST: Variantes de composants")
        self.report.append("-" * 40)
        
        try:
            # Tester quelques composants
            test_components = ["button", "alert", "form", "card", "modal"]
            
            variants_found = 0
            for comp in test_components:
                try:
                    variants = self.registry.get_component_variants(comp)
                    if variants:
                        variants_found += len(variants)
                        self.report.append(f"    {comp}: {len(variants)} variante(s)")
                except:
                    pass
            
            if variants_found > 0:
                self.report.append(f"[OK] {variants_found} variantes trouvées au total")
                self.tests_passed += 1
            else:
                self.report.append("[ERREUR] Aucune variante trouvée")
                self.tests_failed += 1
                
        except Exception as e:
            self.report.append(f"[ERREUR] {str(e)}")
            self.tests_failed += 1
    
    def test_error_handling(self):
        """Test la gestion des erreurs."""
        self.report.append("\nTEST: Gestion des erreurs")
        self.report.append("-" * 40)
        
        errors_handled = 0
        
        # Test 1: Composant inexistant
        try:
            html = self.generator.generate("composant_inexistant")
            if "non trouvé" in html.lower() or "error" in html.lower():
                self.report.append("    [OK] Erreur composant inexistant gérée")
                errors_handled += 1
        except:
            self.report.append("    [OK] Exception composant inexistant levée")
            errors_handled += 1
        
        # Test 2: HTML invalide
        try:
            result = self.validator.validate("<div><div><div>")
            if result and result.get('score', 100) < 50:
                self.report.append("    [OK] HTML invalide détecté")
                errors_handled += 1
        except:
            self.report.append("    [OK] Exception HTML invalide levée")
            errors_handled += 1
        
        if errors_handled >= 2:
            self.report.append("[OK] Gestion des erreurs fonctionnelle")
            self.tests_passed += 1
        else:
            self.report.append("[ERREUR] Gestion des erreurs insuffisante")
            self.tests_failed += 1
    
    def run_all_tests(self):
        """Exécute tous les tests d'intégration."""
        self.report.append("="*60)
        self.report.append("TESTS D'INTEGRATION MCP DSFR")
        self.report.append("="*60)
        self.report.append("Date: 2025-01-06")
        self.report.append("Version: 2.0\n")
        
        # Exécuter les tests
        self.test_generate_component_flow()
        self.test_validate_html_flow()
        self.test_list_components_flow()
        self.test_cognitive_analysis_flow()
        self.test_accessibility_audit_flow()
        self.test_component_variants_flow()
        self.test_error_handling()
        
        # Résumé
        self.report.append("\n" + "="*60)
        total_tests = self.tests_passed + self.tests_failed
        
        if total_tests > 0:
            success_rate = (self.tests_passed / total_tests) * 100
            self.report.append(f"RESULTATS: {self.tests_passed}/{total_tests} tests passés ({success_rate:.0f}%)")
        else:
            self.report.append("RESULTATS: Aucun test exécuté")
        
        if self.tests_failed == 0 and self.tests_passed > 0:
            self.report.append("STATUT: INTEGRATION VALIDEE")
        elif success_rate >= 50:  # Considérer comme fonctionnel à partir de 50%
            self.report.append("STATUT: INTEGRATION FONCTIONNELLE")
        else:
            self.report.append("STATUT: INTEGRATION ECHOUEE")
        
        self.report.append("="*60)
        
        return '\n'.join(self.report)


def main():
    """Point d'entrée principal."""
    # Créer le rapport de test
    output_dir = Path(__file__).parent / "resultats-test"
    output_dir.mkdir(parents=True, exist_ok=True)
    report_path = output_dir / "test_integration_mcp_report.txt"
    
    try:
        # Exécuter les tests
        tester = TestMCPIntegration()
        report = tester.run_all_tests()
        
        # Sauvegarder le rapport
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(report)
        
        # Afficher le rapport
        print(report)
        print(f"\nRapport sauvegardé dans: {report_path}")
        
        # Retourner le code de sortie
        return 0 if tester.tests_failed == 0 else 1
        
    except Exception as e:
        error_msg = f"[ERREUR CRITIQUE] Impossible d'exécuter les tests: {str(e)}"
        print(error_msg)
        
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(error_msg)
        
        return 1


if __name__ == "__main__":
    exit(main())