# Roadmap 7 : PRIORITÉ ABSOLUE - Base de Connaissances DSFR Complète

## BLOQUANT : Cette roadmap est LE prérequis avant toute autre évolution
## Date : 2025-09-12 (Révisée)
## Auteur : Alexandra Guiderdoni
## Objectif : MCP avec base de connaissances DSFR complète (HTML + métadonnées + documentation)
## Timeline : 1 SEMAINE
## Version cible : 3.0.0

---

## Problème Critique ÉLARGI

### Verdict de Claude Desktop (BLOQUANT)
> "Les composants sont trop génériques et ne suivent pas à la lettre le DSFR"

### Découverte majeure : Les fiches contiennent BIEN PLUS que du HTML
- **URL officielle** de chaque composant
- **Description fonctionnelle** ("Le bouton est un élément d'interaction...")
- **30+ variantes par composant** avec noms explicites
- **Notes d'usage** ("A n'appliquer qu'en cas exceptionnel...")
- **Hiérarchie structurée** (primary → simple, sm, lg, disabled, icon-left...)
- **Documentation intégrée** avec liens officiels

### Impact de ne pas exploiter ces données
- Claude Desktop rejette nos composants (HTML incomplet)
- Perte de 90% de la valeur des fiches markdown
- Assistant incapable d'expliquer ou recommander
- Pas de documentation intégrée = support utilisateur impossible

### Le vrai potentiel en 1 phrase
**Transformer 213 fiches markdown en base de connaissances DSFR complète = LE différenciateur de notre MCP**

---

## Solution ENRICHIE : Base de Connaissances Complète

### Ce qu'on extrait maintenant des 213 fiches
```json
{
  "button": {
    "metadata": {
      "url": "https://main--ds-gouv.netlify.app/example/component/button",
      "description": "Le bouton est un élément d'interaction avec l'interface...",
      "version": "DSFR v1.14.0",
      "documentation": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/bouton"
    },
    "categories": {
      "primary": {
        "simple": { "html": "...", "name": "Bouton simple" },
        "sm": { "html": "...", "name": "Bouton simple SM" },
        "disabled": { "html": "...", "name": "Bouton désactivé" },
        "icon-left": { "html": "...", "name": "Bouton icon à gauche" }
        // ... 10+ variantes
      },
      "secondary": { /* 10+ variantes */ },
      "tertiary": { /* 10+ variantes */ },
      "groups": { /* 15+ variantes de groupes */ }
    },
    "usage_notes": [
      "Utiliser <button> par défaut, <a> seulement si impossibilité technique",
      "L'attribut title est obligatoire pour les boutons avec icône seule"
    ]
  }
}
```

### Comparaison qui montre la vraie valeur
| Aspect | Avant (HTML seul) | Après (Knowledge Base) |
|--------|-------------------|------------------------|
| **Données extraites** | 1 bloc HTML | HTML + description + URL + notes + hiérarchie |
| **Variantes** | 1 par fichier | 30+ par composant organisées |
| **Documentation** | Aucune | Intégrée avec sources |
| **Assistant** | "Voici le HTML" | "Pour un bouton d'action principale, utilisez primary.simple car..." |
| **Valeur MCP** | Générateur basique | Base de connaissances DSFR |

---

## Plan PRAGMATIQUE en 3 phases (1 semaine)

### Phase 1 : Extraction Knowledge Base Complète (Jour 1-2)

