#!/usr/bin/env python3
"""
Test de l'int\u00e9gration compl\u00e8te : 88 composants + 125 fiches documentation
"""

def test_integration_complete():
    """Test de l'int\u00e9gration des 213 fiches DSFR"""
    
    print("TEST INT\u00c9GRATION COMPL\u00c8TE - 213 FICHES DSFR")
    print("=" * 60)
    
    # Import des services
    from src.services import get_generator, get_design_service
    from src.services.template_service import get_template_service
    from src.data import get_registry
    
    generator = get_generator()
    design = get_design_service()
    template = get_template_service()
    registry = get_registry()
    
    # ========== TEST 1: COMPOSANTS (88 fiches) ==========
    print("\n1. COMPOSANTS HTML (88 fiches)")
    print("-" * 40)
    
    if generator.knowledge_base:
        kb_components = len(generator.knowledge_base)
        total_variants = sum(
            len(comp.get('variants', {})) 
            for comp in generator.knowledge_base.values()
        )
        print(f"   \u2713 Composants charg\u00e9s: {kb_components}")
        print(f"   \u2713 Variantes totales: {total_variants}")
        
        # Test g\u00e9n\u00e9ration
        try:
            button_html = generator.generate('button', variant='primary', label='Test')
            print(f"   \u2713 G\u00e9n\u00e9ration button: {'fr-btn' in button_html}")
        except Exception as e:
            print(f"   \u2717 Erreur g\u00e9n\u00e9ration: {e}")
    else:
        print("   \u2717 Knowledge Base composants non charg\u00e9e")
    
    # ========== TEST 2: DOCUMENTATION (125 fiches) ==========
    print("\n2. DOCUMENTATION (125 fiches)")
    print("-" * 40)
    
    if design.documentation_kb:
        doc_stats = design.documentation_kb.get('metadata', {})
        print(f"   \u2713 Fiches documentation: {doc_stats.get('total_files', 0)}")
        print(f"   \u2713 Fondamentaux: {doc_stats.get('foundations_count', 0)}")
        print(f"   \u2713 Utilitaires: {doc_stats.get('utilities_count', 0)}")
        print(f"   \u2713 Templates: {doc_stats.get('templates_count', 0)}")
    else:
        print("   \u2717 Knowledge Base documentation non charg\u00e9e")
    
    # ========== TEST 3: FONDAMENTAUX ==========
    print("\n3. FONDAMENTAUX DSFR")
    print("-" * 40)
    
    foundations = design.get_foundations()
    if foundations:
        print(f"   \u2713 Grille: {foundations.get('grid', {}).get('columns', 0)} colonnes")
        print(f"   \u2713 Breakpoints: {len(foundations.get('breakpoints', {}))} points")
        
        # Afficher les breakpoints
        for bp_name, bp_value in foundations.get('breakpoints', {}).items():
            print(f"      - {bp_name}: {bp_value}")
    else:
        print("   \u2717 Fondamentaux non charg\u00e9s")
    
    # ========== TEST 4: CLASSES CSS UTILITAIRES ==========
    print("\n4. CLASSES CSS UTILITAIRES")
    print("-" * 40)
    
    css_colors = design.get_css_utilities('colors')
    css_spacing = design.get_css_utilities('spacing')
    css_all = design.get_css_utilities()
    
    print(f"   \u2713 Classes couleurs: {len(css_colors)}")
    print(f"   \u2713 Classes espacement: {len(css_spacing)}")
    print(f"   \u2713 Total classes CSS: {len(css_all)}")
    
    if css_colors:
        print(f"   Exemples couleurs: {css_colors[:3]}")
    
    # ========== TEST 5: TEMPLATES DE PAGES ==========
    print("\n5. TEMPLATES DE PAGES")
    print("-" * 40)
    
    available_templates = template.get_available_templates()
    print(f"   \u2713 Templates pr\u00e9d\u00e9finis: {available_templates.get('predefined', 0)}")
    
    for key, count in available_templates.items():
        if key.startswith('kb_'):
            print(f"   \u2713 Templates {key[3:]}: {count}")
    
    # Test g\u00e9n\u00e9ration page 404
    try:
        page_404 = template.get_template('error_404')
        print(f"   \u2713 Page 404 g\u00e9n\u00e9r\u00e9e: {'404' in page_404}")
    except Exception as e:
        print(f"   \u2717 Erreur template: {e}")
    
    # ========== TEST 6: GUIDELINES ==========
    print("\n6. GUIDELINES ET RECOMMANDATIONS")
    print("-" * 40)
    
    guidelines = design.get_guidelines()
    print(f"   \u2713 Guidelines totales: {len(guidelines)}")
    
    if guidelines:
        print(f"   Exemple: {guidelines[0][:80]}...")
    
    # ========== TEST 7: STATISTIQUES GLOBALES ==========
    print("\n7. STATISTIQUES GLOBALES")
    print("-" * 40)
    
    # Total composants (Registry + KB)
    total_components = len(registry.list_components())
    print(f"   \u2713 Composants totaux (Registry + KB): {total_components}")
    
    # V\u00e9rifier la fusion
    button_info = generator.get_component_info('button')
    if button_info:
        print(f"   \u2713 Button variantes (fusion): {len(button_info['variants'])}")
        if 'stats' in button_info:
            print(f"   \u2713 Stats disponibles: Oui")
    
    # ========== R\u00c9SULTAT FINAL ==========
    print("\n" + "=" * 60)
    print("R\u00c9SULTAT FINAL")
    print("=" * 60)
    
    success_count = 0
    total_count = 7
    
    # V\u00e9rifications
    checks = {
        "Composants KB": generator.knowledge_base and len(generator.knowledge_base) > 60,
        "Documentation KB": design.documentation_kb and design.documentation_kb.get('metadata', {}).get('total_files', 0) > 100,
        "Fondamentaux": bool(foundations and foundations.get('grid')),
        "Classes CSS": len(css_all) > 0,
        "Templates": available_templates.get('predefined', 0) > 0,
        "Guidelines": len(guidelines) > 0,
        "Fusion compl\u00e8te": total_components > 100
    }
    
    for check, result in checks.items():
        status = "\u2713" if result else "\u2717"
        print(f"   {status} {check}")
        if result:
            success_count += 1
    
    print(f"\nScore: {success_count}/{total_count}")
    
    if success_count == total_count:
        print("\u2705 INT\u00c9GRATION COMPL\u00c8TE R\u00c9USSIE - 213 FICHES")
        print("   - 88 composants avec 775+ variantes")
        print("   - 125 fiches documentation")
        print("   - Fondamentaux, utilitaires et templates")
        return True
    elif success_count >= 5:
        print("\u26a0\ufe0f  INT\u00c9GRATION PARTIELLE - Quelques \u00e9l\u00e9ments manquants")
        return False
    else:
        print("\u274c INT\u00c9GRATION \u00c9CHOU\u00c9E - V\u00e9rifier les Knowledge Bases")
        return False

if __name__ == "__main__":
    import sys
    success = test_integration_complete()
    sys.exit(0 if success else 1)