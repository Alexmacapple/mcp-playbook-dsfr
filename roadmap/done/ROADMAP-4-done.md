# Roadmap 4 : Atteindre 100% de conformité MCP

## Date : 2025-09-11
## Auteur : Alexandra Guiderdoni
## Objectif : Passer de 92% à 100% de conformité aux standards MCP
## Version actuelle : 2.0.0

---

## AUDIT DÉTAILLÉ DE CONFORMITÉ MCP

### Score global : 92/100

#### Critères respectés (92 points)

| Critère | Points | État | Détails |
|---------|--------|------|---------|
| **1. SDK MCP officiel** | 10/10 | OK | `mcp>=0.1.0` dans requirements.txt |
| **2. Transport stdio** | 10/10 | OK | FastMCP utilise stdio par défaut |
| **3. Tools implémentés** | 15/15 | OK | 8 outils documentés et fonctionnels |
| **4. Documentation README** | 10/10 | OK | README complet avec badges, installation, usage |
| **5. Tests** | 8/8 | OK | 13 tests fonctionnels, 100% passent |
| **6. Packaging Python** | 8/8 | OK | pyproject.toml + requirements.txt |
| **7. CI/CD** | 5/5 | OK | GitHub Actions multi-versions (3.9-3.12) |
| **8. Architecture Clean Code** | 8/8 | OK | SOLID, DRY, KISS, YAGNI appliqués |
| **9. Gestion erreurs** | 5/5 | OK | Hiérarchie DSFRError personnalisée |
| **10. Validation entrées** | 5/5 | OK | Sanitization HTML avec bleach |
| **11. Performance** | 3/3 | OK | >1.5M ops/sec mesuré |
| **12. Logging** | 3/3 | OK | Système de logs configurable |
| **13. CONTRIBUTING.md** | 2/2 | OK | Guide complet pour contributeurs |

#### Critères manquants (8 points)

| Critère | Points perdus | État | Action requise |
|---------|---------------|------|----------------|
| **14. Resources MCP** | -4 | NON | Implémenter @app.resource() pour accès gabarits |
| **15. Prompts MCP** | -3 | NON | Ajouter @app.prompt() pour cas d'usage courants |
| **16. SECURITY.md** | -1 | NON | Créer politique de sécurité |

### Analyse par catégorie

#### Infrastructure (30/30) - Complet
- OK : SDK MCP Python officiel
- OK : FastMCP comme framework
- OK : Transport stdio standard
- OK : Gestion erreurs robuste

#### Fonctionnalités (15/22) - Partiel
- OK : Tools : 8/8 implémentés
- MANQUANT : Resources : 0/3 manquantes (-4 points)
- MANQUANT : Prompts : 0/5 manquants (-3 points)

#### Documentation (27/28) - Partiel
- OK : README.md complet
- OK : CHANGELOG.md à jour
- OK : CONTRIBUTING.md détaillé
- OK : CLAUDE.md pour l'IA
- MANQUANT : SECURITY.md absent (-1 point)

#### Qualité (20/20) - Complet
- OK : Tests : 100% passent
- OK : CI/CD : GitHub Actions
- OK : Clean Code : SOLID appliqué
- OK : Performance optimisée

### Progression nécessaire

```
Actuel  : [====================  ] 92%
Objectif: [======================] 100%
Écart   : 8 points à gagner
```

---

## Objectif : 100% de conformité

### Métriques cibles

- **Score final** : 100/100
- **Primitives MCP** : 3/3 (Tools OK, Resources OK, Prompts OK)
- **Documentation sécurité** : Complète
- **Conformité totale** : Serveur MCP de référence

---

## Risques et mitigations

### Risques identifiés

| Risque | Probabilité | Impact | Mitigation |
|--------|-------------|---------|------------|
| **Compatibilité FastMCP** | Élevée | Majeur | Plan B : implémenter via Tools standards |
| **Performance Resources** | Moyenne | Moyen | Cache + pagination des gabarits |
| **Syntaxe decorateurs** | Élevée | Majeur | Adapter selon API FastMCP réelle |
| **Charge 137 gabarits** | Faible | Mineur | Lazy loading + optimisation mémoire |

### Plan B : Si FastMCP ne supporte pas @resource/@prompt

