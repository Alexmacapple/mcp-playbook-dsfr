# Plan de conformité MCP - Corrections des écarts ✅ TERMINÉ

## 📅 Date : 2025-09-11
## 👤 Auteur : Alexandra Guiderdoni
## 🎯 Objectif : Atteindre 100% de conformité aux standards MCP
## ✅ Statut : COMPLÉTÉ LE 2025-01-11

---

## 📋 Informations du projet

| Champ | Valeur |
|-------|--------|
| **Nom** | mcp-playbook-dsfr |
| **Version** | 2.0.0 |
| **Auteur** | Alexandra Guiderdoni |
| **Email** | alexandra.guiderdoni@gmail.com |
| **GitHub** | https://github.com/Alexmacapple/mcp-playbook-dsfr |
| **Type** | Projet personnel (non open source) |
| **Python** | >=3.9 |

---

## 🔍 Analyse des écarts actuels

### ✅ Points conformes (déjà en place)
- Protocole MCP avec SDK Python officiel
- 8 outils exposés via `@app.tool()`
- Transport stdio standard
- Documentation complète (README, CHANGELOG, CONTRIBUTING)
- Structure claire server/services/data
- Gestion d'erreurs avec exceptions personnalisées
- Tests fonctionnels (13 tests via run_tests.sh)

### ⚠️ Écarts identifiés
1. **Pas de LICENSE** → Non nécessaire (projet non open source)
2. **Pas de pyproject.toml** → À créer pour moderniser le packaging
3. **Pas de CI/CD automatisé** → À ajouter via GitHub Actions
4. **Placeholders dans la documentation** → À corriger
5. **Branche master** → À renommer en main (standard moderne)

---

## 📝 Actions à réaliser

### 0️⃣ Prérequis : Migration vers la branche main (Priorité : IMMÉDIATE)

Renommer la branche master en main pour suivre les standards Git modernes :

```bash
# Renommer localement
git branch -m master main

# Pousser la nouvelle branche
git push -u origin main

# Sur GitHub : Settings → Default branch → Changer de master à main

# Supprimer l'ancienne branche distante (après changement sur GitHub)
git push origin --delete master
```

### 1️⃣ Créer `pyproject.toml` (Priorité : HAUTE)

**Fichier** : `/Users/alex/Desktop/mcp-playbook-dsfr/pyproject.toml`

```toml
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "mcp-playbook-dsfr"
version = "2.0.0"
description = "Serveur Model Context Protocol intégrant le Design System de l'État français dans Claude Desktop"
readme = "README.md"
requires-python = ">=3.9"
authors = [
    {name = "Alexandra Guiderdoni", email = "alexandra.guiderdoni@gmail.com"}
]
maintainers = [
    {name = "Alexandra Guiderdoni", email = "alexandra.guiderdoni@gmail.com"}
]
keywords = ["mcp", "dsfr", "claude", "design-system", "france", "accessibility", "rgaa"]
classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
]

dependencies = [
    "mcp>=0.1.0",
    "beautifulsoup4>=4.12.0",
    "lxml>=4.9.0",
    "bleach>=6.0.0",
    "typing-extensions>=4.0.0",
    "python-dotenv>=1.0.0",
    "requests>=2.31.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "pytest-asyncio>=0.21.0",
    "pytest-cov>=4.0.0",
    "pytest-mock>=3.10.0",
    "black>=22.0.0",
    "mypy>=0.950",
    "ruff>=0.1.0",
]

[project.urls]
"Homepage" = "https://github.com/Alexmacapple/mcp-playbook-dsfr"
"Bug Reports" = "https://github.com/Alexmacapple/mcp-playbook-dsfr/issues"
"Source" = "https://github.com/Alexmacapple/mcp-playbook-dsfr"

[tool.setuptools.packages.find]
where = ["."]
include = ["mcp_local*", "src*", "gabarits*"]
exclude = ["tests*", "docs*", "archive*"]

[tool.black]
line-length = 88
target-version = ['py39']
include = '\.pyi?$'
extend-exclude = '''
/(
    \.git
  | \.venv
  | venv
  | build
  | dist
)/
'''

[tool.ruff]
line-length = 88
select = ["E", "F", "I", "N", "W"]
ignore = ["E501"]  # Line too long - handled by black
exclude = [
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    "build",
    "dist",
]

[tool.mypy]
python_version = "3.9"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = false
ignore_missing_imports = true
exclude = [
    "venv",
    ".venv",
    "tests",
]

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py", "*_test.py", "test-*.py"]
addopts = "-v --tb=short"
```

### 2️⃣ Créer GitHub Actions CI/CD (Priorité : HAUTE)

**Fichier** : `/Users/alex/Desktop/mcp-playbook-dsfr/.github/workflows/test.yml`

