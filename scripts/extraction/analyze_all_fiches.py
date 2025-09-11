#!/usr/bin/env python3
"""
analyze_all_fiches.py - Analyse COMPLÈTE des 213 fiches DSFR
Objectif : Identifier TOUTES les variations avant extraction
"""

import re
from pathlib import Path
from collections import Counter
import json

def analyze_fiche_comprehensive(fiche_path):
    """Analyse approfondie d'une fiche pour détecter TOUTES les variations"""
    content = fiche_path.read_text(encoding='utf-8')
    lines = content.split('\n')
    
    analysis = {
        'name': fiche_path.name,
        'has_html': bool(re.search(r'<[^>]+>', content)),
        'html_tags': list(set(re.findall(r'<([a-z]+)', content, re.IGNORECASE))),
        'extrait_patterns': [],
        'format_variations': [],
        'total_lines': len(lines),
        'metadata': {}
    }
    
    # Détecter les différents patterns "Extrait de code"
    for i, line in enumerate(lines):
        # Pattern 1: "###\nExtrait de code"
        if line.strip() == '###' and i+1 < len(lines) and 'Extrait de code' in lines[i+1]:
            analysis['extrait_patterns'].append('###_newline_Extrait')
        # Pattern 2: "### Extrait de code"
        elif line.strip() == '### Extrait de code':
            analysis['extrait_patterns'].append('###_Extrait_same_line')
        # Pattern 3: Autre variation?
        elif 'Extrait' in line and 'code' in line:
            if line.strip() != 'Extrait de code':  # Éviter les faux positifs
                analysis['extrait_patterns'].append(f'Other: {line.strip()[:50]}')
    
    # Compter les patterns
    analysis['extrait_count'] = len(analysis['extrait_patterns'])
    
    # Détecter métadonnées
    if 'URL:' in content:
        analysis['metadata']['has_url'] = True
    if 'Title:' in content:
        analysis['metadata']['has_title'] = True
    if 'DSFR v' in content:
        analysis['metadata']['has_version'] = True
    if '[Documentation]' in content:
        analysis['metadata']['has_doc_link'] = True
    
    # Cas spéciaux
    if not analysis['has_html']:
        analysis['format_variations'].append('NO_HTML')
    if analysis['extrait_count'] == 0:
        analysis['format_variations'].append('NO_EXTRAIT_CODE')
    if '```html' in content:
        analysis['format_variations'].append('HAS_MARKDOWN_CODE_BLOCKS')
    if '```' in content and '```html' not in content:
        analysis['format_variations'].append('HAS_OTHER_CODE_BLOCKS')
    
    return analysis

