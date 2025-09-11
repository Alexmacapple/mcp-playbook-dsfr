#!/usr/bin/env python3
"""
Test d'extraction sur le fichier bouton pour diagnostiquer le problème
"""

import re
from pathlib import Path

def analyze_button_file():
    """Analyse détaillée du fichier bouton"""
    fiche_path = Path('roadmap/Brainstorming/fiches-markdown-v2/fiche-030-bouton-systeme-de-design.md')
    content = fiche_path.read_text(encoding='utf-8')
    
    print("ANALYSE DU FICHIER BOUTON")
    print("="*60)
    
    # Compter les patterns
    extrait_count = content.count('Extrait de code')
    print(f"Nombre de 'Extrait de code': {extrait_count}")
    
    # Analyser la structure ligne par ligne
    lines = content.split('\n')
    extrait_positions = []
    html_blocks_found = []
    
    for i, line in enumerate(lines):
        # Chercher "Extrait de code"
        if 'Extrait de code' in line:
            extrait_positions.append(i)
            print(f"\nLigne {i}: Extrait de code trouvé")
            
            # Regarder les lignes avant
            if i > 0:
                print(f"  Ligne {i-1}: {lines[i-1][:50]}")
            
            # Regarder les lignes après pour trouver le HTML
            for j in range(i+1, min(i+10, len(lines))):
                if lines[j].strip().startswith('<'):
                    print(f"  Ligne {j}: HTML trouvé: {lines[j][:50]}...")
                    html_blocks_found.append(j)
                    break
                elif lines[j].strip() and not lines[j].isspace():
                    print(f"  Ligne {j}: {lines[j][:50]}")
                    if lines[j].startswith('#'):
                        print("    -> Nouvelle section, pas de HTML trouvé")
                        break
    
    print(f"\n{len(html_blocks_found)} blocs HTML trouvés sur {extrait_count} extraits")
    
    # Tester le pattern actuel
    print("\nTEST DU PATTERN ACTUEL:")
    pattern_count = 0
    for i, line in enumerate(lines):
        if line.strip() == '###' and i+1 < len(lines) and 'Extrait de code' in lines[i+1]:
            pattern_count += 1
    
    print(f"Pattern '###\\nExtrait de code' trouvé: {pattern_count} fois")
    
    # Chercher d'autres patterns
    print("\nAUTRES PATTERNS DÉTECTÉS:")
    for i, line in enumerate(lines):
        if 'Extrait de code' in line:
            prev_line = lines[i-1] if i > 0 else ""
            if prev_line.strip() != '###':
                print(f"  Ligne {i-1}: '{prev_line.strip()}' (pas ###)")
    
    return extrait_count, len(html_blocks_found)

if __name__ == "__main__":
    total, found = analyze_button_file()
    
    print("\n" + "="*60)
    print(f"RÉSULTAT: {found}/{total} extraits avec HTML trouvé")
    
    if found < total:
        print("[PROBLÈME] Le parser ne capture pas tous les extraits")
        print("Le format varie probablement entre les extraits")