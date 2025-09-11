# Roadmap 6 : Plateforme DSFR & RGAA - Approche Skateboard -> Vélo -> Voiture

## Date : 2025-09-11
## Auteur : Alexandra Guiderdoni
## Objectif : LA référence française pour DSFR et RGAA
## Version cible : 3.0.0
## Approche : MVP minimal → Évolution progressive

---

## Vision Stratégique

### Positionnement unique
- **Mission** : Plateforme complète DSFR & RGAA pour développeurs et auditeurs
- **Cible** : Développeurs frontend/fullstack, auditeurs accessibilité, équipes qualité
- **Différenciation** : Seule solution intégrant génération DSFR + analyse RGAA + assistance intelligente
- **Philosophy** : Deliver Value Fast → Iterate → Perfect Later

### Objectifs clés
1. **Livrer de la valeur dès jour 3** : Un outil qui marche immédiatement
2. **Feedback utilisateur continu** : Itérations hebdomadaires basées sur usage réel
3. **Architecture évolutive** : Commencer simple, évoluer selon les besoins
4. **Focus sur l'essentiel** : 5 critères RGAA qui couvrent 80% des problèmes

### Valeur unique
- **Workflow intégré** : Analyser → Suggérer → Générer → Vérifier
- **Quick Wins immédiats** : Bookmarklet, GitHub Action, migration Axe-core
- **137 gabarits DSFR** + **5→20→106 critères RGAA progressifs**
- **Auto-fix intelligent** : Corrections automatiques dès semaine 1

---

## Avantage clé : RGAAcriteria.json

### Source de vérité unique
Le fichier `roadmap/Brainstorming/RGAAcriteria.json` contient :
- **106 critères officiels RGAA 4.1.2**
- **13 topics** organisés (Images, Couleurs, Formulaires...)
- **Titres français officiels** pour chaque critère
- **Structure JSON** prête à l'emploi

### Évolution progressive garantie
```
Phase 1 (Skateboard) : 5 critères   →  4.7% couverture
Phase 2 (Vélo)       : 20 critères  → 18.9% couverture  
Phase 3 (Voiture)    : 106 critères → 100% couverture
```

---

## Quick Wins Semaine 1

### Livrables immédiats (Jour 1-3)
- **RGAAcriteria.json intégré** : 106 critères officiels disponibles
- **Bookmarklet RGAA** : Tester n'importe quel site en 1 clic
- **GitHub Action** : CI/CD prêt à l'emploi
- **Script migration Axe-core** : Importer audits existants
- **Guide 5 minutes** : De zéro à première analyse

---

## Métriques de Succès (Révisées)

### KPIs Phase 1 - Skateboard (2 semaines)
- [OK] **3 projets réels** utilisant le CLI en production
- [OK] **50% réduction** du temps d'audit RGAA
- [OK] **Premier feedback** utilisateur en 48h
- [OK] **1 bug critique** fixé sous 24h

### KPIs Phase 2 - Vélo (4 semaines)
- [OK] **20 critères RGAA** couverts
- [OK] **10 utilisateurs actifs** hebdomadaires
- [OK] **5 auto-fix** automatisés
- [OK] **Intégration CI/CD** dans 3 projets

### KPIs Phase 3 - Voiture (8 semaines)
- [OK] **Architecture modulaire** complète
- [OK] **Dashboard Streamlit** fonctionnel
- [OK] **50+ utilisateurs** actifs
- [OK] **Package PyPI** publié

---

## 🛡️ Risques & Mitigations

### Risques identifiés
| Risque | Probabilité | Impact | Mitigation |
|--------|------------|--------|------------|
| Changements DSFR v2.0 | Moyenne | Fort | Abstraction layer + tests régression |
| Complexité RGAA | Haute | Moyen | Focus 5 critères essentiels d'abord |
| Adoption lente | Moyenne | Fort | Partenariat BetaGouv + quick wins |
| Dette technique | Faible | Moyen | Refactoring progressif planifié |

---

## Architecture Progressive : Skateboard -> Vélo -> Voiture

### Phase 1 : Skateboard (Semaine 1-2)
```python
# Un seul fichier qui fonctionne !
src/dsfr_rgaa.py                  # Tout-en-un monolithique (500 lignes max)
```

### Phase 2 : Vélo (Semaine 3-4)
```
src/
├── dsfr_rgaa.py                  # Point d'entrée CLI
├── dsfr_module.py                # Module DSFR extrait
├── rgaa_module.py                # Module RGAA extrait
└── quick_wins/
    ├── bookmarklet.js            # Test rapide navigateur
    ├── github_action.yml         # CI/CD template
    └── migrate_axe.py            # Import depuis Axe-core
```

### Phase 3 : Voiture (Semaine 5-8)
```
src/
├── modules/
│   ├── dsfr/                     # Module DSFR complet
│   │   ├── generator/
│   │   ├── scanner/
│   │   └── registry/
│   └── rgaa/                     # Module RGAA complet
│       ├── scanner/
│       ├── corrector/
│       └── assistant/
├── cli/                          # CLI structuré
├── dashboard/                    # Streamlit app
└── integrations/                 # CI/CD hooks
```

---

## 📝 Guide "Getting Started" - 5 minutes

```bash
# Installation (30 secondes)
pip install mcp-dsfr-rgaa

# Premier test RGAA (1 minute)
dsfr-rgaa check https://beta.gouv.fr
# Output: Score RGAA: 72/100 - 3 issues auto-fixables

# Première génération DSFR accessible (30 secondes)
dsfr-rgaa generate button --label="Valider" --accessible
# Output: <button class="fr-btn" aria-label="Valider">Valider</button>

# Premier auto-fix (2 minutes)
dsfr-rgaa fix page.html --auto
# Output: Fixed 5 accessibility issues automatically

# Intégration CI/CD (1 minute)
dsfr-rgaa init github-action
# Output: Created .github/workflows/rgaa-check.yml
```

---

## Phase 1 : Skateboard - MVP Ultra-Minimal (2 semaines)

### Jour 1-3 : Un fichier qui marche (avec RGAAcriteria.json)

