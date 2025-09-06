# Serveur MCP DSFR

## Architecture

Le répertoire `mcp_local` contient le serveur MCP (Model Context Protocol) pour l'intégration avec Claude Desktop.

### Fichiers principaux

| Fichier | Rôle | Description |
|---------|------|-------------|
| `server.py` | Point d'entrée | Serveur FastMCP avec tous les outils DSFR |
| `__init__.py` | Module Python | Définition du module et exports |

**Note** : Architecture minimaliste suivant le principe YAGNI (You Ain't Gonna Need It). Seulement 2 fichiers nécessaires pour un serveur MCP fonctionnel.

## Configuration

### Variables d'environnement

Le serveur peut utiliser des variables d'environnement système si nécessaire :

```env
# Variables supportées par Claude Desktop
PYTHONPATH=/chemin/vers/mcp-playbook-dsfr
ENV=production              # Pour les logs
LOG_LEVEL=WARNING          # Niveau de logs
```

**Note** : La configuration est directement gérée dans server.py. Pour des besoins spécifiques, les variables d'environnement peuvent être lues avec `os.getenv()` directement dans le code.

## Outils disponibles

Le serveur expose 8 outils MCP :

1. **generate_component** : Génération de composants DSFR
2. **list_components** : Liste des 48 composants disponibles
3. **validate_html** : Validation HTML/DSFR/RGAA
4. **audit_accessibility** : Audit RGAA multi-niveaux
5. **analyze_cognitive** : Analyse cognitive Rumsfeld
6. **get_design_tokens** : Tokens de design DSFR
7. **generate_tests** : Génération de tests automatiques
8. **get_assistant_help** : Assistant contextuel

## Utilisation

### Développement

```bash
# Activer l'environnement virtuel
source venv/bin/activate

# Lancer le serveur
python3 mcp_local/server.py

# Ou avec variables d'environnement
ENV=development LOG_LEVEL=DEBUG python3 mcp_local/server.py
```

### Production

```bash
# Avec systemd
sudo systemctl start mcp-dsfr

# Avec Docker
docker run -d \
  -e ENV=production \
  -e LOG_LEVEL=WARNING \
  -e DEFAULT_RGAA_LEVEL=AA \
  -e ENABLE_HTML_SANITIZATION=true \
  mcp-playbook-dsfr:latest
```

## Tests

```bash
# Test rapide
python3 -c "from mcp_local.server import app; print('OK')"

# Test complet
python3 tests/test-mcp-dsfr-server.py
```

## Sécurité

### Bonnes pratiques appliquées

- Pas de secrets dans le code
- Sanitisation HTML activée par défaut
- Validation des entrées
- Limite de taille des requêtes
- Rate limiting configurable
- Pas d'exécution de code dynamique
- Permissions restrictives en production

### Audit de sécurité

```bash
# Vérifier les permissions
ls -la mcp_local/

# Rechercher des secrets (doit être vide)
grep -i "password\|secret\|token" mcp_local/*.py

# Vérifier les imports dangereux
grep -E "eval\|exec\|__import__" mcp_local/*.py
```

## Architecture FastMCP

Le serveur utilise FastMCP, une API simplifiée du protocole MCP :

```python
from mcp.server import FastMCP

app = FastMCP("mcp-playbook-dsfr")

@app.tool()
def mon_outil(param: str) -> str:
    """Documentation de l'outil"""
    return "Résultat"

app.run()
```

## Intégration Claude Desktop

Configuration dans `claude_desktop_config.json` :

```json
{
  "mcpServers": {
    "mcp-playbook-dsfr": {
      "command": "/chemin/vers/venv/bin/python3",
      "args": ["/chemin/vers/mcp_local/server.py"],
      "env": {
        "PYTHONPATH": "/chemin/vers/mcp-playbook-dsfr",
      }
    }
  }
}
```

## Maintenance

### Logs

```bash
# Développement : logs dans la console
# Production : logs selon configuration

# Suivre les logs
tail -f /var/log/mcp-dsfr.log

# Avec Docker
docker logs -f mcp-dsfr
```

### Mise à jour

```bash
# Arrêter le serveur
sudo systemctl stop mcp-dsfr

# Mettre à jour le code
git pull origin main

# Redémarrer
sudo systemctl start mcp-dsfr
```

## Support

En cas de problème :

1. Vérifier les logs
2. Tester avec `python3 mcp_local/server.py`
3. Vérifier le serveur avec `python3 mcp_local/server.py`
4. Consulter la documentation principale : `/README.md`