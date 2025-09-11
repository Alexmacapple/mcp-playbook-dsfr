#!/usr/bin/env python3
"""
extract_documentation_kb.py - Extraction de la documentation DSFR (125 fiches restantes)
Extrait : fondamentaux, utilitaires, templates, guidelines
"""

import re
import json
from pathlib import Path
from collections import defaultdict
from typing import Dict, Any, List

def categorize_fiche(filename: str, content: str) -> str:
    """
    Cat\u00e9gorise une fiche selon son type.
    
    Returns:
        Cat\u00e9gorie : foundations, utilities, templates, guidelines, pictograms
    """
    filename_lower = filename.lower()
    
    # Fondamentaux (typographie, couleurs, grille, etc.)
    if 'fondamentaux' in filename_lower:
        if 'typographie' in content.lower():
            return 'foundations.typography'
        elif 'grille' in content.lower():
            return 'foundations.grid'
        elif 'couleur' in content.lower() or 'color' in content.lower():
            return 'foundations.colors'
        elif 'espacement' in content.lower() or 'spacing' in content.lower():
            return 'foundations.spacing'
        else:
            return 'foundations.general'
    
    # Utilitaires CSS
    elif 'utilitaire' in filename_lower:
        if 'couleur' in content.lower() or 'color' in content.lower():
            return 'utilities.colors'
        elif 'icone' in content.lower() or 'icon' in content.lower():
            return 'utilities.icons'
        elif 'pictogramme' in content.lower():
            return 'utilities.pictograms'
        else:
            return 'utilities.general'
    
    # Outils d'analyse
    elif 'outils-d-analyse' in filename_lower:
        return 'utilities.analysis'
    
    # Mod\u00e8les de pages
    elif 'modele-de-page' in filename_lower or 'pages-de' in filename_lower:
        if 'erreur' in filename_lower or '404' in content or '500' in content:
            return 'templates.error'
        elif 'connexion' in filename_lower or 'login' in content.lower():
            return 'templates.auth'
        elif 'creation-de-compte' in filename_lower:
            return 'templates.signup'
        else:
            return 'templates.general'
    
    # Pictogrammes th\u00e9matiques
    elif 'pictogramme' in filename_lower:
        if 'accessibilite' in filename_lower:
            return 'pictograms.accessibility'
        elif 'business' in filename_lower:
            return 'pictograms.business'
        elif 'health' in filename_lower:
            return 'pictograms.health'
        elif 'institution' in filename_lower:
            return 'pictograms.institutions'
        else:
            return 'pictograms.general'
    
    # Ic\u00f4nes
    elif 'icone' in filename_lower:
        return 'icons.general'
    
    # Principes et guidelines
    elif 'principe' in filename_lower or 'accessibilite' in filename_lower:
        return 'guidelines.accessibility'
    
    # Codes de statut HTTP
    elif 'codes-de-statut' in filename_lower:
        return 'guidelines.http_status'
    
    return 'other'

