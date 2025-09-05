# 🗺️ Roadmap MCP DSFR Clean Code

## 🎯 Objectif
Transformer `/Users/alex/Desktop/mcp-playbook-dsfr` en un serveur MCP exemplaire suivant les principes SOLID, DRY, KISS et YAGNI.

## 📋 Vue d'ensemble

```
mcp-playbook-dsfr/
├── mcp/                      # Core MCP
│   ├── __init__.py
│   ├── server.py            # Point d'entrée MCP
│   └── config.py            # Configuration
├── src/                     # Code source
│   ├── services/            # Logique métier (S de SOLID)
│   ├── generators/          # Factory Pattern (O de SOLID)
│   ├── validators/          # Validation DSFR/RGAA
│   ├── errors/              # Gestion d'erreurs structurée
│   └── plugins/             # Système d'extensions (O de SOLID)
├── gabarits/                # Templates HTML (déjà créés)
├── data/                    # Données statiques
├── tests/                   # Tests unitaires et d'intégration
└── docs/                    # Documentation
```

---

## 🚀 Phase 1: Structure et Architecture (2h)

### Objectifs
- Créer l'architecture modulaire
- Respecter le principe de **Responsabilité Unique** (S)

### Actions
```python
# 1. Créer la structure de base
mcp/
  __init__.py              # Package principal
  server.py               # Serveur MCP avec @server.call()
  config.py               # Configuration centralisée

src/
  __init__.py
  services/
    __init__.py
    generator_service.py  # Service de génération (Factory)
    validator_service.py  # Service de validation
    assistant_service.py  # Service assistant intelligent
  
  errors/
    __init__.py
    base.py              # DSFRError classe de base
    components.py        # Erreurs spécifiques composants
    validation.py        # Erreurs de validation
```

### Principes appliqués
- **S (SOLID)**: Chaque module a une responsabilité unique
- **DRY**: Réutilisation via imports
- **KISS**: Structure simple et claire

---

## 🔄 Phase 2: Migration des Gabarits (1h)

### Objectifs
- Intégrer les 48 composants HTML existants
- Créer un registre de composants

### Actions
```python
# data/components_registry.py
class ComponentRegistry:
    """Registre centralisé des composants DSFR (DRY)"""
    
    _instance = None  # Singleton pattern
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._load_components()
        return cls._instance
    
    def _load_components(self):
        """Charge tous les composants depuis gabarits/"""
        self.components = {}
        # Scanner gabarits/ et charger les HTML
```

### Principes appliqués
- **DRY**: Un seul registre pour tous les composants
- **KISS**: Chargement simple depuis les fichiers existants
- **O (SOLID)**: Extensible pour ajouter de nouveaux composants

---

## 🏭 Phase 3: Services et Générateurs (3h)

### Objectifs
- Implémenter le Factory Pattern
- Créer les services principaux

### Actions
```python
# src/services/generator_service.py
class GeneratorService:
    """Service de génération avec Factory Pattern (O de SOLID)"""
    
    def __init__(self, registry: ComponentRegistry):
        self.registry = registry
        self.generators = self._init_generators()
    
    def _init_generators(self) -> Dict[str, Callable]:
        """Factory pattern - Évite les switch/case"""
        return {
            'button': self._generate_button,
            'form': self._generate_form,
            # ... mapping pour chaque composant
        }
    
    def generate(self, component: str, **kwargs) -> str:
        """Interface publique simple (KISS)"""
        if component not in self.generators:
            raise ComponentNotFoundError(component)
        return self.generators[component](**kwargs)
```

### Principes appliqués
- **O (SOLID)**: Ouvert à l'extension (nouveaux générateurs)
- **D (SOLID)**: Dépend de l'abstraction ComponentRegistry
- **KISS**: API simple: `generate('button', label='OK')`

---

## 🛡️ Phase 4: Système d'Erreurs (1h)

### Objectifs
- Gestion d'erreurs structurée
- Messages clairs et exploitables

### Actions
```python
# src/errors/base.py
class DSFRError(Exception):
    """Classe de base pour toutes les erreurs DSFR"""
    
    def __init__(self, message: str, code: str, details: dict = None):
        super().__init__(message)
        self.code = code
        self.details = details or {}
    
    def to_dict(self) -> dict:
        """Sérialisation pour MCP"""
        return {
            'error': self.code,
            'message': str(self),
            'details': self.details
        }

# src/errors/components.py
class ComponentNotFoundError(DSFRError):
    """Erreur spécifique: composant non trouvé"""
    
    def __init__(self, component: str):
        super().__init__(
            f"Component '{component}' not found",
            'COMPONENT_NOT_FOUND',
            {'component': component}
        )
```

### Principes appliqués
- **S (SOLID)**: Chaque erreur a une responsabilité
- **L (SOLID)**: Sous-classes interchangeables
- **DRY**: Logique commune dans la classe de base

---

## 🔌 Phase 5: Plugins et Extensibilité (2h)

### Objectifs
- Système de plugins pour extensions futures
- Pattern Observer pour les hooks

