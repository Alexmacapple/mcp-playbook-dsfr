# Guide de mise en production MCP DSFR

## Dépendances

### Pour la production

```bash
pip install -r requirements.txt
```

**7 packages essentiels :**
- `mcp` : Intégration Claude Desktop
- `beautifulsoup4` + `lxml` : Parsing HTML pour l'audit
- `bleach` : Sanitization HTML sécurisée
- `typing-extensions` : Compatibilité types Python
- `python-dotenv` : Variables d'environnement
- `requests` : Client HTTP (pour l'outil de version)

### Pour le développement

```bash
pip install -r requirements-dev.txt
```

Inclut automatiquement les dépendances de production + outils de test et qualité (pytest, black, mypy, ruff).

## Structure optimisée

```
mcp-playbook-dsfr/
├── mcp_local/          # Serveur MCP (2 fichiers seulement)
├── src/                # Code métier optimisé
│   ├── services/       # 7 services SOLID
│   ├── utils/          # Logger et sécurité simplifiés
│   ├── errors/         # Gestion d'erreurs structurée
│   └── data/           # Registre des composants
├── gabarits/           # 48 templates DSFR
├── tests/              # Tests et validation
├── tools/              # Outils de maintenance
└── docs/               # Documentation complète
```

## Optimisations appliquées

### 1. Réduction des dépendances
- ❌ Supprimé : `pydantic`, `structlog`, `pythonjsonlogger`
- ✅ Économie : ~3MB et complexité réduite
- ✅ Logging : Python standard au lieu de structlog

### 2. Simplification du code
- Module `security.py` : 390 → 243 lignes (-38%)
- Module `logger.py` : 185 → 142 lignes (-23%)
- GeneratorService : Suppression des hooks non utilisés

### 3. Sécurité renforcée
- Rejet direct du HTML avec `<script>` (pas seulement nettoyage)
- Validation stricte des noms de composants
- Sanitization préservant les classes DSFR

## Tests de validation

### Test rapide de non-régression
```bash
python3 tests/test_non_regression.py
```

**Résultats attendus :**
- 8/8 tests passent
- Performance : >1.5M opérations/seconde
- Aucune régression détectée

### Suite complète
```bash
./run_tests.sh
```

## Installation production

### 1. Cloner et installer

```bash
git clone https://github.com/yourusername/mcp-playbook-dsfr.git
cd mcp-playbook-dsfr
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Configuration Claude Desktop

Ajouter dans `claude_desktop_config.json` :

```json
{
  "mcpServers": {
    "mcp-playbook-dsfr": {
      "command": "/chemin/vers/venv/bin/python3",
      "args": ["/chemin/vers/mcp_local/server.py"],
      "env": {
        "PYTHONPATH": "/chemin/vers/mcp-playbook-dsfr",
        "ENV": "production",
        "LOG_LEVEL": "INFO"
      }
    }
  }
}
```

### 3. Vérification

```bash
# Test du serveur
python3 mcp_local/server.py

# Test des outils
python3 -c "from mcp_local.server import generer_composant; print(generer_composant('button', options={'label': 'Test'}))"
```

## Monitoring

Les logs sont maintenant en format texte simple (pas JSON) :
```
2024-01-06 10:30:45 [INFO] mcp.dsfr - MCP call: generer_composant | Duration: 5.23ms
```

## Maintenance

### Vérifier les mises à jour DSFR
```bash
python3 tools/check_dsfr_version.py
```

### Tests de non-régression après modifications
```bash
python3 tests/test_non_regression.py
```

## Performance

- **Génération de composants** : >1.5M ops/sec
- **Mémoire** : <50MB en utilisation normale
- **Temps de démarrage** : <1 seconde

## Support

- Documentation utilisateur : `/docs/GUIDE_UTILISATEUR.md`
- Documentation technique : `/README.md`
- Tests : `/tests/`
- Outils : `/tools/`