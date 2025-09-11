# Configuration complète - MCP Playbook DSFR

## Table des matières

1. [Variables d'environnement](#variables-denvironnement)
2. [Configuration Claude Desktop](#configuration-claude-desktop)
3. [Configuration Docker](#configuration-docker)
4. [Paramètres Python](#paramètres-python)
5. [Chemins et structures](#chemins-et-structures)
6. [Niveaux d'accessibilité RGAA](#niveaux-daccessibilité-rgaa)
7. [Logging et monitoring](#logging-et-monitoring)
8. [Référence rapide](#référence-rapide)

---

## Variables d'environnement

### Fichier `.env`

Le projet utilise un fichier `.env` pour la configuration locale. Un template est fourni dans `.env.example`.

#### Variables principales

| Variable | Type | Valeur par défaut | Description |
|----------|------|-------------------|-------------|
| `ENV` | string | `production` | Environnement d'exécution (`development` ou `production`) |
| `LOG_LEVEL` | string | `INFO` | Niveau de logging (`DEBUG`, `INFO`, `WARNING`, `ERROR`) |
| `DEFAULT_RGAA_LEVEL` | string | `AA` | Niveau RGAA par défaut (`A`, `AA`, `AAA`) |
| `ENABLE_HTML_SANITIZATION` | boolean | `true` | Active la sanitization HTML via bleach |

#### Création du fichier `.env`

```bash
# Copier le template
cp .env.example .env

# Éditer selon vos besoins
nano .env
```

#### Exemple de configuration

```bash
# .env
ENV=production
LOG_LEVEL=INFO
DEFAULT_RGAA_LEVEL=AA
ENABLE_HTML_SANITIZATION=true
```

### Utilisation dans le code

Les variables sont chargées automatiquement :

- **Logger** : `src/utils/logger.py:36-39`
  ```python
  log_level = os.getenv('LOG_LEVEL', 'INFO').upper()
  is_production = os.getenv('ENV', 'development') == 'production'
  ```

---

## Configuration Claude Desktop

### Emplacement du fichier

- **macOS** : `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows** : `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux** : `~/.config/Claude/claude_desktop_config.json`

### Structure de configuration

```json
{
  "mcpServers": {
    "mcp-playbook-dsfr": {
      "command": "/chemin/absolu/vers/venv/bin/python3",
      "args": ["/chemin/absolu/vers/mcp_local/server.py"],
      "env": {
        "PYTHONPATH": "/chemin/absolu/vers/projet",
        "ENV": "production",
        "LOG_LEVEL": "INFO",
        "DEFAULT_RGAA_LEVEL": "AA",
        "ENABLE_HTML_SANITIZATION": "true"
      }
    }
  }
}
```

### Installation automatique

Le script `install.sh` génère automatiquement la configuration :

```bash
# Exécuter l'installation
./install.sh

# La configuration sera affichée avec les chemins corrects
# Copier-coller dans claude_desktop_config.json
```

### Vérification

1. Redémarrer Claude Desktop
2. Vérifier l'icône 🔌 dans l'interface
3. Tester avec : "Liste les composants DSFR disponibles"

---

## Configuration Docker

### Docker Compose

Fichier : `docker-compose.yml`

#### Variables d'environnement

```yaml
environment:
  - ENV=${ENV:-production}
  - LOG_LEVEL=${LOG_LEVEL:-INFO}
  - DEFAULT_RGAA_LEVEL=${DEFAULT_RGAA_LEVEL:-AA}
  - ENABLE_HTML_SANITIZATION=${ENABLE_HTML_SANITIZATION:-true}
  - PYTHONPATH=/app
```

#### Limites de ressources

```yaml
deploy:
  resources:
    limits:
      cpus: '1'          # Maximum 1 CPU
      memory: 512M       # Maximum 512 MB RAM
    reservations:
      cpus: '0.5'        # Minimum 0.5 CPU
      memory: 256M       # Minimum 256 MB RAM
```

#### Volumes

```yaml
volumes:
  - ./gabarits:/app/gabarits:ro     # Templates HTML (lecture seule)
  - ./src:/app/src:ro                # Code source (lecture seule)
  - ./mcp_local:/app/mcp_local:ro   # Serveur MCP (lecture seule)
  - logs:/app/logs                   # Logs (écriture)
```

### Commandes Docker

```bash
# Construire l'image
docker-compose build

# Démarrer en mode détaché
docker-compose up -d

# Voir les logs
docker-compose logs -f mcp-dsfr

# Arrêter
docker-compose down

# Nettoyer complètement
docker-compose down -v --rmi all
```

---

## Paramètres Python

### Configuration du projet (`pyproject.toml`)

```toml
[project]
name = "mcp-playbook-dsfr"
version = "2.1.0"
description = "Serveur MCP intégrant le DSFR dans Claude Desktop"
requires-python = ">=3.9"

[project.dependencies]
mcp = ">=0.1.0"
beautifulsoup4 = ">=4.12.0"
lxml = ">=4.9.0"
bleach = ">=6.0.0"
typing-extensions = ">=4.0.0"
python-dotenv = ">=1.0.0"
requests = ">=2.31.0"
```

### Installation

```bash
# Installation production
pip install -r requirements.txt

# Installation développement
pip install -r requirements-dev.txt

# Installation éditable
pip install -e .
```

### Versions supportées

| Python | Support | Testé CI/CD |
|--------|---------|-------------|
| 3.9 | ✅ Minimum | ✅ |
| 3.10 | ✅ Complet | ✅ |
| 3.11 | ✅ Complet | ✅ |
| 3.12 | ✅ Complet | ✅ |
| 3.13 | ⚠️ Expérimental | ❌ |

---

## Chemins et structures

### Arborescence du projet

```
mcp-playbook-dsfr/
├── mcp_local/          # Serveur MCP
│   └── server.py       # Point d'entrée principal
├── src/                # Code source
│   ├── services/       # Services métier (7 services)
│   ├── data/          # Registry et modèles
│   ├── errors/        # Exceptions personnalisées
│   └── utils/         # Utilitaires (logger, etc.)
├── gabarits/          # 137 templates HTML DSFR
│   ├── accordion/     # Templates accordéon
│   ├── alert/         # Templates alertes
│   ├── button/        # Templates boutons
│   └── ...            # 46 autres composants
├── tests/             # 13 tests fonctionnels
├── docs/              # Documentation
└── roadmap/           # Roadmaps du projet
```

### Chemins importants dans le code

| Chemin | Fichier:Ligne | Description |
|--------|---------------|-------------|
| Base des gabarits | `src/data/registry.py:40` | `Path(__file__).parent.parent.parent / 'gabarits'` |
| Import système | `mcp_local/server.py:11` | `sys.path.insert(0, str(Path(__file__).parent.parent))` |
| Accès gabarits | `mcp_local/server.py:408` | `Path(__file__).parent.parent / "gabarits" / component` |
| Résultats tests | `tests/test-*.py:21` | `Path(__file__).parent / "resultats-test"` |

---

## Niveaux d'accessibilité RGAA

### Configuration par défaut

Variable : `DEFAULT_RGAA_LEVEL`

### Niveaux disponibles

| Niveau | Description | Critères | Usage recommandé |
|--------|-------------|----------|------------------|
| **A** | Niveau minimal | Critères essentiels | Sites basiques |
| **AA** | Niveau intermédiaire (défaut) | Critères étendus | Sites publics |
| **AAA** | Niveau maximal | Tous les critères | Sites critiques |

### Critères par niveau

Source : `src/services/audit_service.py:121-132`

#### Niveau A (Essentiel)
- Images : texte alternatif
- Formulaires : labels associés
- Langue : déclaration de langue
- Titre : titre de page
- Liens : contexte clair
- Tableaux : en-têtes

#### Niveau AA (Standard)
- Contraste : ratio 4.5:1 minimum
- Focus : indicateur visible
- Navigation : skip links
- Erreurs : messages explicites

#### Niveau AAA (Avancé)
- Contraste : ratio 7:1
- Aide contextuelle : complète
- Navigation : multiple
- Langage : simplifié

---

## Logging et monitoring

### Configuration des logs

#### Niveau de log

Variable : `LOG_LEVEL`

| Niveau | Verbosité | Usage |
|--------|-----------|-------|
| `DEBUG` | Très élevée | Développement, débogage |
| `INFO` | Normale | Production standard |
| `WARNING` | Réduite | Production, alertes uniquement |
| `ERROR` | Minimale | Production critique |

#### Format des logs

- **Développement** : Format lisible avec timestamps
- **Production** : Format JSON structuré

#### Rotation des logs (Docker)

```yaml
logging:
  driver: "json-file"
  options:
    max-size: "10m"    # Taille max par fichier
    max-file: "3"      # Nombre max de fichiers
```

### Métriques de performance

| Métrique | Valeur cible | Mesure actuelle |
|----------|--------------|-----------------|
| Throughput | >1M ops/sec | 1.5M ops/sec |
| Latence | <15ms | <10ms |
| Mémoire | <100MB | ~80MB |
| CPU | <50% | ~30% |

---

## Référence rapide

### Variables essentielles

```bash
# Copier dans .env
ENV=production
LOG_LEVEL=INFO
DEFAULT_RGAA_LEVEL=AA
ENABLE_HTML_SANITIZATION=true
```

### Configuration minimale Claude Desktop

```json
{
  "mcpServers": {
    "mcp-playbook-dsfr": {
      "command": "/path/to/venv/bin/python3",
      "args": ["/path/to/mcp_local/server.py"]
    }
  }
}
```

### Démarrage rapide

```bash
# Installation
./install.sh

# Test
venv/bin/python3 mcp_local/server.py

# Docker
docker-compose up -d
```

### Endpoints MCP

#### Tools (8)
- `generer_composant`
- `valider_html`
- `audit_accessibilite`
- `analyser_cognitif`
- `lister_composants`
- `obtenir_tokens_design`
- `generer_tests`
- `obtenir_aide_assistant`

#### Resources (3)
- `gabarit://{component}/{variant}`
- `list://gabarits`
- `metadata://component/{component}`

#### Prompts (5)
- `formulaire_accessible`
- `tableau_responsive`
- `page_complete`
- `composant_carte`
- `navigation_complexe`

---

## Support et documentation

- **Documentation principale** : [README.md](../README.md)
- **Changelog** : [CHANGELOG.md](../CHANGELOG.md)
- **Sécurité** : [SECURITY.md](../SECURITY.md)
- **Contribution** : [CONTRIBUTING.md](../CONTRIBUTING.md)
- **Roadmaps** : [roadmap/](../roadmap/)

---

*Document généré le 2025-09-11 - Version 2.1.0*