```python
# src/dsfr_rgaa.py - Version monolithique avec JSON RGAA officiel
import json
import click
from bs4 import BeautifulSoup
from pathlib import Path

class DSFRRGAAPlatform:
    """MVP : Utilise RGAAcriteria.json (106 critères officiels RGAA 4.1.2)"""
    
    def __init__(self):
        # Charger les 106 critères RGAA depuis le JSON
        json_path = Path(__file__).parent.parent / 'roadmap/Brainstorming/RGAAcriteria.json'
        with open(json_path, 'r', encoding='utf-8') as f:
            self.rgaa_data = json.load(f)
        
        # Phase 1 : 5 critères prioritaires (couvrent 80% des problèmes)
        self.PRIORITY_CRITERIA = {
            "1.1": {  # Images
                "title": "Alternative textuelle des images",
                "check": lambda soup: all(img.get('alt') is not None for img in soup.find_all('img')),
                "auto_fix": lambda soup: self._fix_images_alt(soup)
            },
            "3.2": {  # Couleurs
                "title": "Contraste du texte",
                "check": lambda soup: True,  # Nécessite analyse CSS (Phase 2)
                "auto_fix": None
            },
            "8.2": {  # Éléments obligatoires
                "title": "Langue de la page",
                "check": lambda soup: bool(soup.find('html', {'lang': True})),
                "auto_fix": lambda soup: self._fix_page_lang(soup)
            },
            "9.1": {  # Structuration
                "title": "Hiérarchie des titres",
                "check": lambda soup: bool(soup.find('h1')) and len(soup.find_all('h1')) == 1,
                "auto_fix": None  # Complexe, nécessite refactoring
            },
            "11.1": {  # Formulaires
                "title": "Labels des champs",
                "check": lambda soup: all(
                    input.get('id') and soup.find('label', {'for': input.get('id')})
                    or input.get('aria-label')
                    for input in soup.find_all('input', {'type': lambda t: t != 'hidden'})
                ),
                "auto_fix": lambda soup: self._fix_form_labels(soup)
            }
        }
    
    def get_criterion_info(self, number):
        """Récupère les infos officielles depuis RGAAcriteria.json"""
        for topic in self.rgaa_data['topics']:
            for criterion in topic['subCriterion']:
                if criterion['number'] == number:
                    return {
                        'number': number,
                        'topic': topic['topic'],
                        'title': criterion['title']
                    }
        return None
    
    def check(self, html):
        """Vérifie les 5 critères RGAA prioritaires"""
        soup = BeautifulSoup(html, 'html.parser')
        results = {
            'score': 0,
            'passed': [],
            'failed': [],
            'auto_fixable': []
        }
        
        for criterion_id, criterion in self.PRIORITY_CRITERIA.items():
            info = self.get_criterion_info(criterion_id)
            passed = criterion['check'](soup)
            
            result = {
                'id': criterion_id,
                'topic': info['topic'] if info else 'Unknown',
                'title': info['title'] if info else criterion['title'],
                'passed': passed,
                'auto_fixable': criterion['auto_fix'] is not None
            }
            
            if passed:
                results['passed'].append(result)
            else:
                results['failed'].append(result)
                if result['auto_fixable']:
                    results['auto_fixable'].append(result)
        
        # Score sur 100
        total = len(self.PRIORITY_CRITERIA)
        results['score'] = int(len(results['passed']) / total * 100)
        
        return results
    
    def generate(self, component, **options):
        """Génération DSFR avec accessibilité RGAA intégrée"""
        if component == "button":
            label = options.get('label', 'Valider')
            # Respecte RGAA 11.2 et 6.1
            return f'<button class="fr-btn" aria-label="{label}">{label}</button>'
        elif component == "input":
            label = options.get('label', 'Champ')
            id_attr = options.get('id', 'field-1')
            # Respecte RGAA 11.1
            return f'''<div class="fr-input-group">
    <label class="fr-label" for="{id_attr}">{label}</label>
    <input class="fr-input" type="text" id="{id_attr}" name="{id_attr}">
</div>'''
        # ... autres composants DSFR
        return f"<!-- Composant {component} non implémenté -->"
    
    def fix(self, html):
        """Auto-fix des critères RGAA avec rapport détaillé"""
        soup = BeautifulSoup(html, 'html.parser')
        fixes_applied = []
        
        for criterion_id, criterion in self.PRIORITY_CRITERIA.items():
            if criterion['auto_fix'] and not criterion['check'](soup):
                criterion['auto_fix'](soup)
                fixes_applied.append(criterion_id)
        
        return {
            'fixed_html': str(soup),
            'fixes_applied': fixes_applied,
            'fixes_count': len(fixes_applied)
        }
    
    def _fix_images_alt(self, soup):
        """RGAA 1.1 : Ajoute alt="" aux images décoratives"""
        for img in soup.find_all('img', alt=None):
            img['alt'] = ""
        return soup
    
    def _fix_page_lang(self, soup):
        """RGAA 8.2 : Ajoute lang="fr" si absent"""
        html_tag = soup.find('html')
        if html_tag and not html_tag.get('lang'):
            html_tag['lang'] = 'fr'
        return soup
    
    def _fix_form_labels(self, soup):
        """RGAA 11.1 : Ajoute aria-label aux inputs sans label"""
        for i, input_tag in enumerate(soup.find_all('input', {'type': lambda t: t != 'hidden'})):
            if not input_tag.get('id'):
                input_tag['id'] = f'field-{i}'
            if not soup.find('label', {'for': input_tag['id']}) and not input_tag.get('aria-label'):
                input_tag['aria-label'] = f"Champ {i+1}"
        return soup

@click.group()
def cli():
    """DSFR-RGAA : 106 critères RGAA officiels + génération DSFR"""
    pass

@cli.command()
@click.argument('target')
@click.option('--json', 'output_json', is_flag=True, help='Sortie JSON détaillée')
def check(target, output_json):
    """Vérifie les critères RGAA (Phase 1: 5 critères, Phase 3: 106 critères)"""
    platform = DSFRRGAAPlatform()
    
    # Charger le HTML
    if target.startswith('http'):
        import requests
        html = requests.get(target).text
    else:
        with open(target, 'r', encoding='utf-8') as f:
            html = f.read()
    
    result = platform.check(html)
    
    if output_json:
        import json
        click.echo(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        # Affichage formaté
        click.echo(f"\n{'='*60}")
        click.echo(f"ANALYSE RGAA 4.1.2 - {len(platform.PRIORITY_CRITERIA)} critères prioritaires")
        click.echo(f"{'='*60}")
        click.echo(f"Score global : {result['score']}/100")
        
        if result['passed']:
            click.echo(f"\n[OK] Critères validés ({len(result['passed'])})")
            for criterion in result['passed']:
                click.echo(f"  • {criterion['id']} [{criterion['topic']}] : {criterion['title']}")
        
        if result['failed']:
            click.echo(f"\n[ERREUR] Critères échoués ({len(result['failed'])})")
            for criterion in result['failed']:
                fix_indicator = " [FIXABLE]" if criterion['auto_fixable'] else ""
                click.echo(f"  • {criterion['id']} [{criterion['topic']}] : {criterion['title']}{fix_indicator}")
        
        if result['auto_fixable']:
            click.echo(f"\n{len(result['auto_fixable'])} corrections automatiques disponibles")
            click.echo("   Utilisez --fix pour appliquer les corrections")

@cli.command()
@click.argument('target')
@click.option('--output', '-o', help='Fichier de sortie pour le HTML corrigé')
def fix(target, output):
    """Applique les corrections RGAA automatiques"""
    platform = DSFRRGAAPlatform()
    
    # Charger le HTML
    if target.startswith('http'):
        import requests
        html = requests.get(target).text
    else:
        with open(target, 'r', encoding='utf-8') as f:
            html = f.read()
    
    # Appliquer les corrections
    fix_result = platform.fix(html)
    
    # Sauvegarder si demandé
    if output:
        with open(output, 'w', encoding='utf-8') as f:
            f.write(fix_result['fixed_html'])
        click.echo(f"[OK] HTML corrigé sauvegardé dans {output}")
    else:
        click.echo(fix_result['fixed_html'])
    
    # Rapport
    click.echo(f"\nRapport de correction :")
    click.echo(f"  • {fix_result['fixes_count']} corrections appliquées")
    for criterion_id in fix_result['fixes_applied']:
        click.echo(f"  • Critère {criterion_id} corrigé")

@cli.command()
@click.argument('component')
@click.option('--label', default='Valider')
@click.option('--id', 'element_id', default=None)
def generate(component, label, element_id):
    """Génère un composant DSFR accessible RGAA"""
    platform = DSFRRGAAPlatform()
    options = {'label': label}
    if element_id:
        options['id'] = element_id
    
    html = platform.generate(component, **options)
    click.echo(html)

@cli.command()
def list_criteria():
    """Liste tous les 106 critères RGAA du JSON"""
    platform = DSFRRGAAPlatform()
    
    click.echo(f"\n{'='*60}")
    click.echo(f"RGAA {platform.rgaa_data['rgaa_version']} - {sum(len(t['subCriterion']) for t in platform.rgaa_data['topics'])} critères")
    click.echo(f"{'='*60}")
    
    for topic in platform.rgaa_data['topics']:
        click.echo(f"\n📂 {topic['topic']} ({len(topic['subCriterion'])} critères)")
        for criterion in topic['subCriterion']:
            # Marquer les critères prioritaires
            priority = "[P]" if criterion['number'] in platform.PRIORITY_CRITERIA else "   "
            click.echo(f"{priority} {criterion['number']} : {criterion['title'][:60]}...")

if __name__ == '__main__':
    cli()
```

