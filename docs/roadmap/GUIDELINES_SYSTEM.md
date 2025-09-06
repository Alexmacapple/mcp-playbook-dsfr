# Système de Guidelines DSFR Personnalisées

## Contexte

### Situation actuelle
- **131 fichiers HTML statiques** dans `/gabarits/`
- Générés le 05/09/2025, figés depuis
- Structure : commentaires DSFR + HTML brut
- Pas de système de règles/guidelines intégré

### Problèmes identifiés
- Surcapitalisation des titres (ex: "Titre De La Carte")
- Icônes potentielles dans les titres
- Pas de contrôle centralisé du formatage
- Templates statiques difficiles à faire évoluer

## Architecture actuelle

```
mcp-playbook-dsfr/
├── gabarits/              # 131 templates HTML statiques
│   ├── alert/
│   ├── button/
│   ├── card/
│   └── ...
├── src/
│   ├── services/
│   │   └── generator_service.py  # Factory pattern
│   └── data/
│       └── registry.py           # Charge les templates
```

### Flux actuel
1. `ComponentRegistry` charge les templates HTML au démarrage
2. `GeneratorService` sélectionne le template approprié
3. Retour du HTML brut sans transformation

## Solutions analysées

### Option 1 : Post-processing avec Guidelines Service
**Principe** : Appliquer des transformations après génération

**Avantages :**
- Non-invasif sur l'existant
- Évolutif et centralisé
- Facile à activer/désactiver

**Inconvénients :**
- Impact performance (parsing à chaque génération)
- Complexité des regex pour HTML

### Option 2 : Templates dynamiques
**Principe** : Remplacer le HTML statique par des templates avec variables

**Avantages :**
- Performance optimale
- Contrôle total sur le rendu

**Inconvénients :**
- Refonte complète des 131 templates
- Perte de la simplicité actuelle

### Option 3 : Configuration avec Registry (RECOMMANDÉ)
**Principe** : Système de règles chargé au démarrage avec cache

**Avantages :**
- Modulaire et maintenable
- Performance avec cache LRU
- Compatible avec l'existant

**Inconvénients :**
- Ajout de complexité modérée

## Solution recommandée : Option 3

### 1. Structure des guidelines

```yaml
# /config/guidelines.yaml
version: "1.0"
enabled: true

# Règles globales
global:
  typography:
    titles:
      capitalization: "sentence"  # sentence | title | upper | lower | none
      allow_icons: false
      max_length: 60
    
    paragraphs:
      max_length: 150
      
  accessibility:
    aria_labels: "required"
    alt_text: "required"

# Règles par composant
components:
  card:
    title:
      format: "sentence_case"
      required: true
    description:
      max_length: 100
      
  alert:
    title:
      required: false
      prefix_icon: false
      
  button:
    label:
      max_length: 30
      capitalization: "sentence"
      
  modal:
    title:
      required: true
      close_button: true

# Règles de transformation
transformations:
  - name: "remove_title_icons"
    pattern: '<i class=".*?"></i>\s*(?=<h[1-6])'
    replacement: ""
    
  - name: "sentence_case_titles"
    selector: "h1, h2, h3, h4, h5, h6"
    transform: "sentence_case"
    
  - name: "limit_title_length"
    selector: ".fr-card__title"
    max_length: 60
    ellipsis: "..."
```

### 2. Guidelines Service

```python
# /src/services/guidelines_service.py
from typing import Dict, Any, Optional
from functools import lru_cache
import yaml
import re
from bs4 import BeautifulSoup

class GuidelinesService:
    """
    Service de gestion des guidelines DSFR personnalisées.
    Applique les règles de formatage et de style.
    """
    
    def __init__(self, config_path: str = "config/guidelines.yaml"):
        self.config = self._load_config(config_path)
        self.enabled = self.config.get('enabled', True)
        self.transformers = self._init_transformers()
    
    def _load_config(self, path: str) -> Dict:
        """Charge la configuration des guidelines."""
        with open(path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    
    @lru_cache(maxsize=128)
    def apply_guidelines(
        self, 
        component: str, 
        html: str, 
        context: Optional[Dict] = None
    ) -> str:
        """
        Applique les guidelines au HTML généré.
        Utilise le cache pour les transformations répétées.
        """
        if not self.enabled:
            return html
            
        # Règles globales
        html = self._apply_global_rules(html)
        
        # Règles spécifiques au composant
        if component in self.config.get('components', {}):
            html = self._apply_component_rules(component, html)
        
        # Transformations personnalisées
        html = self._apply_transformations(html)
        
        return html
    
    def _apply_global_rules(self, html: str) -> str:
        """Applique les règles globales de typography."""
        soup = BeautifulSoup(html, 'html.parser')
        
        # Traitement des titres
        for title in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
            # Supprimer les icônes
            if not self.config['global']['typography']['titles']['allow_icons']:
                for icon in title.find_all('i'):
                    icon.decompose()
            
            # Appliquer la capitalisation
            if title.string:
                title.string = self._apply_capitalization(
                    title.string,
                    self.config['global']['typography']['titles']['capitalization']
                )
        
        return str(soup)
    
    def _apply_capitalization(self, text: str, style: str) -> str:
        """Applique le style de capitalisation."""
        if style == "sentence":
            return text[0].upper() + text[1:].lower() if text else text
        elif style == "title":
            return text.title()
        elif style == "upper":
            return text.upper()
        elif style == "lower":
            return text.lower()
        return text
```