#### Script d'extraction enrichi avec TOUTES les métadonnées
```python
# extract_knowledge_base.py - Extraction complète des fiches
import re
from pathlib import Path
import json

def extract_metadata(content):
    """Extrait URL, titre, version, description"""
    metadata = {}
    
    # URL officielle
    url_match = re.search(r'URL:\s*\n(.+)', content)
    if url_match:
        metadata['url'] = url_match.group(1).strip()
    
    # Titre
    title_match = re.search(r'Title:\s*\n(.+)', content)
    if title_match:
        metadata['title'] = title_match.group(1).strip()
    
    # Version DSFR
    version_match = re.search(r'DSFR v([\d.]+)', content)
    if version_match:
        metadata['version'] = f"DSFR v{version_match.group(1)}"
    
    # Description du composant
    desc_match = re.search(r'#\s+[^\n]+\n\n([^\n]+)', content)
    if desc_match:
        metadata['description'] = desc_match.group(1).strip()
    
    # Lien documentation
    doc_match = re.search(r'\[Documentation\]\(([^)]+)\)', content)
    if doc_match:
        metadata['documentation'] = doc_match.group(1)
    
    return metadata

def extract_variants_with_context(content):
    """Extrait les variantes avec leur nom et contexte"""
    variants = {}
    current_category = None
    current_variant = None
    
    # Parser ligne par ligne pour capturer la hiérarchie
    lines = content.split('\n')
    for i, line in enumerate(lines):
        # Catégorie principale (## Bouton primaire)
        if line.startswith('## ') and 'Extrait' not in line:
            current_category = line.replace('##', '').strip()
            if current_category not in variants:
                variants[current_category] = {}
        
        # Sous-variante (### Bouton simple)
        elif line.startswith('### ') and 'Extrait' not in line:
            current_variant = line.replace('###', '').strip()
        
        # Bloc HTML
        elif '```html' in line:
            # Extraire le HTML jusqu'à ```
            html_lines = []
            j = i + 1
            while j < len(lines) and '```' not in lines[j]:
                html_lines.append(lines[j])
                j += 1
            
            if current_category and current_variant:
                if current_category not in variants:
                    variants[current_category] = {}
                variants[current_category][current_variant] = '\n'.join(html_lines).strip()
    
    return variants

def extract_usage_notes(content):
    """Extrait les notes d'usage importantes"""
    notes = []
    
    # Chercher les paragraphes avec recommandations
    note_patterns = [
        r"A n'appliquer qu'en cas[^.]+\.",
        r"L'attribut [^.]+obligatoire[^.]+\.",
        r"Utiliser <button>[^.]+\."
    ]
    
    for pattern in note_patterns:
        matches = re.findall(pattern, content)
        notes.extend(matches)
    
    return notes

def extract_complete_knowledge():
    """Extrait TOUTES les informations des 213 fiches"""
    knowledge_base = {}
    script_dir = Path(__file__).parent if '__file__' in globals() else Path.cwd()
    fiches_dir = script_dir / 'roadmap/Brainstorming/fiches-markdown-v2'
    
    name_map = {
        'bouton': 'button', 'formulaire': 'form', 'alerte': 'alert',
        'carte': 'card', 'modale': 'modal', 'tableau': 'table',
        'accordeon': 'accordion', 'badge': 'badge', 'tag': 'tag'
    }
    
    for fiche in fiches_dir.glob('*.md'):
        content = fiche.read_text(encoding='utf-8')
        
        # Déterminer le nom du composant
        stem = fiche.stem.lower()
        component_name = next((en for fr, en in name_map.items() if fr in stem), 
                              stem.split('-')[-1])
        
        # Extraire TOUT
        knowledge_base[component_name] = {
            'metadata': extract_metadata(content),
            'variants': extract_variants_with_context(content),
            'usage_notes': extract_usage_notes(content),
            'source_file': fiche.name
        }
    
    # Sauvegarder la base de connaissances complète
    output_path = script_dir / 'components_knowledge_base.json'
    output_path.write_text(
        json.dumps(knowledge_base, indent=2, ensure_ascii=False)
    )
    
    # Stats
    total_variants = sum(
        sum(len(cat) for cat in comp.get('variants', {}).values())
        for comp in knowledge_base.values()
    )
    
    print(f"{len(knowledge_base)} composants extraits")
    print(f"{total_variants} variantes totales")
    print(f"Base de connaissances : components_knowledge_base.json")
    
    return knowledge_base

if __name__ == "__main__":
    extract_complete_knowledge()
```

#### Test immédiat sur 3 composants critiques
```bash
# Extraire
python3 extract_markdown.py

# Tester avec Claude Desktop
# 1. Bouton (le plus critique)
# 2. Formulaire (structure complexe)  
# 3. Alerte (accessibilité)
```

---

### Phase 2 : Services Enrichis avec Knowledge Base (Jour 3-4)

#### GeneratorService avec navigation hiérarchique
```python
# src/services/generator_service.py - Version Knowledge Base
from pathlib import Path
import json

