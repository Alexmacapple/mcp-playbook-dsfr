# CLAUDE.md

Ce fichier fournit des directives à Claude Code (claude.ai/code) pour travailler avec le code de ce dépôt.

## Vue d'ensemble du projet

MCP Playbook DSFR est un serveur Model Context Protocol qui fournit des outils pour générer, valider et auditer des composants du Système de Design de l'État Français (DSFR v1.14). Le projet suit les principes Clean Code avec une architecture SOLID.

### Conventions importantes

- **Langue** : Toute la documentation et les commentaires sont en français
- **Style** : Code professionnel sans émojis
- **Architecture** : SOLID, DRY, KISS, YAGNI

## Commandes essentielles

### Installation et configuration
```bash
# Script d'installation automatique
./install.sh

# Ou installation manuelle
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Développement
```bash
# Activer l'environnement virtuel
source venv/bin/activate

# Démarrer le serveur MCP (pour tests hors Claude)
python3 mcp_local/server.py

# Lancer les tests
python3 -m pytest tests/ -v                    # Tous les tests
python3 -m pytest tests/ --cov=src             # Avec couverture
python3 -m pytest tests/ -m "not slow"         # Sans tests lents
python3 -m pytest tests/ -m "unit"             # Tests unitaires uniquement

# Vérification du code
mypy src/                                       # Vérification des types
ruff check src/                                 # Linting
black src/ --check                              # Formatage
```

### Docker (alternative)
```bash
# Construction et lancement avec Docker
docker-compose up --build                      # Développement
docker-compose up -d                           # Production
docker-compose logs -f mcp-dsfr                # Logs
docker-compose down                            # Arrêt
```

## Architecture

### Architecture orientée services (SOLID)

```
mcp_local/server.py             # Point d'entrée FastMCP - pont protocole MCP
    ↓
src/services/                   # Logique métier (responsabilité unique par service)
    ├── generator_service.py    # Génération de composants (Pattern Factory)
    ├── validator_service.py    # Validation HTML/DSFR
    ├── assistant_service.py    # Assistance intelligente
    ├── cognitive_service.py    # Analyse Connu-Inconnu de Rumsfeld
    ├── design_service.py       # Tokens de design DSFR (couleurs, icônes)
    ├── audit_service.py        # Audit d'accessibilité RGAA
    └── test_generator_service.py # Génération de tests (Jest, Cypress, Playwright)
    ↓
src/data/registry.py           # Registre des composants - source unique de vérité
    ↓
gabarits/                       # 48 templates HTML de composants DSFR
```

### Patterns de conception

1. **Pattern Singleton** : Les services utilisent des fonctions `get_*()` retournant des instances singleton
2. **Pattern Factory** : GeneratorService crée des composants selon leur type
3. **Pattern Registry** : ComponentRegistry gère toutes les métadonnées des composants DSFR
4. **Pattern Bridge** : FastMCP fait le pont entre le protocole MCP et les services internes

### Gestion des erreurs

Hiérarchie d'erreurs personnalisée dans `src/errors/` :
- `DSFRError` (base)
  - `ComponentNotFoundError`
  - `InvalidVariantError`
  - `ValidationError`
  - `AccessibilityError`

## Mapping des outils MCP

Chaque outil MCP correspond à une méthode de service spécifique :
- `generate_component` → GeneratorService.generate()
- `validate_html` → ValidatorService.validate()
- `audit_accessibility` → AuditService.audit()
- `analyze_cognitive` → CognitiveService.analyze_request()
- `get_design_tokens` → DesignService.get_colors/spacing/typography()
- `generate_tests` → TestGeneratorService.generate_tests()
- `get_assistant_help` → AssistantService.analyze_needs()
- `list_components` → Registry.get_all_components()

## Système de composants

48 composants DSFR avec 131 variantes, supportant chacun :
- Multiples variantes (ex : bouton : primary, secondary, tertiary)
- Options configurables (labels, icônes, tailles)
- Conformité accessibilité RGAA
- Génération automatique de tests

## Stratégie de tests

✅ **100% des tests passent** (11/11 tests fonctionnels)

### Fichiers de tests
```bash
# Tests autonomes (sans pytest) avec nomenclature cohérente
tests/test-mcp-dsfr-generator.py        # Factory Pattern
tests/test-mcp-dsfr-cognitive.py        # Agent cognitif Rumsfeld
tests/test-mcp-dsfr-design.py           # Outils design DSFR
tests/test-mcp-dsfr-assistant.py        # Service assistant
tests/test-mcp-dsfr-registry.py         # Singleton Pattern
tests/test-mcp-dsfr-all-components.py   # 48 composants DSFR
tests/test-mcp-dsfr-integration.py      # Tests end-to-end
tests/test-mcp-dsfr-server.py           # Serveur MCP
tests/test-mcp-dsfr-conformity.py       # Conformité DSFR
tests/test-mcp-dsfr-test-generator.py   # Génération Cypress/Playwright/Jest
tests/test-mcp-dsfr-assistant-generation.py # Assistant de génération

# Exécuter tous les tests automatiquement
./run_tests.sh

# Exécuter un test spécifique
venv/bin/python3 tests/test-mcp-dsfr-generator.py

# Résultats dans tests/resultats-test/
```

### Scripts d'exécution
```bash
# Installation avec dépendances
./install.sh

