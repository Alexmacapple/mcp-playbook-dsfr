#!/usr/bin/env python3
"""
extract_components_kb_v2.py - Version améliorée pour capturer TOUTES les variantes
Corrige : déduplication et extraction incomplète
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

def normalize_component_name(filename, metadata):
    """Normalise le nom du composant en utilisant les métadonnées"""
    # D'abord essayer d'extraire depuis les métadonnées
    if metadata and 'component_name' in metadata:
        comp_name = metadata['component_name'].lower()
        # Nettoyer le nom
        comp_name = re.sub(r'\([^)]+\)', '', comp_name)  # Enlever (button) etc.
        comp_name = comp_name.strip()
        
        # Mapping FR → EN
        name_map = {
            'bouton': 'button',
            'carte': 'card',
            'alerte': 'alert',
            'formulaire': 'form',
            'tableau': 'table',
            'accordéon': 'accordion',
            'badge': 'badge',
            'tag': 'tag',
            'interrupteur': 'toggle',
            'tuile': 'tile',
            'navigation': 'navigation',
            'en-tête': 'header',
            'pied de page': 'footer',
            'modale': 'modal',
            'bandeau': 'banner',
            'case à cocher': 'checkbox',
            'champ de saisie': 'input',
            'bouton radio': 'radio',
            'pagination': 'pagination',
            "fil d'ariane": 'breadcrumb',
            'onglet': 'tab',
            'onglets': 'tabs',
            'menu': 'menu',
            'liste': 'list',
            'lien': 'link',
            'contenu médias': 'media',
            'mise en exergue': 'highlight',
            'mises en exergue': 'highlight',
            'citation': 'quote',
            'bouton franceconnect': 'button_franceconnect'
        }
        
        for fr, en in name_map.items():
            if fr in comp_name:
                return en
    
    # Fallback sur le nom de fichier
    stem = filename.lower()
    stem = re.sub(r'fiche-\d+-', '', stem)  # Enlever fiche-030-
    stem = stem.replace('-systeme-de-design', '').replace('.md', '')
    stem = stem.replace('-', '_')
    
    # Dernier mapping sur le stem
    simple_map = {
        'bouton': 'button',
        'carte': 'card',
        'alerte': 'alert'
    }
    
    for fr, en in simple_map.items():
        if fr in stem:
            return en + '_' + stem.replace(fr, '').strip('_') if stem != fr else en
    
    return stem

def extract_all_variants(content):
    """Extrait TOUTES les variantes avec une méthode améliorée"""
    variants = {}
    lines = content.split('\n')
    
    current_category = "default"
    current_variant = None
    variant_counter = 0
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Catégorie principale (## Bouton primaire)
        if line.startswith('## ') and 'Extrait' not in line:
            current_category = line.replace('##', '').strip()
            current_category = re.sub(r'[^a-zA-Z0-9À-ÿ\s]', '', current_category)
            current_category = current_category.replace(' ', '_').lower()
        
        # Sous-variante (### Bouton simple) - AVANT le pattern ###\nExtrait
        elif line.startswith('### ') and 'Extrait' not in line and line.strip() != '###':
            current_variant = line.replace('###', '').strip()
            current_variant = re.sub(r'[^a-zA-Z0-9À-ÿ\s]', '', current_variant)
            current_variant = current_variant.replace(' ', '_').lower()
        
        # Pattern "###\nExtrait de code"
        elif line.strip() == '###' and i+1 < len(lines) and 'Extrait de code' in lines[i+1]:
            i += 2  # Sauter "###" et "Extrait de code"
            
            # Collecter tout le HTML qui suit
            html_lines = []
            found_html = False
            
            while i < len(lines):
                current_line = lines[i].strip()
                
                # Si on trouve une ligne qui commence par <
                if current_line.startswith('<'):
                    found_html = True
                    html_lines.append(lines[i])
                    i += 1
                    
                    # Continuer à collecter jusqu'à une ligne vide ou nouvelle section
                    while i < len(lines):
                        if not lines[i].strip():  # Ligne vide
                            break
                        if lines[i].startswith('#'):  # Nouvelle section
                            break
                        html_lines.append(lines[i])
                        i += 1
                    break
                    
                # Si on trouve une nouvelle section sans avoir trouvé de HTML
                elif current_line.startswith('#'):
                    break
                    
                # Ligne vide, continuer à chercher
                elif not current_line:
                    i += 1
                    
                # Autre contenu (peut-être description), ignorer
                else:
                    i += 1
                    if i - (i-2) > 10:  # Sécurité : ne pas chercher trop loin
                        break
            
            # Sauvegarder la variante si on a trouvé du HTML
            if html_lines:
                variant_counter += 1
                # Créer une clé unique
                if current_variant:
                    variant_key = f"{current_category}.{current_variant}_{variant_counter}"
                else:
                    variant_key = f"{current_category}.variant_{variant_counter}"
                
                html_code = '\n'.join(html_lines).strip()
                
                variants[variant_key] = {
                    'name': current_variant or f"Variante {variant_counter}",
                    'category': current_category,
                    'html': html_code,
                    'order': variant_counter
                }
                
                # Reset current_variant pour la prochaine
                current_variant = None
            
            continue  # Important : on a déjà incrémenté i
        
        i += 1
    
    return variants

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
    """Extrait les 88 composants avec méthode améliorée"""
    fiches_dir = Path('roadmap/Brainstorming/fiches-markdown-v2')
    
    # Charger la liste des composants avec HTML
    with open('components_analysis.json', 'r', encoding='utf-8') as f:
        analysis = json.load(f)
    
    components_with_html = analysis['components_with_html']
    knowledge_base = {}
    
    # Pour éviter les duplications, on va grouper par type de composant
    components_by_type = defaultdict(list)
    
    print(f"Extraction améliorée de {len(components_with_html)} fichiers...")
    
    # Première passe : grouper les fichiers par type
    for filename in components_with_html:
        fiche_path = fiches_dir / filename
        if not fiche_path.exists():
            continue
            
        content = fiche_path.read_text(encoding='utf-8')
        metadata = extract_metadata(content)
        component_name = normalize_component_name(filename, metadata)
        
        components_by_type[component_name].append({
            'filename': filename,
            'content': content,
            'metadata': metadata
        })
    
    print(f"Types de composants uniques: {len(components_by_type)}")
    
    # Deuxième passe : extraire et fusionner les variantes
    for component_name, files in components_by_type.items():
        print(f"\nTraitement de {component_name} ({len(files)} fichier(s))...")
        
        all_variants = {}
        all_notes = []
        merged_metadata = {}
        
        for file_data in files:
            try:
                # Extraire les variantes de ce fichier
                variants = extract_all_variants(file_data['content'])
                
                # Ajouter les variantes (avec préfixe si plusieurs fichiers)
                if len(files) > 1:
                    file_prefix = file_data['filename'].split('-')[1] if '-' in file_data['filename'] else ''
                    for key, variant in variants.items():
                        new_key = f"{file_prefix}_{key}" if file_prefix else key
                        all_variants[new_key] = variant
                else:
                    all_variants.update(variants)
                
                # Fusionner les métadonnées (priorité au premier fichier)
                if not merged_metadata and file_data['metadata']:
                    merged_metadata = file_data['metadata']
                
                # Collecter les notes
                notes = extract_usage_notes(file_data['content'])
                all_notes.extend(notes)
                
                print(f"  - {file_data['filename']}: {len(variants)} variantes")
                
            except Exception as e:
                print(f"  [ERREUR] {file_data['filename']}: {e}")
        
        # Créer l'entrée dans la knowledge base
        knowledge_base[component_name] = {
            'source_files': [f['filename'] for f in files],
            'metadata': merged_metadata,
            'variants': all_variants,
            'usage_notes': list(set(all_notes)),
            'stats': {
                'variant_count': len(all_variants),
                'file_count': len(files),
                'has_documentation': bool(merged_metadata.get('documentation')),
                'has_usage_notes': len(all_notes) > 0
            }
        }
        
        print(f"  Total: {len(all_variants)} variantes extraites")
    
    # Sauvegarder la Knowledge Base
    output_path = Path('components_knowledge_base_v2.json')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(knowledge_base, f, indent=2, ensure_ascii=False)
    
    # Rapport final
    print("\n" + "="*60)
    print("EXTRACTION AMÉLIORÉE TERMINÉE")
    print("="*60)
    print(f"Composants uniques extraits: {len(knowledge_base)}")
    
    total_variants = sum(comp['stats']['variant_count'] for comp in knowledge_base.values())
    print(f"Total variantes: {total_variants}")
    
    # Top 10 composants
    top_components = sorted(
        knowledge_base.items(),
        key=lambda x: x[1]['stats']['variant_count'],
        reverse=True
    )[:10]
    
    print("\nTop 10 composants (par nombre de variantes):")
    for name, data in top_components:
        print(f"  {name}: {data['stats']['variant_count']} variantes ({data['stats']['file_count']} fichier(s))")
    
    print(f"\nKnowledge Base V2 sauvegardée: {output_path.absolute()}")
    
    # Taille du fichier
    size_mb = output_path.stat().st_size / (1024 * 1024)
    print(f"Taille: {size_mb:.2f} MB")
    
    return knowledge_base

if __name__ == "__main__":
    kb = extract_all_components()
    
    # Test sur le bouton
    if 'button' in kb:
        button = kb['button']
        print(f"\n[TEST] Composant 'button':")
        print(f"  - Fichiers sources: {button['stats']['file_count']}")
        print(f"  - Variantes totales: {button['stats']['variant_count']}")
        if button['variants']:
            first_key = list(button['variants'].keys())[0]
            first_variant = button['variants'][first_key]
            print(f"  - Première variante: {first_variant['name']}")
            print(f"    HTML: {first_variant['html'][:100]}...")