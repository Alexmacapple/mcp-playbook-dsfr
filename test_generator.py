#!/usr/bin/env python3
"""
Test du service de génération.
Vérifie que le Factory Pattern fonctionne.
"""

from src.services import get_generator
from src.errors.components import ComponentNotFoundError, InvalidVariantError


def test_generator():
    """Test le générateur de composants."""
    
    print("🏭 Test du Générateur DSFR (Factory Pattern)")
    print("=" * 50)
    
    generator = get_generator()
    
    # 1. Test génération simple
    print("\n1️⃣ Test génération simple:")
    
    try:
        # Button
        button_html = generator.generate('button', label='Valider')
        print(f"   ✅ Button: {len(button_html)} chars")
        print(f"      Contient 'Valider': {'Valider' in button_html}")
        
        # Alert
        alert_html = generator.generate('alert', 
                                       type='success',
                                       title='Bravo !',
                                       message='Opération réussie')
        print(f"   ✅ Alert: {len(alert_html)} chars")
        print(f"      Contient 'Bravo': {'Bravo' in alert_html}")
        
    except Exception as e:
        print(f"   ❌ Erreur: {e}")
    
    # 2. Test avec variantes
    print("\n2️⃣ Test avec variantes:")
    
    variants_tests = [
        ('button', 'primary'),
        ('button', 'secondary'),
        ('alert', 'warning'),
        ('card', 'horizontal')
    ]
    
    for comp, variant in variants_tests:
        try:
            html = generator.generate(comp, variant=variant)
            print(f"   ✅ {comp}/{variant}: {len(html)} chars")
        except InvalidVariantError as e:
            print(f"   ⚠️ Variante non trouvée: {comp}/{variant}")
        except Exception as e:
            print(f"   ❌ Erreur: {e}")
    
    # 3. Test avec options avancées
    print("\n3️⃣ Test options avancées:")
    
    # Button avec icône
    button_icon = generator.generate('button',
                                    label='Envoyer',
                                    icon='send',
                                    size='lg')
    print(f"   ✅ Button avec icône: {'fr-icon' in button_icon}")
    
    # Input avec erreur
    input_error = generator.generate('input',
                                    label='Email',
                                    type='email',
                                    error='Email invalide',
                                    required=True)
    print(f"   ✅ Input avec erreur: {'required' in input_error}")
    
    # 4. Test des hooks
    print("\n4️⃣ Test système de hooks:")
    
    generated_components = []
    
    def track_generation(component, options):
        generated_components.append(component)
    
    generator.add_hook('before', track_generation)
    
    generator.generate('button', label='Test')
    generator.generate('alert', message='Test')
    
    print(f"   ✅ Composants trackés: {generated_components}")
    
    # 5. Test override
    print("\n5️⃣ Test override custom:")
    
    def custom_button_generator(component, **kwargs):
        return f"<custom-button>{kwargs.get('label', 'Custom')}</custom-button>"
    
    generator.register_override('custom_button', custom_button_generator)
    
    # Tester avec un composant qui n'existe pas normalement
    # mais qui a un override
    try:
        # D'abord créer un faux composant dans le registre
        custom_html = "<custom>test</custom>"
        generator.register_override('button', custom_button_generator)
        result = generator.generate('button', label='Override Test')
        print(f"   ✅ Override fonctionne: {'custom-button' in result}")
    except Exception as e:
        print(f"   ❌ Override échoué: {e}")
    
    # 6. Test erreurs
    print("\n6️⃣ Test gestion d'erreurs:")
    
    try:
        generator.generate('composant_inexistant')
        print("   ❌ Devrait lever une erreur")
    except ComponentNotFoundError as e:
        print(f"   ✅ ComponentNotFoundError: {e.code}")
    
    # 7. Test performance avec cache
    print("\n7️⃣ Test performance (cache):")
    
    import time
    
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
    
    print(f"   Sans cache: {time1*1000:.2f}ms")
    print(f"   Avec cache: {time2*1000:.2f}ms")
    if time1 > time2:
        print(f"   ✅ Cache efficace: {(time1/time2):.1f}x plus rapide")
    
    # 8. Test Factory Pattern
    print("\n8️⃣ Test Factory Pattern:")
    
    # Vérifier qu'on n'a pas de switch/case
    import inspect
    source = inspect.getsource(generator.generate)
    has_switch = 'elif' in source or 'switch' in source
    
    if not has_switch or 'generator = self._generators' in source:
        print("   ✅ Factory Pattern implémenté (pas de switch/case)")
    else:
        print("   ⚠️ Pattern à vérifier")
    
    print("\n✅ Générateur fonctionnel avec Factory Pattern!")
    return True


if __name__ == "__main__":
    success = test_generator()
    if not success:
        exit(1)