**Alternative 1 : Via Tools standards**
```python
@app.tool()
def get_resource_gabarit(component: str, variant: str = "default") -> str:
    """Tool alternatif pour accéder aux gabarits si Resources non supportées."""
    # Même logique que @app.resource mais via @app.tool
    return get_gabarit_content(component, variant)

@app.tool()
def get_prompt_template(prompt_name: str) -> str:
    """Tool alternatif pour les prompts si Prompts non supportés."""
    prompts = {
        "formulaire_accessible": {...},
        "tableau_responsive": {...}
    }
    return json.dumps(prompts.get(prompt_name))
```

**Alternative 2 : Extension FastMCP**
- Forker FastMCP et ajouter le support Resources/Prompts
- Contribuer au projet upstream
- Utiliser une version patchée temporairement

### Estimation impact performance

| Métrique | Actuel | Avec Resources | Impact |
|----------|---------|----------------|--------|
| Mémoire serveur | ~50 MB | ~80 MB | +60% |
| Temps démarrage | <1s | ~1.5s | +50% |
| Latence requete | <10ms | <15ms | +50% |
| Throughput | >1.5M ops/s | >1M ops/s | -33% |

**Optimisations prévues :**
- Cache LRU pour gabarits fréquents
- Chargement lazy des gabarits
- Compression gzip des réponses
- Index en mémoire des métadonnées

---

## Dépendances requises

### Versions minimales

| Package | Version actuelle | Version requise | Changement nécessaire |
|---------|------------------|-----------------|------------------------|
| mcp | >=0.1.0 | >=0.1.0 | Non |
| FastMCP | Non spécifié | >=1.0.0 | À vérifier/installer |
| Python | 3.9+ | 3.9+ | Non |
| pathlib | Built-in | Built-in | Non |

### Vérification compatibilité

```bash
# Vérifier version FastMCP
python3 -c "import mcp; print(mcp.__version__)"

# Vérifier support decorateurs
python3 -c "
import inspect
from mcp.server import FastMCP
print('resource' in dir(FastMCP))  # Doit retourner True
print('prompt' in dir(FastMCP))    # Doit retourner True
"
```

---

## Actions à réaliser

### 1. Implémenter les Resources MCP (Gain : +4%)

#### Contexte
Les 137 gabarits HTML organisés en dossiers dans `/gabarits/` ne sont pas exposés via le protocole MCP. Les Resources permettraient aux clients MCP d'accéder directement aux templates.

#### Implementation dans `mcp_local/server.py`

```python
from pathlib import Path

@app.resource("gabarit://{component}/{variant}")
async def get_gabarit(component: str, variant: str = "default") -> str:
    """
    Récupère le gabarit HTML d'un composant DSFR.
    
    Args:
        component: Nom du composant (button, alert, form, etc.)
        variant: Variante du composant (default, primary, secondary, etc.)
    
    Returns:
        Contenu HTML du gabarit
    """
    try:
        # Chercher d'abord avec variante
        gabarit_dir = Path(__file__).parent.parent / "gabarits" / component
        gabarit_path = gabarit_dir / f"{variant}.html"
        
        # Si pas trouvé, chercher default.html ou {component}.html
        if not gabarit_path.exists():
            gabarit_path = gabarit_dir / "default.html"
        if not gabarit_path.exists():
            gabarit_path = gabarit_dir / f"{component}.html"
            
        if gabarit_path.exists():
            with open(gabarit_path, 'r', encoding='utf-8') as f:
                content = f.read()
            return json.dumps({
                "component": component,
                "variant": variant,
                "content": content,
                "path": str(gabarit_path)
            })
        return json.dumps({
            "error": f"Gabarit {component}/{variant} non trouvé",
            "available": registry.list_components()
        })
    except Exception as e:
        return json.dumps({"error": str(e)})

@app.resource("list://gabarits")
async def list_gabarits() -> str:
    """
    Liste tous les gabarits HTML disponibles.
    
    Returns:
        JSON avec la liste des gabarits et métadonnées
    """
    gabarits_dir = Path(__file__).parent.parent / "gabarits"
    gabarits = []
    
    # Parcourir récursivement tous les fichiers HTML
    for f in gabarits_dir.glob("**/*.html"):
        stat = f.stat()
        # Extraire le chemin relatif component/variant
        rel_path = f.relative_to(gabarits_dir)
        component = rel_path.parts[0] if len(rel_path.parts) > 1 else "index"
        variant = f.stem
        
        gabarits.append({
            "component": component,
            "variant": variant,
            "file": str(rel_path),
            "size": stat.st_size,
            "modified": stat.st_mtime
        })
    
    return json.dumps({
        "gabarits": sorted(gabarits, key=lambda x: (x["component"], x["variant"])),
        "count": len(gabarits),
        "total_size": sum(g["size"] for g in gabarits),
        "components": list(set(g["component"] for g in gabarits))
    })

@app.resource("metadata://component/{component}")
async def get_component_metadata(component: str) -> str:
    """
    Récupère les métadonnées d'un composant depuis le registry.
    
    Args:
        component: Nom du composant
        
    Returns:
        JSON avec métadonnées complètes
    """
    try:
        metadata = registry.get_component(component)
        if metadata:
            return json.dumps(metadata)
        return json.dumps({"error": f"Composant {component} non trouvé"})
    except Exception as e:
        return json.dumps({"error": str(e)})
```

