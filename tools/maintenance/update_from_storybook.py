#!/usr/bin/env python3
"""
Script de mise à jour de la documentation DSFR depuis Storybook
Extrait et fusionne les données depuis :
1. Storybook : https://www.systeme-de-design.gouv.fr/v1.14/storybook/
2. NPM : @gouvfr/dsfr
"""

import json
import os
import re
import subprocess
from datetime import datetime
from typing import Dict, List, Optional
import requests

class DSFRDocUpdater:
    def __init__(self):
        self.storybook_base = "https://www.systeme-de-design.gouv.fr/v1.14/storybook/"
        self.components_urls = {
            # Navigation
            "header": "?path=/docs/composants-en-tête-header--docs",
            "footer": "?path=/docs/composants-pied-de-page-footer--docs",
            "navigation": "?path=/docs/composants-navigation-navigation--docs",
            "breadcrumb": "?path=/docs/composants-fil-d-ariane-breadcrumb--docs",
            "sidemenu": "?path=/docs/composants-menu-latéral-sidemenu--docs",
            "skiplinks": "?path=/docs/composants-liens-d-évitement-skiplinks--docs",
            
            # Boutons et liens
            "button": "?path=/docs/composants-bouton-button--docs",
            "button-group": "?path=/docs/composants-groupe-de-boutons-buttons-group--docs",
            "link": "?path=/docs/composants-lien-link--docs",
            "back-to-top": "?path=/docs/composants-retour-en-haut-de-page-back-to-top--docs",
            
            # Formulaires
            "input": "?path=/docs/composants-champ-de-saisie-input--docs",
            "select": "?path=/docs/composants-liste-déroulante-select--docs",
            "checkbox": "?path=/docs/composants-case-à-cocher-checkbox--docs",
            "radio": "?path=/docs/composants-boutons-radio-radio--docs",
            "toggle": "?path=/docs/composants-interrupteur-toggle--docs",
            "search": "?path=/docs/composants-barre-de-recherche-search--docs",
            "upload": "?path=/docs/composants-ajout-de-fichier-upload--docs",
            "range": "?path=/docs/composants-curseur-range--docs",
            
            # Affichage
            "accordion": "?path=/docs/composants-accordéon-accordion--docs",
            "alert": "?path=/docs/composants-alerte-alert--docs",
            "badge": "?path=/docs/composants-badge-badge--docs",
            "callout": "?path=/docs/composants-mise-en-avant-callout--docs",
            "card": "?path=/docs/composants-carte-card--docs",
            "content": "?path=/docs/composants-gestionnaire-de-contenu-content--docs",
            "highlight": "?path=/docs/composants-mise-en-exergue-highlight--docs",
            "modal": "?path=/docs/composants-modale-modal--docs",
            "notice": "?path=/docs/composants-bandeau-d-information-importante-notice--docs",
            "quote": "?path=/docs/composants-citation-quote--docs",
            "stepper": "?path=/docs/composants-indicateur-d-étapes-stepper--docs",
            "summary": "?path=/docs/composants-sommaire-summary--docs",
            "table": "?path=/docs/composants-tableau-table--docs",
            "tabs": "?path=/docs/composants-onglets-tabs--docs",
            "tag": "?path=/docs/composants-tag-tag--docs",
            "tile": "?path=/docs/composants-tuile-tile--docs",
            "transcription": "?path=/docs/composants-transcription-transcription--docs",
            
            # Médias
            "video": "?path=/docs/composants-lecteur-vidéo-video--docs",
            
            # Autres
            "consent": "?path=/docs/composants-gestionnaire-de-consentement-consent--docs",
            "display": "?path=/docs/composants-paramètres-d-affichage-display--docs",
            "follow": "?path=/docs/composants-lettre-d-information-et-réseaux-sociaux-follow--docs",
            "pagination": "?path=/docs/composants-pagination-pagination--docs",
            "password": "?path=/docs/composants-mot-de-passe-password--docs",
            "share": "?path=/docs/composants-partage-share--docs",
            "translate": "?path=/docs/composants-sélecteur-de-langue-translate--docs",
            "version": "?path=/docs/composants-indicateur-de-version-version--docs"
        }
        
        self.current_version = "1.14"
        
    def check_npm_version(self) -> str:
        """Vérifie la dernière version via API NPM"""
        try:
            import requests
            response = requests.get("https://registry.npmjs.org/@gouvfr/dsfr/latest", timeout=10)
            if response.status_code == 200:
                return response.json()["version"]
            else:
                raise Exception("API NPM indisponible")
        except:
            return self.current_version
    
    def extract_from_storybook(self, component: str, url: str) -> Optional[Dict]:
        """Extrait les données d'un composant depuis Storybook via proxy"""
        full_url = self.storybook_base + url
        
        # Utiliser r.jina.ai comme proxy pour éviter les erreurs 403
        proxy_url = f"https://r.jina.ai/{full_url}"
        
        print(f"  Extraction de {component}...")
        
        try:
            response = requests.get(proxy_url, headers={
                'User-Agent': 'Mozilla/5.0 (compatible; DSFRUpdater/1.0)'
            })
            
            if response.status_code == 200:
                content = response.text
                
                # Extraire les informations clés
                data = {
                    "name": component,
                    "url": full_url,
                    "content": self.parse_storybook_content(content),
                    "extracted_at": datetime.now().isoformat()
                }
                
                return data
            else:
                print(f"    [ATTENTION]  Erreur {response.status_code} pour {component}")
                return None
                
        except Exception as e:
            print(f"    [ERREUR] Erreur pour {component}: {e}")
            return None
    
    def parse_storybook_content(self, html: str) -> Dict:
        """Parse le contenu HTML de Storybook"""
        # Extraction simplifiée - à améliorer selon la structure réelle
        content = {
            "description": "",
            "props": [],
            "examples": [],
            "accessibility": {}
        }
        
        # Recherche de patterns communs
        if "Description" in html:
            desc_match = re.search(r'Description[^<]*<[^>]*>([^<]+)', html)
            if desc_match:
                content["description"] = desc_match.group(1).strip()
        
        # Extraction des propriétés
        prop_matches = re.findall(r'prop["\']?\s*:\s*["\']([^"\']+)', html)
        content["props"] = list(set(prop_matches))
        
        # Extraction des exemples de code
        code_matches = re.findall(r'```[^`]*```', html)
        content["examples"] = code_matches[:3]  # Limiter à 3 exemples
        
        # Info accessibilité
        if "aria-" in html.lower():
            content["accessibility"]["hasAria"] = True
        if "rgaa" in html.lower():
            content["accessibility"]["rgaaCompliant"] = True
        
        return content
    
    def get_npm_data(self) -> Dict:
        """Récupère les données depuis le package NPM installé"""
        print("\n📦 Extraction depuis NPM...")
        
        npm_data = {}
        
        # Récupérer les informations du package via API
        try:
            # Extraire les métadonnées depuis l'API NPM
            npm_data["version"] = self.check_npm_version()
            npm_data["installed"] = True
            
            print(f"  [OK] Version NPM : {npm_data['version']}")
            
        except:
            npm_data["installed"] = False
            npm_data["version"] = self.current_version
            print("  [ATTENTION]  Impossible de récupérer les infos NPM")
        
        return npm_data
    
    def merge_data(self, storybook_data: List[Dict], npm_data: Dict) -> Dict:
        """Fusionne les données Storybook et NPM"""
        print("\n[MAJ] Fusion des données...")
        
        merged = {
            "version": npm_data.get("version", self.current_version),
            "updated_at": datetime.now().isoformat(),
            "sources": {
                "storybook": f"{self.storybook_base}",
                "npm": "@gouvfr/dsfr"
            },
            "components": {}
        }
        
        # Ajouter les données Storybook
        for component in storybook_data:
            if component:
                merged["components"][component["name"]] = component
        
        # Enrichir avec les données NPM si disponibles
        if npm_data.get("installed"):
            merged["npm_metadata"] = npm_data
        
        print(f"  [OK] {len(merged['components'])} composants fusionnés")
        
        return merged
    
    def generate_markdown(self, data: Dict) -> str:
        """Génère le fichier Markdown à partir des données"""
        print("\n[DOC] Génération du Markdown...")
        
        md = f"""# 🇫🇷 DSFR v{data['version']} - Documentation Complète

*Mise à jour : {datetime.now().strftime('%d/%m/%Y %H:%M')}*

## [STATS] Résumé

- **Version** : {data['version']}
- **Composants** : {len(data['components'])}
- **Sources** : Storybook + NPM
- **Dernière extraction** : {data['updated_at']}

## 📦 Sources

1. **Storybook** : {data['sources']['storybook']}
2. **NPM** : {data['sources']['npm']}

---

## 🎨 Composants DSFR

"""
        
        # Organiser par catégories
        categories = {
            "Navigation": ["header", "footer", "navigation", "breadcrumb", "sidemenu", "skiplinks"],
            "Boutons et liens": ["button", "button-group", "link", "back-to-top"],
            "Formulaires": ["input", "select", "checkbox", "radio", "toggle", "search", "upload", "range"],
            "Affichage": ["accordion", "alert", "badge", "callout", "card", "modal", "table", "tabs", "tag"],
            "Autres": []
        }
        
        # Classer les composants
        categorized = {cat: [] for cat in categories}
        for comp_name, comp_data in data['components'].items():
            placed = False
            for cat, comps in categories.items():
                if comp_name in comps:
                    categorized[cat].append(comp_data)
                    placed = True
                    break
            if not placed:
                categorized["Autres"].append(comp_data)
        
        # Générer le markdown par catégorie
        for category, components in categorized.items():
            if components:
                md += f"\n### {category}\n\n"
                
                for comp in components:
                    md += f"""
#### 🔹 {comp['name'].upper()}

**URL Storybook** : {comp['url']}

"""
                    if comp['content'].get('description'):
                        md += f"**Description** : {comp['content']['description']}\n\n"
                    
                    if comp['content'].get('props'):
                        md += "**Propriétés** :\n"
                        for prop in comp['content']['props']:
                            md += f"- `{prop}`\n"
                        md += "\n"
                    
                    if comp['content'].get('examples'):
                        md += "**Exemples** :\n"
                        for i, example in enumerate(comp['content']['examples'][:2]):
                            md += f"\nExemple {i+1}:\n{example}\n"
                        md += "\n"
                    
                    if comp['content'].get('accessibility'):
                        acc = comp['content']['accessibility']
                        if acc:
                            md += "**Accessibilité** :\n"
                            if acc.get('hasAria'):
                                md += "- [OK] Support ARIA\n"
                            if acc.get('rgaaCompliant'):
                                md += "- [OK] Conforme RGAA\n"
                            md += "\n"
                    
                    md += "---\n"
        
        return md
    
    def update_documentation(self):
        """Lance la mise à jour complète de la documentation"""
        print("[START] Mise à jour de la documentation DSFR\n")
        print("=" * 50)
        
        # 1. Vérifier la version NPM
        npm_version = self.check_npm_version()
        print(f"📦 Version NPM actuelle : {npm_version}")
        
        # 2. Extraire depuis Storybook
        print(f"\n🌐 Extraction depuis Storybook ({len(self.components_urls)} composants)...")
        
        storybook_data = []
        for comp_name, comp_url in self.components_urls.items():
            data = self.extract_from_storybook(comp_name, comp_url)
            if data:
                storybook_data.append(data)
        
        print(f"\n[OK] {len(storybook_data)} composants extraits depuis Storybook")
        
        # 3. Récupérer les données NPM
        npm_data = self.get_npm_data()
        
        # 4. Fusionner les données
        merged_data = self.merge_data(storybook_data, npm_data)
        
        # 5. Générer le Markdown
        markdown_content = self.generate_markdown(merged_data)
        
        # 6. Sauvegarder
        timestamp = datetime.now().strftime('%Y%m%d_%H%M')
        filename = f"docs/DSFR_v{npm_version}_UPDATED_{timestamp}.md"
        
        os.makedirs("docs", exist_ok=True)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        print(f"\n[OK] Documentation mise à jour : {filename}")
        print(f"   Taille : {len(markdown_content) / 1024:.1f} KB")
        print(f"   Composants : {len(merged_data['components'])}")
        
        # 7. Sauvegarder aussi en JSON pour traitement ultérieur
        json_filename = f"docs/DSFR_v{npm_version}_DATA_{timestamp}.json"
        with open(json_filename, 'w', encoding='utf-8') as f:
            json.dump(merged_data, f, indent=2, ensure_ascii=False)
        
        print(f"[OK] Données JSON sauvegardées : {json_filename}")
        
        return filename

def main():
    updater = DSFRDocUpdater()
    
    print("╔════════════════════════════════════════════╗")
    print("║   Mise à jour Documentation DSFR          ║")
    print("╚════════════════════════════════════════════╝\n")
    
    try:
        filename = updater.update_documentation()
        
        print("\n" + "=" * 50)
        print("[SUCCES] Mise à jour terminée avec succès !")
        print(f"📄 Fichier généré : {filename}")
        print("\nPour utiliser la nouvelle documentation :")
        print(f"  ./dsfr-agent")
        
    except Exception as e:
        print(f"\n[ERREUR] Erreur lors de la mise à jour : {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())