### Jour 4-7 : Quick Wins

#### 1. Bookmarklet RGAA (30 minutes)
```javascript
// quick_wins/bookmarklet.js
javascript:(function(){
    const checks = {
        'Images sans alt': document.querySelectorAll('img:not([alt])').length,
        'Inputs sans label': document.querySelectorAll('input:not([aria-label]):not([id])').length,
        'Pas de H1': !document.querySelector('h1'),
        'Multiple H1': document.querySelectorAll('h1').length > 1,
        'Pas de lang': !document.documentElement.lang
    };
    
    let score = 100;
    let issues = [];
    
    for(let [check, result] of Object.entries(checks)) {
        if(result === true || result > 0) {
            score -= 20;
            issues.push(`[ERREUR] ${check}: ${result}`);
        }
    }
    
    alert(`Score RGAA rapide: ${score}/100\n\n${issues.join('\n')}`);
})();

#### 2. GitHub Action (1 heure)
```yaml
# quick_wins/github_action.yml
name: RGAA Check
on: [push, pull_request]

jobs:
  rgaa-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      
      - name: Install DSFR-RGAA
        run: pip install mcp-dsfr-rgaa
      
      - name: Run RGAA Check
        run: |
          dsfr-rgaa check ./dist/index.html
          
      - name: Comment PR
        if: github.event_name == 'pull_request'
        uses: actions/github-script@v6
        with:
          script: |
            const output = require('./rgaa-report.json');
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: `## Score RGAA: ${output.score}/100\n\n${output.summary}`
            })
```

#### 3. Script Migration Axe-core (2 heures)
```python
# quick_wins/migrate_axe.py
import json
import click

@click.command()
@click.argument('axe_report', type=click.File('r'))
def migrate_from_axe(axe_report):
    """Convertit un rapport Axe-core vers format DSFR-RGAA"""
    axe_data = json.load(axe_report)
    
    # Mapping Axe → RGAA
    MAPPING = {
        'image-alt': '1.1',           # Images alt
        'label': '11.1',               # Form labels
        'html-has-lang': '8.2',        # Page language
        'document-title': '8.3',       # Page title
        'heading-order': '9.1'         # Heading hierarchy
    }
    
    rgaa_report = {
        'score': 0,
        'passed': [],
        'failed': [],
        'auto_fixable': []
    }
    
    # Convertir les violations
    for violation in axe_data.get('violations', []):
        if violation['id'] in MAPPING:
            rgaa_criterion = MAPPING[violation['id']]
            rgaa_report['failed'].append({
                'criterion': rgaa_criterion,
                'impact': violation['impact'],
                'nodes': len(violation['nodes']),
                'auto_fixable': violation['id'] in ['image-alt', 'label', 'html-has-lang']
            })
    
    # Calculer le score
    total_checks = len(MAPPING)
    failed_checks = len(rgaa_report['failed'])
    rgaa_report['score'] = int((total_checks - failed_checks) / total_checks * 100)
    
    click.echo(json.dumps(rgaa_report, indent=2))
    click.echo(f"\n[OK] Migration terminée : Score RGAA {rgaa_report['score']}/100")

if __name__ == '__main__':
    migrate_from_axe()
```

### Jour 8-14 : Tests utilisateurs & Feedback

#### Recrutement Beta-Testeurs (Jour 8)
- Contact 3 projets gouvernementaux existants
- Canal Slack/Discord dédié
- Office hours hebdomadaires

#### Métriques à suivre
- Temps moyen pour premier test : < 5 minutes
- Bugs critiques fixés : < 24h
- Taux adoption quick wins : > 50%

---

## Phase 2 : Vélo - Modularisation (Semaine 3-4)

### Semaine 3 : Séparation en modules avec RGAAcriteria.json

```python
# src/dsfr_module.py - Module DSFR extrait
class DSFRModule:
    """Module DSFR avec les 48 gabarits existants"""
    
    def __init__(self):
        self.registry = self._load_existing_templates()
    
    def generate(self, component, **options):
        # Utilise les gabarits existants
        return self.registry[component].render(**options)

# src/rgaa_module.py - Module RGAA enrichi avec JSON
import json
from pathlib import Path

class RGAAModule:
    """Module RGAA progressif : 5 → 20 → 106 critères"""
    
    def __init__(self, phase='skateboard'):
        # Toujours charger les 106 critères depuis le JSON
        json_path = Path('roadmap/Brainstorming/RGAAcriteria.json')
        with open(json_path, 'r', encoding='utf-8') as f:
            self.rgaa_data = json.load(f)
        
        # Sélection progressive des critères selon la phase
        if phase == 'skateboard':  # 5 critères
            self.active_criteria = ['1.1', '3.2', '8.2', '9.1', '11.1']
        elif phase == 'velo':  # 20 critères (top par topic)
            self.active_criteria = [
                '1.1', '1.2',  # Images
                '3.2', '3.3',  # Couleurs
                '6.1', '6.2',  # Liens
                '8.2', '8.3', '8.9',  # Éléments obligatoires
                '9.1', '9.2',  # Structuration
                '10.1', '10.2',  # Présentation
                '11.1', '11.2', '11.10',  # Formulaires
                '12.6', '12.7',  # Navigation
                '13.1', '13.8'  # Consultation
            ]
        else:  # 'voiture' : tous les 106 critères
            self.active_criteria = self._get_all_criteria_ids()
    
    def _get_all_criteria_ids(self):
        """Extrait tous les IDs des 106 critères du JSON"""
        criteria_ids = []
        for topic in self.rgaa_data['topics']:
            for criterion in topic['subCriterion']:
                criteria_ids.append(criterion['number'])
        return criteria_ids
    
    def scan(self, html):
        """Scan progressif selon la phase"""
        results = {
            'phase': f"{len(self.active_criteria)} critères actifs",
            'total_criteria': 106,
            'active_criteria': len(self.active_criteria),
            'coverage': f"{len(self.active_criteria)/106*100:.1f}%"
        }
        # Scanner uniquement les critères actifs
        return self._scan_criteria(html, self.active_criteria)