### Exemples d'usage des Resources

#### Client MCP utilisant les Resources

```python
# Client Python accédant aux gabarits
import mcp_client

client = mcp_client.connect("mcp-playbook-dsfr")

# Récupérer un gabarit spécifique
button_html = client.get_resource("gabarit://button/primary")
print(button_html['content'])

# Lister tous les gabarits
all_gabarits = client.get_resource("list://gabarits")
print(f"Total: {all_gabarits['count']} gabarits")
for g in all_gabarits['gabarits'][:5]:
    print(f"- {g['component']}/{g['variant']} ({g['size']} bytes)")

# Récupérer métadonnées
meta = client.get_resource("metadata://component/alert")
print(f"Variantes alert: {meta['variants']}")
```

#### Intégration Claude Desktop

```typescript
// Claude Desktop accédant aux resources
const resources = await mcp.listResources();
// Affichage dans l'UI : "137 gabarits DSFR disponibles"

const buttonTemplate = await mcp.getResource("gabarit://button/primary");
// Utilisation directe du HTML dans la génération
```

### 2. Ajouter les Prompts MCP prédéfinis (Gain : +3%)

#### Contexte
Les Prompts permettent de proposer des templates de demandes prédéfinies pour les cas d'usage courants.

#### Implementation dans `mcp_local/server.py`