def extract_documentation(content: str) -> Dict[str, Any]:
    """
    Extrait la documentation structur\u00e9e d'une fiche.
    """
    doc = {
        'title': '',
        'description': '',
        'sections': [],
        'code_examples': [],
        'links': [],
        'tokens': {},
        'guidelines': []
    }
    
    # Titre
    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if title_match:
        doc['title'] = title_match.group(1).strip()
    
    # Description (premier paragraphe apr\u00e8s le titre)
    desc_match = re.search(r'^#[^\n]+\n\n([^\n]+)', content, re.MULTILINE)
    if desc_match:
        doc['description'] = desc_match.group(1).strip()
    
    # Sections (### headers)
    sections = re.findall(r'^###\s+([^\n]+)\n\n([^#]+?)(?=^###|\Z)', content, re.MULTILINE | re.DOTALL)
    for section_title, section_content in sections:
        if 'Extrait de code' not in section_title:
            doc['sections'].append({
                'title': section_title.strip(),
                'content': section_content.strip()
            })
    
    # Exemples de code
    code_blocks = re.findall(r'```(?:html|css|javascript)?\n(.*?)\n```', content, re.DOTALL)
    doc['code_examples'].extend(code_blocks)
    
    # Extraits HTML apr\u00e8s "Extrait de code"
    html_extracts = re.findall(r'###\s*\nExtrait de code\s*\n+((?:<[^>]+>.*?</[^>]+>)+)', content, re.DOTALL)
    doc['code_examples'].extend(html_extracts)
    
    # Liens de documentation
    links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)
    for link_text, link_url in links:
        if 'systeme-de-design.gouv.fr' in link_url:
            doc['links'].append({
                'text': link_text,
                'url': link_url
            })
    
    # Extraction de tokens (couleurs, espacements, etc.)
    # Couleurs hex
    colors = re.findall(r'#[0-9A-Fa-f]{3,6}\b', content)
    if colors:
        doc['tokens']['colors'] = list(set(colors))
    
    # Espacements (fr-* classes mentionn\u00e9es)
    spacing_classes = re.findall(r'fr-[mp][btlrxy]?-\d+[vw]?', content)
    if spacing_classes:
        doc['tokens']['spacing'] = list(set(spacing_classes))
    
    # Guidelines et recommandations
    guidelines_patterns = [
        r"Il est recommand\u00e9[^.]+\.",
        r"Attention[^.]+\.",
        r"Important[^.]+\.",
        r"Ne pas[^.]+\.",
        r"Toujours[^.]+\.",
        r"Eviter[^.]+\."
    ]
    
    for pattern in guidelines_patterns:
        matches = re.findall(pattern, content, re.IGNORECASE)
        doc['guidelines'].extend(matches)
    
    return doc

def extract_css_utilities(content: str) -> Dict[str, List[str]]:
    """
    Extrait les classes CSS utilitaires d'une fiche.
    """
    utilities = {
        'colors': [],
        'spacing': [],
        'typography': [],
        'display': [],
        'grid': [],
        'other': []
    }
    
    # Classes de couleurs
    color_classes = re.findall(r'fr-(?:background|text)-[a-z0-9-]+', content)
    utilities['colors'].extend(color_classes)
    
    # Classes d'espacement
    spacing_classes = re.findall(r'fr-[mp][btlrxy]?-\d+[vw]?', content)
    utilities['spacing'].extend(spacing_classes)
    
    # Classes typographiques
    typo_classes = re.findall(r'fr-(?:text|h\d|display)-[a-z0-9-]+', content)
    utilities['typography'].extend(typo_classes)
    
    # Classes de display
    display_classes = re.findall(r'fr-(?:hidden|unhidden|displayed|undisplayed)', content)
    utilities['display'].extend(display_classes)
    
    # Classes de grille
    grid_classes = re.findall(r'fr-(?:grid-row|col)(?:-\d+)?(?:-[a-z]+)?', content)
    utilities['grid'].extend(grid_classes)
    
    # D\u00e9dupliquer
    for key in utilities:
        utilities[key] = list(set(utilities[key]))
    
    return utilities

