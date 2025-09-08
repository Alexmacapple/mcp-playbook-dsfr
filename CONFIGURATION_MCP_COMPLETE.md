# Configuration Complète MCP Playbook DSFR

## Vue d'ensemble
Ce document détaille la configuration complète et fonctionnelle du serveur MCP Playbook DSFR pour Claude Desktop et Claude Code.

## 🎯 Configuration Fonctionnelle Actuelle

### 1. Structure des Fichiers Essentiels

```
/Users/alex/Desktop/mcp-playbook-dsfr/
├── mcp_local/              # Module Python du serveur MCP
│   ├── server.py          # Point d'entrée principal du serveur MCP
│   └── __init__.py        # Module Python
├── venv/                   # Environnement virtuel Python
│   └── bin/python3        # Interpréteur Python isolé
├── src/                    # Code source principal
├── gabarits/              # Templates DSFR
├── tests/                 # Tests unitaires
├── tools/                 # Outils utilitaires
├── claude_desktop_config.json  # Configuration exemple pour Claude Desktop
└── .claude/               # Configuration locale Claude Code
    └── mcp-config.json    # Configuration spécifique Claude Code
```

### 2. Configuration Claude Desktop

**Fichier**: `/Users/alex/.claude.json` (configuration globale utilisateur)

```json
{
  "mcpServers": {
    "dsfr": {
      "command": "/Users/alex/Desktop/mcp-playbook-dsfr/venv/bin/python3",
      "args": [
        "/Users/alex/Desktop/mcp-playbook-dsfr/mcp_local/server.py"
      ],
      "env": {
        "PYTHONPATH": "/Users/alex/Desktop/mcp-playbook-dsfr",
        "ENV": "production",
        "LOG_LEVEL": "INFO",
        "DEFAULT_RGAA_LEVEL": "AA",
        "ENABLE_HTML_SANITIZATION": "true"
      }
    }
  }
}
```

### 3. Configuration Claude Code

**Fichier**: `/Users/alex/Desktop/mcp-playbook-dsfr/.claude/mcp-config.json` (configuration locale projet)

```json
{
  "mcpServers": {
    "dsfr": {
      "command": "/Users/alex/Desktop/mcp-playbook-dsfr/venv/bin/python3",
      "args": [
        "/Users/alex/Desktop/mcp-playbook-dsfr/mcp_local/server.py"
      ],
      "env": {
        "PYTHONPATH": "/Users/alex/Desktop/mcp-playbook-dsfr",
        "ENV": "production",
        "LOG_LEVEL": "INFO",
        "DEFAULT_RGAA_LEVEL": "AA",
        "ENABLE_HTML_SANITIZATION": "true"
      }
    }
  }
}
```

### 4. Variables d'Environnement

Les variables d'environnement spécifiques au serveur MCP DSFR :

```env
PYTHONPATH=/Users/alex/Desktop/mcp-playbook-dsfr
ENV=production                    # Mode production
LOG_LEVEL=INFO                    # Niveau de log
DEFAULT_RGAA_LEVEL=AA             # Niveau d'accessibilité par défaut
ENABLE_HTML_SANITIZATION=true     # Activer la sanitisation HTML
```

## 🔧 Points Clés de Configuration

### Environnement Python
- **Interpréteur**: `/Users/alex/Desktop/mcp-playbook-dsfr/venv/bin/python3`
- **Module principal**: `mcp_local/server.py`
- **PYTHONPATH**: Doit pointer vers la racine du projet

### Hiérarchie des Configurations
1. **Claude Desktop**: lit `/Users/alex/.claude.json` (global)
2. **Claude Code**: lit `.claude/mcp-config.json` (local)
3. **Priorité**: Configuration locale > Configuration globale

### Dépendances Python
Le serveur nécessite un environnement virtuel Python configuré :
```bash
# Vérifier l'environnement virtuel
ls -la /Users/alex/Desktop/mcp-playbook-dsfr/venv/bin/python3

# Installer les dépendances si nécessaire
cd /Users/alex/Desktop/mcp-playbook-dsfr
./venv/bin/pip install -r requirements.txt
```

## 🚨 Problèmes Courants et Solutions

### 1. "Server failed to start"
**Symptôme**: Le serveur MCP ne démarre pas dans Claude

**Vérifications**:
1. Environnement virtuel Python présent : `ls venv/bin/python3`
2. Dépendances installées : `./venv/bin/pip list`
3. Module server.py exécutable : `./venv/bin/python3 mcp_local/server.py`
4. PYTHONPATH correctement configuré

### 2. "Module not found"
**Symptôme**: Erreur d'import Python

**Solution**:
```bash
cd /Users/alex/Desktop/mcp-playbook-dsfr
./venv/bin/pip install -r requirements.txt
```

### 3. Configuration non reconnue
**Symptôme**: Claude ne voit pas le serveur DSFR

**Solution**: Vérifier que le nom du serveur est cohérent :
- Dans Claude Desktop : `"dsfr"` dans `.claude.json`
- Dans Claude Code : `"dsfr"` dans `.claude/mcp-config.json`

## 📝 Commandes de Vérification

```bash
# Tester le serveur MCP manuellement
cd /Users/alex/Desktop/mcp-playbook-dsfr
./venv/bin/python3 mcp_local/server.py

# Vérifier les dépendances Python
./venv/bin/pip list | grep -E "mcp|claude"

# Vérifier la configuration Claude Code
cat .claude/mcp-config.json

# Tester l'import du module
./venv/bin/python3 -c "import mcp_local.server"
```