class GeneratorService:
    def __init__(self):
        self.registry = get_registry()
        self._generators = self._init_generators()
        
        # NOUVEAU : Charger la base de connaissances complète
        self.knowledge_base = {}
        kb_path = Path(__file__).parent.parent.parent / 'components_knowledge_base.json'
        if kb_path.exists():
            with open(kb_path) as f:
                self.knowledge_base = json.load(f)
    
    def generate(self, component: str, variant_path: str = 'primary.simple', **kwargs) -> str:
        """
        Génération avec navigation hiérarchique
        Ex: generate('button', 'primary.icon-left', label='Valider')
        """
        if component in self.knowledge_base:
            kb = self.knowledge_base[component]
            
            # Navigation dans la hiérarchie (primary.icon-left)
            parts = variant_path.split('.')
            html = None
            
            if len(parts) == 2 and 'variants' in kb:
                category, variant = parts
                if category in kb['variants'] and variant in kb['variants'][category]:
                    html = kb['variants'][category][variant]
            
            if html:
                # Remplacements avec contexte
                if 'label' in kwargs:
                    html = html.replace('Libellé bouton', kwargs['label'])
                    html = html.replace('Label bouton', kwargs['label'])
                return html
        
        # Fallback sur ancienne méthode
        return self._generators.get(component, self._generate_default)(component, **kwargs)
    
    def get_documentation(self, component: str) -> Dict:
        """Retourne la documentation complète d'un composant"""
        if component in self.knowledge_base:
            return self.knowledge_base[component].get('metadata', {})
        return {}
    
    def list_variants_tree(self, component: str) -> Dict:
        """Retourne l'arbre complet des variantes"""
        if component in self.knowledge_base:
            return self.knowledge_base[component].get('variants', {})
        return {}
    
    def get_usage_notes(self, component: str) -> List[str]:
        """Retourne les notes d'usage importantes"""
        if component in self.knowledge_base:
            return self.knowledge_base[component].get('usage_notes', [])
        return []
```

#### AssistantService enrichi avec la knowledge base
```python
# src/services/assistant_service.py - Version enrichie
class AssistantService:
    def __init__(self):
        self.knowledge_base = self._load_knowledge_base()
    
    def explain_component(self, component: str) -> str:
        """Explique un composant avec sa description officielle"""
        if component in self.knowledge_base:
            kb = self.knowledge_base[component]
            metadata = kb.get('metadata', {})
            
            response = []
            if 'description' in metadata:
                response.append(metadata['description'])
            
            if 'documentation' in metadata:
                response.append(f"Documentation : {metadata['documentation']}")
            
            if 'usage_notes' in kb:
                response.append("\nNotes d'usage :")
                for note in kb['usage_notes']:
                    response.append(f"- {note}")
            
            return '\n'.join(response)
        
        return f"Composant {component} non documenté"
    
    def recommend_variant(self, component: str, use_case: str) -> str:
        """Recommande la meilleure variante selon le cas d'usage"""
        if component not in self.knowledge_base:
            return "Composant non trouvé"
        
        kb = self.knowledge_base[component]
        recommendations = {
            'mobile': 'Utilisez la variante SM pour les mobiles',
            'principal': 'Utilisez primary.simple pour l\'action principale',
            'secondaire': 'Utilisez secondary pour les actions secondaires',
            'danger': 'Utilisez une alerte + bouton pour les actions dangereuses',
            'icone': 'N\'oubliez pas l\'attribut title sur les boutons icon-only'
        }
        
        for key, recommendation in recommendations.items():
            if key in use_case.lower():
                return recommendation
        
        # Lister les variantes disponibles
        variants = kb.get('variants', {})
        return f"Variantes disponibles : {', '.join(variants.keys())}"
```

#### Test immédiat
```bash
# Tester le bouton avec le nouveau système
python3 -c "
from src.services import get_generator
html = get_generator().generate('button', label='Test')
print('OK' if 'type=\"button\"' in html else 'KO')
print(html)
"
```

---

### Phase 3 : Migration complète (Jour 5-7)

#### Migrer les 48 composants prioritaires
```python
# migrate_components.py - Script de migration
from pathlib import Path
import json

def migrate_priority_components():
    """Migre les composants utilisés par Claude Desktop"""
    
    PRIORITY = [
        'button', 'input', 'form', 'alert', 'card',
        'modal', 'table', 'accordion', 'breadcrumb',
        'badge', 'tag', 'link', 'navigation'
    ]
    
    success = []
    failed = []
    
    for component in PRIORITY:
        try:
            # Tester avec le nouveau système
            from src.services import get_generator
            html = get_generator().generate(component)
            
            # Vérifier les attributs critiques
            if 'aria-' in html or 'type=' in html or 'role=' in html:
                success.append(component)
                print(f"[OK] {component} - Conforme DSFR")
            else:
                failed.append(component)
                print(f"[ATTENTION] {component} - À vérifier")
        except Exception as e:
            failed.append(component)
            print(f"[ERREUR] {component} - Erreur: {e}")
    
    print(f"\nRésultat: {len(success)}/{len(PRIORITY)} migrés")
    return success, failed

