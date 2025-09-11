#!/usr/bin/env python3
"""
extract_components_kb.py - Extraction des 88 composants DSFR en Knowledge Base
Basé sur l'analyse : 88/98 composants ont du HTML (89.8% de succès)
"""

import re
import json
from pathlib import Path
from collections import defaultdict

def is_real_component(filename):
    """Filtre pour garder seulement les vrais composants"""
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
    return True

def extract_metadata(content):
    """Extrait les métadonnées du composant"""
    metadata = {}
    
    # URL officielle
    url_match = re.search(r'URL:\s*\n(.+)', content)
    if url_match:
        metadata['url'] = url_match.group(1).strip()
    
    # Title
    title_match = re.search(r'Title:\s*\n(.+)', content)
    if title_match:
        metadata['title'] = title_match.group(1).strip()
    
    # Version DSFR
    version_match = re.search(r'DSFR v([\d.]+)', content)
    if version_match:
        metadata['version'] = f"DSFR v{version_match.group(1)}"
    
    # Description (après le premier #)
    desc_match = re.search(r'#\s+([^\n]+)\n\n([^\n]+)', content)
    if desc_match:
        metadata['component_name'] = desc_match.group(1).strip()
        metadata['description'] = desc_match.group(2).strip()
    
    # Lien documentation
    doc_match = re.search(r'\[Documentation\]\(([^)]+)\)', content)
    if doc_match:
        metadata['documentation'] = doc_match.group(1)
    
    return metadata

def normalize_component_name(filename):
    """Normalise le nom du composant depuis le nom de fichier"""
    # Mapping FR → EN pour cohérence
    name_map = {
        'bouton': 'button',
        'carte': 'card',
        'alerte': 'alert',
        'formulaire': 'form',
        'tableau': 'table',
        'accordeon': 'accordion',
        'badge': 'badge',
        'tag': 'tag',
        'interrupteur': 'toggle',
        'tuile': 'tile',
        'navigation': 'navigation',
        'en-tete': 'header',
        'pied-de-page': 'footer',
        'modale': 'modal',
        'bandeau': 'banner',
        'case-a-cocher': 'checkbox',
        'champ-de-saisie': 'input',
        'bouton-radio': 'radio',
        'pagination': 'pagination',
        'fil-d-ariane': 'breadcrumb',
        'onglet': 'tab',
        'menu': 'menu',
        'liste': 'list',
        'lien': 'link'
    }
    
    stem = filename.lower()
    for fr, en in name_map.items():
        if fr in stem:
            return en
    
    # Fallback : extraire le mot principal
    parts = stem.replace('fiche-', '').replace('-systeme-de-design', '').replace('.md', '').split('-')
    if len(parts) > 1:
        return parts[1] if parts[0].isdigit() else parts[0]
    return parts[0] if parts else 'unknown'

