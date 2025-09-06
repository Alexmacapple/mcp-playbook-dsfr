# MCP DSFR

[![Version](https://img.shields.io/badge/version-2.0.0-blue)](https://github.com/yourusername/mcp-playbook-dsfr/releases)
[![Python](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Tests](https://img.shields.io/badge/tests-100%25_passing-brightgreen)](tests/resultats-test/RAPPORT_100_POURCENT.txt)
[![DSFR](https://img.shields.io/badge/DSFR-v1.14-red)](https://www.systeme-de-design.gouv.fr)

Serveur Model Context Protocol intégrant le Design System de l'État français (DSFR) dans Claude Desktop. Génération, validation et audit de composants DSFR conformes RGAA 4.1.

## Table des matières

- [Installation](#installation)
- [Démarrage rapide](#démarrage-rapide)
- [Fonctionnalités](#fonctionnalités)
- [Documentation](#documentation)
- [Architecture](#architecture)
- [Tests](#tests)
- [Contribution](#contribution)
- [Support](#support)
- [Licence](#licence)

## Prérequis

- Python 3.9 ou supérieur
- Claude Desktop installé
- macOS, Linux ou Windows
- 200MB d'espace disque

## Installation

### Installation automatique (recommandée)

```bash
git clone https://github.com/yourusername/mcp-playbook-dsfr.git
cd mcp-playbook-dsfr
./install.sh
```

Le script d'installation :
1. Vérifie la version Python
2. Crée l'environnement virtuel
3. Installe les dépendances (incluant beautifulsoup4)
4. Teste le serveur
5. Génère la configuration Claude Desktop

### Exécution des tests

```bash
# Lancer tous les tests automatiquement
./run_tests.sh
```

Le script run_tests.sh active l'environnement virtuel et exécute les 12 tests de validation.

### Installation manuelle

```bash
# Cloner le repository
git clone https://github.com/yourusername/mcp-playbook-dsfr.git
cd mcp-playbook-dsfr

# Créer l'environnement virtuel
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Installer les dépendances
pip install -r requirements.txt

# Tester l'installation
python3 -c "from mcp_local.server import app; print('Installation réussie')"
```

### Configuration Claude Desktop

1. Localiser le fichier de configuration :
   - **macOS** : `~/Library/Application Support/Claude/claude_desktop_config.json`
   - **Windows** : `%APPDATA%\Claude\claude_desktop_config.json`
   - **Linux** : `~/.config/Claude/claude_desktop_config.json`

2. Ajouter la configuration MCP (remplacer `/chemin/absolu/vers/` par votre chemin réel) :

```json
{
  "mcpServers": {
    "mcp-playbook-dsfr": {
      "command": "/chemin/absolu/vers/venv/bin/python3",
      "args": ["/chemin/absolu/vers/mcp_local/server.py"],
      "env": {
        "PYTHONPATH": "/chemin/absolu/vers/mcp-playbook-dsfr",
        "ENV": "production",
        "LOG_LEVEL": "INFO",
        "DEFAULT_RGAA_LEVEL": "AA",
        "ENABLE_HTML_SANITIZATION": "true"
      }
    }
  }
}
```

3. Redémarrer Claude Desktop
4. Vérifier la présence de l'icône de connexion MCP

## Démarrage rapide

Une fois installé, utilisez ces commandes dans Claude Desktop :

```
# Générer un composant
"Génère un bouton DSFR primaire"

# Valider du HTML
"Valide ce code : <button class='fr-btn'>Cliquer</button>"

# Audit d'accessibilité
"Fais un audit RGAA de mon formulaire"

# Lister les composants
"Liste tous les composants DSFR disponibles"
```

## Fonctionnalités

### Outils MCP disponibles

| Outil | Description | Usage |
|-------|-------------|-------|
| `generate_component` | Génère des composants DSFR | Création de boutons, formulaires, cartes, etc. |
| `validate_html` | Valide la conformité HTML/DSFR | Vérification structure et classes CSS |
| `audit_accessibility` | Audit RGAA 4.1 | Analyse A, AA, AAA avec recommandations |
| `analyze_cognitive` | Analyse cognitive Rumsfeld | Identification des inconnues du projet |
| `list_components` | Liste les 48 composants | Catalogue complet avec variantes |
| `get_design_tokens` | Tokens de design DSFR | Couleurs, espacements, typographie |
| `generate_tests` | Génération de tests | Jest, Cypress, Playwright |
| `get_assistant_help` | Assistant contextuel | Aide et bonnes pratiques |

### Composants supportés

48 composants DSFR répartis en catégories :

- **Navigation** : header, footer, breadcrumb, navigation, sidemenu, pagination
- **Formulaires** : form, input, select, checkbox, radio, toggle, upload, password
- **Actions** : button, button-group, link, download, share
- **Contenu** : accordion, alert, badge, card, table, quote, callout, summary
- **Feedback** : modal, notice, tag, stepper, highlight
- **Layout** : grid, container, tile, tabs
- **Autres** : logo, consent, connect, translate, follow, tooltip, transcription

## Documentation

### Guides principaux

- [CLAUDE.md](CLAUDE.md) - Guide technique pour Claude Code
- [Guide de déploiement](docs/deployment/DEPLOYMENT.md) - Déploiement production
- [Tests exhaustifs](docs/tests/CAHIER_TEST_EXHAUSTIF.md) - 60 tests détaillés
- [Validation finale](docs/tests/VERIFICATION_FINALE.md) - Rapport de validation
- [Roadmap](docs/roadmap/ROADMAP.md) - Évolutions futures

### Documentation technique

```
docs/
├── deployment/         # Guides de déploiement
├── tests/             # Documentation des tests
└── roadmap/           # Évolutions planifiées
```

## Architecture

### Structure du projet

```
mcp-playbook-dsfr/
├── mcp_local/         # Serveur MCP FastMCP
│   ├── server.py      # Point d'entrée principal
│   └── __init__.py    # Module Python
├── src/
│   ├── services/      # Services métier (SOLID)
│   ├── data/         # Registre des composants
│   ├── errors/       # Gestion des erreurs
│   └── utils/        # Utilitaires
├── gabarits/         # Templates HTML (48 composants)
├── tests/            # Suite de tests (100% de réussite)
├── tools/            # Outils de développement (EXCLU en production)
│   └── maintenance/  # Scripts de mise à jour DSFR
├── docs/             # Documentation
│   ├── deployment/   # Guide de déploiement
│   └── roadmap/      # Feuille de route
├── requirements.txt  # Dépendances Python
├── install.sh        # Script d'installation
└── run_tests.sh      # Script d'exécution des tests
```

### Principes d'architecture

- **SOLID** : Chaque service a une responsabilité unique
- **DRY** : Pas de duplication de code
- **KISS** : Solutions simples et directes
- **YAGNI** : Uniquement les fonctionnalités nécessaires

### Services principaux

- `GeneratorService` : Génération de composants via Factory Pattern
- `ValidatorService` : Validation HTML avec détection de balises croisées
- `AuditService` : Audit RGAA multi-niveaux
- `CognitiveService` : Analyse Known-Unknown de Rumsfeld
- `DesignService` : Gestion des tokens de design
- `TestGeneratorService` : Génération de tests automatiques
- `AssistantService` : Aide contextuelle intelligente

## Tests

### Suite de tests complète

✅ **100% des tests passent** (11/11 tests fonctionnels)

### Lancer les tests

```bash
# Script recommandé (active l'environnement virtuel automatiquement)
./run_tests.sh

# OU manuellement avec l'environnement virtuel
source venv/bin/activate
python3 tests/test-mcp-dsfr-all-components.py
# ... autres tests
deactivate
```

### Résultats actuels

- ✅ 11 tests réussis sur 11 (100%)
- 📊 48 composants DSFR testés
- 🔧 Tous les services fonctionnels
- 📝 Génération automatique de tests (Cypress, Playwright, Jest)

### Validation manuelle

```bash
# Tester le serveur
python3 -c "
from mcp_local.server import app
from src.services import get_generator
html = get_generator().generate('button', label='Test')
print('OK' if 'fr-btn' in html else 'Erreur')
"
```

## Développement

### Configuration de l'environnement

```bash
# Environnement de développement
cp .env.example .env
# Éditer .env selon vos besoins
```

### Variables d'environnement

| Variable | Valeurs | Description |
|----------|---------|-------------|
| `ENV` | development, production | Environnement d'exécution |
| `LOG_LEVEL` | DEBUG, INFO, WARNING, ERROR | Niveau de logs |
| `DEFAULT_RGAA_LEVEL` | A, AA, AAA | Niveau RGAA par défaut |
| `ENABLE_HTML_SANITIZATION` | true, false | Sanitisation HTML |

### Workflow de développement

1. Créer une branche : `git checkout -b feature/nouvelle-fonctionnalite`
2. Développer avec tests : `pytest tests/ --watch`
3. Vérifier le code : `black . && ruff check . && mypy .`
4. Commiter : `git commit -m "feat: description"`
5. Push : `git push origin feature/nouvelle-fonctionnalite`
6. Créer une Pull Request

### Conventions de commit

Format : `<type>(<scope>): <description>`

Types :
- `feat` : Nouvelle fonctionnalité
- `fix` : Correction de bug
- `docs` : Documentation
- `style` : Formatage
- `refactor` : Refactoring
- `test` : Ajout de tests
- `chore` : Maintenance

## Déploiement

### Docker

```bash
# Construction
docker-compose build

# Lancement
docker-compose up -d

# Logs
docker-compose logs -f

# Arrêt
docker-compose down
```

### Production

Voir le [guide de déploiement complet](docs/deployment/DEPLOYMENT.md) pour :
- Configuration systemd
- Reverse proxy nginx
- Monitoring Prometheus
- Backup et restauration

## Contribution

Les contributions sont les bienvenues ! Voir [CONTRIBUTING.md](CONTRIBUTING.md) pour :

1. Standards de code
2. Process de review
3. Guidelines de test
4. Documentation requise

### Comment contribuer

1. Fork le projet
2. Créer votre branche (`git checkout -b feature/AmazingFeature`)
3. Commiter vos changements (`git commit -m 'feat: Add AmazingFeature'`)
4. Push sur la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

## Support

### Obtenir de l'aide

- [Issues GitHub](https://github.com/yourusername/mcp-playbook-dsfr/issues) - Rapporter des bugs
- [Discussions](https://github.com/yourusername/mcp-playbook-dsfr/discussions) - Questions et idées
- [Wiki](https://github.com/yourusername/mcp-playbook-dsfr/wiki) - Documentation étendue

### Dépannage courant

| Problème | Solution |
|----------|----------|
| ModuleNotFoundError | Réinstaller : `pip install -r requirements.txt` |
| Icône MCP absente | Redémarrer Claude Desktop |
| Permission denied | `chmod +x install.sh` |
| Python non trouvé | Installer Python 3.9+ |

## Auteurs

- **Auteur principal** - [Votre nom](https://github.com/yourusername)

Voir la liste des [contributeurs](https://github.com/yourusername/mcp-playbook-dsfr/contributors).

## Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

## Remerciements

- Équipe DSFR pour le Design System
- Anthropic pour le Model Context Protocol
- Communauté open source française
- Contributeurs et testeurs

## Ressources

- [Documentation DSFR officielle](https://www.systeme-de-design.gouv.fr)
- [Référentiel RGAA 4.1](https://www.numerique.gouv.fr/publications/rgaa-accessibilite/)
- [Claude Desktop](https://claude.ai/desktop)
- [Model Context Protocol](https://modelcontextprotocol.io)

---

Développé pour l'accessibilité et la conformité DSFR des services publics numériques français.