def analyze_all_fiches():
    """Analyse TOUTES les fiches et génère un rapport détaillé"""
    fiches_dir = Path('roadmap/Brainstorming/fiches-markdown-v2')
    
    if not fiches_dir.exists():
        print(f"[ERREUR] Dossier non trouvé: {fiches_dir}")
        print(f"Répertoire actuel: {Path.cwd()}")
        return False
    
    all_fiches = list(fiches_dir.glob('*.md'))
    
    if not all_fiches:
        print(f"[ERREUR] Aucune fiche trouvée dans {fiches_dir}")
        return False
    
    print(f"Analyse de {len(all_fiches)} fiches...")
    
    results = []
    pattern_counter = Counter()
    problematic_fiches = []
    
    for fiche in all_fiches:
        try:
            analysis = analyze_fiche_comprehensive(fiche)
            results.append(analysis)
            
            # Compter les patterns
            for pattern in analysis['extrait_patterns']:
                pattern_counter[pattern] += 1
            
            # Identifier les fiches problématiques
            if not analysis['has_html'] or analysis['extrait_count'] == 0:
                problematic_fiches.append({
                    'name': analysis['name'],
                    'issues': analysis['format_variations']
                })
        except Exception as e:
            print(f"[ERREUR] Analyse de {fiche.name}: {e}")
            problematic_fiches.append({
                'name': fiche.name,
                'issues': ['PARSE_ERROR']
            })
    
    # Générer le rapport
    report = {
        'total_fiches': len(all_fiches),
        'fiches_analyzed': len(results),
        'fiches_with_html': sum(1 for r in results if r['has_html']),
        'fiches_without_html': sum(1 for r in results if not r['has_html']),
        'pattern_distribution': dict(pattern_counter),
        'problematic_fiches': problematic_fiches,
        'html_tags_found': list(set(tag for r in results for tag in r['html_tags'])),
        'metadata_coverage': {
            'with_url': sum(1 for r in results if r['metadata'].get('has_url')),
            'with_title': sum(1 for r in results if r['metadata'].get('has_title')),
            'with_version': sum(1 for r in results if r['metadata'].get('has_version')),
            'with_doc_link': sum(1 for r in results if r['metadata'].get('has_doc_link'))
        },
        'recommendations': []
    }
    
    # Analyser et recommander
    if report['fiches_without_html'] > 0:
        report['recommendations'].append(
            f"ATTENTION: {report['fiches_without_html']} fiches sans HTML - Prévoir fallback ou exclusion"
        )
    
    pattern_types = len(set(pattern_counter.keys()))
    if pattern_types > 2:
        report['recommendations'].append(
            f"VARIATION: {pattern_types} formats différents détectés - Parser adaptatif nécessaire"
        )
    
    # Afficher le rapport
    print("\n" + "="*60)
    print("RAPPORT D'ANALYSE DES FICHES DSFR")
    print("="*60)
    print(f"Total fiches trouvées: {report['total_fiches']}")
    print(f"Fiches analysées avec succès: {report['fiches_analyzed']}")
    print(f"Fiches avec HTML: {report['fiches_with_html']}")
    print(f"Fiches SANS HTML: {report['fiches_without_html']}")
    
    print(f"\nCouverture des métadonnées:")
    print(f"  - Avec URL: {report['metadata_coverage']['with_url']}")
    print(f"  - Avec Title: {report['metadata_coverage']['with_title']}")
    print(f"  - Avec Version DSFR: {report['metadata_coverage']['with_version']}")
    print(f"  - Avec lien Documentation: {report['metadata_coverage']['with_doc_link']}")
    
    print(f"\nDistribution des patterns d'extraction:")
    for pattern, count in pattern_counter.most_common():
        print(f"  - {pattern}: {count} occurrences")
    
    if problematic_fiches:
        print(f"\nFiches problématiques ({len(problematic_fiches)}):")
        for pf in problematic_fiches[:10]:  # Afficher les 10 premières
            print(f"  - {pf['name']}: {', '.join(pf['issues'])}")
        if len(problematic_fiches) > 10:
            print(f"  ... et {len(problematic_fiches)-10} autres")
    
    if report['html_tags_found']:
        print(f"\nTags HTML trouvés (top 15): {', '.join(sorted(report['html_tags_found'])[:15])}")
    
    if report['recommendations']:
        print("\nRECOMMANDATIONS:")
        for rec in report['recommendations']:
            print(f"  • {rec}")
    
    # Sauvegarder le rapport complet
    report_path = Path('fiches_analysis_report.json')
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"\nRapport complet sauvegardé: {report_path.absolute()}")
    
    # Décision Go/No-Go
    if report['fiches_analyzed'] == 0:
        print("\n[ERREUR] Aucune fiche analysée - Vérifier le chemin")
        return False
    
    success_rate = report['fiches_with_html'] / report['fiches_analyzed'] * 100
    print(f"\n" + "="*60)
    print(f"TAUX DE FICHES AVEC HTML: {success_rate:.1f}%")
    print("="*60)
    
    if success_rate >= 90:
        print("[GO] ✓ Extraction possible avec parser standard")
        print("     → Les fiches sans HTML seront ignorées ou marquées 'doc-only'")
        return True
    elif success_rate >= 70:
        print("[ATTENTION] ⚠ Extraction possible mais adaptations nécessaires")
        print("     → Parser multi-patterns recommandé")
        print("     → Prévoir +1 jour pour adaptations")
        return True
    else:
        print("[NO-GO] ✗ Trop de variations - Stratégie alternative requise")
        print("     → Option 1: Focus sur top 48 composants")
        print("     → Option 2: Parser l'ancien projet Node.js")
        print("     → Option 3: Extraction manuelle ciblée")
        return False

if __name__ == "__main__":
    import sys
    success = analyze_all_fiches()
    sys.exit(0 if success else 1)