### 3. Intégration dans GeneratorService

```python
# Modification de generator_service.py
def __init__(self):
    self.registry = get_registry()
    self._generators = self._init_generators()
    self.guidelines = GuidelinesService()  # Nouveau

def generate(self, component: str, **kwargs) -> str:
    """Génère un composant avec application des guidelines."""
    # Génération standard
    html = self._generate_raw(component, **kwargs)
    
    # Application des guidelines
    if self.guidelines.enabled:
        html = self.guidelines.apply_guidelines(component, html, kwargs)
    
    return html
```

### 4. Script de régénération

```python
#!/usr/bin/env python3
# /tools/regenerate_templates.py
"""
Régénère tous les templates en appliquant les guidelines.
Crée une sauvegarde avant modification.
"""

import sys
from pathlib import Path
from datetime import datetime
import shutil

sys.path.append(str(Path(__file__).parent.parent))

from src.services import get_generator, GuidelinesService

def regenerate_all_templates():
    """Régénère tous les templates avec les guidelines."""
    
    gabarits_dir = Path("gabarits")
    backup_dir = Path(f"gabarits_backup_{datetime.now():%Y%m%d_%H%M%S}")
    
    # Sauvegarde
    print(f"Création de la sauvegarde dans {backup_dir}")
    shutil.copytree(gabarits_dir, backup_dir)
    
    # Chargement des services
    generator = get_generator()
    guidelines = GuidelinesService()
    
    # Parcours et régénération
    count = 0
    for template_path in gabarits_dir.glob("**/*.html"):
        with open(template_path, 'r', encoding='utf-8') as f:
            original_html = f.read()
        
        # Extraction du composant depuis le commentaire
        component = extract_component_name(original_html)
        
        # Application des guidelines
        new_html = guidelines.apply_guidelines(component, original_html)
        
        if new_html != original_html:
            with open(template_path, 'w', encoding='utf-8') as f:
                f.write(new_html)
            count += 1
            print(f"✓ Mis à jour : {template_path}")
    
    print(f"\n{count} templates mis à jour")
    print(f"Sauvegarde disponible dans : {backup_dir}")

if __name__ == "__main__":
    regenerate_all_templates()
```

## Plan de mise en œuvre

### Phase 1 : Infrastructure (Sprint 1)
- [ ] Créer `/config/guidelines.yaml` avec règles de base
- [ ] Implémenter `GuidelinesService` avec tests
- [ ] Ajouter le cache LRU pour les performances

### Phase 2 : Intégration (Sprint 2)
- [ ] Modifier `GeneratorService` pour utiliser les guidelines
- [ ] Ajouter les tests d'intégration
- [ ] Documenter l'API des guidelines

### Phase 3 : Outils (Sprint 3)
- [ ] Créer le script `regenerate_templates.py`
- [ ] Ajouter commande de validation des guidelines
- [ ] Interface de test des règles

### Phase 4 : Documentation (Sprint 4)
- [ ] Guide d'utilisation des guidelines
- [ ] Exemples de règles personnalisées
- [ ] Migration guide pour les templates existants

## Avantages de cette approche

1. **Évolutivité** : Ajout facile de nouvelles règles sans toucher au code
2. **Performance** : Cache LRU + transformations optimisées
3. **Maintenabilité** : Configuration YAML lisible et versionnable
4. **Compatibilité** : Fonctionne avec les templates existants
5. **Flexibilité** : Activation/désactivation par composant ou globale

## Questions résolues

### Les gabarits sont-ils figés ?
**Actuellement** : Oui, statiques depuis septembre 2025
**Avec guidelines** : Évolutifs via configuration YAML

### Comment régénérer les templates ?
```bash
# Régénération complète avec sauvegarde
python tools/regenerate_templates.py

# Validation des guidelines
python tools/validate_guidelines.py

# Test sur un composant
python tools/test_guideline.py card
```

### Où stocker les guidelines ?
- Configuration principale : `/config/guidelines.yaml`
- Overrides par projet : `/config/guidelines.local.yaml`
- Hot-reload en développement via variable `GUIDELINES_HOT_RELOAD=true`

## Métriques de succès

- Réduction de 100% des problèmes de capitalisation
- Temps de régénération < 5 secondes pour 131 templates
- Zero régression sur les tests existants
- Adoption par 3+ projets utilisant le MCP DSFR

## Prochaines étapes

1. **Validation du concept** avec l'équipe
2. **POC** sur 5 composants critiques (card, alert, button, modal, form)
3. **Review** de l'architecture proposée
4. **Planning** de l'implémentation (estimation : 2-3 semaines)

---

*Document créé le : 2025-01-06*
*Auteur : Alexandra Guiderdoni & Claude*
*Version : 1.0*