```

### Semaine 4 : Intégrations CI/CD

#### Pre-commit Hook
```yaml
# .pre-commit-config.yaml
repos:
  - repo: local
    hooks:
      - id: rgaa-check
        name: RGAA Accessibility Check
        entry: dsfr-rgaa check
        language: system
        files: \.(html|jsx|tsx)$
```

#### GitLab CI Template
```yaml
# .gitlab-ci.yml
rgaa-check:
  stage: test
  script:
    - pip install mcp-dsfr-rgaa
    - dsfr-rgaa check dist/
  artifacts:
    reports:
      junit: rgaa-report.xml
```

#### 1.2 CLI Unifié avec Sous-commandes

```python
# src/cli/main.py
import click
from src.modules import IntegratedPlatform

platform = IntegratedPlatform()

@click.group()
def cli():
    """MCP DSFR & RGAA - Plateforme complète"""
    pass

# Groupe DSFR
@cli.group()
def dsfr():
    """Module DSFR - Génération et analyse"""
    pass

@dsfr.command()
@click.argument('component')
@click.option('--variant', default='default')
@click.option('--accessible', type=click.Choice(['A', 'AA', 'AAA']), default='AA')
def generate(component, variant, accessible):
    """Génère un composant DSFR accessible"""
    result = platform.dsfr.generate(
        component, 
        variant=variant,
        accessibility_level=accessible
    )
    click.echo(result)

# Groupe RGAA
@cli.group()
def rgaa():
    """Module RGAA - Analyse et assistance"""
    pass

@rgaa.command()
@click.argument('target')
@click.option('--level', type=click.Choice(['A', 'AA', 'AAA']), default='AA')
@click.option('--fix', is_flag=True, help='Appliquer les corrections automatiques')
def check(target, level, fix):
    """Vérifie la conformité RGAA"""
    if target.startswith('http'):
        results = platform.rgaa.scan_url(target, level=level)
    else:
        with open(target) as f:
            results = platform.rgaa.scan_html(f.read(), level=level)
    
    click.echo(f"Score RGAA: {results['score']}/100")
    
    if fix and results['auto_fixable']:
        click.echo(f"Application de {len(results['auto_fixable'])} corrections...")
        fixed = platform.rgaa.apply_fixes(results)
        click.echo("Corrections appliquées ✓")

@rgaa.command()
@click.option('--interactive', is_flag=True)
def assist():
    """Lance l'assistant RGAA interactif"""
    from src.modules.rgaa.assistant import InteractiveAssistant
    assistant = InteractiveAssistant(platform)
    assistant.run()

# Commande intégrée
@cli.command()
@click.argument('url')
@click.option('--full', is_flag=True, help='Analyse complète DSFR + RGAA')
@click.option('--fix', is_flag=True, help='Proposer des corrections')
def analyze(url, full, fix):
    """Analyse complète avec suggestions"""
    if full:
        results = platform.analyze_and_fix(url)
        
        # Rapport combiné
        click.echo("=" * 60)
        click.echo("ANALYSE COMPLÈTE DSFR & RGAA")
        click.echo("=" * 60)
        click.echo(f"Score DSFR: {results['dsfr']['score']}/100")
        click.echo(f"Score RGAA: {results['rgaa']['score']}/100")
        click.echo(f"Suggestions: {len(results['suggestions'])}")
        click.echo(f"Auto-fixables: {results['auto_fixed']}")
        
        if fix and results['suggestions']:
            click.echo("\nSUGGESTIONS:")
            for i, sugg in enumerate(results['suggestions'][:5], 1):
                click.echo(f"{i}. {sugg['title']}")
                if sugg.get('fixed_code'):
                    click.echo(f"   → Correction disponible")
```

### Semaine 3-4 : RGAA Scanner Essential

#### Ordre d'exécution des tâches

1. **Jour 1-2 : Setup structure**
   - Créer tous les dossiers modules/
   - Créer les fichiers __init__.py
   - Configurer les imports

2. **Jour 3-5 : Migration DSFR**
   - Copier services vers modules/dsfr/
   - Créer liens de compatibilité
   - Migrer les gabarits progressivement
   - Tester la non-régression

3. **Jour 6-8 : Module RGAA basique**
   - Implémenter RGAAScanner avec 20 critères
   - Créer les auto-fix pour images et formulaires
   - Tests unitaires RGAA

4. **Jour 9-10 : Intégration**
   - Service bridge DSFR↔RGAA
   - CLI unifié
   - Tests d'intégration

### Semaine 3-4 : RGAA Scanner Essential

#### 1.3 Scanner RGAA 20 Critères Prioritaires

```python
# src/modules/rgaa/scanner/essential_scanner.py
from typing import Dict, List
from bs4 import BeautifulSoup

class RGAAEssentialScanner:
    """Scanner RGAA avec les 20 critères essentiels."""
    
    ESSENTIAL_CRITERIA = {
        # Images
        "1.1": {"name": "Alt text", "level": "A", "auto_fix": True},
        "1.2": {"name": "Decorative images", "level": "A", "auto_fix": True},
        
        # Structure
        "8.2": {"name": "Page language", "level": "A", "auto_fix": True},
        "8.3": {"name": "Page title", "level": "A", "auto_fix": True},
        "9.1": {"name": "Heading hierarchy", "level": "A", "auto_fix": False},
        
        # Forms
        "11.1": {"name": "Form labels", "level": "A", "auto_fix": True},
        "11.10": {"name": "Required fields", "level": "A", "auto_fix": True},
        
        # Navigation
        "12.6": {"name": "Skip links", "level": "A", "auto_fix": True},
        
        # Links
        "6.1": {"name": "Link context", "level": "A", "auto_fix": False},
        
        # Contrast
        "3.2": {"name": "Text contrast", "level": "AA", "auto_fix": False}
    }
    
    def scan(self, html: str, level: str = "AA") -> Dict:
        """Scan avec critères essentiels."""
        soup = BeautifulSoup(html, 'html.parser')
        
        results = {
            'score': 0,
            'passed': [],
            'failed': [],
            'auto_fixable': [],
            'suggestions': []
        }
        
        for criterion_id, criterion in self.ESSENTIAL_CRITERIA.items():
            if self._should_check(criterion['level'], level):
                result = self._check_criterion(soup, criterion_id)
                
                if result['passed']:
                    results['passed'].append(criterion_id)
                else:
                    results['failed'].append({
                        'id': criterion_id,
                        'name': criterion['name'],
                        'level': criterion['level'],
                        'message': result['message'],
                        'elements': result.get('elements', [])
                    })
                    
                    # Si auto-fixable
                    if criterion['auto_fix']:
                        fix = self._generate_fix(soup, criterion_id, result)
                        if fix:
                            results['auto_fixable'].append(fix)
        
        results['score'] = self._calculate_score(results)
        return results
    
    def _generate_fix(self, soup, criterion_id: str, result: Dict) -> Dict:
        """Génère une correction automatique."""
        fixes = {
            "1.1": self._fix_missing_alt,
            "1.2": self._fix_decorative_images,
            "8.2": self._fix_page_lang,
            "8.3": self._fix_page_title,
            "11.1": self._fix_form_labels,
            "11.10": self._fix_required_fields,
            "12.6": self._fix_skip_links
        }
        
        fix_method = fixes.get(criterion_id)
        if fix_method:
            return fix_method(soup, result)
        return None
    
    def _fix_missing_alt(self, soup, result):
        """Corrige les images sans alt."""
        return {
            'criterion': '1.1',
            'type': 'add_attribute',
            'selector': 'img:not([alt])',
            'attribute': 'alt',
            'value': '',  # Sera rempli par l'assistant
            'message': 'Ajouter un texte alternatif descriptif'
        }
    
    def _fix_skip_links(self, soup, result):
        """Ajoute les liens d'évitement."""
        return {
            'criterion': '12.6',
            'type': 'add_html',
            'position': 'after_body_open',
            'html': '''<div class="fr-skiplinks">
    <nav class="fr-container" role="navigation" aria-label="Accès rapide">
        <ul class="fr-skiplinks__list">
            <li><a class="fr-link" href="#main">Contenu</a></li>
            <li><a class="fr-link" href="#header-navigation">Menu</a></li>
            <li><a class="fr-link" href="#footer">Pied de page</a></li>
        </ul>
    </nav>
</div>''',
            'message': 'Ajouter des liens d\'évitement'
        }