if __name__ == "__main__":
    migrate_priority_components()
```

#### Validation automatique avec script
```python
# validate_conformity.py - Test automatique de conformité DSFR
from pathlib import Path
import sys

def validate_dsfr_conformity():
    """Vérifie automatiquement la conformité DSFR"""
    from src.services import get_generator
    
    tests = {
        'button': {
            'required': ['type="button"', 'fr-btn'],
            'test_params': {'label': 'Test', 'variant': 'primary'}
        },
        'form': {
            'required': ['fr-fieldset', 'aria-labelledby'],
            'test_params': {'variant': 'contact'}
        },
        'alert': {
            'required': ['fr-alert', 'role="alert"'],
            'test_params': {'message': 'Test alert', 'type': 'info'}
        }
    }
    
    results = []
    generator = get_generator()
    
    for component, config in tests.items():
        try:
            html = generator.generate(component, **config['test_params'])
            
            # Vérifier les attributs requis
            missing = [attr for attr in config['required'] if attr not in html]
            
            if not missing:
                print(f"[OK] {component}: Conforme DSFR")
                results.append((component, True))
            else:
                print(f"[ERREUR] {component}: Manque {', '.join(missing)}")
                results.append((component, False))
                
        except Exception as e:
            print(f"[ATTENTION] {component}: Erreur - {e}")
            results.append((component, False))
    
    # Résumé
    success = sum(1 for _, ok in results if ok)
    print(f"\nScore conformité: {success}/{len(tests)} ({success*100//len(tests)}%)")
    
    # Retour code pour CI/CD
    return 0 if success == len(tests) else 1

if __name__ == "__main__":
    sys.exit(validate_dsfr_conformity())
```

#### Test rapide en une ligne
```bash
# Validation complète automatique
python3 validate_conformity.py && echo "[OK] Prêt pour Claude Desktop" || echo "[ERREUR] Corrections nécessaires"
```

---

## Checklist JOUR PAR JOUR

### Lundi (Jour 1)
- [ ] Créer `extract_markdown.py`
- [ ] Extraire les 213 fiches → `components_official.json`
- [ ] Tester sur bouton : `type="button"` présent ?

### Mardi (Jour 2)
- [ ] Tester 3 composants critiques avec Claude Desktop
- [ ] Noter les problèmes trouvés
- [ ] Ajuster le script d'extraction si besoin

### Mercredi (Jour 3)
- [ ] Modifier `generator_service.py` (10 lignes de code)
- [ ] Ajouter le chargement de `components_official.json`
- [ ] Tester le fallback marche toujours

### Jeudi (Jour 4)
- [ ] Intégration complète dans GeneratorService
- [ ] Test end-to-end avec Claude Desktop
- [ ] Validation : "composants trop génériques" résolu ?

### Vendredi (Jour 5)
- [ ] Migration des 13 composants prioritaires
- [ ] Script `migrate_components.py`
- [ ] Rapport de migration

### Weekend (Jour 6-7)
- [ ] Tests de non-régression
- [ ] Documentation minimale
- [ ] Release v3.0.0

---

## Impact sur ROADMAP-6 (RGAA)

### Synergie avec l'audit RGAA grâce à la Knowledge Base

Avec la base de connaissances complète, ROADMAP-6 devient plus puissante :

1. **Validation RGAA contextuelle**
   - Les notes d'usage contiennent les règles d'accessibilité
   - Ex: "L'attribut title est obligatoire pour les boutons avec icône seule"
   - L'audit peut vérifier ces règles automatiquement

2. **Assistant RGAA intelligent**
   ```python
   # L'assistant peut maintenant :
   - Expliquer POURQUOI une règle RGAA s'applique (avec la doc officielle)
   - Proposer la bonne variante pour corriger
   - Citer la source officielle DSFR
   ```

3. **Tests générés avec contexte**
   - Les tests incluent les vérifications des notes d'usage
   - Validation des attributs obligatoires documentés
   - Tests spécifiques par variante

---

## Quick Win IMMÉDIAT (30 minutes)

### Test rapide pour valider l'extraction enrichie
```bash
# 1. Créer le script (2 min)
cat > extract_test.py << 'EOF'
import re
from pathlib import Path