def process_all_documentation_fiches():
    """
    Traite les 125 fiches de documentation non-composants.
    """
    fiches_dir = Path('roadmap/Brainstorming/fiches-markdown-v2')
    
    # Charger la liste des composants d\u00e9j\u00e0 trait\u00e9s
    with open('components_analysis.json', 'r', encoding='utf-8') as f:
        analysis = json.load(f)
    
    already_processed = set(analysis['components_with_html'])
    
    # Structure de la knowledge base documentation
    doc_kb = {
        'foundations': {},
        'utilities': {},
        'templates': {},
        'guidelines': {},
        'pictograms': {},
        'icons': {},
        'other': {},
        'metadata': {
            'total_files': 0,
            'categories': {}
        }
    }
    
    # Stats par cat\u00e9gorie
    category_stats = defaultdict(int)
    
    print("EXTRACTION DE LA DOCUMENTATION DSFR")
    print("=" * 60)
    
    # Parcourir tous les fichiers
    all_files = list(fiches_dir.glob('*.md'))
    remaining_files = [f for f in all_files if f.name not in already_processed]
    
    print(f"Fichiers \u00e0 traiter: {len(remaining_files)}")
    
    for fiche_path in remaining_files:
        try:
            content = fiche_path.read_text(encoding='utf-8')
            category = categorize_fiche(fiche_path.name, content)
            category_stats[category] += 1
            
            # Extraire la documentation
            doc_data = extract_documentation(content)
            doc_data['source_file'] = fiche_path.name
            
            # Extraire les utilitaires CSS si pertinent
            if 'utilities' in category or 'foundations' in category:
                doc_data['css_utilities'] = extract_css_utilities(content)
            
            # Stocker dans la bonne cat\u00e9gorie
            main_cat = category.split('.')[0]
            sub_cat = category.split('.')[1] if '.' in category else 'general'
            
            if main_cat not in doc_kb:
                doc_kb[main_cat] = {}
            
            if sub_cat not in doc_kb[main_cat]:
                doc_kb[main_cat][sub_cat] = []
            
            doc_kb[main_cat][sub_cat].append(doc_data)
            
            # Afficher la progression
            if len(doc_kb[main_cat][sub_cat]) == 1:
                print(f"  [{main_cat}] Nouvelle sous-cat\u00e9gorie: {sub_cat}")
            
        except Exception as e:
            print(f"  [ERREUR] {fiche_path.name}: {e}")
    
    # Ajouter les m\u00e9tadonn\u00e9es
    doc_kb['metadata']['total_files'] = len(remaining_files)
    doc_kb['metadata']['categories'] = dict(category_stats)
    
    # Statistiques par cat\u00e9gorie principale
    for main_cat in ['foundations', 'utilities', 'templates', 'guidelines']:
        if main_cat in doc_kb:
            total = sum(len(items) for items in doc_kb[main_cat].values() if isinstance(items, list))
            doc_kb['metadata'][f'{main_cat}_count'] = total
    
    # Sauvegarder la knowledge base documentation
    output_path = Path('documentation_knowledge_base.json')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(doc_kb, f, indent=2, ensure_ascii=False)
    
    # Rapport final
    print("\n" + "=" * 60)
    print("EXTRACTION TERMIN\u00c9E")
    print("=" * 60)
    print(f"Fichiers trait\u00e9s: {len(remaining_files)}")
    print("\nR\u00e9partition par cat\u00e9gorie:")
    
    for category, count in sorted(category_stats.items()):
        print(f"  {category}: {count} fichiers")
    
    print(f"\nKnowledge Base Documentation sauv\u00e9e: {output_path.absolute()}")
    
    # Taille du fichier
    size_kb = output_path.stat().st_size / 1024
    print(f"Taille: {size_kb:.2f} KB")
    
    # Exemples de contenu extrait
    print("\nExemples de contenu extrait:")
    
    if 'foundations' in doc_kb and doc_kb['foundations']:
        print("  Fondamentaux:")
        for sub_cat, items in doc_kb['foundations'].items():
            if items:
                print(f"    - {sub_cat}: {len(items)} fiches")
    
    if 'utilities' in doc_kb and doc_kb['utilities']:
        print("  Utilitaires:")
        for sub_cat, items in doc_kb['utilities'].items():
            if items:
                print(f"    - {sub_cat}: {len(items)} fiches")
    
    return doc_kb

if __name__ == "__main__":
    doc_kb = process_all_documentation_fiches()
    
    # Test rapide
    print("\n[TEST] V\u00e9rification de l'extraction:")
    
    # V\u00e9rifier les fondamentaux
    if 'foundations' in doc_kb:
        print(f"  Fondamentaux extraits: {doc_kb['metadata'].get('foundations_count', 0)}")
    
    # V\u00e9rifier les utilitaires
    if 'utilities' in doc_kb:
        print(f"  Utilitaires extraits: {doc_kb['metadata'].get('utilities_count', 0)}")
    
    # V\u00e9rifier les templates
    if 'templates' in doc_kb:
        print(f"  Templates extraits: {doc_kb['metadata'].get('templates_count', 0)}")
    
    print("\nExtraction documentation compl\u00e8te!")