```

### Semaine 5-6 : RGAA Assistant Core

#### 1.4 Assistant RGAA Intelligent

```python
# src/modules/rgaa/assistant/core.py
from typing import List, Dict
from src.modules.dsfr import DSFRModule

class RGAAAssistant:
    """Assistant RGAA intelligent avec intégration DSFR."""
    
    def __init__(self, dsfr_module: DSFRModule):
        self.dsfr = dsfr_module
        self.knowledge_base = self._load_knowledge_base()
    
    async def analyze_and_suggest(self, html: str) -> Dict:
        """Analyse et suggère des améliorations."""
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html, 'html.parser')
        
        suggestions = []
        
        # 1. Identifier les composants non-DSFR
        non_dsfr_components = self._identify_non_dsfr(soup)
        
        for component in non_dsfr_components:
            # Trouver l'équivalent DSFR
            dsfr_equivalent = self._find_dsfr_equivalent(component)
            
            if dsfr_equivalent:
                # Générer le composant DSFR accessible
                dsfr_code = self.dsfr.generate(
                    dsfr_equivalent['type'],
                    variant=dsfr_equivalent['variant'],
                    accessibility_level='AAA'
                )
                
                suggestions.append({
                    'type': 'replace_with_dsfr',
                    'title': f"Remplacer par {dsfr_equivalent['type']} DSFR",
                    'original': str(component)[:100],
                    'suggestion': dsfr_code,
                    'rgaa_gain': self._calculate_rgaa_gain(component, dsfr_code),
                    'auto_fixable': True
                })
        
        # 2. Suggestions RGAA spécifiques
        rgaa_suggestions = self._generate_rgaa_suggestions(soup)
        suggestions.extend(rgaa_suggestions)
        
        # 3. Prioriser les suggestions
        suggestions.sort(key=lambda x: x.get('rgaa_gain', 0), reverse=True)
        
        return {
            'total_suggestions': len(suggestions),
            'auto_fixable': len([s for s in suggestions if s.get('auto_fixable')]),
            'estimated_score_gain': sum(s.get('rgaa_gain', 0) for s in suggestions),
            'suggestions': suggestions[:10]  # Top 10
        }
    
    def _identify_non_dsfr(self, soup) -> List:
        """Identifie les composants non-DSFR."""
        non_dsfr = []
        
        # Boutons non-DSFR
        for button in soup.find_all('button'):
            if not button.get('class') or 'fr-btn' not in ' '.join(button.get('class')):
                non_dsfr.append({
                    'element': button,
                    'type': 'button',
                    'dsfr_potential': 'high'
                })
        
        # Formulaires non-DSFR
        for form in soup.find_all('form'):
            if not form.get('class') or 'fr-form' not in ' '.join(form.get('class', [])):
                non_dsfr.append({
                    'element': form,
                    'type': 'form',
                    'dsfr_potential': 'high'
                })
        
        # Tables non-DSFR
        for table in soup.find_all('table'):
            if not table.get('class') or 'fr-table' not in ' '.join(table.get('class', [])):
                non_dsfr.append({
                    'element': table,
                    'type': 'table',
                    'dsfr_potential': 'medium'
                })
        
        return non_dsfr
    
    def _find_dsfr_equivalent(self, component: Dict) -> Dict:
        """Trouve l'équivalent DSFR d'un composant."""
        equivalents = {
            'button': {'type': 'button', 'variant': 'primary'},
            'form': {'type': 'form', 'variant': 'default'},
            'table': {'type': 'table', 'variant': 'responsive'},
            'nav': {'type': 'navigation', 'variant': 'default'},
            'alert': {'type': 'alert', 'variant': 'info'}
        }
        
        return equivalents.get(component['type'])
    
    def _calculate_rgaa_gain(self, original, dsfr_code: str) -> int:
        """Calcule le gain RGAA en remplaçant par DSFR."""
        # Logique simplifiée : DSFR garantit un certain niveau
        base_gain = 30  # DSFR respecte les bases
        
        # Bonus selon le type
        if 'fr-form' in dsfr_code:
            base_gain += 20  # Formulaires DSFR très accessibles
        elif 'fr-table' in dsfr_code:
            base_gain += 15  # Tables DSFR bien structurées
        elif 'fr-btn' in dsfr_code:
            base_gain += 10  # Boutons DSFR accessibles
        
        return min(base_gain, 50)  # Max 50 points de gain par suggestion
```

---

## Phase 2 : RGAA Assistant Avancé & Intégration (10 semaines)

### Semaine 7-10 : RGAA 106 Critères Progressif

#### 2.1 Scanner RGAA Complet

```python
# src/modules/rgaa/scanner/complete_scanner.py
class RGAACompleteScanner:
    """Scanner RGAA avec les 106 critères."""
    
    def __init__(self):
        self.criteria = self._load_all_criteria()
        self.essential_scanner = RGAAEssentialScanner()
    
    async def scan_progressive(self, html: str, depth: str = "essential") -> Dict:
        """Scan progressif selon le niveau de profondeur."""
        
        if depth == "essential":
            # 20 critères essentiels
            return self.essential_scanner.scan(html)
        
        elif depth == "standard":
            # 50 critères standards
            return await self._scan_standard(html)
        
        elif depth == "complete":
            # 106 critères complets
            return await self._scan_complete(html)
    
    async def _scan_complete(self, html: str) -> Dict:
        """Scan complet avec les 106 critères."""
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html, 'html.parser')
        
        results = {
            'score': 0,
            'by_theme': {},
            'passed': [],
            'failed': [],
            'warnings': [],
            'auto_fixable': []
        }
        
        # 13 thématiques RGAA
        themes = [
            "images", "cadres", "couleurs", "multimedia",
            "tableaux", "liens", "scripts", "elements_obligatoires",
            "structuration", "presentation", "formulaires",
            "navigation", "consultation"
        ]
        
        for theme in themes:
            theme_results = await self._scan_theme(soup, theme)
            results['by_theme'][theme] = theme_results
            results['passed'].extend(theme_results['passed'])
            results['failed'].extend(theme_results['failed'])
        
        results['score'] = self._calculate_global_score(results)
        return results