# Exécution de tous les tests
./run_tests.sh
```

## Configuration du serveur MCP

Pour l'intégration avec Claude Desktop :
```json
{
  "mcpServers": {
    "mcp-playbook-dsfr": {
      "command": "/chemin/absolu/vers/venv/bin/python3",
      "args": ["/chemin/absolu/vers/mcp_local/server.py"],
      "env": {
        "PYTHONPATH": "/chemin/absolu/vers/projet",
        "ENV": "production",
        "LOG_LEVEL": "INFO"
      }
    }
  }
}
```

## Structure du projet

```
mcp-playbook-dsfr/
├── mcp_local/          # Implémentation serveur MCP
├── src/                # Logique métier
│   ├── services/       # Couche service (SOLID)
│   ├── data/          # Registre et modèles de données
│   ├── errors/        # Exceptions personnalisées
│   └── utils/         # Utilitaires
├── gabarits/          # Templates HTML (48 composants)
├── tests/             # Suite de tests
├── docs/              # Documentation
├── requirements.txt   # Dépendances Python
├── install.sh         # Script d'installation
├── docker-compose.yml # Configuration Docker
├── Dockerfile         # Image Docker
└── .gitignore        # Règles Git
```

## Variables d'environnement

Configuration optionnelle via `.env` :
```bash
ENV=development|production              # Environnement d'exécution
LOG_LEVEL=DEBUG|INFO|WARNING|ERROR     # Niveau de log
DEFAULT_RGAA_LEVEL=A|AA|AAA           # Niveau RGAA par défaut
ENABLE_HTML_SANITIZATION=true|false    # Sanitisation HTML
MAX_CACHE_SIZE=256                     # Taille max du cache (MB)
RATE_LIMIT_PER_MINUTE=60              # Limite de requêtes/minute
```

## Validation rapide

```bash
# Vérifier l'installation
python3 -c "from mcp_local.server import app; print('Serveur MCP OK')"

# Tester la génération de composant
python3 -c "
from src.services import get_generator
html = get_generator().generate('button', label='Test')
print('Génération OK' if 'fr-btn' in html else 'Erreur')
"

# Vérifier tous les services
python3 -c "
from src.services import *
services = [get_generator(), get_validator(), get_audit_service()]
print(f'{len(services)} services chargés')
"
```

## Conventions de commit

Format des messages de commit :
```bash
# Format
<type>(<scope>): <description>

# Types
feat:     # Nouvelle fonctionnalité
fix:      # Correction de bug
docs:     # Documentation
style:    # Formatage (sans changement de code)
refactor: # Refactoring
test:     # Ajout/modification de tests
chore:    # Maintenance, configuration

# Exemples
feat(generator): ajouter support variante XL pour boutons
fix(validator): corriger détection balises auto-fermantes
docs(readme): mettre à jour instructions Docker
test(audit): ajouter tests niveau AAA
refactor(services): extraire logique commune dans BaseService
```

## Dépannage (Troubleshooting)

### Erreurs courantes et solutions

| Problème | Solution |
|----------|----------|
| `ModuleNotFoundError: No module named 'mcp'` | `pip install -r requirements.txt` |
| `ImportError: cannot import name 'app'` | Vérifier PYTHONPATH : `export PYTHONPATH=$(pwd)` |
| Icône 🔌 absente dans Claude Desktop | 1. Vérifier config JSON<br>2. Redémarrer Claude Desktop<br>3. Vérifier logs : `~/Library/Logs/Claude/` |
| `Permission denied` sur install.sh | `chmod +x install.sh` |
| Port 9090 déjà utilisé (Docker) | Modifier `METRICS_PORT` dans `.env` |
| Tests échouent avec timeout | Augmenter timeout : `pytest --timeout=30` |
| `python3: command not found` | Installer Python 3.9+ depuis python.org |
| Erreur SSL/certificat | `pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org` |
| Mémoire insuffisante Docker | Augmenter limites dans `docker-compose.yml` |

### Logs et débogage

```bash
# Activer mode debug
export LOG_LEVEL=DEBUG
export DEBUG=true

# Localisation des logs
logs/mcp.log                    # Logs application
~/.cache/claude/logs/           # Logs Claude Desktop (macOS)
%APPDATA%/Claude/logs/          # Logs Claude Desktop (Windows)

# Vérifier état des services
python3 -c "
from src.services import *
for name in ['generator', 'validator', 'audit_service']:
    service = eval(f'get_{name}()')
    print(f'{name}: {type(service).__name__}')
"
```

## Notes importantes

- Utilise la matrice Connu-Inconnu de Rumsfeld pour l'analyse cognitive avancée
- Tous les composants sont conformes RGAA avec niveaux d'accessibilité A/AA/AAA
- Les templates dans `gabarits/` sont la source de vérité pour la génération HTML
- Le registre (`src/data/registry.py`) contient toutes les métadonnées des composants
- Les services sont sans état et utilisent le pattern singleton pour l'efficacité
- Le framework FastMCP gère la communication du protocole MCP
- Support complet Docker pour déploiement production

## Badges de statut

```markdown
![Version](https://img.shields.io/badge/version-2.0.0-blue)
![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![Tests](https://img.shields.io/badge/tests-passing-green)
![Coverage](https://img.shields.io/badge/coverage-100%25-green)
![DSFR](https://img.shields.io/badge/DSFR-v1.14-red)
![RGAA](https://img.shields.io/badge/RGAA-4.1-green)
```

## Workflow de développement recommandé

1. **Créer une branche** : `git checkout -b feat/ma-fonctionnalite`
2. **Développer** avec tests : `pytest tests/ --watch`
3. **Vérifier** : `black . && ruff check . && mypy .`
4. **Commiter** : `git commit -m "feat: description"`
5. **Pousser** : `git push origin feat/ma-fonctionnalite`
6. **Pull Request** avec description détaillée

---

*Ce document est la référence principale pour Claude Code. Maintenir à jour lors de changements majeurs d'architecture.*