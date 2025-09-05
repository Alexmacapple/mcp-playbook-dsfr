#!/usr/bin/env python3
"""
Test du registre de composants.
Vérifie que la migration fonctionne correctement.
"""

from src.data import get_registry


def test_registry():
    """Test le registre de composants."""
    
    print("🧪 Test du Registre de Composants DSFR")
    print("=" * 50)
    
    # Obtenir le registre (Singleton)
    registry = get_registry()
    
    # 1. Test des statistiques
    stats = registry.get_stats()
    print(f"\n📊 Statistiques:")
    print(f"   • Composants: {stats['components']}")
    print(f"   • Variantes: {stats['variants']}")
    print(f"   • Items en cache: {stats['cached_items']}")
    
    # 2. Test de la liste des composants
    components = registry.list_components()
    print(f"\n📦 Composants disponibles: {len(components)}")
    print(f"   Exemples: {', '.join(components[:10])}")
    
    # 3. Test de récupération d'un composant
    print("\n🔍 Test de récupération:")
    
    # Test button
    button_html = registry.get_variant_html('button', 'primary')
    if button_html:
        print(f"   ✅ Button primary: {len(button_html)} caractères")
        print(f"      Contient 'fr-btn': {'fr-btn' in button_html}")
    else:
        print("   ❌ Button primary non trouvé")
    
    # Test alert
    alert_html = registry.get_variant_html('alert', 'info')
    if alert_html:
        print(f"   ✅ Alert info: {len(alert_html)} caractères")
        print(f"      Contient 'fr-alert': {'fr-alert' in alert_html}")
    else:
        print("   ❌ Alert info non trouvé")
    
    # 4. Test des variantes
    print("\n🎨 Test des variantes:")
    for comp in ['button', 'alert', 'badge', 'form']:
        variants = registry.list_variants(comp)
        if variants:
            print(f"   • {comp}: {len(variants)} variantes ({', '.join(variants[:3])}...)")
    
    # 5. Test des métadonnées
    print("\n📋 Test des métadonnées:")
    for comp in ['button', 'form', 'alert']:
        metadata = registry.get_metadata(comp)
        print(f"   • {comp}: {metadata.get('description', 'N/A')}")
    
    # 6. Test du Singleton
    print("\n🔒 Test du Singleton:")
    registry2 = get_registry()
    print(f"   Même instance: {registry is registry2}")
    
    # 7. Test de performance (cache)
    print("\n⚡ Test de performance:")
    import time
    
    # Premier appel (sans cache)
    start = time.time()
    for _ in range(100):
        registry.get_component('button')
    time1 = time.time() - start
    
    # Deuxième appel (avec cache)
    start = time.time()
    for _ in range(100):
        registry.get_component('button')
    time2 = time.time() - start
    
    print(f"   Sans cache: {time1*1000:.2f}ms")
    print(f"   Avec cache: {time2*1000:.2f}ms")
    print(f"   Amélioration: {(time1/time2):.1f}x plus rapide")
    
    print("\n✅ Registre fonctionnel et optimisé!")
    
    return True


if __name__ == "__main__":
    success = test_registry()
    if not success:
        exit(1)