```python
@app.prompt("formulaire_accessible")
async def prompt_formulaire_accessible() -> str:
    """Prompt pour créer un formulaire DSFR accessible niveau AA."""
    return {
        "name": "Formulaire accessible DSFR",
        "description": "Génère un formulaire conforme RGAA niveau AA",
        "prompt": """Crée un formulaire DSFR accessible avec :
        
        Accessibilité (RGAA 4.1 niveau AA) :
        - Labels associés à chaque champ via attribut 'for'
        - Messages d'erreur avec role="alert" et aria-live="polite"
        - Champs obligatoires avec aria-required="true" et astérisque (*)
        - Instructions en début de formulaire : "Les champs marqués * sont obligatoires"
        - Structure fieldset/legend pour les groupes de champs liés
        - Ordre de tabulation logique (pas de tabindex > 0)
        
        Classes DSFR à utiliser :
        - fr-input-group : conteneur de champ
        - fr-label : pour les labels
        - fr-input : pour les champs de saisie
        - fr-error-text : messages d'erreur
        - fr-valid-text : messages de succès
        - fr-btn : boutons d'action
        
        Validation :
        - Côté client avec HTML5 (required, pattern, type)
        - Messages d'erreur explicites et contextuels
        - Indication visuelle des champs valides/invalides"""
    }

@app.prompt("tableau_responsive")
async def prompt_tableau_responsive() -> str:
    """Prompt pour créer un tableau DSFR responsive et accessible."""
    return {
        "name": "Tableau responsive DSFR",
        "description": "Génère un tableau accessible et adaptatif",
        "prompt": """Crée un tableau DSFR responsive avec :
        
        Structure accessible :
        - Balise <caption> descriptive du contenu
        - En-têtes de colonnes avec <th scope="col">
        - En-têtes de lignes avec <th scope="row"> si applicable
        - Attribut summary pour décrire l'organisation (déprécié mais utile)
        
        Classes DSFR :
        - fr-table : classe de base
        - fr-table--responsive : adaptation mobile
        - fr-table--bordered : bordures visibles
        - fr-table--no-scroll : désactiver le scroll horizontal
        
        Fonctionnalités :
        - Tri sur colonnes (attributs data-sort)
        - Pagination si > 50 lignes
        - Export CSV/Excel si données importantes
        - Filtre/recherche si > 20 lignes
        
        Mobile :
        - Transformation en cards sur petits écrans
        - Priorité aux colonnes essentielles
        - Scroll horizontal comme fallback"""
    }

@app.prompt("page_complete")
async def prompt_page_complete() -> str:
    """Prompt pour créer une page DSFR complète."""
    return {
        "name": "Page complète DSFR",
        "description": "Génère une page avec tous les éléments obligatoires",
        "prompt": """Crée une page DSFR complète avec :
        
        Header (obligatoire) :
        - Logo République Française
        - Nom du service
        - Navigation principale
        - Recherche
        - Accès direct (connexion, langues)
        
        Navigation :
        - Fil d'Ariane (breadcrumb)
        - Navigation latérale si nécessaire
        - Navigation mobile (burger menu)
        
        Contenu principal :
        - Titre h1 unique et descriptif
        - Structure de titres logique (h1 > h2 > h3)
        - Zones ARIA (main, nav, aside)
        - Skip links ("Aller au contenu", "Aller au menu")
        
        Footer (obligatoire) :
        - Liens obligatoires : Accessibilité, Mentions légales, Données personnelles
        - Plan du site
        - Contact
        - Réseaux sociaux si applicable
        
        Accessibilité RGAA AA :
        - Lang="fr" sur <html>
        - Meta viewport pour mobile
        - Contraste suffisant (4.5:1 minimum)
        - Focus visible
        - Alternative textuelle pour les images"""
    }

@app.prompt("composant_carte")
async def prompt_composant_carte() -> str:
    """Prompt pour créer une carte DSFR."""
    return {
        "name": "Carte DSFR",
        "description": "Génère une carte (card) avec image et contenu",
        "prompt": """Crée une carte DSFR avec :
        
        Structure :
        - Image (optionnelle) avec alt descriptif
        - Titre cliquable (lien principal)
        - Description courte
        - Métadonnées (date, auteur, catégorie)
        - Actions (lire plus, partager)
        
        Classes DSFR :
        - fr-card : conteneur principal
        - fr-card__img : image
        - fr-card__body : contenu
        - fr-card__title : titre
        - fr-card__desc : description
        - fr-card__detail : métadonnées
        
        Variantes :
        - Horizontale : fr-card--horizontal
        - Sans image : pas de fr-card__img
        - Mise en avant : fr-card--lg
        
        Accessibilité :
        - Un seul lien principal par carte
        - Titre descriptif et unique
        - Image décorative ou avec alt pertinent"""
    }

@app.prompt("navigation_complexe")
async def prompt_navigation_complexe() -> str:
    """Prompt pour créer une navigation complexe DSFR."""
    return {
        "name": "Navigation complexe DSFR",
        "description": "Génère un système de navigation multi-niveaux",
        "prompt": """Crée une navigation DSFR complexe avec :
        
        Types de navigation :
        - Menu principal (fr-nav)
        - Mega menu pour catégories larges
        - Navigation latérale (fr-sidemenu)
        - Fil d'Ariane (fr-breadcrumb)
        - Pagination (fr-pagination)
        
        Accessibilité navigation :
        - Attributs ARIA : aria-current, aria-expanded
        - Navigation au clavier (Tab, Entrée, Échap)
        - Indicateur visuel de position
        - Menu burger pour mobile
        
        Structure mega menu :
        - Catégories principales
        - Sous-catégories en colonnes
        - Liens directs mis en avant
        - Zone de contenu éditorial
        
        Mobile first :
        - Menu burger avec overlay
        - Navigation en accordéon
        - Retour haptique sur touch
        - Zone de tap 44x44px minimum"""
    }
```