# Chemins absolus pour éviter les erreurs
script_dir = Path.cwd()
fiche_path = script_dir / 'roadmap/Brainstorming/fiches-markdown-v2/fiche-030-bouton-systeme-de-design-de-letat.md'

if not fiche_path.exists():
    print(f"[ERREUR] Fichier non trouvé: {fiche_path}")
    print(f"   Répertoire actuel: {script_dir}")
    exit(1)

content = fiche_path.read_text(encoding='utf-8')

# Extraire TOUS les blocs HTML
html_blocks = re.findall(r'```html\n(.*?)```', content, re.DOTALL)

if html_blocks:
    print(f"[OK] {len(html_blocks)} blocs HTML trouvés")
    print("\nPREMIER BLOC (default):")
    print(html_blocks[0])
    print(f"\n[OK] type='button' présent? {'type=\"button\"' in html_blocks[0]}")
    print(f"[OK] aria-* présent? {'aria-' in html_blocks[0]}")
    
    if len(html_blocks) > 1:
        print(f"\n{len(html_blocks)-1} VARIANTES disponibles")
else:
    print("[ERREUR] Aucun bloc HTML trouvé")
EOF

# 2. Lancer (5 sec)
python3 extract_test.py

# 3. Si OK -> GO pour le reste
# 4. Si ERREUR -> Investiguer le format des fiches
```

### Si ça marche → Script complet
```python
# extract_all.py - Version améliorée avec chemins absolus
from pathlib import Path
import json
import re

# Chemins absolus pour éviter les erreurs
script_dir = Path(__file__).parent if '__file__' in globals() else Path.cwd()
fiches_dir = script_dir / 'roadmap/Brainstorming/fiches-markdown-v2'

# Mapping FR→EN pour les noms
name_map = {
    'bouton': 'button', 'formulaire': 'form', 'alerte': 'alert',
    'carte': 'card', 'modale': 'modal', 'tableau': 'table'
}

components = {}
for fiche in fiches_dir.glob('*.md'):
    content = fiche.read_text(encoding='utf-8')
    html_blocks = re.findall(r'```html\n(.*?)```', content, re.DOTALL)
    
    if html_blocks:
        # Nom intelligent
        stem = fiche.stem.lower()
        name = next((en for fr, en in name_map.items() if fr in stem), 
                   stem.split('-')[-1])
        
        components[name] = {
            'default': html_blocks[0].strip(),
            'variants': html_blocks[1:]
        }

# Sauvegarder avec chemin absolu
output = script_dir / 'components_official.json'
output.write_text(json.dumps(components, indent=2, ensure_ascii=False))

print(f"{len(components)} composants, {sum(len(c['variants']) for c in components.values())} variantes")
```

---

## Métriques de Succès ENRICHIES

### KPIs principaux
1. **Claude Desktop satisfait** : "Les composants suivent exactement le DSFR"
2. **Base de connaissances complète** : 213 composants avec métadonnées
3. **1000+ variantes** accessibles par navigation hiérarchique
4. **Documentation intégrée** : Chaque composant a sa description et notes

### Tests de validation enrichis
1. **HTML conforme** : `type="button"`, `aria-*`, `role` présents
2. **Métadonnées extraites** : URL, description, version DSFR
3. **Hiérarchie navigable** : `button.primary.icon-left` fonctionne
4. **Notes d'usage** : Règles et recommandations capturées
5. **Assistant intelligent** : Peut expliquer et recommander

---

## Points d'attention

### Ce qu'on NE fait PAS (YAGNI)
- Parser complexe avec AST (NON)
- Cache LRU prématuré (NON)
- Architecture sur-engineerée (NON)
- Documentation de 50 pages (NON)

### Ce qu'on fait (KISS)
- Script simple qui extrait (OUI)
- Modification minimale de GeneratorService (OUI)
- Test avec Claude Desktop (OUI)
- Ship it! (OUI)

---

## Décision Go/No-Go

### GO si :
- Le script d'extraction trouve le HTML dans les fiches
- Le HTML contient `type="button"`
- Claude Desktop valide un composant test

### NO-GO si :
- Les fiches sont dans un format incompatible
- → Plan B : Parser l'ancien projet Node.js

---

*Roadmap révisée le 2025-09-12*
*Priorité : CRITIQUE ABSOLU - Base de connaissances DSFR complète*
*Effort : 1 SEMAINE*
*ROI : Transformation du MCP en véritable référence DSFR*
*Différenciateur : Knowledge Base avec documentation intégrée (le vrai plus de l'ancien MCP)*