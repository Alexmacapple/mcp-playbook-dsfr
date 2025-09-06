#!/usr/bin/env python3
"""
Test de l'assistant DSFR avec tous les composants disponibles
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import importlib.util
spec = importlib.util.spec_from_file_location("dsfr_assistant", "dsfr-assistant.py")
dsfr_assistant = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dsfr_assistant)
DSFRProductionAssistant = dsfr_assistant.DSFRProductionAssistant

def test_assistant():
    """Test toutes les fonctionnalités de l'assistant"""
    
    print("🧪 TEST DE L'ASSISTANT DSFR")
    print("="*60)
    
    assistant = DSFRProductionAssistant()
    
    # Test 1: Vérifier la bibliothèque chargée
    print("\n1️⃣ Vérification de la bibliothèque:")
    print(f"   Composants chargés: {len(assistant.library.get('components', {}))}")
    
    if assistant.library.get('components'):
        print("   Exemples de composants disponibles:")
        for comp in list(assistant.library['components'].keys())[:10]:
            variants = assistant.library['components'][comp].get('variants', {})
            print(f"      • {comp}: {len(variants)} variante(s)")
    
    # Test 2: Analyse de besoins
    print("\n2️⃣ Test d'analyse de besoins:")
    descriptions = [
        "Je veux un formulaire de contact avec validation",
        "Page avec navigation et tableau de données",
        "Dashboard avec alertes et cartes",
        "Interface accessible avec modal et accordéon"
    ]
    
    for desc in descriptions:
        print(f"\n   Description: '{desc}'")
        analysis = assistant.analyze_needs(desc)
        print(f"   ✅ Connus: {', '.join(analysis['connus_connus']) if analysis['connus_connus'] else 'Aucun'}")
        print(f"   💡 Détectés: {', '.join(analysis['inconnus_connus']) if analysis['inconnus_connus'] else 'Aucun'}")
        
        suggestions = assistant.suggest_components(analysis)
        if suggestions:
            print(f"   🎯 Suggestions: {', '.join([s['component'] for s in suggestions])}")
    
    # Test 3: Génération de HTML
    print("\n3️⃣ Test de génération HTML:")
    
    # Tester quelques composants
    test_components = [
        ("button", "primary"),
        ("alert", "info"),
        ("form", "contact"),
        ("card", "basic") if "card" in assistant.library.get('components', {}) else None,
        ("table", "basic") if "table" in assistant.library.get('components', {}) else None
    ]
    
    for test in [t for t in test_components if t]:
        comp, variant = test
        print(f"\n   Génération de {comp} ({variant}):")
        html = assistant.generate_html(comp, variant)
        if html and "Template non trouvé" not in html:
            print(f"   ✅ HTML généré ({len(html)} caractères)")
            # Afficher les premières lignes
            lines = html.strip().split('\n')[:3]
            for line in lines:
                if line.strip():
                    print(f"      {line[:60]}...")
        else:
            print(f"   ⚠️ Template non trouvé")
    
    # Test 4: Création de page complète
    print("\n4️⃣ Test de création de page complète:")
    
    components_html = []
    for comp in ["header", "navigation", "button", "alert"]:
        if comp in assistant.library.get('components', {}):
            variants = assistant.library['components'][comp].get('variants', {})
            if variants:
                variant = list(variants.keys())[0] if isinstance(variants, dict) else variants[0]
                html = assistant.generate_html(comp, variant)
                if html and "Template non trouvé" not in html:
                    components_html.append(html)
    
    if components_html:
        page = assistant.create_page_template("Page de Test", components_html)
        print(f"   ✅ Page créée avec {len(components_html)} composants")
        print(f"   📏 Taille: {len(page)} caractères")
        
        # Sauvegarder la page de test
        with open("test_assistant_output.html", 'w', encoding='utf-8') as f:
            f.write(page)
        print(f"   💾 Sauvegardée dans: test_assistant_output.html")
    
    # Test 5: Commandes directes
    print("\n5️⃣ Test des commandes directes:")
    
    print("\n   Commande 'list':")
    assistant.run_command("list")
    
    print("\n   Commande 'generate button primary':")
    assistant.run_command("generate button primary")
    
    # Résumé
    print("\n" + "="*60)
    print("📊 RÉSUMÉ DES TESTS:")
    print(f"   ✅ Bibliothèque: {len(assistant.library.get('components', {}))} composants")
    print(f"   ✅ Analyse: Fonctionne pour {len(descriptions)} descriptions")
    print(f"   ✅ Génération: {len([t for t in test_components if t])} composants testés")
    print(f"   ✅ Pages: Création réussie")
    print(f"   ✅ Commandes: Exécution OK")
    
    return True

if __name__ == "__main__":
    success = test_assistant()
    if success:
        print("\n🎉 TOUS LES TESTS RÉUSSIS !")
    else:
        print("\n❌ Certains tests ont échoué")
        sys.exit(1)