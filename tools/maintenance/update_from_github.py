#!/usr/bin/env python3
"""
Script de mise à jour de la documentation DSFR depuis le dépôt GitHub officiel
Source : https://github.com/GouvernementFR/dsfr
"""

import json
import os
import re
import base64
from datetime import datetime
from typing import Dict, List, Optional
import time
import urllib.request
import urllib.error

class DSFRGitHubUpdater:
    def __init__(self):
        self.github_api = "https://api.github.com"
        self.repo = "GouvernementFR/dsfr"
        self.components_path = "src/dsfr/component"
        
        # Liste complète des composants trouvés
        self.components = [
            "accordion", "alert", "badge", "breadcrumb", "button", "callout",
            "card", "checkbox", "combobox", "composition", "connect", "consent",
            "content", "display", "download", "dropdown", "follow", "footer",
            "form", "header", "highlight", "input", "link", "logo", "modal",
            "navigation", "notice", "pagination", "password", "quote", "radio",
            "range", "search", "segmented", "select", "share", "sidemenu",
            "skiplink", "stepper", "summary", "tab", "table", "tabnav", "tag",
            "tile", "toggle", "tooltip", "transcription", "translate", "upload", "user"
        ]
        
        # Headers pour l'API GitHub
        self.headers = {
            'Accept': 'application/vnd.github.v3+json',
            'User-Agent': 'DSFR-Documentation-Updater/1.0'
        }
    
    def get_file_content(self, path: str) -> Optional[str]:
        """Récupère le contenu d'un fichier depuis GitHub"""
        url = f"{self.github_api}/repos/{self.repo}/contents/{path}"
        
        try:
            req = urllib.request.Request(url, headers=self.headers)
            with urllib.request.urlopen(req) as response:
                data = json.loads(response.read().decode('utf-8'))
                
                if data.get('encoding') == 'base64':
                    content = base64.b64decode(data['content']).decode('utf-8')
                    return content
                
            return None
            
        except Exception as e:
            print(f"    [ERREUR] Erreur récupération {path}: {e}")
            return None
    
    def get_component_files(self, component: str) -> Dict:
        """Récupère tous les fichiers d'un composant"""
        base_path = f"{self.components_path}/{component}"
        
        # Récupérer la liste des fichiers du composant
        url = f"{self.github_api}/repos/{self.repo}/contents/{base_path}"
        
        component_data = {
            "name": component,
            "files": {},
            "documentation": "",
            "scss": "",
            "js": "",
            "examples": []
        }
        
        try:
            req = urllib.request.Request(url, headers=self.headers)
            with urllib.request.urlopen(req) as response:
                files = json.loads(response.read().decode('utf-8'))
                
                for file in files:
                    if file['type'] == 'file':
                        filename = file['name']
                        
                        # Récupérer les fichiers importants
                        if filename == 'README.md':
                            content = self.get_file_content(f"{base_path}/{filename}")
                            if content:
                                component_data['documentation'] = content
                                
                        elif filename.endswith('.scss'):
                            content = self.get_file_content(f"{base_path}/{filename}")
                            if content:
                                component_data['scss'] += content + "\n"
                                
                        elif filename.endswith('.js'):
                            content = self.get_file_content(f"{base_path}/{filename}")
                            if content:
                                component_data['js'] += content + "\n"
                                
                        elif filename == 'example.html' or filename.endswith('-example.html'):
                            content = self.get_file_content(f"{base_path}/{filename}")
                            if content:
                                component_data['examples'].append({
                                    "filename": filename,
                                    "content": content
                                })
                
            # Delay pour éviter le rate limiting
            time.sleep(0.5)
                
        except Exception as e:
            print(f"    [ERREUR] Erreur pour {component}: {e}")
        
        return component_data
    
    def extract_component_info(self, component_data: Dict) -> Dict:
        """Extrait les informations structurées d'un composant"""
        info = {
            "name": component_data['name'],
            "className": f"fr-{component_data['name']}",
            "description": "",
            "properties": [],
            "variants": [],
            "examples": [],
            "accessibility": {},
            "scss_variables": [],
            "js_api": []
        }
        
        # Extraire depuis le README
        if component_data['documentation']:
            doc = component_data['documentation']
            
            # Description (première ligne non vide après le titre)
            lines = doc.split('\n')
            for line in lines:
                if line and not line.startswith('#') and line.strip():
                    info['description'] = line.strip()
                    break
            
            # Variantes (chercher les modifiers)
            variant_matches = re.findall(r'--([a-z\-]+)', doc)
            info['variants'] = list(set(variant_matches))
            
            # Accessibilité
            if 'aria-' in doc.lower():
                info['accessibility']['aria'] = True
            if 'role=' in doc.lower():
                info['accessibility']['roles'] = True
            if 'rgaa' in doc.lower() or 'accessibilité' in doc.lower():
                info['accessibility']['rgaa_compliant'] = True
        
        # Extraire depuis le SCSS
        if component_data['scss']:
            scss = component_data['scss']
            
            # Variables SCSS
            var_matches = re.findall(r'\$([a-z\-]+):', scss)
            info['scss_variables'] = list(set(var_matches))[:10]  # Limiter à 10
            
            # Classes CSS
            class_matches = re.findall(r'\.fr-[a-z\-]+', scss)
            info['css_classes'] = list(set(class_matches))[:10]
        
        # Extraire depuis le JS
        if component_data['js']:
            js = component_data['js']
            
            # API JavaScript
            method_matches = re.findall(r'(?:this\.|prototype\.)([a-zA-Z]+)\s*=\s*function', js)
            info['js_api'] = list(set(method_matches))[:10]
            
            # Events
            event_matches = re.findall(r'dispatch\([\'"]([a-z\-]+)', js)
            info['js_events'] = list(set(event_matches))
        
        # Ajouter les exemples
        for example in component_data['examples']:
            info['examples'].append({
                "title": example['filename'].replace('.html', '').replace('-', ' ').title(),
                "code": example['content'][:500]  # Limiter la taille
            })
        
        return info
    
    def get_version(self) -> str:
        """Récupère la version depuis package.json"""
        content = self.get_file_content("package.json")
        
        if content:
            try:
                package = json.loads(content)
                return package.get('version', 'unknown')
            except:
                pass
        
        return "unknown"
    
    def generate_markdown(self, components_data: List[Dict], version: str) -> str:
        """Génère le fichier Markdown complet"""
        
        md = f"""# 🇫🇷 DSFR v{version} - Documentation GitHub

*Généré automatiquement depuis : https://github.com/GouvernementFR/dsfr*
*Date : {datetime.now().strftime('%d/%m/%Y %H:%M')}*

## [STATS] Résumé

- **Version** : {version}
- **Composants** : {len(components_data)}
- **Source** : GitHub officiel
- **Chemin** : src/dsfr/component/

---

## 📦 Installation

```bash
npm install @gouvfr/dsfr@{version}
```

## 🎨 Composants DSFR

"""
        
        # Organiser par catégories
        categories = {
            "Navigation": ["header", "footer", "navigation", "breadcrumb", "sidemenu", "skiplink"],
            "Formulaires": ["input", "select", "checkbox", "radio", "toggle", "search", "upload", "range", "password", "form"],
            "Boutons": ["button", "link", "download"],
            "Affichage": ["accordion", "alert", "badge", "callout", "card", "modal", "table", "tab", "tag", "tile", "tooltip"],
            "Contenu": ["content", "highlight", "quote", "summary", "transcription", "notice"],
            "Autres": []
        }
        
        # Classer les composants
        categorized = {cat: [] for cat in categories}
        
        for comp in components_data:
            placed = False
            for cat, comp_names in categories.items():
                if comp['name'] in comp_names:
                    categorized[cat].append(comp)
                    placed = True
                    break
            if not placed:
                categorized["Autres"].append(comp)
        
        # Générer le markdown par catégorie
        for category, components in categorized.items():
            if components:
                md += f"\n### [DOSSIER] {category}\n\n"
                
                for comp in sorted(components, key=lambda x: x['name']):
                    md += f"""
#### 🔹 {comp['name'].upper()}

**Classe CSS** : `{comp['className']}`
"""
                    
                    if comp.get('description'):
                        md += f"**Description** : {comp['description']}\n"
                    
                    if comp.get('variants'):
                        md += f"\n**Variantes** :\n"
                        for variant in comp['variants'][:5]:
                            md += f"- `{comp['className']}--{variant}`\n"
                    
                    if comp.get('scss_variables'):
                        md += f"\n**Variables SCSS** :\n"
                        for var in comp['scss_variables'][:5]:
                            md += f"- `${var}`\n"
                    
                    if comp.get('js_api'):
                        md += f"\n**API JavaScript** :\n"
                        for method in comp['js_api'][:5]:
                            md += f"- `.{method}()`\n"
                    
                    if comp.get('examples'):
                        md += f"\n**Exemple** :\n"
                        example = comp['examples'][0]
                        md += f"```html\n{example['code'][:300]}...\n```\n"
                    
                    if comp.get('accessibility'):
                        acc = comp['accessibility']
                        if acc:
                            md += "\n**Accessibilité** :\n"
                            if acc.get('aria'):
                                md += "- [OK] Support ARIA\n"
                            if acc.get('roles'):
                                md += "- [OK] Rôles WAI-ARIA\n"
                            if acc.get('rgaa_compliant'):
                                md += "- [OK] Conforme RGAA\n"
                    
                    # Lien GitHub
                    md += f"\n📄 [Voir sur GitHub](https://github.com/{self.repo}/tree/main/src/dsfr/component/{comp['name']})\n"
                    
                    md += "\n---\n"
        
        # Ajouter les liens utiles
        md += f"""

## 🔗 Liens utiles

- **GitHub** : https://github.com/{self.repo}
- **Site officiel** : https://www.systeme-de-design.gouv.fr/
- **NPM** : https://www.npmjs.com/package/@gouvfr/dsfr
- **Storybook** : https://www.systeme-de-design.gouv.fr/storybook/

## [DOC] Notes

Cette documentation a été générée automatiquement depuis le code source GitHub.
Pour la documentation complète et les exemples interactifs, consultez le site officiel.
"""
        
        return md
    
    def update_from_github(self):
        """Lance la mise à jour depuis GitHub"""
        print("[START] Mise à jour depuis GitHub\n")
        print("=" * 50)
        
        # 1. Récupérer la version
        print("📦 Récupération de la version...")
        version = self.get_version()
        print(f"   Version : {version}")
        
        # 2. Extraire les composants
        print(f"\n📚 Extraction de {len(self.components)} composants...")
        print("   (cela peut prendre quelques minutes)\n")
        
        all_components_data = []
        
        for i, component in enumerate(self.components):
            print(f"  [{i+1}/{len(self.components)}] {component}...", end="")
            
            # Récupérer les fichiers
            component_files = self.get_component_files(component)
            
            # Extraire les informations
            component_info = self.extract_component_info(component_files)
            
            all_components_data.append(component_info)
            
            if component_files['documentation']:
                print(" [OK]")
            else:
                print(" [ATTENTION]  (pas de README)")
        
        # 3. Générer le Markdown
        print("\n[DOC] Génération du document...")
        markdown = self.generate_markdown(all_components_data, version)
        
        # 4. Sauvegarder
        timestamp = datetime.now().strftime('%Y%m%d_%H%M')
        filename = f"docs/DSFR_v{version}_GITHUB_{timestamp}.md"
        
        os.makedirs("docs", exist_ok=True)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(markdown)
        
        print(f"\n[OK] Documentation générée : {filename}")
        print(f"   Taille : {len(markdown) / 1024:.1f} KB")
        print(f"   Composants : {len(all_components_data)}")
        
        # Sauvegarder aussi en JSON
        json_filename = f"docs/DSFR_v{version}_GITHUB_{timestamp}.json"
        with open(json_filename, 'w', encoding='utf-8') as f:
            json.dump({
                "version": version,
                "updated_at": datetime.now().isoformat(),
                "source": f"https://github.com/{self.repo}",
                "components": all_components_data
            }, f, indent=2, ensure_ascii=False)
        
        print(f"[OK] Données JSON : {json_filename}")
        
        return filename

def main():
    updater = DSFRGitHubUpdater()
    
    print("╔════════════════════════════════════════════╗")
    print("║   DSFR - Extraction depuis GitHub          ║")
    print("╚════════════════════════════════════════════╝\n")
    
    try:
        filename = updater.update_from_github()
        
        print("\n" + "=" * 50)
        print("[SUCCES] Extraction terminée avec succès !")
        print(f"📄 Documentation : {filename}")
        
    except Exception as e:
        print(f"\n[ERREUR] Erreur : {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())