#!/usr/bin/env python3
"""
analyze_components_only.py - Analyse CIBLÉE sur les vrais composants DSFR
Ignore les outils, analyses et modèles de pages
"""

import re
from pathlib import Path
import json

def is_real_component(filename):
    """Détermine si c'est un vrai composant DSFR ou juste de la doc"""
    # Patterns à EXCLURE (documentation, outils, etc.)
    exclude_patterns = [
        'outils-d-analyse',
        'modele-de-page',
        'modeles-et-exemples',
        'utilitaires',
        'fondamentaux',
        'combinaison',
        'icones-',
        'principes',
        'accessibilite',
        'rgaa',
        'grille',
        'espacements'
    ]
    
    name_lower = filename.lower()
    for pattern in exclude_patterns:
        if pattern in name_lower:
            return False
    
    # Patterns à INCLURE (vrais composants)
    include_patterns = [
        'bouton',
        'formulaire',
        'alerte',
        'carte',
        'modale',
        'tableau',
        'accordeon',
        'badge',
        'tag',
        'navigation',
        'input',
        'select',
        'checkbox',
        'radio',
        'toggle',
        'stepper',
        'breadcrumb',
        'pagination',
        'tabs',
        'tooltip',
        'dropdown',
        'menu',
        'header',
        'footer',
        'sidebar',
        'dialog',
        'notification',
        'progress',
        'spinner',
        'avatar',
        'chip'
    ]
    
    for pattern in include_patterns:
        if pattern in name_lower:
            return True
    
    # Par défaut, vérifier si le nom contient "systeme-de-design" 
    # mais pas "outils" ou "modele"
    if 'systeme-de-design' in name_lower:
        if not any(ex in name_lower for ex in ['outils', 'modele', 'utilitaire']):
            return True
    
    return False

def analyze_components():
    """Analyse uniquement les VRAIS composants DSFR"""
    fiches_dir = Path('roadmap/Brainstorming/fiches-markdown-v2')
    all_fiches = list(fiches_dir.glob('*.md'))
    
    # Filtrer pour garder seulement les composants
    component_fiches = [f for f in all_fiches if is_real_component(f.name)]
    non_component_fiches = [f for f in all_fiches if not is_real_component(f.name)]
    
    print(f"Total fiches: {len(all_fiches)}")
    print(f"Composants identifiés: {len(component_fiches)}")
    print(f"Documentation/Outils: {len(non_component_fiches)}")
    
    # Analyser les composants
    components_with_html = []
    components_without_html = []
    
    for fiche in component_fiches:
        content = fiche.read_text(encoding='utf-8')
        has_html = bool(re.search(r'<[^>]+>', content))
        
        if has_html:
            # Compter les variantes
            extrait_count = content.count('Extrait de code')
            components_with_html.append({
                'name': fiche.name,
                'extrait_count': extrait_count
            })
        else:
            components_without_html.append(fiche.name)
    
    # Rapport
    print("\n" + "="*60)
    print("ANALYSE DES COMPOSANTS DSFR UNIQUEMENT")
    print("="*60)
    print(f"Composants avec HTML: {len(components_with_html)}/{len(component_fiches)}")
    print(f"Composants sans HTML: {len(components_without_html)}/{len(component_fiches)}")
    
    if len(component_fiches) > 0:
        success_rate = len(components_with_html) / len(component_fiches) * 100
        print(f"Taux de succès: {success_rate:.1f}%")
    
    # Lister les composants avec HTML (top 20)
    print("\nTop composants avec HTML (et nombre de variantes):")
    components_with_html.sort(key=lambda x: x['extrait_count'], reverse=True)
    for comp in components_with_html[:20]:
        print(f"  ✓ {comp['name']}: {comp['extrait_count']} variantes")
    
    if components_without_html:
        print(f"\nComposants SANS HTML ({len(components_without_html)}):")
        for comp in components_without_html[:10]:
            print(f"  ✗ {comp}")
    
    # Sauvegarder les résultats
    results = {
        'total_fiches': len(all_fiches),
        'components_identified': len(component_fiches),
        'components_with_html': [c['name'] for c in components_with_html],
        'components_without_html': components_without_html,
        'top_components': components_with_html[:48],  # Top 48 pour la migration
        'success_rate': success_rate if len(component_fiches) > 0 else 0
    }
    
    with open('components_analysis.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    print(f"\nRésultats sauvegardés dans: components_analysis.json")
    
    # Décision
    if success_rate >= 80:
        print("\n[GO] ✓ Extraction possible en se concentrant sur les vrais composants")
        return True
    else:
        print("\n[ATTENTION] ⚠ Même les composants ont un taux faible")
        return False

if __name__ == "__main__":
    import sys
    success = analyze_components()
    sys.exit(0 if success else 1)