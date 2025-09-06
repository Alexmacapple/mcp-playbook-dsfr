# Tests MCP DSFR

## Nomenclature cohérente

Tous les tests suivent la nomenclature : `test-mcp-dsfr-[fonction].py`

## Organisation du répertoire

### Scripts de test (11 fichiers)

| Fichier | Description | Outils MCP testés |
|---------|-------------|-------------------|
| **test-mcp-dsfr-conformity.py** | Vérification de conformité DSFR v1.14.1 | Validation CSS, ARIA, RGAA |
| **test-mcp-dsfr-assistant-generation.py** | Assistant de génération de templates HTML | create_page, analyse cognitive |
| **test-mcp-dsfr-all-components.py** | Test de rendu des 48 composants | Tous les composants et variantes |
| **test-mcp-dsfr-assistant.py** | Test du service assistant | analyze_needs, create_page |
| **test-mcp-dsfr-cognitive.py** | Agent cognitif Rumsfeld | cognitive_analysis |
| **test-mcp-dsfr-design.py** | Outils design DSFR | get_dsfr_colors, get_dsfr_icons, search_components |
| **test-mcp-dsfr-generator.py** | Générateur Factory Pattern | generate_component |
| **test-mcp-dsfr-integration.py** | Tests d'intégration end-to-end | Tous les services |
| **test-mcp-dsfr-registry.py** | Registre Singleton | list_components, list_variants |
| **test-mcp-dsfr-server.py** | Serveur MCP | Protocole MCP, appels Claude |
| **test-mcp-dsfr-test-generator.py** | Générateur de tests | generate_tests (Cypress, Playwright, Jest) |

### Dossier html_outputs/
Contient les pages HTML générées par les tests.

## Exécution des tests

### Installation des dépendances

```bash
# Installation automatique avec le script principal
./install.sh

# OU installation manuelle des dépendances
pip install -r requirements.txt
```

### Exécution automatique de tous les tests

```bash
# Script recommandé pour exécuter tous les tests
./run_tests.sh
```

Ce script :
- Active automatiquement l'environnement virtuel
- Vérifie les dépendances (beautifulsoup4)
- Exécute tous les 11 tests actifs
- Affiche un résumé avec statistiques
- Liste les rapports générés

### Résultats actuels

```
Tests réussis    : 11/11 (100%)
Tests partiels   : 0/11  (0%)
Tests échoués    : 0/11  (0%)
SCORE FINAL      : 100%
```

### Exécution manuelle des tests

```bash
# Activer l'environnement virtuel d'abord
source venv/bin/activate

# Tests individuels
python3 tests/test-mcp-dsfr-registry.py
python3 tests/test-mcp-dsfr-all-components.py
python3 tests/test-mcp-dsfr-assistant.py
python3 tests/test-mcp-dsfr-server.py
python3 tests/test-mcp-dsfr-conformity.py
python3 tests/test-mcp-dsfr-cognitive.py
python3 tests/test-mcp-dsfr-generator.py
python3 tests/test-mcp-dsfr-integration.py
python3 tests/test-mcp-dsfr-design.py
python3 tests/test-mcp-dsfr-test-generator.py
python3 tests/test-mcp-dsfr-assistant-generation.py

# Désactiver l'environnement virtuel
deactivate
```

### Suite de tests complète (méthode alternative)

```bash
# Avec l'environnement virtuel activé
source venv/bin/activate
for test in tests/test-mcp-dsfr-*.py; do
    echo "Exécution de $(basename $test)..."
    python3 "$test"
done
deactivate
```

## Rapports générés

Tous les rapports sont sauvegardés dans `/tests/resultats-test/` avec l'extension `.txt` :

- `test_registry_report.txt`
- `test_generator_report.txt`
- `test_mcp_report.txt`
- `test_integration_mcp_report.txt`
- `test_assistant_report.txt`
- `test_cognitive_report.txt`
- `test_design_tools_report.txt`
- `test_all_components_report.txt`
- `test_test_generator_report.txt`
- `conformity_report.txt`
- `assistant_test_report.txt`

## Couverture des tests

### Statistiques
- **11 scripts de test** (100% fonctionnels)
- **13 outils MCP** (12 testés = 92% de couverture)
- **48 composants DSFR**
- **131 variantes**
- **7 services** (tous testés)

### Outils MCP testés

**Complètement testés (12/14)**
- generate_component
- list_components
- list_variants
- validate_html
- analyze_needs
- create_page
- get_component_info
- cognitive_analysis (inclut détection des angles morts)
- get_dsfr_colors
- get_dsfr_icons
- generate_tests

**Partiellement testés (2/14)**
- accessibility_audit (tests basiques uniquement)
- search_components (tests partiels)

## Caractéristiques

- **100% des tests passent** (objectif atteint)
- Sans émojis (convention du projet)
- En français
- Sans pytest (tests autonomes)
- Aligné avec MCP DSFR v2.0.0
- DSFR v1.14.1
- Génération de rapports dans `/tests/resultats-test/`
- Nomenclature cohérente : `test-mcp-dsfr-*.py`
- Scripts d'exécution : `install.sh` et `run_tests.sh`

## Architecture

```
tests/
├── test-mcp-dsfr-*.py                   # 11 tests actifs
├── test-mcp-dsfr-blind-spots-DEPRECATED.py # Test déprécié
├── resultats-test/                      # Rapports de tests générés
│   ├── RAPPORT_100_POURCENT.txt        # Rapport final 100%
│   ├── BILAN_FINAL_TESTS.txt           # Bilan détaillé
│   ├── test_registry_report.txt
│   ├── test_generator_report.txt
│   ├── test_mcp_report.txt
│   └── ...                              # Autres rapports
├── html_outputs/                         # Pages HTML générées
│   ├── test_all_components.html
│   ├── test_assistant_output.html
│   └── ...
├── README.md                             # Cette documentation
└── ROADMAP.md                            # Feuille de route des tests
```