#!/usr/bin/env python3
"""
Test du serveur MCP avec Knowledge Base int\u00e9gr\u00e9e
"""

def test_mcp_kb():
    """Test de l'int\u00e9gration Knowledge Base dans le serveur MCP"""
    
    print("TEST DU SERVEUR MCP AVEC KNOWLEDGE BASE")
    print("=" * 60)
    
    # Import direct des services
    from src.services import get_generator
    from src.data import get_registry
    
    generator = get_generator()
    registry = get_registry()
    
    # Test 1: G\u00e9n\u00e9ration d'un bouton
    print("\n1. G\u00e9n\u00e9ration d'un bouton primary:")
    try:
        html = generator.generate(
            component="button",
            variant="primary",
            label="Valider le formulaire"
        )
        print(f"   \u2713 HTML g\u00e9n\u00e9r\u00e9: {html[:80]}...")
        print(f"   \u2713 Contient 'fr-btn': {'fr-btn' in html}")
        print(f"   \u2713 Label remplac\u00e9: {'Valider le formulaire' in html}")
    except Exception as e:
        print(f"   \u2717 Erreur: {e}")
    
    # Test 2: Liste des composants
    print("\n2. Liste des composants disponibles:")
    components = registry.list_components()
    print(f"   \u2713 {len(components)} composants disponibles")
    print(f"   \u2713 Exemples: {components[:5]}")
    
    # Test 3: G\u00e9n\u00e9ration d'une alerte
    print("\n3. G\u00e9n\u00e9ration d'une alerte info:")
    try:
        # Chercher d'abord si 'alert' existe dans la KB
        if 'alert' in generator.knowledge_base:
            alert_variants = list(generator.knowledge_base['alert']['variants'].keys())
            print(f"   Variantes alert disponibles: {alert_variants[:3]}")
            # Utiliser la premi\u00e8re variante
            variant = alert_variants[0] if alert_variants else 'info'
        else:
            variant = 'info'
            
        html = generator.generate(
            component="alert",
            variant=variant,
            message="Information importante"
        )
        print(f"   \u2713 HTML g\u00e9n\u00e9r\u00e9: {html[:80]}...")
        print(f"   \u2713 Contient 'fr-alert': {'fr-alert' in html}")
    except Exception as e:
        print(f"   \u2717 Erreur: {e}")
    
    # Test 4: V\u00e9rifier les stats de la KB
    print("\n4. Statistiques Knowledge Base:")
    
    if generator.knowledge_base:
        total_variants = sum(
            len(comp.get('variants', {})) 
            for comp in generator.knowledge_base.values()
        )
        print(f"   \u2713 Composants KB: {len(generator.knowledge_base)}")
        print(f"   \u2713 Total variantes: {total_variants}")
        
        # Top 3 composants
        top_components = sorted(
            [(name, len(data.get('variants', {}))) 
             for name, data in generator.knowledge_base.items()],
            key=lambda x: x[1],
            reverse=True
        )[:3]
        
        print(f"   \u2713 Top 3 composants:")
        for name, count in top_components:
            print(f"      - {name}: {count} variantes")
    else:
        print("   \u2717 Knowledge Base non charg\u00e9e")
    
    # Test 5: V\u00e9rifier la fusion Registry + KB
    print("\n5. Fusion Registry + Knowledge Base:")
    button_info = generator.get_component_info('button')
    print(f"   \u2713 Variantes button: {len(button_info['variants'])}")
    if 'metadata' in button_info and button_info['metadata']:
        print(f"   \u2713 M\u00e9tadonn\u00e9es disponibles")
    if 'stats' in button_info:
        print(f"   \u2713 Stats disponibles: {button_info['stats']}")
    
    print("\n" + "=" * 60)
    
    # V\u00e9rification finale
    if generator.knowledge_base and len(generator.knowledge_base) > 50:
        print("R\u00c9SULTAT: Knowledge Base int\u00e9gr\u00e9e avec succ\u00e8s!")
        print(f"         {len(generator.knowledge_base)} composants charg\u00e9s")
        print(f"         {total_variants} variantes disponibles")
        return True
    else:
        print("ATTENTION: Knowledge Base partiellement charg\u00e9e")
        return False

if __name__ == "__main__":
    success = test_mcp_kb()
    exit(0 if success else 1)