### Actions
```python
# src/plugins/base.py
from abc import ABC, abstractmethod

class DSFRPlugin(ABC):
    """Interface pour les plugins (I de SOLID)"""
    
    @abstractmethod
    def on_generate(self, component: str, html: str) -> str:
        """Hook appelé après génération"""
        pass
    
    @abstractmethod
    def get_custom_components(self) -> dict:
        """Retourne des composants custom"""
        pass

# src/plugins/manager.py
class PluginManager:
    """Gestionnaire de plugins (Pattern Observer)"""
    
    def __init__(self):
        self.plugins: List[DSFRPlugin] = []
    
    def register(self, plugin: DSFRPlugin):
        """Enregistre un plugin (YAGNI: simple)"""
        self.plugins.append(plugin)
    
    def emit(self, event: str, **kwargs):
        """Émet un événement aux plugins"""
        for plugin in self.plugins:
            getattr(plugin, f'on_{event}', lambda **k: None)(**kwargs)
```

### Principes appliqués
- **I (SOLID)**: Interface ségrégée pour les plugins
- **O (SOLID)**: Extensible sans modifier le core
- **YAGNI**: Système simple, pas over-engineered

---

## ✅ Phase 6: Tests et Validation (2h)

### Objectifs
- Tests unitaires pour chaque service
- Validation RGAA automatisée

### Actions
```python
# tests/test_generator.py
def test_generator_factory_pattern():
    """Test que le factory pattern fonctionne"""
    service = GeneratorService()
    html = service.generate('button', label='Test')
    assert 'fr-btn' in html
    assert 'Test' in html

# src/validators/rgaa_validator.py
class RGAAValidator:
    """Validateur d'accessibilité RGAA"""
    
    def validate(self, html: str) -> ValidationResult:
        """Valide selon les critères RGAA"""
        checks = [
            self._check_aria_labels,
            self._check_alt_texts,
            self._check_heading_hierarchy
        ]
        
        errors = []
        for check in checks:
            errors.extend(check(html))
        
        return ValidationResult(valid=len(errors) == 0, errors=errors)
```

### Principes appliqués
- **S (SOLID)**: Chaque validateur a un rôle
- **DRY**: Logique de validation réutilisable
- **KISS**: Tests simples et clairs

---

## ⚙️ Phase 7: Configuration MCP (1h)

### Objectifs
- Serveur MCP fonctionnel
- Configuration pour Claude Desktop

### Actions
```python
# mcp/server.py
from mcp.server import Server, stdio_server
from mcp.server.models import CallToolRequest, CallToolResult

server = Server("mcp-playbook-dsfr")

@server.call("generate_component")
async def handle_generate(request: CallToolRequest) -> CallToolResult:
    """Génère un composant DSFR"""
    component = request.params.get("component")
    options = request.params.get("options", {})
    
    try:
        html = generator_service.generate(component, **options)
        return CallToolResult(content=[{"text": html}])
    except DSFRError as e:
        return CallToolResult(error=e.to_dict())

# package.json pour npm
{
  "name": "mcp-dsfr-clean",
  "version": "2.0.0",
  "type": "module",
  "bin": {
    "mcp-dsfr": "python3 mcp/server.py"
  }
}
```

### Principes appliqués
- **KISS**: Configuration minimale
- **DRY**: Réutilise les services existants
- **YAGNI**: Seulement les commandes nécessaires

---

## 📚 Phase 8: Documentation (1h)

### Objectifs
- Documentation complète et maintenable
- Exemples d'utilisation

### Actions
```markdown
# docs/API.md
## API MCP DSFR

### generate_component
Génère un composant DSFR

**Paramètres:**
- `component` (string): Nom du composant
- `options` (object): Options du composant

**Exemple:**
```json
{
  "tool": "generate_component",
  "params": {
    "component": "button",
    "options": {
      "label": "Valider",
      "variant": "primary"
    }
  }
}
```
```

### Principes appliqués
- **DRY**: Templates de documentation réutilisables
- **KISS**: Documentation claire et concise
- **S (SOLID)**: Chaque doc a un objectif

---

## 📈 Métriques de Succès

### Clean Code
- ✅ Pas de duplication de code (DRY)
- ✅ Fonctions < 20 lignes (KISS)
- ✅ Classes avec responsabilité unique (S)
- ✅ Zéro code mort (YAGNI)

### Architecture
- ✅ Modules indépendants
- ✅ Factory pattern pour les générateurs
- ✅ Système d'erreurs structuré
- ✅ Plugins pour extensibilité

### Performance
- ✅ Chargement < 100ms
- ✅ Génération < 10ms par composant
- ✅ Mémoire < 50MB

---

## 🚦 Prochaines Étapes

1. **Immédiat**: Créer la structure de base
2. **Court terme**: Migrer les services existants
3. **Moyen terme**: Ajouter les plugins
4. **Long terme**: Intégration Claude Desktop

## 💡 Notes d'Implémentation

- Commencer par le plus simple (KISS)
- Refactorer progressivement (pas de Big Bang)
- Tester chaque phase avant la suivante
- Documenter au fur et à mesure

---

**Temps estimé total**: 12-15 heures
**Priorité**: Structure → Services → MCP → Tests → Plugins