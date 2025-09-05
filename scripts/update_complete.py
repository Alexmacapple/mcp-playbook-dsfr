#!/usr/bin/env python3
"""
Script de mise à jour COMPLÈTE de la documentation DSFR
Combine toutes les sources :
1. GitHub (code source)
2. Storybook (documentation interactive)
3. NPM (package officiel)
"""

import json
import os
import re
import subprocess
import shutil
from datetime import datetime
from typing import Dict, List, Optional
import urllib.request
import urllib.error
import time

class DSFRCompleteUpdater:
    def __init__(self):
        self.temp_dir = "/tmp/dsfr_update"
        self.repo_url = "https://github.com/GouvernementFR/dsfr.git"
        self.storybook_base = "https://www.systeme-de-design.gouv.fr/v1.14/storybook/"
        self.components_map = {
            # Map des composants avec leurs URLs Storybook
            "accordion": "?path=/docs/composants-accordéon-accordion--docs",
            "alert": "?path=/docs/composants-alerte-alert--docs",
            "badge": "?path=/docs/composants-badge-badge--docs",
            "breadcrumb": "?path=/docs/composants-fil-d-ariane-breadcrumb--docs",
            "button": "?path=/docs/composants-bouton-button--docs",
            "callout": "?path=/docs/composants-mise-en-avant-callout--docs",
            "card": "?path=/docs/composants-carte-card--docs",
            "checkbox": "?path=/docs/composants-case-à-cocher-checkbox--docs",
            "consent": "?path=/docs/composants-gestionnaire-de-consentement-consent--docs",
            "content": "?path=/docs/composants-gestionnaire-de-contenu-content--docs",
            "display": "?path=/docs/composants-paramètres-d-affichage-display--docs",
            "download": "?path=/docs/composants-téléchargement-de-fichier-download--docs",
            "follow": "?path=/docs/composants-lettre-d-information-et-réseaux-sociaux-follow--docs",
            "footer": "?path=/docs/composants-pied-de-page-footer--docs",
            "form": "?path=/docs/composants-formulaire-form--docs",
            "header": "?path=/docs/composants-en-tête-header--docs",
            "highlight": "?path=/docs/composants-mise-en-exergue-highlight--docs",
            "input": "?path=/docs/composants-champ-de-saisie-input--docs",
            "link": "?path=/docs/composants-lien-link--docs",
            "modal": "?path=/docs/composants-modale-modal--docs",
            "navigation": "?path=/docs/composants-navigation-navigation--docs",
            "notice": "?path=/docs/composants-bandeau-d-information-importante-notice--docs",
            "pagination": "?path=/docs/composants-pagination-pagination--docs",
            "password": "?path=/docs/composants-mot-de-passe-password--docs",
            "quote": "?path=/docs/composants-citation-quote--docs",
            "radio": "?path=/docs/composants-boutons-radio-radio--docs",
            "range": "?path=/docs/composants-curseur-range--docs",
            "search": "?path=/docs/composants-barre-de-recherche-search--docs",
            "select": "?path=/docs/composants-liste-déroulante-select--docs",
            "share": "?path=/docs/composants-partage-share--docs",
            "sidemenu": "?path=/docs/composants-menu-latéral-sidemenu--docs",
            "skiplink": "?path=/docs/composants-liens-d-évitement-skiplinks--docs",
            "stepper": "?path=/docs/composants-indicateur-d-étapes-stepper--docs",
            "summary": "?path=/docs/composants-sommaire-summary--docs",
            "table": "?path=/docs/composants-tableau-table--docs",
            "tab": "?path=/docs/composants-onglets-tabs--docs",
            "tag": "?path=/docs/composants-tag-tag--docs",
            "tile": "?path=/docs/composants-tuile-tile--docs",
            "toggle": "?path=/docs/composants-interrupteur-toggle--docs",
            "tooltip": "?path=/docs/composants-infobulle-tooltip--docs",
            "transcription": "?path=/docs/composants-transcription-transcription--docs",
            "translate": "?path=/docs/composants-sélecteur-de-langue-translate--docs",
            "upload": "?path=/docs/composants-ajout-de-fichier-upload--docs",
        }
        
    def clone_repository(self) -> bool:
        """Clone le dépôt GitHub localement"""
        print("📦 Clonage du dépôt GitHub...")
        
        # Nettoyer le dossier temporaire
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)
        os.makedirs(self.temp_dir)
        
        try:
            # Cloner le dépôt
            result = subprocess.run(
                ["git", "clone", "--depth", "1", self.repo_url, self.temp_dir],
                capture_output=True, text=True, check=True
            )
            print("   ✅ Dépôt cloné avec succès")
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"   ❌ Erreur lors du clonage : {e}")
            return False
    
    def extract_from_github_local(self) -> Dict:
        """Extrait les données depuis le dépôt cloné"""
        print("\n📂 Extraction depuis le dépôt local...")
        
        components_data = {}
        components_dir = os.path.join(self.temp_dir, "src/dsfr/component")
        
        if not os.path.exists(components_dir):
            print("   ❌ Dossier des composants non trouvé")
            return components_data
        
        # Parcourir chaque composant
        for component_name in os.listdir(components_dir):
            component_path = os.path.join(components_dir, component_name)
            
            if os.path.isdir(component_path):
                component_data = {
                    "name": component_name,
                    "files": {},
                    "scss": "",
                    "js": "",
                    "examples": [],
                    "readme": "",
                    "template": ""
                }
                
                # Parcourir les fichiers du composant
                for root, dirs, files in os.walk(component_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        
                        try:
                            if file == "README.md":
                                with open(file_path, 'r', encoding='utf-8') as f:
                                    component_data["readme"] = f.read()
                                    
                            elif file.endswith('.scss'):
                                with open(file_path, 'r', encoding='utf-8') as f:
                                    component_data["scss"] += f.read() + "\n"
                                    
                            elif file.endswith('.js'):
                                with open(file_path, 'r', encoding='utf-8') as f:
                                    component_data["js"] += f.read() + "\n"
                                    
                            elif file.endswith('.ejs') or file.endswith('.html'):
                                with open(file_path, 'r', encoding='utf-8') as f:
                                    content = f.read()
                                    component_data["examples"].append({
                                        "filename": file,
                                        "content": content
                                    })
                                    if file == "template.ejs":
                                        component_data["template"] = content
                                        
                        except Exception as e:
                            print(f"      ⚠️  Erreur lecture {file}: {e}")
                
                components_data[component_name] = component_data
                print(f"   ✅ {component_name}")
        
        return components_data
    
    def extract_from_storybook(self, component_name: str) -> Dict:
        """Extrait la documentation depuis Storybook"""
        if component_name not in self.components_map:
            return {}
        
        url = self.storybook_base + self.components_map[component_name]
        
        # Utiliser r.jina.ai comme proxy
        proxy_url = f"https://r.jina.ai/{url}"
        
        try:
            req = urllib.request.Request(proxy_url, headers={
                'User-Agent': 'Mozilla/5.0 DSFR Updater'
            })
            
            with urllib.request.urlopen(req) as response:
                content = response.read().decode('utf-8')
                
                # Extraire les informations
                data = {
                    "storybook_url": url,
                    "interactive_doc": self.parse_storybook_content(content)
                }
                
                return data
                
        except Exception as e:
            print(f"      ⚠️  Pas de doc Storybook pour {component_name}")
            return {}
    
    def parse_storybook_content(self, html: str) -> Dict:
        """Parse le contenu Storybook"""
        doc = {
            "description": "",
            "usage": "",
            "variants": [],
            "props": [],
            "examples": []
        }
        
        # Extraire description
        desc_match = re.search(r'Description[^<]*<[^>]*>([^<]+)', html)
        if desc_match:
            doc["description"] = desc_match.group(1).strip()
        
        # Extraire les variantes
        variant_matches = re.findall(r'variant["\']?\s*:\s*["\']([^"\']+)', html)
        doc["variants"] = list(set(variant_matches))
        
        # Extraire les propriétés
        prop_matches = re.findall(r'prop["\']?\s*:\s*["\']([^"\']+)', html)
        doc["props"] = list(set(prop_matches))
        
        return doc
    
    def merge_all_data(self, github_data: Dict, npm_version: str) -> Dict:
        """Fusionne toutes les sources de données"""
        print("\n🔄 Fusion des données...")
        
        merged = {
            "version": npm_version,
            "updated_at": datetime.now().isoformat(),
            "components": {}
        }
        
        # Pour chaque composant GitHub
        for comp_name, comp_github in github_data.items():
            print(f"   Fusion {comp_name}...", end="")
            
            # Données de base depuis GitHub
            component = {
                "name": comp_name,
                "className": f"fr-{comp_name}",
                "github": comp_github,
                "storybook": {},
                "complete_code": {
                    "scss": comp_github.get("scss", ""),
                    "js": comp_github.get("js", ""),
                    "template": comp_github.get("template", ""),
                    "examples": comp_github.get("examples", [])
                }
            }
            
            # Ajouter les données Storybook si disponibles
            storybook_data = self.extract_from_storybook(comp_name)
            if storybook_data:
                component["storybook"] = storybook_data
                print(" ✅")
            else:
                print(" ⚠️")
            
            # Délai pour éviter le rate limiting
            time.sleep(0.3)
            
            merged["components"][comp_name] = component
        
        return merged
    
    def generate_ultra_complete_markdown(self, data: Dict) -> str:
        """Génère la documentation ULTRA COMPLÈTE"""
        
        md = f"""# 🇫🇷 DSFR v{data['version']} - DOCUMENTATION ULTRA COMPLÈTE

*Généré le {datetime.now().strftime('%d/%m/%Y %H:%M')}*

## 📊 SOURCES COMBINÉES

1. **GitHub** : Code source complet (SCSS, JS, Templates)
2. **Storybook** : Documentation interactive
3. **NPM** : Package officiel @gouvfr/dsfr

## 📦 INSTALLATION

```bash
# NPM
npm install @gouvfr/dsfr@{data['version']}

# CDN
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@gouvfr/dsfr@{data['version']}/dist/dsfr.min.css">
<script src="https://cdn.jsdelivr.net/npm/@gouvfr/dsfr@{data['version']}/dist/dsfr.module.min.js"></script>
```

---

# 🎨 COMPOSANTS COMPLETS ({len(data['components'])})

"""
        
        # Organiser par catégories
        categories = {
            "🧭 Navigation": ["header", "footer", "navigation", "breadcrumb", "sidemenu", "skiplink"],
            "📝 Formulaires": ["input", "select", "checkbox", "radio", "toggle", "search", "upload", "range", "password", "form"],
            "🔘 Boutons et Actions": ["button", "link", "download"],
            "📊 Affichage": ["accordion", "alert", "badge", "callout", "card", "modal", "table", "tab", "tag", "tile", "tooltip"],
            "📄 Contenu": ["content", "highlight", "quote", "summary", "transcription", "notice"],
            "🔧 Utilitaires": ["consent", "display", "follow", "pagination", "share", "stepper", "translate"]
        }
        
        # Classer les composants
        for category, comp_names in categories.items():
            md += f"\n## {category}\n\n"
            
            for comp_name in comp_names:
                if comp_name in data['components']:
                    comp = data['components'][comp_name]
                    
                    md += f"""
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🔹 {comp_name.upper()}

### 📋 INFORMATIONS GÉNÉRALES

- **Classe CSS** : `{comp['className']}`
- **Dossier GitHub** : `/src/dsfr/component/{comp_name}/`
"""
                    
                    # Documentation Storybook
                    if comp.get('storybook') and comp['storybook'].get('interactive_doc'):
                        doc = comp['storybook']['interactive_doc']
                        if doc.get('description'):
                            md += f"- **Description** : {doc['description']}\n"
                        if doc.get('variants'):
                            md += f"- **Variantes** : {', '.join(doc['variants'])}\n"
                        
                        if comp['storybook'].get('storybook_url'):
                            md += f"\n📖 [Documentation interactive]({comp['storybook']['storybook_url']})\n"
                    
                    # Code SCSS
                    if comp['complete_code']['scss']:
                        scss = comp['complete_code']['scss'][:1000]  # Limiter
                        
                        # Extraire les variables
                        variables = re.findall(r'\$([a-z\-]+):', scss)
                        if variables:
                            md += f"\n### 🎨 VARIABLES SCSS\n\n"
                            for var in list(set(variables))[:10]:
                                md += f"- `${var}`\n"
                        
                        # Extraire les classes
                        classes = re.findall(r'\.fr-[a-z\-]+', scss)
                        if classes:
                            md += f"\n### 📝 CLASSES CSS\n\n"
                            for cls in list(set(classes))[:15]:
                                md += f"- `{cls}`\n"
                    
                    # Code JavaScript
                    if comp['complete_code']['js']:
                        js = comp['complete_code']['js'][:1000]
                        
                        # Extraire l'API
                        methods = re.findall(r'(?:this\.|prototype\.)([a-zA-Z]+)\s*=', js)
                        if methods:
                            md += f"\n### ⚙️ API JAVASCRIPT\n\n"
                            for method in list(set(methods))[:10]:
                                md += f"- `.{method}()`\n"
                        
                        # Extraire les événements
                        events = re.findall(r'dispatch\([\'"]([a-z\-]+)', js)
                        if events:
                            md += f"\n### 📢 ÉVÉNEMENTS\n\n"
                            for event in list(set(events)):
                                md += f"- `{event}`\n"
                    
                    # Template/Exemples
                    if comp['complete_code']['template']:
                        md += f"\n### 📄 TEMPLATE HTML\n\n```html\n"
                        template = comp['complete_code']['template'][:800]
                        md += template
                        if len(comp['complete_code']['template']) > 800:
                            md += "\n..."
                        md += "\n```\n"
                    
                    elif comp['complete_code']['examples'] and len(comp['complete_code']['examples']) > 0:
                        example = comp['complete_code']['examples'][0]
                        md += f"\n### 📄 EXEMPLE ({example['filename']})\n\n```html\n"
                        code = example['content'][:800]
                        md += code
                        if len(example['content']) > 800:
                            md += "\n..."
                        md += "\n```\n"
                    
                    # README GitHub
                    if comp['github'].get('readme'):
                        readme = comp['github']['readme'][:500]
                        if readme:
                            md += f"\n### 📚 DOCUMENTATION GITHUB\n\n"
                            md += readme
                            if len(comp['github']['readme']) > 500:
                                md += "\n..."
                            md += "\n"
                    
                    # Liens
                    md += f"\n### 🔗 LIENS\n\n"
                    md += f"- [GitHub](https://github.com/GouvernementFR/dsfr/tree/main/src/dsfr/component/{comp_name})\n"
                    if comp.get('storybook') and comp['storybook'].get('storybook_url'):
                        md += f"- [Storybook]({comp['storybook']['storybook_url']})\n"
                    md += f"- [Site officiel](https://www.systeme-de-design.gouv.fr/elements-d-interface/{comp_name})\n"
                    
                    md += "\n"
        
        # Ajouter les ressources
        md += """
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# 📚 RESSOURCES COMPLÈTES

## 🔗 Liens officiels

- **Site web** : https://www.systeme-de-design.gouv.fr/
- **GitHub** : https://github.com/GouvernementFR/dsfr
- **NPM** : https://www.npmjs.com/package/@gouvfr/dsfr
- **Storybook** : https://www.systeme-de-design.gouv.fr/storybook/
- **Figma** : https://www.figma.com/community/file/1039777231080123654

## 📖 Documentation

- [Guide de démarrage](https://www.systeme-de-design.gouv.fr/utilisation-et-organisation/developpeurs/prise-en-main)
- [Accessibilité RGAA](https://www.systeme-de-design.gouv.fr/utilisation-et-organisation/accessibilite-et-rgaa)
- [Marque État](https://www.systeme-de-design.gouv.fr/utilisation-et-organisation/charte-graphique)

## 🛠️ Outils

- [Générateur de thème](https://www.systeme-de-design.gouv.fr/utilisation-et-organisation/developpeurs/personnalisation)
- [Migration guide](https://github.com/GouvernementFR/dsfr/blob/main/MIGRATION.md)
- [Changelog](https://github.com/GouvernementFR/dsfr/blob/main/CHANGELOG.md)

---

*Documentation ULTRA COMPLÈTE générée automatiquement*
*Combinaison de : GitHub + Storybook + NPM*
"""
        
        return md
    
    def update_complete(self):
        """Lance la mise à jour complète"""
        print("🚀 MISE À JOUR COMPLÈTE DSFR\n")
        print("=" * 50)
        
        # 1. Vérifier la version NPM
        print("\n📦 Vérification version NPM...")
        try:
            result = subprocess.run(
                ["npm", "view", "@gouvfr/dsfr", "version"],
                capture_output=True, text=True, check=True
            )
            npm_version = result.stdout.strip()
            print(f"   Version NPM : {npm_version}")
        except:
            npm_version = "1.14.1"
            print(f"   Version par défaut : {npm_version}")
        
        # 2. Cloner le dépôt
        if not self.clone_repository():
            print("❌ Impossible de cloner le dépôt")
            return None
        
        # 3. Extraire depuis GitHub local
        github_data = self.extract_from_github_local()
        print(f"\n✅ {len(github_data)} composants extraits depuis GitHub")
        
        # 4. Fusionner avec Storybook
        print("\n📖 Ajout de la documentation Storybook...")
        merged_data = self.merge_all_data(github_data, npm_version)
        
        # 5. Générer la documentation ULTRA COMPLÈTE
        print("\n📝 Génération de la documentation ULTRA COMPLÈTE...")
        markdown = self.generate_ultra_complete_markdown(merged_data)
        
        # 6. Sauvegarder
        timestamp = datetime.now().strftime('%Y%m%d_%H%M')
        filename = f"docs/DSFR_v{npm_version}_ULTRA_COMPLETE_{timestamp}.md"
        
        os.makedirs("docs", exist_ok=True)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(markdown)
        
        print(f"\n✅ Documentation sauvegardée : {filename}")
        print(f"   Taille : {len(markdown) / 1024:.1f} KB")
        print(f"   Composants : {len(merged_data['components'])}")
        
        # Sauvegarder aussi en JSON
        json_filename = f"docs/DSFR_v{npm_version}_COMPLETE_DATA_{timestamp}.json"
        with open(json_filename, 'w', encoding='utf-8') as f:
            # Nettoyer les données pour JSON (limiter la taille)
            json_data = {
                "version": merged_data["version"],
                "updated_at": merged_data["updated_at"],
                "components": {}
            }
            
            for name, comp in merged_data["components"].items():
                json_data["components"][name] = {
                    "name": name,
                    "className": comp["className"],
                    "has_scss": bool(comp["complete_code"]["scss"]),
                    "has_js": bool(comp["complete_code"]["js"]),
                    "has_template": bool(comp["complete_code"]["template"]),
                    "examples_count": len(comp["complete_code"]["examples"]),
                    "storybook_url": comp["storybook"].get("storybook_url", "")
                }
            
            json.dump(json_data, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Métadonnées JSON : {json_filename}")
        
        # 7. Nettoyer
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)
            print("✅ Fichiers temporaires nettoyés")
        
        return filename

def main():
    updater = DSFRCompleteUpdater()
    
    print("╔════════════════════════════════════════════════════╗")
    print("║   MISE À JOUR ULTRA COMPLÈTE DSFR                  ║")
    print("║   GitHub + Storybook + NPM                         ║")
    print("╚════════════════════════════════════════════════════╝\n")
    
    try:
        filename = updater.update_complete()
        
        if filename:
            print("\n" + "=" * 50)
            print("🎉 MISE À JOUR TERMINÉE AVEC SUCCÈS !")
            print(f"📄 Documentation : {filename}")
            print("\n✨ La documentation contient :")
            print("   - Code source complet (SCSS, JS)")
            print("   - Templates HTML")
            print("   - Documentation Storybook")
            print("   - Exemples d'utilisation")
            print("   - Variables et API")
        else:
            print("\n❌ Échec de la mise à jour")
            
    except Exception as e:
        print(f"\n❌ Erreur : {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())