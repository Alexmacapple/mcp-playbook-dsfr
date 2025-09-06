# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Vue d'ensemble du projet

MCP Playbook DSFR est un serveur Model Context Protocol qui fournit des outils pour générer, valider et auditer des composants du Système de Design de l'État Français (DSFR v1.14.1). Le projet suit les principes Clean Code avec une architecture SOLID.

## Commandes

### Développement
```bash
# Installer les dépendances
pip3 install -r requirements.txt

# Démarrer le serveur MCP (pour tests hors Claude)
python3 mcp/server.py

# Lancer la suite de tests principale
python3 test_mcp.py

# Tester les services individuels
python3 test_generator.py      # Test génération de composants
python3 test_assistant.py      # Test service assistant
python3 test_cognitive.py      # Test analyse cognitive
python3 test_design_tools.py   # Test outils de design
python3 test_registry.py       # Test registre des composants

# Vérifier la conformité DSFR
python3 check_conformity.py

# Scripts de mise à jour (si nécessaire)
./update_dsfr.sh              # Mettre à jour la version DSFR
./UPDATE_COMPLETE.sh          # Processus de mise à jour complet
```

### Stratégie de tests
- Fichiers de test individuels pour chaque service (test_*.py)
- Les tests simulent les appels MCP que Claude ferait
- Pas de framework de test spécifique requis - utilise la bibliothèque standard Python
- Exécuter les tests directement avec python3

## Architecture

### Architecture orientée services (SOLID)

Le code suit une architecture orientée services stricte où chaque service a une responsabilité unique :

```
mcp/server.py                   # Point d'entrée MCP - fait le pont entre protocole MCP et services
    ↓
src/services/                   # Logique métier (chaque service = responsabilité unique)
    ├── generator_service.py    # Génération de composants (Factory Pattern)
    ├── validator_service.py    # Validation HTML/RGAA
    ├── assistant_service.py    # Assistance intelligente
    ├── cognitive_service.py    # Analyse Connu-Inconnu (matrice de Rumsfeld)
    ├── design_service.py       # Ressources design DSFR (couleurs, icônes)
    ├── audit_service.py        # Audit d'accessibilité RGAA
    └── test_generator_service.py # Génération de tests (Cypress, Playwright, Jest)
    ↓
src/data/registry.py           # Registre des composants - source unique de vérité pour les composants DSFR
    ↓
gabarits/                       # 141 templates HTML pour les composants DSFR
```

### Patterns de conception clés

1. **Pattern Singleton** : Chaque service utilise des fonctions `get_*()` qui retournent des instances singleton
2. **Pattern Factory** : GeneratorService crée des composants selon leur type
3. **Pattern Registry** : ComponentRegistry gère toutes les métadonnées des composants DSFR
4. **Pattern Bridge** : DSFRMCPServer fait le pont entre le protocole MCP et les services internes

### Flux d'interaction des services

1. Le serveur MCP reçoit un appel d'outil de Claude
2. Le serveur délègue au service approprié selon le nom de l'outil
3. Le service effectue l'opération en utilisant les données du registre et les templates
4. Le service retourne le résultat via le protocole MCP

### Gestion des erreurs

Hiérarchie d'erreurs personnalisée dans `src/errors/` :
- `DSFRError` (base)
  - `ComponentNotFoundError`
  - `InvalidVariantError`
  - `ValidationError`
  - `AccessibilityError`

### Mapping des outils MCP

Chaque outil MCP correspond à une méthode de service spécifique :
- `generate_component` → GeneratorService.generate()
- `validate_html` → ValidatorService.validate()
- `accessibility_audit` → AuditService.audit()
- `cognitive_analysis` → CognitiveService.analyze_known_unknown()
- `generate_tests` → TestGeneratorService.generate()

## Système de composants

Le projet inclut 48 composants DSFR avec 131 variantes. Les composants sont définis dans le registre et ont des templates HTML correspondants dans `gabarits/`. Chaque composant supporte :
- Plusieurs variantes (ex : bouton : primary, secondary, tertiary)
- Options configurables (labels, icônes, tailles)
- Conformité accessibilité RGAA
- Génération de tests

## Configuration du serveur MCP

Le serveur MCP est configuré dans Claude Desktop via :
```json
{
  "mcpServers": {
    "mcp-playbook-dsfr": {
      "command": "python3",
      "args": ["/Users/alex/Desktop/mcp-playbook-dsfr/mcp/server.py"]
    }
  }
}
```

## Notes importantes

- Le projet utilise un agent cognitif basé sur la matrice Connu-Inconnu de Rumsfeld pour l'analyse avancée
- Tous les composants sont conformes RGAA avec niveaux d'accessibilité A/AA/AAA
- Les templates dans `gabarits/` sont la source de vérité pour la génération HTML
- Le registre (`src/data/registry.py`) contient toutes les métadonnées des composants
- Les services sont sans état et utilisent le pattern singleton pour l'efficacité