```yaml
name: Tests CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix:
        python-version: ["3.9", "3.10", "3.11", "3.12"]

    steps:
    - uses: actions/checkout@v4
    
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v5
      with:
        python-version: ${{ matrix.python-version }}
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install -r requirements-dev.txt
    
    - name: Format check with Black
      run: |
        black --check src/ mcp_local/
    
    - name: Lint with Ruff
      run: |
        ruff check src/ mcp_local/
    
    - name: Type check with MyPy
      run: |
        mypy src/ mcp_local/
    
    - name: Run tests
      run: |
        chmod +x run_tests.sh
        ./run_tests.sh
    
    - name: Generate coverage report
      if: matrix.python-version == '3.11'
      run: |
        pytest tests/ --cov=src --cov-report=xml --cov-report=html
    
    - name: Upload coverage to Codecov
      if: matrix.python-version == '3.11'
      uses: codecov/codecov-action@v3
      with:
        file: ./coverage.xml
        flags: unittests
        name: codecov-umbrella
        fail_ci_if_error: false
```

### 3️⃣ Mettre à jour la documentation (Priorité : MOYENNE)

#### Modifications dans `CONTRIBUTING.md`

**Ligne 65** : Remplacer
```markdown
git clone https://github.com/votre-username/mcp-playbook-dsfr.git
```
Par :
```markdown
git clone https://github.com/Alexmacapple/mcp-playbook-dsfr.git
```

**Ligne 67** : Remplacer
```markdown
git remote add upstream https://github.com/original/mcp-playbook-dsfr.git
```
Par :
```markdown
git remote add upstream https://github.com/Alexmacapple/mcp-playbook-dsfr.git
```

**Ligne 517** : Remplacer
```markdown
4. **Email** : contact@example.com pour les questions privées
```
Par :
```markdown
4. **Email** : alexandra.guiderdoni@gmail.com pour les questions privées
```

#### Modifications dans `README.md`

**Ligne 3** : Remplacer
```markdown
[![Version](https://img.shields.io/badge/version-2.0.0-blue)](https://github.com/yourusername/mcp-playbook-dsfr/releases)
```
Par :
```markdown
[![Version](https://img.shields.io/badge/version-2.0.0-blue)](https://github.com/Alexmacapple/mcp-playbook-dsfr/releases)
```

**Ajouter après la ligne 7** :
```markdown
[![Tests CI](https://github.com/Alexmacapple/mcp-playbook-dsfr/workflows/Tests%20CI/badge.svg)](https://github.com/Alexmacapple/mcp-playbook-dsfr/actions)
```

**Ligne 37** : Remplacer
```markdown
git clone https://github.com/yourusername/mcp-playbook-dsfr.git
```
Par :
```markdown
git clone https://github.com/Alexmacapple/mcp-playbook-dsfr.git
```

**Ligne 62** : Remplacer
```markdown
git clone https://github.com/yourusername/mcp-playbook-dsfr.git
```
Par :
```markdown
git clone https://github.com/Alexmacapple/mcp-playbook-dsfr.git
```

**Lignes 351-353** : Remplacer toutes les occurrences de `yourusername` par `Alexmacapple`
```markdown
- [Issues GitHub](https://github.com/Alexmacapple/mcp-playbook-dsfr/issues)
- [Discussions](https://github.com/Alexmacapple/mcp-playbook-dsfr/discussions)
- [Wiki](https://github.com/Alexmacapple/mcp-playbook-dsfr/wiki)
```

---

## 🎯 Bénéfices attendus

| Amélioration | Impact |
|--------------|--------|
| **pyproject.toml** | Packaging moderne Python (PEP 517/621), prêt pour PyPI |
| **GitHub Actions** | Tests automatiques sur chaque commit, badges de statut |
| **Documentation à jour** | Informations de contact correctes, URLs valides |
| **Installation simplifiée** | `pip install .` fonctionnel |
| **Conformité MCP** | 100% des standards respectés |

---

## 📊 Métriques de succès

- [x] pyproject.toml créé et fonctionnel
- [x] Installation via `pip install .` réussie
- [x] GitHub Actions configuré et tests passants
- [x] Badge CI vert dans README
- [x] Tous les placeholders remplacés dans la documentation
- [x] Black, Ruff et MyPy passent sans erreurs

---

## 🚀 Ordre d'implémentation

1. **Prérequis** : Renommer la branche master → main
2. **Immédiat** : Créer pyproject.toml
3. **Immédiat** : Mettre à jour CONTRIBUTING.md et README.md (toutes les occurrences)
4. **Court terme** : Créer workflow GitHub Actions
5. **Validation** : Tester l'installation complète sur environnement vierge

---

## 📝 Notes

- Pas de LICENSE nécessaire (projet personnel non open source)
- Les requirements.txt restent pour compatibilité
- GitHub Actions est gratuit pour les repos publics et privés
- La configuration proposée est compatible avec une future publication PyPI

---

## ✅ Checklist de validation

- [x] Branche main configurée comme branche par défaut
- [x] pyproject.toml présent à la racine
- [x] `pip install -e .` fonctionne en développement
- [x] `pip install .` fonctionne en production
- [x] Tests passent sur Python 3.9, 3.10, 3.11, 3.12
- [x] Black formatage OK
- [x] Ruff linting OK
- [x] MyPy types OK
- [x] Badge CI affiché dans README
- [x] Emails et URLs corrects dans la documentation

---

*Document créé le 2025-09-11 par Alexandra Guiderdoni*
*Projet : MCP Playbook DSFR v2.0.0*