def extract_variants(content):
    """Extrait toutes les variantes HTML du composant"""
    variants = defaultdict(list)
    lines = content.split('\n')
    
    current_category = None
    current_variant = None
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Catégorie principale (## Bouton primaire)
        if line.startswith('## ') and 'Extrait' not in line:
            current_category = line.replace('##', '').strip()
        
        # Sous-variante (### Bouton simple)
        elif line.startswith('### ') and 'Extrait' not in line and line.strip() != '###':
            current_variant = line.replace('###', '').strip()
        
        # Pattern observé : "###" seul puis "Extrait de code"
        elif line.strip() == '###' and i+1 < len(lines) and 'Extrait de code' in lines[i+1]:
            i += 2  # Sauter "###" et "Extrait de code"
            
            # Extraire le HTML
            html_lines = []
            while i < len(lines):
                if lines[i].strip():
                    if lines[i].strip().startswith('<'):
                        # Début du HTML
                        html_lines.append(lines[i])
                        i += 1
                        # Continuer jusqu'à la fin du bloc
                        while i < len(lines) and lines[i].strip() and not lines[i].startswith('#'):
                            html_lines.append(lines[i])
                            i += 1
                        break
                    elif lines[i].startswith('#'):
                        break
                i += 1
            
            # Sauvegarder la variante
            if html_lines and current_variant:
                html_code = '\n'.join(html_lines).strip()
                variant_key = f"{current_category or 'default'}.{current_variant}".replace(' ', '_').lower()
                variants[variant_key] = {
                    'name': current_variant,
                    'category': current_category or 'default',
                    'html': html_code
                }
        
        i += 1
    
    return dict(variants)

def extract_usage_notes(content):
    """Extrait les notes d'usage et recommandations"""
    notes = []
    
    # Patterns de recommandations
    patterns = [
        r"A n'appliquer qu'en cas[^.]+\.",
        r"L'attribut [^.]+obligatoire[^.]+\.",
        r"Utiliser <[^>]+>[^.]+\.",
        r"Ne pas utiliser[^.]+\.",
        r"Attention[^.]+\.",
        r"Important[^.]+\."
    ]
    
    for pattern in patterns:
        matches = re.findall(pattern, content, re.IGNORECASE)
        notes.extend(matches)
    
    return list(set(notes))  # Dédupliquer

def extract_all_components():
    """Extrait les 88 composants identifiés en Knowledge Base complète"""
    fiches_dir = Path('roadmap/Brainstorming/fiches-markdown-v2')
    
    # Charger la liste des composants avec HTML depuis l'analyse
    with open('components_analysis.json', 'r', encoding='utf-8') as f:
        analysis = json.load(f)
    
    components_with_html = analysis['components_with_html']
    knowledge_base = {}
    
    print(f"Extraction de {len(components_with_html)} composants...")
    
    for filename in components_with_html:
        fiche_path = fiches_dir / filename
        if not fiche_path.exists():
            print(f"[ATTENTION] Fichier non trouvé: {filename}")
            continue
        
        try:
            content = fiche_path.read_text(encoding='utf-8')
            component_name = normalize_component_name(filename)
            
            # Extraire toutes les données
            knowledge_base[component_name] = {
                'source_file': filename,
                'metadata': extract_metadata(content),
                'variants': extract_variants(content),
                'usage_notes': extract_usage_notes(content),
                'stats': {
                    'variant_count': 0,
                    'has_documentation': False,
                    'has_usage_notes': False
                }
            }
            
            # Calculer les stats
            kb = knowledge_base[component_name]
            kb['stats']['variant_count'] = len(kb['variants'])
            kb['stats']['has_documentation'] = bool(kb['metadata'].get('documentation'))
            kb['stats']['has_usage_notes'] = len(kb['usage_notes']) > 0
            
            print(f"✓ {component_name}: {kb['stats']['variant_count']} variantes extraites")
            
        except Exception as e:
            print(f"[ERREUR] {filename}: {e}")
    
    # Sauvegarder la Knowledge Base
    output_path = Path('components_knowledge_base.json')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(knowledge_base, f, indent=2, ensure_ascii=False)
    
    # Rapport final
    print("\n" + "="*60)
    print("EXTRACTION TERMINÉE")
    print("="*60)
    print(f"Composants extraits: {len(knowledge_base)}")
    
    total_variants = sum(comp['stats']['variant_count'] for comp in knowledge_base.values())
    print(f"Total variantes: {total_variants}")
    
    with_doc = sum(1 for comp in knowledge_base.values() if comp['stats']['has_documentation'])
    print(f"Avec documentation: {with_doc}/{len(knowledge_base)}")
    
    with_notes = sum(1 for comp in knowledge_base.values() if comp['stats']['has_usage_notes'])
    print(f"Avec notes d'usage: {with_notes}/{len(knowledge_base)}")
    
    # Top 10 composants par nombre de variantes
    top_components = sorted(
        knowledge_base.items(),
        key=lambda x: x[1]['stats']['variant_count'],
        reverse=True
    )[:10]
    
    print("\nTop 10 composants (par nombre de variantes):")
    for name, data in top_components:
        print(f"  {name}: {data['stats']['variant_count']} variantes")
    
    print(f"\nKnowledge Base sauvegardée: {output_path.absolute()}")
    
    # Taille du fichier
    size_mb = output_path.stat().st_size / (1024 * 1024)
    print(f"Taille: {size_mb:.2f} MB")
    
    if size_mb < 2:
        print("[OK] Taille optimale pour chargement rapide")
    else:
        print("[ATTENTION] Fichier >2MB, considérer compression")
    
    return knowledge_base

if __name__ == "__main__":
    kb = extract_all_components()
    
    # Test rapide sur le bouton
    if 'button' in kb:
        button = kb['button']
        print(f"\n[TEST] Bouton:")
        print(f"  - Variantes: {button['stats']['variant_count']}")
        print(f"  - Description: {button['metadata'].get('description', 'N/A')[:100]}...")
        
        # Afficher une variante
        if button['variants']:
            first_variant = list(button['variants'].values())[0]
            print(f"  - Exemple HTML ({first_variant['name']}):")
            print(f"    {first_variant['html'][:200]}...")