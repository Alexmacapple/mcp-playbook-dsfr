# Exemples d'utilisation API MCP DSFR

## G\u00e9n\u00e9ration de composants

### Bouton simple
```python
# Via Claude Desktop
result = generer_composant(
    component="button",
    variant="primary",
    options={"label": "Valider"}
)
# Output: <button type="button" class="fr-btn">Valider</button>
```

### Formulaire de contact
```python
result = generer_composant(
    component="form",
    variant="contact",
    options={
        "action": "/contact",
        "method": "post"
    }
)
```

### Alerte avec fermeture
```python
result = generer_composant(
    component="alert",
    variant="info",
    options={
        "message": "Votre demande a \u00e9t\u00e9 prise en compte",
        "closable": True
    }
)
```

## Fondamentaux et design

### R\u00e9cup\u00e9rer la grille DSFR
```python
grid = obtenir_fondamentaux(category="grid")
# {
#   "columns": 12,
#   "gutter": "24px",
#   "container_max_width": "1248px",
#   "classes": ["fr-container", "fr-grid-row", "fr-col"]
# }
```

### Classes CSS utilitaires
```python
colors = obtenir_classes_css(type="colors")
# {
#   "type": "colors",
#   "count": 185,
#   "classes": [
#     "fr-background-action-low--green-tilleul-verveine",
#     "fr-text-inverted--error",
#     ...
#   ]
# }
```

## Templates de pages

### Page d'erreur 404
```python
page_404 = obtenir_template_page(
    template_type="error_404"
)
# HTML complet avec header et footer DSFR
```

### Page de connexion
```python
login_page = obtenir_template_page(
    template_type="login",
    title="Connexion - Mon Service"
)
```

### Page personnalis\u00e9e
```python
custom_page = obtenir_template_page(
    template_type="basic",
    title="Ma Page",
    content="<h1>Bienvenue</h1><p>Contenu de ma page</p>"
)
```

## Validation et accessibilit\u00e9

### Valider du HTML
```python
result = valider_html(
    html='<button class="fr-btn">Test</button>'
)
# {
#   "valid": true,
#   "score": 95,
#   "errors": [],
#   "warnings": ["Attribut type manquant sur button"]
# }
```

### Audit RGAA
```python
audit = audit_accessibilite(
    html='<form>...</form>',
    level="AA"
)
# {
#   "level": "AA",
#   "score": 87,
#   "conformity": true,
#   "issues": [...]
# }
```

## Recherche dans la documentation

### Rechercher sur la grille
```python
results = rechercher_documentation(topic="grille")
# {
#   "topic": "grille",
#   "guidelines": [
#     "La grille DSFR utilise 12 colonnes...",
#     "Toujours utiliser fr-container..."
#   ],
#   "foundations": {
#     "grid": {...}
#   },
#   "utilities": ["fr-grid-row", "fr-col-12", ...]
# }
```

## G\u00e9n\u00e9ration de tests

### Tests unitaires pour un bouton
```python
tests = generer_tests(
    component="button",
    test_type="unit"
)
# Code Jest g\u00e9n\u00e9r\u00e9 avec tests de conformit\u00e9 DSFR
```

### Tests E2E pour un formulaire
```python
tests = generer_tests(
    component="form",
    test_type="e2e"
)
# Code Cypress/Playwright pour tester le formulaire
```

## Analyse cognitive

### Analyser une demande utilisateur
```python
analysis = analyser_cognitif(
    description="Je veux cr\u00e9er un formulaire accessible avec validation"
)
# {
#   "known_knowns": ["formulaire", "validation"],
#   "known_unknowns": ["type de validation", "champs requis"],
#   "unknown_unknowns": ["contraintes m\u00e9tier", "int\u00e9gration backend"],
#   "recommendations": [...]
# }
```

## Cas d'usage complets

### Cr\u00e9er une page de connexion compl\u00e8te
```python
# 1. G\u00e9n\u00e9rer le template
page = obtenir_template_page(template_type="login")

# 2. Valider l'accessibilit\u00e9
audit = audit_accessibilite(html=page, level="AA")

# 3. G\u00e9n\u00e9rer les tests
tests = generer_tests(component="form", test_type="e2e")

# 4. V\u00e9rifier la conformit\u00e9
validation = valider_html(html=page)
```

### Construire un dashboard avec composants
```python
# 1. R\u00e9cup\u00e9rer les fondamentaux
grid = obtenir_fondamentaux(category="grid")
colors = obtenir_classes_css(type="colors")

# 2. G\u00e9n\u00e9rer les composants
alert = generer_composant("alert", variant="success")
cards = [generer_composant("card", variant=v) for v in ["basic", "horizontal"]]
table = generer_composant("table", variant="sortable")

# 3. Assembler dans un template
dashboard = obtenir_template_page(
    template_type="basic",
    title="Dashboard",
    content=f'''
        <div class="fr-grid-row">
            <div class="fr-col-12">{alert}</div>
            <div class="fr-col-md-6">{cards[0]}</div>
            <div class="fr-col-md-6">{cards[1]}</div>
            <div class="fr-col-12">{table}</div>
        </div>
    '''
)
```

## Notes d'utilisation

- **Knowledge Base**: 775 variantes de composants disponibles
- **Documentation**: 213 fiches DSFR extraites et accessibles
- **Performance**: R\u00e9ponses < 100ms gr\u00e2ce au cache LRU
- **Conformit\u00e9**: Tous les composants respectent DSFR v1.14.0 et RGAA 4.1
- **Fallback**: Si une variante n'existe pas dans la KB, fallback sur le Registry