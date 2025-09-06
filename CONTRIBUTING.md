# Guide de contribution

Merci de votre intérêt pour contribuer à MCP DSFR ! Ce document fournit les directives et les meilleures pratiques pour contribuer au projet.

## Table des matières

- [Code de conduite](#code-de-conduite)
- [Comment contribuer](#comment-contribuer)
- [Développement](#développement)
- [Standards de code](#standards-de-code)
- [Tests](#tests)
- [Documentation](#documentation)
- [Process de Pull Request](#process-de-pull-request)
- [Signaler des bugs](#signaler-des-bugs)
- [Suggérer des améliorations](#suggérer-des-améliorations)
- [Questions](#questions)

## Conventions du projet

### Langue et style

- **Langue** : Tout le code, la documentation et les commentaires sont en français
- **Style** : Professionnel et sobre, sans émojis dans le code ou la documentation
- **Ton** : Direct, clair et technique

## Code de conduite

### Notre engagement

Nous nous engageons à faire de la participation à ce projet une expérience sans harcèlement pour tous, indépendamment de l'âge, de la taille, du handicap, de l'ethnicité, de l'identité et de l'expression de genre, du niveau d'expérience, de la nationalité, de l'apparence personnelle, de la race, de la religion ou de l'identité et de l'orientation sexuelles.

### Standards de comportement

Exemples de comportements contribuant à créer un environnement positif :

- Utiliser un langage accueillant et inclusif
- Respecter les différents points de vue et expériences
- Accepter gracieusement les critiques constructives
- Se concentrer sur ce qui est le mieux pour la communauté
- Faire preuve d'empathie envers les autres membres de la communauté

Exemples de comportements inacceptables :

- L'utilisation de langage ou d'images sexualisés et d'attention sexuelle non sollicitée
- Le trolling, les commentaires insultants/désobligeants et les attaques personnelles ou politiques
- Le harcèlement public ou privé
- La publication d'informations privées d'autrui sans permission explicite
- Tout autre comportement qui pourrait raisonnablement être considéré comme inapproprié dans un cadre professionnel

## Comment contribuer

### Prérequis

1. Avoir un compte GitHub
2. Connaître les bases de Git
3. Avoir Python 3.9+ installé
4. Avoir lu la documentation du projet

### Processus de contribution

1. **Fork le repository**
   ```bash
   # Sur GitHub, cliquer sur "Fork"
   git clone https://github.com/votre-username/mcp-playbook-dsfr.git
   cd mcp-playbook-dsfr
   git remote add upstream https://github.com/original/mcp-playbook-dsfr.git
   ```

2. **Vérifier l'installation**
   
   Après avoir suivi les étapes d'installation, vérifiez que :
   - L'environnement virtuel est créé (`venv/` existe)
   - Les dépendances sont installées (`pip list` montre mcp, beautifulsoup4, etc.)
   - Le serveur MCP fonctionne (`python3 -c "from mcp_local.server import app"`)
   - La configuration Claude Desktop est générée par install.sh

3. **Créer une branche**
   ```bash
   git checkout -b feature/ma-fonctionnalite
   # ou
   git checkout -b fix/mon-correctif
   ```

3. **Configurer l'environnement**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   pip install -r requirements-dev.txt  # Outils de développement
   ```

4. **Faire vos modifications**
   - Écrire du code propre et documenté
   - Suivre les standards du projet
   - Ajouter des tests si nécessaire

5. **Tester vos changements**
   ```bash
   # Lancer tous les tests
   pytest tests/
   
   # Vérifier la couverture
   pytest tests/ --cov=src --cov-report=html
   
   # Vérifier le style
   black --check .
   ruff check .
   mypy src/
   ```

6. **Commiter vos changements**
   ```bash
   git add .
   git commit -m "type(scope): description"
   ```

7. **Pousser et créer une Pull Request**
   ```bash
   git push origin feature/ma-fonctionnalite
   # Puis créer une PR sur GitHub
   ```

## Développement

### Structure du projet

```
mcp-playbook-dsfr/
├── mcp_local/         # Serveur MCP
├── src/
│   ├── services/      # Services métier (1 responsabilité par service)
│   ├── data/         # Modèles de données
│   ├── errors/       # Exceptions personnalisées
│   └── utils/        # Utilitaires
├── gabarits/         # Templates HTML
└── tests/            # Tests unitaires et d'intégration
```

### Environnement de développement

```bash
# Installation des dépendances de dev
pip install black ruff mypy pytest pytest-cov

# Variables d'environnement pour dev
export ENV=development
export LOG_LEVEL=DEBUG
export DEBUG=true
```

### Commandes utiles

```bash
# Formatage automatique
black .

# Linting
ruff check . --fix

# Type checking
mypy src/

# Tests avec watch mode
pytest-watch tests/

# Générer rapport de couverture HTML
pytest --cov=src --cov-report=html
open htmlcov/index.html
```

## Standards de code

### Style Python

Nous suivons [PEP 8](https://www.python.org/dev/peps/pep-0008/) avec les outils suivants :

- **Black** : Formatage automatique (ligne max: 88 caractères)
- **Ruff** : Linting rapide
- **MyPy** : Vérification de types

Configuration dans `pyproject.toml` :

```toml
[tool.black]
line-length = 88
target-version = ['py39']

[tool.ruff]
line-length = 88
select = ["E", "F", "I", "N", "W"]

[tool.mypy]
python_version = "3.9"
warn_return_any = true
warn_unused_configs = true
```

### Principes de code

1. **SOLID**
   - Single Responsibility : Une classe/fonction = une responsabilité
   - Open/Closed : Ouvert à l'extension, fermé à la modification
   - Liskov Substitution : Les sous-types doivent être substituables
   - Interface Segregation : Interfaces spécifiques plutôt que générales
   - Dependency Inversion : Dépendre d'abstractions

2. **DRY** (Don't Repeat Yourself)
   - Pas de duplication de code
   - Extraire les fonctions communes

3. **KISS** (Keep It Simple, Stupid)
   - Solutions simples et directes
   - Code lisible et maintenable

4. **YAGNI** (You Ain't Gonna Need It)
   - Ne pas ajouter de fonctionnalités non demandées

### Conventions de nommage

```python
# Classes : PascalCase
class GeneratorService:
    pass

# Fonctions et variables : snake_case
def generate_component(component_type: str) -> str:
    pass

# Constantes : UPPER_SNAKE_CASE
MAX_RETRY_COUNT = 3

# Privé : préfixe underscore
def _internal_method():
    pass
```

### Documentation du code

```python
def generate_component(
    component_type: str,
    variant: str = "default",
    **options: Any
) -> str:
    """
    Génère un composant DSFR.
    
    Args:
        component_type: Type de composant (button, alert, etc.)
        variant: Variante du composant (primary, secondary, etc.)
        **options: Options supplémentaires du composant
        
    Returns:
        HTML du composant généré
        
    Raises:
        ComponentNotFoundError: Si le composant n'existe pas
        InvalidVariantError: Si la variante n'est pas valide
        
    Example:
        >>> generate_component("button", variant="primary", label="Cliquer")
        '<button class="fr-btn fr-btn--primary">Cliquer</button>'
    """
    pass
```

## Tests

### Structure des tests

```
tests/
├── unit/              # Tests unitaires
│   ├── test_generator.py
│   └── test_validator.py
├── integration/       # Tests d'intégration
│   └── test_mcp_integration.py
└── fixtures/          # Données de test
    └── components.json
```

### Écrire des tests

```python
import pytest
from src.services import get_generator

class TestGeneratorService:
    """Tests pour GeneratorService."""
    
    @pytest.fixture
    def generator(self):
        """Fixture pour le service generator."""
        return get_generator()
    
    def test_generate_button_default(self, generator):
        """Test génération bouton par défaut."""
        # Arrange
        component_type = "button"
        
        # Act
        html = generator.generate(component_type)
        
        # Assert
        assert "fr-btn" in html
        assert "<button" in html
    
    @pytest.mark.parametrize("variant,expected_class", [
        ("primary", "fr-btn--primary"),
        ("secondary", "fr-btn--secondary"),
        ("tertiary", "fr-btn--tertiary"),
    ])
    def test_generate_button_variants(self, generator, variant, expected_class):
        """Test génération bouton avec variantes."""
        html = generator.generate("button", variant=variant)
        assert expected_class in html
```

### Couverture de code

Nous visons une couverture de **80% minimum** :

```bash
# Vérifier la couverture
pytest --cov=src --cov-report=term-missing

# Générer rapport HTML
pytest --cov=src --cov-report=html
```

## Documentation

### Documentation du code

- Toutes les fonctions publiques doivent avoir une docstring
- Format Google ou NumPy pour les docstrings
- Exemples d'usage dans les docstrings quand pertinent

### Documentation utilisateur

- Mettre à jour README.md pour les changements majeurs
- Documenter les nouvelles fonctionnalités dans docs/
- Ajouter des exemples d'usage

### Changelog

Maintenir `CHANGELOG.md` à jour :

```markdown
## [2.1.0] - 2024-01-15

### Added
- Nouveau composant X
- Support pour Y

### Changed
- Amélioration de Z

### Fixed
- Correction du bug #123
```

## Process de Pull Request

### Avant de soumettre

- [ ] Le code suit les standards du projet
- [ ] Les tests passent (`pytest tests/`)
- [ ] La couverture est maintenue (>80%)
- [ ] Le code est formaté (`black .`)
- [ ] Le linting passe (`ruff check .`)
- [ ] Les types sont vérifiés (`mypy src/`)
- [ ] La documentation est à jour
- [ ] Le CHANGELOG est mis à jour

### Template de Pull Request

```markdown
## Description
Brève description des changements

## Type de changement
- [ ] Bug fix
- [ ] Nouvelle fonctionnalité
- [ ] Breaking change
- [ ] Documentation

## Tests
- [ ] Tests unitaires ajoutés/modifiés
- [ ] Tests d'intégration ajoutés/modifiés
- [ ] Tests manuels effectués

## Checklist
- [ ] Mon code suit les standards du projet
- [ ] J'ai mis à jour la documentation
- [ ] Mes changements ne cassent pas l'existant
- [ ] J'ai ajouté des tests couvrant mes changements
```

### Review process

1. **Auto-review** : Relisez votre propre code
2. **Tests CI** : Tous les tests doivent passer
3. **Code review** : Au moins 1 approbation requise
4. **Merge** : Squash and merge préféré

## Signaler des bugs

### Avant de signaler

1. Vérifier les [issues existantes](https://github.com/yourusername/mcp-playbook-dsfr/issues)
2. Tester avec la dernière version
3. Collecter les informations nécessaires

### Template de bug report

```markdown
## Description
Description claire du bug

## Reproduction
1. Étape 1
2. Étape 2
3. ...

## Comportement attendu
Ce qui devrait se passer

## Comportement actuel
Ce qui se passe réellement

## Environnement
- OS: [ex: macOS 14.0]
- Python: [ex: 3.11.5]
- Version MCP DSFR: [ex: 2.0.0]
- Claude Desktop: [ex: 1.0.0]

## Logs
```
Coller les logs pertinents
```

## Screenshots
Si applicable
```

## Suggérer des améliorations

### Process

1. Vérifier les [discussions](https://github.com/yourusername/mcp-playbook-dsfr/discussions)
2. Ouvrir une discussion pour les changements majeurs
3. Créer une issue pour les améliorations approuvées

### Template de feature request

```markdown
## Problème
Quel problème cette fonctionnalité résout-elle ?

## Solution proposée
Description de la solution

## Alternatives considérées
Autres solutions possibles

## Contexte supplémentaire
Toute information utile
```

## Questions

### Où poser des questions

1. **Documentation** : Vérifier d'abord la [documentation](docs/)
2. **Discussions GitHub** : Pour les questions générales
3. **Issues** : Pour les problèmes spécifiques
4. **Email** : contact@example.com pour les questions privées

### Comment poser une bonne question

1. Rechercher d'abord si la question existe
2. Fournir le contexte complet
3. Inclure les versions utilisées
4. Montrer ce que vous avez déjà essayé
5. Être clair et concis

## Reconnaissance

Les contributeurs sont listés dans [AUTHORS.md](AUTHORS.md) et dans la section Contributors de GitHub.

Merci de contribuer à rendre le DSFR plus accessible via Claude Desktop !

---

Pour toute question sur ce guide, ouvrez une [discussion](https://github.com/yourusername/mcp-playbook-dsfr/discussions).