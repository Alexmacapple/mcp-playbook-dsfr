#!/usr/bin/env python3
"""
test_integration.py - Test de l'intégration de la Knowledge Base avec GeneratorService
"""

import json
from pathlib import Path

class GeneratorServiceWithKB:
    """Version simplifiée du GeneratorService avec Knowledge Base"""
    
    def __init__(self):
        """Charge la Knowledge Base au démarrage"""
        self.knowledge_base = {}
        kb_path = Path('components_knowledge_base_v2.json')
        
        if kb_path.exists():
            with open(kb_path, 'r', encoding='utf-8') as f:
                self.knowledge_base = json.load(f)
            print(f"✓ Knowledge Base chargée: {len(self.knowledge_base)} composants")
        else:
            print("✗ Knowledge Base non trouvée")
    
    def generate(self, component: str, variant: str = None, **kwargs):
        """
        Génère un composant depuis la Knowledge Base
        
        Args:
            component: Nom du composant (ex: 'button')
            variant: Chemin de la variante (ex: 'bouton_primaire.bouton_simple_1')
            **kwargs: Paramètres pour personnalisation (label, etc.)
        """
        if component not in self.knowledge_base:
            return f"[ERREUR] Composant '{component}' non trouvé"
        
        comp_data = self.knowledge_base[component]
        
        # Si pas de variante spécifiée, prendre la première
        if not variant:
            if comp_data['variants']:
                variant = list(comp_data['variants'].keys())[0]
            else:
                return f"[ERREUR] Aucune variante pour '{component}'"
        
        # Récupérer le HTML de la variante
        if variant in comp_data['variants']:
            html = comp_data['variants'][variant]['html']
            
            # Remplacements de base
            if 'label' in kwargs:
                html = html.replace('Libellé bouton', kwargs['label'])
                html = html.replace('Label bouton', kwargs['label'])
                html = html.replace('[À MODIFIER', f'[{kwargs["label"]}')
            
            return html
        else:
            return f"[ERREUR] Variante '{variant}' non trouvée pour '{component}'"
    
    def list_components(self):
        """Liste tous les composants disponibles"""
        return list(self.knowledge_base.keys())
    
    def list_variants(self, component: str):
        """Liste toutes les variantes d'un composant"""
        if component in self.knowledge_base:
            return list(self.knowledge_base[component]['variants'].keys())
        return []
    
    def get_documentation(self, component: str):
        """Récupère la documentation d'un composant"""
        if component in self.knowledge_base:
            return self.knowledge_base[component].get('metadata', {})
        return {}
    
    def get_stats(self):
        """Statistiques de la Knowledge Base"""
        total_variants = sum(
            comp['stats']['variant_count'] 
            for comp in self.knowledge_base.values()
        )
        return {
            'total_components': len(self.knowledge_base),
            'total_variants': total_variants,
            'components_with_doc': sum(
                1 for comp in self.knowledge_base.values() 
                if comp['stats']['has_documentation']
            )
        }

def test_generator():
    """Test complet du générateur avec Knowledge Base"""
    print("TEST D'INTÉGRATION KNOWLEDGE BASE")
    print("="*60)
    
    # Initialiser le service
    generator = GeneratorServiceWithKB()
    
    # Stats globales
    stats = generator.get_stats()
    print(f"\nStatistiques:")
    print(f"  - Composants: {stats['total_components']}")
    print(f"  - Variantes: {stats['total_variants']}")
    print(f"  - Avec doc: {stats['components_with_doc']}")
    
    # Test 1: Générer un bouton simple
    print("\n1. TEST BOUTON SIMPLE:")
    html = generator.generate('button', label='Valider')
    if '[ERREUR]' not in html:
        print(f"✓ HTML généré: {html[:100]}...")
    else:
        print(f"✗ {html}")
    
    # Test 2: Générer une variante spécifique
    print("\n2. TEST VARIANTE SPÉCIFIQUE:")
    variants = generator.list_variants('button')
    if len(variants) > 5:
        test_variant = variants[5]  # 6ème variante
        html = generator.generate('button', test_variant, label='Test')
        print(f"✓ Variante '{test_variant}' générée")
        print(f"  HTML: {html[:100]}...")
    
    # Test 3: Composant carte
    print("\n3. TEST CARTE:")
    card_variants = generator.list_variants('card')
    print(f"  {len(card_variants)} variantes disponibles")
    if card_variants:
        html = generator.generate('card', card_variants[0])
        print(f"✓ Carte générée: {html[:100]}...")
    
    # Test 4: Documentation
    print("\n4. TEST DOCUMENTATION:")
    doc = generator.get_documentation('button')
    if doc:
        print(f"✓ Documentation trouvée:")
        for key, value in doc.items():
            if isinstance(value, str) and len(value) > 50:
                print(f"  - {key}: {value[:50]}...")
            else:
                print(f"  - {key}: {value}")
    
    # Test 5: Liste des composants populaires
    print("\n5. COMPOSANTS LES PLUS RICHES:")
    components = generator.list_components()
    rich_components = []
    for comp in components[:10]:  # Top 10
        variant_count = len(generator.list_variants(comp))
        if variant_count > 10:
            rich_components.append((comp, variant_count))
    
    rich_components.sort(key=lambda x: x[1], reverse=True)
    for comp, count in rich_components[:5]:
        print(f"  - {comp}: {count} variantes")
    
    # Test 6: Vérification conformité DSFR
    print("\n6. CONFORMITÉ DSFR:")
    button_html = generator.generate('button')
    checks = {
        'type="button"': 'type="button"' in button_html,
        'class="fr-btn"': 'fr-btn' in button_html,
        'Balises fermées': button_html.count('<') == button_html.count('>')
    }
    
    for check, passed in checks.items():
        status = "✓" if passed else "✗"
        print(f"  {status} {check}")
    
    # Résultat final
    all_passed = all(checks.values())
    print("\n" + "="*60)
    if all_passed:
        print("✅ INTÉGRATION RÉUSSIE - Prêt pour production")
    else:
        print("⚠️ INTÉGRATION PARTIELLE - Corrections nécessaires")
    
    return all_passed

if __name__ == "__main__":
    import sys
    success = test_generator()
    sys.exit(0 if success else 1)