## ✅ Validation de Configuration

Une configuration correcte doit :
1. ✅ Afficher "✔ connected" pour DSFR dans `/mcp` de Claude
2. ✅ Lister les outils DSFR disponibles
3. ✅ Permettre la génération de composants DSFR
4. ✅ Respecter les normes d'accessibilité RGAA

## 🛠️ Outils MCP Disponibles

Le serveur MCP Playbook DSFR fournit des outils pour :
- Générer des composants DSFR conformes
- Créer des pages web accessibles
- Valider l'accessibilité RGAA
- Générer des templates Drupal/Twig
- Créer de la documentation technique

## 🔄 Processus de Mise à Jour

Lors de modifications du serveur MCP :
1. Modifier le code Python dans `mcp_local/`
2. Tester : `./venv/bin/python3 mcp_local/server.py`
3. Redémarrer Claude Code/Desktop ou reconnecter MCP via `/mcp`
4. Vérifier la connexion et tester les outils

## 📌 Configuration de Référence

Cette configuration a été validée et fonctionne le 2025-09-08 avec :
- Claude Desktop et Claude Code
- Python 3.x avec environnement virtuel
- Serveur MCP Playbook DSFR en mode production

## 🔗 Configuration Multi-MCP Complète

### Configuration Globale Active

**Fichier**: `/Users/alex/.claude.json`

Configuration complète avec MariaDB et DSFR :

```json
{
  "mcpServers": {
    "mariadb": {
      "command": "node",
      "args": ["/Users/alex/Desktop/mcp-mariadb/mcp-server.js"],
      "env": {
        "NODE_ENV": "production",
        "DB_HOST": "localhost",
        "DB_PORT": "3306",
        "DB_USER": "drupal_user",
        "DB_PASSWORD": "Drupal@123456!",
        "DB_NAME": "drupal_db",
        "MCP_LOG_LEVEL": "info"
      }
    },
    "dsfr": {
      "command": "/Users/alex/Desktop/mcp-playbook-dsfr/venv/bin/python3",
      "args": ["/Users/alex/Desktop/mcp-playbook-dsfr/mcp_local/server.py"],
      "env": {
        "PYTHONPATH": "/Users/alex/Desktop/mcp-playbook-dsfr",
        "ENV": "production",
        "LOG_LEVEL": "INFO",
        "DEFAULT_RGAA_LEVEL": "AA",
        "ENABLE_HTML_SANITIZATION": "true"
      }
    }
  }
}
```

### Configuration Locale du Projet

**Fichier**: `/Users/alex/Desktop/mcp-playbook-dsfr/.claude/mcp-config.json`

Configuration spécifique au projet DSFR :

```json
{
  "mcpServers": {
    "dsfr": {
      "command": "/Users/alex/Desktop/mcp-playbook-dsfr/venv/bin/python3",
      "args": ["/Users/alex/Desktop/mcp-playbook-dsfr/mcp_local/server.py"],
      "env": {
        "PYTHONPATH": "/Users/alex/Desktop/mcp-playbook-dsfr",
        "ENV": "production",
        "LOG_LEVEL": "INFO",
        "DEFAULT_RGAA_LEVEL": "AA",
        "ENABLE_HTML_SANITIZATION": "true"
      }
    }
  }
}
```

## 🔍 État Actuel des Serveurs MCP

### Serveurs Configurés et Opérationnels

1. **DSFR** (mcp-playbook-dsfr)
   - ✅ Configuré dans `.claude.json` global
   - ✅ Configuré dans `.claude/mcp-config.json` local
   - ✅ Environnement virtuel Python actif
   - ✅ Serveur FastMCP fonctionnel
   - ✅ 8 outils DSFR disponibles

2. **MariaDB** (mcp-mariadb)
   - ✅ Configuré dans `.claude.json` global
   - ✅ Serveur Node.js fonctionnel
   - ✅ Connexion à la base Drupal établie
   - ✅ 4 outils MariaDB disponibles

### Outils MCP Disponibles

#### Outils DSFR (préfixe `mcp__dsfr__`)
- `generer_composant` - Génère des composants DSFR
- `lister_composants` - Liste tous les composants disponibles
- `valider_html` - Valide le HTML selon DSFR/RGAA
- `audit_accessibilite` - Audit d'accessibilité RGAA
- `analyser_cognitif` - Analyse cognitive Rumsfeld
- `obtenir_tokens_design` - Design tokens DSFR
- `generer_tests` - Génère des tests automatisés
- `obtenir_aide_assistant` - Assistant DSFR

#### Outils MariaDB (préfixe `mcp__mariadb__`)
- `query` - Requêtes en langage naturel
- `schema` - Exploration du schéma
- `analyze` - Analyse de santé/performance
- `suggest` - Suggestions de questions

### Vérification Rapide

```bash
# Vérifier DSFR
cd /Users/alex/Desktop/mcp-playbook-dsfr
./venv/bin/python3 mcp_local/server.py

# Vérifier MariaDB
cd /Users/alex/Desktop/mcp-mariadb
node mcp-server.js

# Dans Claude Code
/mcp  # Doit afficher les deux serveurs connectés
```

---

*Document mis à jour le 08/09/2025 - Configuration validée et opérationnelle avec deux serveurs MCP*