### Exemples d'usage des Prompts

#### Cas d'usage formulaire accessible

```python
# Utilisateur sélectionne le prompt dans Claude
prompt = client.get_prompt("formulaire_accessible")

# Claude génère automatiquement :
"""
<form class="fr-form">
  <p class="fr-hint-text">Les champs marqués * sont obligatoires</p>
  
  <div class="fr-input-group">
    <label class="fr-label" for="email">
      Email *
    </label>
    <input class="fr-input" type="email" id="email" 
           required aria-required="true">
    <p class="fr-error-text" role="alert" aria-live="polite">
      Veuillez saisir une adresse email valide
    </p>
  </div>
  
  <button class="fr-btn" type="submit">
    Valider
  </button>
</form>
"""
```

#### Cas d'usage navigation complexe

```python
# Sélection prompt navigation
prompt = client.get_prompt("navigation_complexe")

# Génération automatique mega menu
result = generate_from_prompt(prompt, {
    "categories": ["Services", "Documentation", "Support"],
    "mobile_first": true
})
```

### 3. Créer SECURITY.md (Gain : +1%)

#### Fichier : `/Users/alex/Desktop/mcp-playbook-dsfr/SECURITY.md`

```markdown
# Politique de sécurité

## Engagement sécurité

MCP Playbook DSFR s'engage à maintenir un niveau de sécurité élevé pour protéger les utilisateurs et leurs données.

## Versions supportées

| Version | Statut | Support sécurité | Fin de support |
|---------|--------|------------------|----------------|
| 2.0.x   | Actuelle | Actif | - |
| 1.x.x   | Obsolète | Critique uniquement | 2025-06-01 |
| < 1.0   | Non supportée | Aucun | Terminé |

## Signaler une vulnérabilité

### Process de signalement

Pour signaler une vulnérabilité de sécurité :

1. **NE PAS créer d'issue publique GitHub**
2. **Envoyer un email privé à** : alexandra.guiderdoni@gmail.com
3. **Sujet de l'email** : `[SECURITY] MCP DSFR - [Description courte]`

### Informations à fournir

Votre rapport doit inclure :

- **Description détaillée** de la vulnérabilité
- **Étapes pour reproduire** le problème
- **Version affectée** du serveur MCP
- **Impact potentiel** (exécution de code, fuite de données, déni de service, etc.)
- **Preuve de concept** (code ou commandes, si applicable)
- **Solution suggérée** ou mitigation temporaire
- **Votre contact** pour le suivi

### Délais de réponse

| Étape | Délai |
|-------|-------|
| Accusé de réception | 48 heures |
| Évaluation initiale | 7 jours |
| Plan de correction | 14 jours |
| Correctif publié | 30 jours* |
| Divulgation publique | 90 jours** |

*Selon la gravité et la complexité
**Ou après publication du correctif

## Pratiques de sécurité actuelles

### Validation et sanitization

- **HTML** : Sanitization via `bleach` pour prévenir XSS
- **Entrées utilisateur** : Validation stricte des paramètres
- **Templates** : Échappement automatique des variables

### Architecture sécurisée

- **Pas d'exécution de code arbitraire**
- **Pas de commandes système directes**
- **Isolation des services** (pattern SOLID)
- **Permissions minimales** requises

### Dépendances

- **Audit régulier** des dépendances
- **Versions minimales** spécifiées dans requirements.txt
- **7 dépendances seulement** en production

### Données

- **Aucun stockage persistant** de données utilisateur
- **Pas de cookies** ou tracking
- **Pas de données sensibles** en logs
- **Configuration locale** uniquement (.env ignoré par git)

## Hall of Fame

Nous remercions les chercheurs en sécurité qui ont contribué à améliorer MCP DSFR :

| Date | Contributeur | Vulnérabilité | Sévérité |
|------|--------------|---------------|----------|
| - | - | - | - |

## Ressources sécurité

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [CWE/SANS Top 25](https://cwe.mitre.org/top25/)
- [ANSSI - Guides](https://www.ssi.gouv.fr/guides/)
- [CERT-FR](https://www.cert.ssi.gouv.fr/)

## Checklist sécurité pour contributeurs

Avant de soumettre une PR :

- [ ] Pas de secrets dans le code (clés API, mots de passe)
- [ ] Validation des entrées utilisateur
- [ ] Échappement des sorties HTML
- [ ] Pas de `eval()` ou `exec()`
- [ ] Dépendances à jour
- [ ] Tests de sécurité passés

## Contact

**Email sécurité** : alexandra.guiderdoni@gmail.com
**PGP Key** : [À ajouter si disponible]

---

*Dernière mise à jour : 2025-09-11*
```

