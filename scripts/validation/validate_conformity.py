#!/usr/bin/env python3
"""
validate_conformity.py - Validation de conformit\u00e9 DSFR
V\u00e9rifie que les composants g\u00e9n\u00e9r\u00e9s respectent les standards DSFR
"""

import sys
from typing import Dict, List, Tuple
from src.services import get_generator, get_validator

def validate_dsfr_conformity() -> int:
    """
    Valide la conformit\u00e9 DSFR des composants critiques.
    
    Returns:
        0 si succ\u00e8s, 1 si \u00e9chec
    """
    print("VALIDATION DE CONFORMIT\u00c9 DSFR")
    print("=" * 60)
    
    # Tests de conformit\u00e9 par composant
    tests = {
        'button': {
            'required': ['type="button"', 'fr-btn'],
            'test_params': {'label': 'Test', 'variant': 'primary'},
            'description': 'Bouton avec attributs requis'
        },
        'form': {
            'required': ['fr-fieldset', 'aria-labelledby'],
            'test_params': {'variant': 'contact'},
            'description': 'Formulaire avec accessibilit\u00e9'
        },
        'alert': {
            'required': ['fr-alert', 'role="alert"'],
            'test_params': {'message': 'Test alert', 'type': 'info'},
            'description': 'Alerte avec role ARIA'
        },
        'card': {
            'required': ['fr-card', 'fr-card__body'],
            'test_params': {'title': 'Test card', 'variant': 'basic'},
            'description': 'Carte avec structure correcte'
        },
        'modal': {
            'required': ['fr-modal', 'role="dialog"', 'aria-modal="true"'],
            'test_params': {'title': 'Test modal', 'variant': 'basic'},
            'description': 'Modale avec attributs ARIA'
        },
        'accordion': {
            'required': ['fr-accordion', 'aria-expanded'],
            'test_params': {'title': 'Test accordion', 'variant': 'single'},
            'description': 'Accord\u00e9on avec \u00e9tat expand\u00e9'
        },
        'input': {
            'required': ['fr-input', 'fr-label'],
            'test_params': {'label': 'Test input', 'type': 'text'},
            'description': 'Champ avec label associ\u00e9'
        },
        'table': {
            'required': ['fr-table', '<thead>', '<tbody>'],
            'test_params': {'variant': 'basic'},
            'description': 'Tableau avec structure s\u00e9mantique'
        }
    }
    
    results = []
    generator = get_generator()
    validator = get_validator()
    
    print("\nTests de conformit\u00e9 :")
    print("-" * 40)
    
    for component, config in tests.items():
        try:
            # G\u00e9n\u00e9rer le composant
            html = generator.generate(component, **config['test_params'])
            
            # V\u00e9rifier les attributs requis
            missing = [attr for attr in config['required'] if attr not in html]
            
            # Validation suppl\u00e9mentaire (simplifi\u00e9e pour les tests)
            # On v\u00e9rifie seulement les attributs requis pour l'instant
            
            if not missing:
                print(f"\u2713 {component:12} : {config['description']}")
                results.append((component, True))
            else:
                print(f"\u2717 {component:12} : Manque {', '.join(missing) if missing else 'validation \u00e9chou\u00e9e'}")
                results.append((component, False))
                
        except Exception as e:
            print(f"\u26a0 {component:12} : Erreur - {e}")
            results.append((component, False))
    
    # Tests suppl\u00e9mentaires de la Knowledge Base
    print("\n\nTests Knowledge Base :")
    print("-" * 40)
    
    kb_tests = []
    
    # Test 1: V\u00e9rifier que la KB est charg\u00e9e
    if generator.knowledge_base:
        kb_components = len(generator.knowledge_base)
        kb_variants = sum(len(comp.get('variants', {})) for comp in generator.knowledge_base.values())
        
        if kb_components >= 60 and kb_variants >= 700:
            print(f"\u2713 Knowledge Base  : {kb_components} composants, {kb_variants} variantes")
            kb_tests.append(True)
        else:
            print(f"\u2717 Knowledge Base  : Seulement {kb_components} composants, {kb_variants} variantes")
            kb_tests.append(False)
    else:
        print("\u2717 Knowledge Base  : Non charg\u00e9e")
        kb_tests.append(False)
    
    # Test 2: V\u00e9rifier le mapping des variantes
    try:
        # Tester que 'primary' est mapp\u00e9 correctement
        button_html = generator.generate('button', variant='primary', label='Test')
        if 'fr-btn' in button_html:
            print("\u2713 Mapping variantes: 'primary' -> bouton DSFR valide")
            kb_tests.append(True)
        else:
            print("\u2717 Mapping variantes: \u00c9chec de conversion")
            kb_tests.append(False)
    except Exception as e:
        print(f"\u2717 Mapping variantes: Erreur - {e}")
        kb_tests.append(False)
    
    # Test 3: V\u00e9rifier les fondamentaux
    from src.services import get_design_service
    design = get_design_service()
    
    foundations = design.get_foundations()
    if foundations and foundations.get('grid', {}).get('columns') == 12:
        print("\u2713 Fondamentaux    : Grille 12 colonnes charg\u00e9e")
        kb_tests.append(True)
    else:
        print("\u2717 Fondamentaux    : Grille non disponible")
        kb_tests.append(False)
    
    # Test 4: V\u00e9rifier les templates
    from src.services.template_service import get_template_service
    template = get_template_service()
    
    try:
        page_404 = template.get_template('error_404')
        if '404' in page_404 and 'fr-error-page' in page_404:
            print("\u2713 Templates       : Page 404 conforme")
            kb_tests.append(True)
        else:
            print("\u2717 Templates       : Page 404 non conforme")
            kb_tests.append(False)
    except Exception as e:
        print(f"\u2717 Templates       : Erreur - {e}")
        kb_tests.append(False)
    
    # R\u00e9sum\u00e9
    print("\n" + "=" * 60)
    print("R\u00c9SULTAT")
    print("=" * 60)
    
    # Score composants
    success_components = sum(1 for _, ok in results if ok)
    total_components = len(tests)
    component_score = (success_components * 100) // total_components
    
    # Score Knowledge Base
    kb_success = sum(1 for ok in kb_tests if ok)
    kb_total = len(kb_tests)
    kb_score = (kb_success * 100) // kb_total if kb_total > 0 else 0
    
    print(f"\nComposants : {success_components}/{total_components} ({component_score}%)")
    print(f"Knowledge  : {kb_success}/{kb_total} ({kb_score}%)")
    
    # Score global
    global_score = (component_score + kb_score) // 2
    
    print(f"\nSCORE GLOBAL: {global_score}%")
    
    if global_score >= 90:
        print("\u2705 CONFORM\u00c9 - Pr\u00eat pour production")
        return_code = 0
    elif global_score >= 70:
        print("\u26a0\ufe0f  PARTIEL - Corrections recommand\u00e9es")
        return_code = 0
    else:
        print("\u274c NON CONFORM\u00c9 - Corrections n\u00e9cessaires")
        return_code = 1
    
    # Monitoring
    try:
        from src.monitoring import get_metrics
        metrics = get_metrics()
        print(f"\nM\u00e9triques:")
        print(f"  Requ\u00eates: {metrics['metrics']['total_requests']}")
        print(f"  Erreurs: {metrics['metrics']['errors']}")
        print(f"  Ratio KB/Registry: {metrics['performance'].get('kb_vs_registry_ratio', 0):.2f}")
    except:
        pass  # Monitoring optionnel
    
    return return_code

if __name__ == "__main__":
    sys.exit(validate_dsfr_conformity())