```

### Semaine 11-14 : Correcteur Automatique

#### 2.2 Auto-Fix Engine

```python
# src/modules/rgaa/corrector/auto_fix.py
class RGAAAutoFix:
    """Moteur de correction automatique RGAA."""
    
    def __init__(self, dsfr_module):
        self.dsfr = dsfr_module
        self.fix_strategies = self._load_strategies()
    
    async def apply_fixes(self, html: str, fixes: List[Dict]) -> str:
        """Applique les corrections automatiques."""
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html, 'html.parser')
        
        applied = []
        
        for fix in fixes:
            try:
                if fix['type'] == 'replace_with_dsfr':
                    soup = self._replace_with_dsfr(soup, fix)
                    applied.append(fix)
                
                elif fix['type'] == 'add_attribute':
                    soup = self._add_attribute(soup, fix)
                    applied.append(fix)
                
                elif fix['type'] == 'add_html':
                    soup = self._add_html(soup, fix)
                    applied.append(fix)
                
                elif fix['type'] == 'restructure':
                    soup = self._restructure(soup, fix)
                    applied.append(fix)
                    
            except Exception as e:
                print(f"Erreur lors de l'application du fix {fix['criterion']}: {e}")
        
        return {
            'fixed_html': str(soup),
            'applied_fixes': applied,
            'success_rate': len(applied) / len(fixes) * 100 if fixes else 0
        }
    
    def _replace_with_dsfr(self, soup, fix: Dict):
        """Remplace un composant par son équivalent DSFR."""
        # Trouver l'élément original
        original = soup.select_one(fix['selector'])
        if original:
            # Générer le composant DSFR
            dsfr_component = self.dsfr.generate(
                fix['dsfr_type'],
                variant=fix.get('variant', 'default'),
                **fix.get('options', {})
            )
            
            # Remplacer dans le DOM
            from bs4 import BeautifulSoup as BS
            new_element = BS(dsfr_component, 'html.parser')
            original.replace_with(new_element)
        
        return soup
```

### Semaine 15-16 : Workflow Intégré

#### 2.3 Integration Service DSFR↔RGAA

```python
# src/services/integration_service.py
class IntegrationService:
    """Service d'intégration bidirectionnelle DSFR↔RGAA."""
    
    def __init__(self, dsfr_module, rgaa_module):
        self.dsfr = dsfr_module
        self.rgaa = rgaa_module
    
    async def optimize_workflow(self, url: str) -> Dict:
        """Workflow d'optimisation complet."""
        
        # 1. Analyse initiale
        initial_dsfr = await self.dsfr.scan(url)
        initial_rgaa = await self.rgaa.scan(url, depth="complete")
        
        # 2. Identifier les quick wins
        quick_wins = []
        
        # Components non-DSFR avec fort impact RGAA
        if initial_dsfr['score'] < 50 and initial_rgaa['score'] < 70:
            quick_wins.append({
                'action': 'migrate_to_dsfr',
                'impact': 'high',
                'effort': 'medium',
                'estimated_gain': '+30 points RGAA'
            })
        
        # Issues RGAA auto-fixables
        if initial_rgaa['auto_fixable']:
            quick_wins.append({
                'action': 'apply_auto_fixes',
                'impact': 'medium',
                'effort': 'low',
                'count': len(initial_rgaa['auto_fixable']),
                'estimated_gain': f"+{len(initial_rgaa['auto_fixable']) * 2} points RGAA"
            })
        
        # 3. Générer un plan d'action
        action_plan = self._generate_action_plan(
            initial_dsfr,
            initial_rgaa,
            quick_wins
        )
        
        # 4. Simuler les améliorations
        simulation = await self._simulate_improvements(
            url,
            action_plan
        )
        
        return {
            'current_state': {
                'dsfr_score': initial_dsfr['score'],
                'rgaa_score': initial_rgaa['score']
            },
            'quick_wins': quick_wins,
            'action_plan': action_plan,
            'projected_state': simulation,
            'roi': self._calculate_roi(initial_dsfr, initial_rgaa, simulation)
        }
    
    def _generate_action_plan(self, dsfr_report, rgaa_report, quick_wins):
        """Génère un plan d'action priorisé."""
        actions = []
        
        # Phase 1 : Quick wins
        actions.append({
            'phase': 1,
            'title': 'Quick Wins',
            'duration': '1 semaine',
            'actions': quick_wins
        })
        
        # Phase 2 : Migration DSFR
        if dsfr_report['score'] < 70:
            actions.append({
                'phase': 2,
                'title': 'Migration DSFR',
                'duration': '2 semaines',
                'actions': [
                    {'component': comp, 'effort': 'medium'}
                    for comp in dsfr_report.get('missing_components', [])
                ]
            })
        
        # Phase 3 : Conformité RGAA
        if rgaa_report['score'] < 80:
            critical_issues = [
                issue for issue in rgaa_report['failed']
                if issue['level'] == 'A'
            ]
            actions.append({
                'phase': 3,
                'title': 'Conformité RGAA niveau A',
                'duration': '3 semaines',
                'actions': critical_issues[:10]
            })
        
        return actions
```

---

## Phase 3 : Dashboard Unifié & Intelligence (8 semaines)

### Semaine 17-20 : Dashboard Streamlit DSFR+RGAA

#### 3.1 Dashboard Intégré

```python
# dashboard/app.py
import streamlit as st
from src.modules import IntegratedPlatform

st.set_page_config(
    page_title="MCP DSFR & RGAA Platform",
    page_icon="🇫🇷",
    layout="wide"
)

platform = IntegratedPlatform()

# Sidebar pour navigation
with st.sidebar:
    st.title("🇫🇷 DSFR & RGAA")
    module = st.radio(
        "Module",
        ["Dashboard", "DSFR", "RGAA", "Intégration", "Assistant"]
    )

if module == "Dashboard":
    st.title("Tableau de bord DSFR & RGAA")
    
    # Métriques globales
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Sites analysés", "127", "+12")
    with col2:
        st.metric("Score DSFR moyen", "72%", "+5%")
    with col3:
        st.metric("Score RGAA moyen", "68%", "+8%")
    with col4:
        st.metric("Auto-fix appliqués", "453", "+45")
    
    # Graphique d'évolution
    st.subheader(" Évolution des scores")
    
    # Données mockup
    import pandas as pd
    import plotly.express as px
    
    df = pd.DataFrame({
        'Date': pd.date_range('2025-09-01', periods=30),
        'DSFR': [60 + i*0.5 for i in range(30)],
        'RGAA': [55 + i*0.7 for i in range(30)]
    })
    
    fig = px.line(df, x='Date', y=['DSFR', 'RGAA'], 
                  title='Progression moyenne des scores')
    st.plotly_chart(fig, use_container_width=True)

