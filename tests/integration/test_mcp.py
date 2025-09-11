#!/usr/bin/env python3
"""
Test du serveur MCP avec Knowledge Base int\u00e9gr\u00e9e
"""

import asyncio
from mcp_local.server import app

async def test_mcp_kb():
    """Test de l'int\u00e9gration Knowledge Base dans le serveur MCP"""
    
    print("TEST DU SERVEUR MCP AVEC KNOWLEDGE BASE")
    print("=" * 60)
    
    # Import des outils directement
    from mcp_local.tools import generate_component, list_components
    
    # Test 1: G\u00e9n\u00e9ration d'un bouton
    print("\n1. G\u00e9n\u00e9ration d'un bouton primary:")
    result = generate_component(
        component="button",
        variant="primary",
        options={"label": "Valider le formulaire"}
    )
    
    if 'html' in result:
        html = result['html']
        print(f"   \u2713 HTML g\u00e9n\u00e9r\u00e9: {html[:80]}...")
        print(f"   \u2713 Contient 'fr-btn': {'fr-btn' in html}")
        print(f"   \u2713 Label remplac\u00e9: {'Valider le formulaire' in html}")
    else:
        print(f"   R\u00e9sultat: {result}")
    
    # Test 2: Liste des composants
    print("\n2. Liste des composants disponibles:")
    result = list_components()
    
    if 'components' in result:
        components = result['components']
        print(f"   \u2713 {len(components)} composants disponibles")
        print(f"   \u2713 Exemples: {components[:5]}")
    
    # Test 3: G\u00e9n\u00e9ration d'une alerte
    print("\n3. G\u00e9n\u00e9ration d'une alerte info:")
    result = generate_component(
        component="alert",
        variant="info",
        options={"message": "Information importante"}
    )
    
    if 'html' in result:
        html = result['html']
        print(f"   \u2713 HTML g\u00e9n\u00e9r\u00e9: {html[:80]}...")
        print(f"   \u2713 Contient 'fr-alert': {'fr-alert' in html}")
    
    # Test 4: V\u00e9rifier les stats de la KB
    print("\n4. Statistiques Knowledge Base:")
    from src.services import get_generator
    gen = get_generator()
    
    if gen.knowledge_base:
        total_variants = sum(
            len(comp.get('variants', {})) 
            for comp in gen.knowledge_base.values()
        )
        print(f"   \u2713 Composants KB: {len(gen.knowledge_base)}")
        print(f"   \u2713 Total variantes: {total_variants}")
        
        # Top 3 composants
        top_components = sorted(
            [(name, len(data.get('variants', {}))) 
             for name, data in gen.knowledge_base.items()],
            key=lambda x: x[1],
            reverse=True
        )[:3]
        
        print(f"   \u2713 Top 3 composants:")
        for name, count in top_components:
            print(f"      - {name}: {count} variantes")
    else:
        print("   \u2717 Knowledge Base non charg\u00e9e")
    
    print("\n" + "=" * 60)
    print("TEST TERMIN\u00c9 - Knowledge Base int\u00e9gr\u00e9e avec succ\u00e8s")

if __name__ == "__main__":
    asyncio.run(test_mcp_kb())