---

## Bénéfices attendus

| Amélioration | Impact | Valeur ajoutée |
|--------------|---------|----------------|
| **Resources MCP** | +4% | Accès direct aux 137 gabarits HTML |
| **Prompts MCP** | +3% | 5 prompts prédéfinis pour cas courants |
| **SECURITY.md** | +1% | Transparence et confiance |
| **Score final** | 100% | Serveur MCP de référence |

---

## Métriques de succès

### Avant (92%)
- Tools : 8 (OK)
- Resources : 0 (NON)
- Prompts : 0 (NON)
- Security doc : Non

### Après (100%)
- Tools : 8 (OK)
- Resources : 3+ (OK)
- Prompts : 5+ (OK)
- Security doc : Oui

---

## Ordre d'implémentation

1. **Jours 1-2** : Resources MCP
   - Implémenter les 3 endpoints de resources
   - Adapter pour structure en dossiers (137 fichiers)
   - Tester l'accès aux gabarits
   - Documenter dans README

2. **Jour 3** : Prompts MCP
   - Vérifier syntaxe FastMCP pour prompts
   - Ajouter les 5 prompts prédéfinis
   - Tester chaque prompt
   - Créer exemples d'utilisation

3. **Jour 4** : Documentation sécurité
   - Créer SECURITY.md
   - Mettre à jour README avec badge sécurité
   - Ajouter section sécurité dans CONTRIBUTING.md

4. **Jours 5-6** : Tests et validation
   - Test d'intégration MCP avec nouvelles primitives
   - Vérification compatibilité Claude Desktop
   - Benchmark performance avec Resources
   - Mettre à jour les tests existants
   - Valider la conformité 100%

**Durée totale estimée : 1 semaine**

---

## Checklist de validation

### Resources
- [x] Endpoint `gabarit://{component}/{variant}` fonctionnel
- [x] Endpoint `list://gabarits` retourne les 137 gabarits
- [x] Endpoint `metadata://component/{component}` opérationnel
- [x] Documentation des resources dans README
- [x] Tests unitaires pour resources

### Prompts
- [x] Prompt `formulaire_accessible` implémenté
- [x] Prompt `tableau_responsive` implémenté
- [x] Prompt `page_complete` implémenté
- [x] Prompt `composant_carte` implémenté
- [x] Prompt `navigation_complexe` implémenté
- [x] Documentation des prompts dans README
- [x] Exemples d'utilisation créés

### Sécurité
- [x] SECURITY.md créé et complet
- [x] Process de signalement documenté
- [x] Pratiques de sécurité listées
- [x] Badge sécurité ajouté au README

### Validation finale
- [x] Score de conformité MCP : 100%
- [x] Tous les tests passent
- [x] Documentation à jour
- [x] Test d'intégration MCP avec nouvelles primitives
- [x] Vérification compatibilité Claude Desktop
- [x] Benchmark performance avec Resources
- [x] Roadmap-4 marquée comme terminée

---

## Notes

- Les Resources et Prompts augmentent significativement la valeur du serveur MCP
- SECURITY.md renforce la confiance et la transparence
- Cette roadmap finalise la conformité totale aux standards MCP
- Le projet devient une référence d'implémentation MCP en Python

---

## Résultat attendu

**MCP Playbook DSFR v2.1.0** : Premier serveur MCP français avec 100% de conformité, servant de référence pour l'écosystème MCP francophone.

**Note importante** : La section "Risques et mitigations" détaille le plan B si FastMCP ne supporte pas les décorateurs @app.resource() et @app.prompt(). L'alternative via Tools standards garantit l'implémentation même en cas d'incompatibilité.

---

*Document créé le 2025-09-11 par Alexandra Guiderdoni*
*Projet : MCP Playbook DSFR - Roadmap vers la perfection*