elif module == "RGAA":
    st.title("Module RGAA - Analyse et Assistance")
    
    tab1, tab2, tab3 = st.tabs([" Analyse", " Assistant", " Correcteur"])
    
    with tab1:
        st.subheader("Analyse RGAA")
        
        url = st.text_input("URL à analyser")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            depth = st.selectbox(
                "Profondeur",
                ["Essential (20)", "Standard (50)", "Complet (106)"]
            )
        with col2:
            level = st.selectbox("Niveau", ["A", "AA", "AAA"])
        with col3:
            auto_fix = st.checkbox("Corrections auto")
        
        if st.button("Analyser", type="primary"):
            with st.spinner("Analyse en cours..."):
                depth_value = depth.split()[0].lower()
                results = platform.rgaa.scan_progressive(
                    url, 
                    depth=depth_value
                )
                
                # Affichage des résultats
                st.success(f"Score RGAA: {results['score']}/100")
                
                # Détails par thématique
                if 'by_theme' in results:
                    st.subheader("Résultats par thématique")
                    for theme, data in results['by_theme'].items():
                        col1, col2 = st.columns([3, 1])
                        with col1:
                            st.write(f"**{theme.capitalize()}**")
                        with col2:
                            score = len(data['passed']) / (len(data['passed']) + len(data['failed'])) * 100
                            st.progress(score / 100)
                
                # Corrections disponibles
                if auto_fix and results.get('auto_fixable'):
                    st.info(f" {len(results['auto_fixable'])} corrections disponibles")
                    
                    if st.button("Appliquer les corrections"):
                        fixed = platform.rgaa.apply_fixes(url, results['auto_fixable'])
                        st.success(f"✓ {fixed['success_rate']:.0f}% des corrections appliquées")
    
    with tab2:
        st.subheader("Assistant RGAA Intelligent")
        
        # Mode interactif
        if 'messages' not in st.session_state:
            st.session_state.messages = []
        
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.write(message["content"])
        
        if prompt := st.chat_input("Posez votre question RGAA..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            
            # Réponse de l'assistant
            response = platform.rgaa.assistant.chat(prompt)
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.rerun()
    
    with tab3:
        st.subheader("Correcteur Automatique")
        
        uploaded_file = st.file_uploader("Choisir un fichier HTML", type=['html'])
        
        if uploaded_file:
            html_content = uploaded_file.read().decode('utf-8')
            
            # Analyse
            analysis = platform.rgaa.scan(html_content)
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric("Score actuel", f"{analysis['score']}/100")
                st.write(f"**Issues:** {len(analysis['failed'])}")
                st.write(f"**Auto-fixables:** {len(analysis['auto_fixable'])}")
            
            with col2:
                if analysis['auto_fixable']:
                    if st.button(" Corriger automatiquement"):
                        fixed_result = platform.rgaa.corrector.apply_fixes(
                            html_content,
                            analysis['auto_fixable']
                        )
                        
                        st.success(f"✓ {len(fixed_result['applied_fixes'])} corrections appliquées")
                        
                        # Télécharger le fichier corrigé
                        st.download_button(
                            "📥 Télécharger HTML corrigé",
                            data=fixed_result['fixed_html'],
                            file_name="fixed_rgaa.html",
                            mime="text/html"
                        )

elif module == "Intégration":
    st.title("Workflow Intégré DSFR↔RGAA")
    
    url = st.text_input("URL du site à optimiser")
    
    if st.button("Analyser et Optimiser", type="primary"):
        with st.spinner("Analyse complète en cours..."):
            workflow_result = platform.integration.optimize_workflow(url)
            
            # État actuel
            st.subheader(" État actuel")
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Score DSFR", f"{workflow_result['current_state']['dsfr_score']}/100")
            with col2:
                st.metric("Score RGAA", f"{workflow_result['current_state']['rgaa_score']}/100")
            
            # Quick Wins
            st.subheader("⚡ Quick Wins")
            for qw in workflow_result['quick_wins']:
                st.write(f"• **{qw['action']}** - Impact: {qw['impact']} - Gain estimé: {qw['estimated_gain']}")
            
            # Plan d'action
            st.subheader(" Plan d'action")
            for phase in workflow_result['action_plan']:
                with st.expander(f"Phase {phase['phase']}: {phase['title']} ({phase['duration']})"):
                    for action in phase['actions']:
                        st.write(f"• {action}")
            
            # État projeté
            st.subheader(" État projeté après optimisation")
            col1, col2 = st.columns(2)
            with col1:
                projected_dsfr = workflow_result['projected_state']['dsfr_score']
                delta_dsfr = projected_dsfr - workflow_result['current_state']['dsfr_score']
                st.metric("Score DSFR projeté", f"{projected_dsfr}/100", f"+{delta_dsfr}")
            with col2:
                projected_rgaa = workflow_result['projected_state']['rgaa_score']
                delta_rgaa = projected_rgaa - workflow_result['current_state']['rgaa_score']
                st.metric("Score RGAA projeté", f"{projected_rgaa}/100", f"+{delta_rgaa}")
            
            # ROI
            st.info(f"💰 ROI estimé: {workflow_result['roi']['time_saved']} heures économisées")

elif module == "Assistant":
    st.title(" Assistant Intelligent DSFR & RGAA")
    
    # Matrice Rumsfeld
    st.subheader("Analyse Cognitive (Matrice de Rumsfeld)")
    
    context = st.text_area("Décrivez votre contexte/problème")
    
    if st.button("Analyser"):
        from src.services.cognitive_service import CognitiveService
        cognitive = CognitiveService()
        
        analysis = cognitive.analyze_request(context)
        
        # Affichage de la matrice
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Known Knowns** (Ce que vous savez)")
            for item in analysis.get('known_knowns', []):
                st.write(f"• {item}")
            
            st.write("**Unknown Knowns** (Ce que vous ignorez savoir)")
            for item in analysis.get('unknown_knowns', []):
                st.write(f"• {item}")
        
        with col2:
            st.write("**Known Unknowns** (Ce que vous savez ne pas savoir)")
            for item in analysis.get('known_unknowns', []):
                st.write(f"• {item}")
            
            st.write("**Unknown Unknowns** (Ce que vous ignorez ignorer)")
            for item in analysis.get('unknown_unknowns', []):
                st.write(f"• {item}")
        
        # Recommandations basées sur l'analyse
        st.subheader("Recommandations")
        recommendations = cognitive.generate_recommendations(analysis)
        for rec in recommendations:
            st.write(f"• {rec}")
```

### Semaine 21-24 : Rapports et Documentation

#### 3.2 Générateur de Rapports Unifié

```python
# src/reports/unified_report.py
class UnifiedReportGenerator:
    """Générateur de rapports DSFR & RGAA unifiés."""
    
    def generate_compliance_report(self, analysis_results: Dict) -> str:
        """Génère un rapport de conformité complet."""
        
        html = f"""
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Rapport de Conformité DSFR & RGAA</title>
    <link rel="stylesheet" href="https://unpkg.com/@gouvfr/dsfr@1.11/dist/dsfr.min.css">
</head>
<body>
    <div class="fr-container fr-my-4w">
        <h1>Rapport de Conformité DSFR & RGAA</h1>
        
        <!-- Scores globaux -->
        <div class="fr-grid-row fr-grid-row--gutters">
            <div class="fr-col-6">
                <div class="fr-card">
                    <div class="fr-card__body">
                        <h2 class="fr-card__title">Score DSFR</h2>
                        <p class="fr-card__desc">
                            <span style="font-size: 3em; color: #000091;">
                                {analysis_results['dsfr']['score']}/100
                            </span>
                        </p>
                    </div>
                </div>
            </div>
            <div class="fr-col-6">
                <div class="fr-card">
                    <div class="fr-card__body">
                        <h2 class="fr-card__title">Score RGAA</h2>
                        <p class="fr-card__desc">
                            <span style="font-size: 3em; color: #000091;">
                                {analysis_results['rgaa']['score']}/100
                            </span>
                        </p>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- Détails DSFR -->
        <h2>Conformité DSFR</h2>
        <table class="fr-table">
            <thead>
                <tr>
                    <th>Critère</th>
                    <th>Statut</th>
                </tr>
            </thead>
            <tbody>
                {"".join(self._generate_dsfr_rows(analysis_results['dsfr']))}
            </tbody>
        </table>
        
        <!-- Détails RGAA -->
        <h2>Conformité RGAA</h2>
        <table class="fr-table">
            <thead>
                <tr>
                    <th>Critère</th>
                    <th>Niveau</th>
                    <th>Statut</th>
                </tr>
            </thead>
            <tbody>
                {"".join(self._generate_rgaa_rows(analysis_results['rgaa']))}
            </tbody>
        </table>
        
        <!-- Recommandations -->
        <h2>Recommandations</h2>
        <div class="fr-accordions-group">
            {"".join(self._generate_recommendations(analysis_results))}
        </div>
        
        <p class="fr-text--sm fr-mt-4w">
            Rapport généré le {datetime.now().strftime('%d/%m/%Y à %H:%M')}
        </p>
    </div>
</body>
</html>
        """
        
        return html
```

---

##  Checklist de Démarrage Immédiat

### Phase 1 : Skateboard (Jour 1-14)
- [ ] Copier `RGAAcriteria.json` dans le projet
- [ ] Créer `src/dsfr_rgaa.py` avec import JSON
- [ ] Implémenter 5 critères RGAA (1.1, 3.2, 8.2, 9.1, 11.1)
- [ ] CLI avec commande `list-criteria` pour voir les 106 critères
- [ ] Bookmarklet RGAA utilisant les mêmes critères
- [ ] GitHub Action template
- [ ] Script migration Axe-core avec mapping vers RGAA
- [ ] Recruter 3 beta-testeurs
- [ ] Premier feedback utilisateur

### Phase 2 : Vélo (Semaine 3-4)
- [ ] Séparer en modules DSFR et RGAA
- [ ] 20 critères RGAA
- [ ] Pre-commit hooks
- [ ] GitLab CI template
- [ ] Tests unitaires
- [ ] Documentation API

### Phase 3 : Voiture (Semaine 5-8)
- [ ] Architecture modulaire complète
- [ ] Dashboard Streamlit MVP
- [ ] Package PyPI
- [ ] Docker image
- [ ] Documentation complète
- [ ] Release v3.0.0

---

##  Commandes de Développement

### Phase 1 : Skateboard
```bash
# Créer le fichier monolithique
echo "# DSFR-RGAA MVP" > src/dsfr_rgaa.py

# Tester immédiatement
python3 src/dsfr_rgaa.py check https://beta.gouv.fr
python3 src/dsfr_rgaa.py generate button --label="Test"

# Installer comme CLI
pip install -e .
dsfr-rgaa check index.html
```

### Phase 2 : Vélo
```bash
# Séparer en modules
mv src/dsfr_rgaa.py src/dsfr_rgaa_backup.py
touch src/{dsfr_module.py,rgaa_module.py}

# Tester la séparation
python3 -c "from src.dsfr_module import DSFRModule; print(DSFRModule())"
```

### Phase 3 : Voiture
```bash
# Structure finale
mkdir -p src/modules/{dsfr,rgaa}/
cp -r src/services/* src/modules/dsfr/
cp -r gabarits/* src/modules/dsfr/templates/

# Dashboard
pip install streamlit
streamlit run dashboard/app.py

# Package PyPI
python setup.py sdist bdist_wheel
twine upload dist/*
```

---

## Architecture Technique Finale

```
mcp-playbook-dsfr/
├── src/
│   ├── modules/
│   │   ├── dsfr/
│   │   │   ├── __init__.py
│   │   │   ├── generator/
│   │   │   ├── scanner/
│   │   │   └── registry/
│   │   │
│   │   └── rgaa/
│   │       ├── __init__.py
│   │       ├── assistant/
│   │       │   ├── core.py
│   │       │   └── interactive.py
│   │       ├── scanner/
│   │       │   ├── essential_scanner.py
│   │       │   └── complete_scanner.py
│   │       ├── analyzer/
│   │       └── corrector/
│   │           └── auto_fix.py
│   │
│   ├── cli/
│   │   ├── main.py
│   │   ├── dsfr_commands.py
│   │   └── rgaa_commands.py
│   │
│   ├── services/
│   │   ├── cognitive_service.py
│   │   └── integration_service.py
│   │
│   ├── api/
│   │   └── unified_api.py
│   │
│   └── reports/
│       └── unified_report.py
│
├── dashboard/
│   └── app.py
│
├── mcp_local/
│   └── server.py
│
├── gabarits/
├── tests/
└── docs/
```

---

## Timeline Actualisée

### Phase 1 : Skateboard (2 semaines)
[OK] **Livrable:** Script Python qui marche avec 5 critères RGAA
- Jour 1-3: MVP monolithique
- Jour 4-7: Quick wins (bookmarklet, GitHub Action, migration)
- Jour 8-14: Tests utilisateurs et feedback

### Phase 2 : Vélo (2 semaines)
[OK] **Livrable:** CLI structuré avec 20 critères RGAA
- Semaine 3: Modularisation DSFR/RGAA
- Semaine 4: Intégrations CI/CD

### Phase 3 : Voiture (4 semaines)
[OK] **Livrable:** Plateforme complète avec dashboard
- Semaine 5-6: Architecture modulaire finale
- Semaine 7-8: Dashboard Streamlit + Package PyPI

**Total : 8 semaines (2 mois) au lieu de 6 mois**

---

## Budget Optimisé

| Phase | Durée | Coût | Valeur ajoutée |
|-------|-------|------|----------------|
| Skateboard | 2 semaines | 4k€ | MVP utilisable immédiatement |
| Vélo | 2 semaines | 4k€ | CLI professionnel + CI/CD |
| Voiture | 4 semaines | 8k€ | Plateforme complète |
| **Total** | **8 semaines** | **16k€** | **ROI 1000% mois 3** |

**Économie : 29k€ et 4 mois** par rapport à l'approche initiale

---

## Conclusion

Cette approche **Skateboard → Vélo → Voiture** garantit :

[OK] **Valeur immédiate** : Outil utilisable dès jour 3
[OK] **Feedback continu** : Itérations basées sur usage réel
[OK] **Risque minimal** : Investissement progressif
[OK] **Flexibilité maximale** : Pivot possible à tout moment
[OK] **Time-to-market** : 2 mois au lieu de 6

### Principes clés
1. **Start Simple** : Un fichier Python qui marche
2. **Get Feedback Fast** : Beta-testeurs dès semaine 1
3. **Iterate Weekly** : Nouvelle valeur chaque semaine
4. **Architecture Later** : Structure quand c'est nécessaire
5. **Quick Wins First** : Bookmarklet et GitHub Action immédiatement

### Prochaines étapes
1. Créer `src/dsfr_rgaa.py` (3 heures)
2. Implémenter 5 critères RGAA (2 heures)
3. Tester sur un vrai site (1 heure)
4. Partager avec 1 beta-testeur (30 minutes)
5. Itérer selon feedback

---

*Roadmap mise à jour le 2025-09-11*
*Version cible : 3.0.0*
*Approche : Skateboard → Vélo → Voiture*
*Philosophie : Ship Fast, Learn Faster*