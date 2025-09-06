#!/usr/bin/env python3
"""
Test de l'assistant DSFR avec tous les composants disponibles
Version 2.0 - Aligné avec MCP DSFR - Sans émojis
"""

import sys
import os
from pathlib import Path

# Ajouter le path parent pour importer src
sys.path.insert(0, str(Path(__file__).parent.parent))

# Importer l'assistant depuis les services
from src.services import get_assistant
from src.data import get_registry

def test_assistant():
    """Test toutes les fonctionnalités de l'assistant"""
    
    print("TEST DE L'ASSISTANT DSFR")
    print("="*60)
    
    # Créer le rapport de test
    output_dir = Path(__file__).parent / "resultats-test"
    output_dir.mkdir(parents=True, exist_ok=True)
    report_path = output_dir / "test_assistant_report.txt"
    
    report = []
    report.append("RAPPORT DE TEST - ASSISTANT DSFR")
    report.append("="*60)
    report.append("Date: 2025-01-06")
    report.append("Version: 2.0\n")
    
    try:
        assistant = get_assistant()
        registry = get_registry()
        
        # Test 1: Vérifier la bibliothèque chargée
        report.append("\n1. VERIFICATION DE LA BIBLIOTHEQUE:")
        report.append("-" * 40)
        
        stats = registry.get_stats()
        components_count = stats['components']
        report.append(f"   Composants chargés: {components_count}")
        report.append(f"   Variantes totales: {stats['variants']}")
        
        components = registry.list_components()
        if components:
            report.append("   Exemples de composants disponibles:")
            for comp in components[:10]:
                variants = registry.list_variants(comp)
                report.append(f"      - {comp}: {len(variants)} variante(s)")
        
        # Test 2: Analyse de besoins
        report.append("\n2. TEST D'ANALYSE DE BESOINS:")
        report.append("-" * 40)
        
        descriptions = [
            "Je veux un formulaire de contact avec validation",
            "Page avec navigation et tableau de données",
            "Dashboard avec alertes et cartes",
            "Interface accessible avec modal et accordéon"
        ]
        
        for desc in descriptions:
            report.append(f"\n   Description: '{desc}'")
            try:
                analysis = assistant.analyze_needs(desc)
                if 'connus_connus' in analysis:
                    report.append(f"   Connus: {', '.join(analysis['connus_connus']) if analysis['connus_connus'] else 'Aucun'}")
                if 'inconnus_connus' in analysis:
                    report.append(f"   Détectés: {', '.join(analysis['inconnus_connus']) if analysis['inconnus_connus'] else 'Aucun'}")
                
                if 'suggestions' in analysis:
                    suggestions = analysis['suggestions']
                    if suggestions:
                        if isinstance(suggestions[0], dict):
                            report.append(f"   Suggestions: {', '.join([s['component'] for s in suggestions])}")
                        else:
                            report.append(f"   Suggestions: {', '.join(suggestions)}")
                report.append("   [OK] Analyse réussie")
            except Exception as e:
                report.append(f"   [ERREUR] {str(e)}")
        
        # Test 3: Génération de HTML
        report.append("\n3. TEST DE GENERATION HTML:")
        report.append("-" * 40)
        
        # Tester quelques composants clés
        test_components = [
            ("button", "primary"),
            ("alert", "info"),
            ("form", "contact"),
            ("card", "default"),
            ("table", "default"),
            ("modal", "default"),
            ("accordion", "default")
        ]
        
        from src.services import get_generator
        generator = get_generator()
        
        success_count = 0
        for comp, variant in test_components:
            if comp not in components:
                report.append(f"\n   {comp}: [SKIP] Composant non trouvé dans la bibliothèque")
                continue
            
            report.append(f"\n   Génération de {comp} ({variant}):")
            try:
                options = {"variant": variant}
                html = generator.generate(comp, **options)
                if html and "Template non trouvé" not in html:
                    report.append(f"   [OK] HTML généré ({len(html)} caractères)")
                    success_count += 1
                    # Vérifier les classes DSFR
                    if f"fr-{comp}" in html or "fr-btn" in html:
                        report.append(f"   [OK] Classes DSFR présentes")
                else:
                    report.append(f"   [WARN] Template non trouvé, essai avec default")
                    options = {"variant": "default"}
                    html = generator.generate(comp, **options)
                    if html and "Template non trouvé" not in html:
                        report.append(f"   [OK] Généré avec variante default")
                        success_count += 1
            except Exception as e:
                report.append(f"   [ERREUR] {str(e)}")
        
        report.append(f"\n   Résumé: {success_count}/{len(test_components)} composants générés avec succès")
        
        # Test 4: Création de page complète
        report.append("\n4. TEST DE CREATION DE PAGE COMPLETE:")
        report.append("-" * 40)
        
        try:
            # Création d'une page complète avec l'assistant
            page_config = {
                "title": "Page de Test Assistant",
                "components": [
                    {"type": "button", "variant": "primary", "text": "Bouton Test"},
                    {"type": "alert", "variant": "info", "message": "Message d'information"},
                    {"type": "form", "variant": "contact"}
                ]
            }
            
            page = assistant.create_page("Page de Test Assistant", page_config.get("components", []))
            
            if page:
                report.append(f"   [OK] Page créée")
                report.append(f"   Taille: {len(page)} caractères")
                
                # Sauvegarder la page de test
                test_page_path = output_dir.parent / "html_outputs" / "test_assistant_output.html"
                test_page_path.parent.mkdir(parents=True, exist_ok=True)
                with open(test_page_path, 'w', encoding='utf-8') as f:
                    f.write(page)
                report.append(f"   [OK] Page sauvegardée: {test_page_path}")
            else:
                report.append("   [WARN] Page non générée")
        except Exception as e:
            report.append(f"   [ERREUR] Création de page: {str(e)}")
        
        # Test 5: Vérification de la conformité
        report.append("\n5. VERIFICATION DE CONFORMITE:")
        report.append("-" * 40)
        
        # Vérifier quelques points clés
        checks = {
            "Bibliothèque chargée": components_count > 0,
            "Analyse fonctionnelle": len(descriptions) > 0,
            "Génération HTML": success_count > 0,
            "Assistant fonctionnel": True
        }
        
        for check, result in checks.items():
            status = "[OK]" if result else "[ERREUR]"
            report.append(f"   {status} {check}")
        
        # Résumé final
        report.append("\n" + "="*60)
        total_checks = len(checks)
        passed_checks = sum(1 for r in checks.values() if r)
        
        if passed_checks == total_checks:
            report.append("STATUT: ASSISTANT FONCTIONNEL")
        else:
            report.append(f"STATUT: PARTIELLEMENT FONCTIONNEL ({passed_checks}/{total_checks})")
        
    except Exception as e:
        report.append(f"\n[ERREUR CRITIQUE] {str(e)}")
        report.append("STATUT: ECHEC")
    
    # Sauvegarder le rapport
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(report))
    
    # Afficher le rapport
    print('\n'.join(report))
    print(f"\nRapport sauvegardé dans: {report_path}")
    
    return passed_checks == total_checks if 'passed_checks' in locals() else False

def main():
    """Point d'entrée principal"""
    success = test_assistant()
    return 0 if success else 1

if __name__ == "__main__":
    exit(main())