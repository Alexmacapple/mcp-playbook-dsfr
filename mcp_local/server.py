#!/usr/bin/env python3
"""
Serveur MCP DSFR - Version FastMCP simplifiée
"""

import sys
from pathlib import Path
import json

# Ajouter le chemin parent
sys.path.insert(0, str(Path(__file__).parent.parent))

from mcp.server import FastMCP
from mcp.types import TextContent

from src.services import (
    get_generator, get_validator, get_assistant,
    get_cognitive_service, get_design_service,
    get_audit_service, get_test_generator
)
from src.services.template_service import get_template_service
from src.data import get_registry
from src.errors.base import DSFRError

# Créer le serveur FastMCP
app = FastMCP("mcp-playbook-dsfr")

# Services
generator = get_generator()
validator = get_validator()
assistant = get_assistant()
cognitive = get_cognitive_service()
design = get_design_service()
audit = get_audit_service()
test_gen = get_test_generator()
template = get_template_service()
registry = get_registry()


@app.tool()
def generer_composant(component: str, variant: str = None, options: dict = None) -> str:
    """
    Génère un composant DSFR.
    
    Args:
        component: Nom du composant (button, alert, form, etc.)
        variant: Variante du composant (optionnel)
        options: Options du composant (label, icon, etc.)
    
    Returns:
        HTML du composant DSFR généré
    """
    try:
        if options is None:
            options = {}
        
        # Si variant est fourni, l'ajouter aux options
        if variant:
            options["variant"] = variant
        
        html = generator.generate(component, **options)
        return html
    except DSFRError as e:
        return f"Erreur DSFR: {e.message}\nCode: {e.code}\nDétails: {json.dumps(e.details)}"
    except Exception as e:
        return f"Erreur: {str(e)}"


@app.tool()
def lister_composants() -> str:
    """
    Liste tous les composants DSFR disponibles.
    
    Returns:
        JSON avec la liste des composants et leurs catégories
    """
    try:
        components = registry.list_components()
        result = {
            "components": components,
            "count": len(components),
            "categories": {
                "navigation": ["header", "footer", "breadcrumb", "navigation", "sidemenu"],
                "forms": ["form", "input", "select", "checkbox", "radio", "toggle"],
                "content": ["accordion", "alert", "badge", "button", "card", "table"],
                "feedback": ["modal", "notice", "callout", "highlight"],
                "layout": ["grid", "container", "tile", "tabs"]
            }
        }
        return json.dumps(result, indent=2, ensure_ascii=False)
    except Exception as e:
        return f"Erreur: {str(e)}"


@app.tool()
def valider_html(html: str) -> str:
    """
    Valide du HTML selon les standards DSFR et RGAA.
    
    Args:
        html: HTML à valider
    
    Returns:
        JSON avec les résultats de validation
    """
    try:
        validation_result = validator.validate(html)
        return json.dumps(validation_result, indent=2, ensure_ascii=False)
    except Exception as e:
        return f"Erreur: {str(e)}"


@app.tool()
def audit_accessibilite(html: str, level: str = "AA") -> str:
    """
    Effectue un audit d'accessibilité RGAA.
    
    Args:
        html: HTML à auditer
        level: Niveau RGAA (A, AA, AAA)
    
    Returns:
        JSON avec les résultats de l'audit
    """
    try:
        # Convertir le niveau string en enum RGAALevel
        from src.services.audit_service import RGAALevel
        rgaa_level = RGAALevel[level.upper()] if level.upper() in ['A', 'AA', 'AAA'] else RGAALevel.AA
        
        # Appeler audit() au lieu de analyze()
        audit_result = audit.audit(html, level=rgaa_level)
        
        # Convertir le rapport en dictionnaire
        result = {
            "scores": {
                "A": audit_result.score_a,
                "AA": audit_result.score_aa,
                "AAA": audit_result.score_aaa
            },
            "total_issues": audit_result.total_issues,
            "critical_issues": audit_result.critical_issues,
            "issues": [
                {
                    "criterion": issue.criterion.value,
                    "level": issue.level.value,
                    "impact": issue.impact,
                    "issue": issue.issue,
                    "suggestion": issue.suggestion,
                    "element": issue.element[:100]
                }
                for issue in audit_result.issues[:10]  # Limiter à 10 pour la lisibilité
            ],
            "recommendations": audit_result.recommendations
        }
        
        return json.dumps(result, indent=2, ensure_ascii=False)
    except Exception as e:
        return f"Erreur d'audit: {str(e)}"


@app.tool()
def analyser_cognitif(description: str) -> str:
    """
    Analyse cognitive selon la matrice de Rumsfeld.
    
    Args:
        description: Description du contexte à analyser
    
    Returns:
        JSON avec l'analyse cognitive
    """
    try:
        # Appeler analyze_request au lieu de analyze
        analysis = cognitive.analyze_request(description)
        
        # Convertir les CognitiveInsight en dict pour la sérialisation
        def insight_to_dict(insight):
            if hasattr(insight, '__dict__'):
                return {
                    'quadrant': insight.quadrant.value if hasattr(insight.quadrant, 'value') else str(insight.quadrant),
                    'insight': insight.insight,
                    'confidence': insight.confidence,
                    'action_required': insight.action_required,
                    'risk_level': insight.risk_level
                }
            return insight
        
        # Convertir la matrice
        if 'matrix' in analysis:
            for quadrant, insights in analysis['matrix'].items():
                if isinstance(insights, list):
                    analysis['matrix'][quadrant] = [insight_to_dict(i) for i in insights]
        
        # Convertir les insights
        if 'insights' in analysis and isinstance(analysis['insights'], list):
            analysis['insights'] = [insight_to_dict(i) if hasattr(i, '__dict__') else i for i in analysis['insights']]
        
        return json.dumps(analysis, indent=2, ensure_ascii=False)
    except Exception as e:
        return f"Erreur: {str(e)}"


@app.tool()
def obtenir_tokens_design(category: str = None) -> str:
    """
    Récupère les design tokens DSFR.
    
    Args:
        category: Catégorie de tokens (colors, spacing, typography, icons)
    
    Returns:
        JSON avec les design tokens
    """
    try:
        # Router vers la bonne méthode selon la catégorie
        if category == "colors" or category == "couleurs":
            tokens = design.get_colors()
        elif category == "spacing" or category == "espacement":
            tokens = design.get_spacing()
        elif category == "typography" or category == "typographie":
            tokens = design.get_typography()
        elif category == "icons" or category == "icones":
            tokens = design.get_icons()
        else:
            # Retourner tous les tokens si pas de catégorie spécifiée
            tokens = {
                "colors": design.get_colors(),
                "spacing": design.get_spacing(),
                "typography": design.get_typography(),
                "icons": design.get_icons()
            }
        
        return json.dumps(tokens, indent=2, ensure_ascii=False)
    except Exception as e:
        return f"Erreur: {str(e)}"


@app.tool()
def generer_tests(component: str, test_type: str = "unit") -> str:
    """
    Génère des tests pour un composant.
    
    Args:
        component: Nom du composant
        test_type: Type de test (unit, integration, e2e)
    
    Returns:
        Code des tests générés
    """
    try:
        # Utiliser la bonne méthode selon le type de test
        if test_type == "e2e":
            # Pour les tests e2e, utiliser generate_e2e_scenario
            from src.services.test_generator_service import TestFramework
            tests = test_gen.generate_e2e_scenario(
                component=component,
                framework=TestFramework.CYPRESS,
                scenario="Interaction complète avec le composant"
            )
        else:
            # Pour unit et integration, utiliser generate_tests
            from src.services.test_generator_service import TestFramework
            tests = test_gen.generate_tests(
                component=component,
                framework=TestFramework.JEST if test_type == "unit" else TestFramework.CYPRESS
            )
        return tests
    except Exception as e:
        return f"Erreur: {str(e)}"


@app.tool()
def obtenir_fondamentaux(category: str = None) -> str:
    """
    R\u00e9cup\u00e8re les fondamentaux DSFR (grille, breakpoints, typographie).
    
    Args:
        category: Cat\u00e9gorie sp\u00e9cifique (grid, typography, breakpoints, spacing)
    
    Returns:
        JSON avec les fondamentaux demand\u00e9s
    """
    try:
        foundations = design.get_foundations(category)
        return json.dumps(foundations, indent=2, ensure_ascii=False)
    except Exception as e:
        return f"Erreur: {str(e)}"


@app.tool()
def obtenir_classes_css(type: str = None) -> str:
    """
    R\u00e9cup\u00e8re les classes CSS utilitaires DSFR.
    
    Args:
        type: Type d'utilitaire (colors, spacing, typography, display, grid)
    
    Returns:
        Liste des classes CSS disponibles
    """
    try:
        utilities = design.get_css_utilities(type)
        return json.dumps({
            "type": type or "all",
            "count": len(utilities),
            "classes": utilities
        }, indent=2, ensure_ascii=False)
    except Exception as e:
        return f"Erreur: {str(e)}"


@app.tool()
def obtenir_template_page(template_type: str, title: str = None, content: str = None) -> str:
    """
    G\u00e9n\u00e8re un template de page compl\u00e8te DSFR.
    
    Args:
        template_type: Type de template (error_404, error_500, login, signup, basic)
        title: Titre de la page (optionnel)
        content: Contenu principal (optionnel)
    
    Returns:
        HTML du template de page
    """
    try:
        if template_type in ['error_404', 'error_500', 'login', 'signup']:
            # Templates pr\u00e9d\u00e9finis
            html = template.get_template(template_type)
        else:
            # Page personnalis\u00e9e
            html = template.create_page(
                title=title or "Page DSFR",
                content=content or "<p>Contenu de la page</p>",
                template=template_type
            )
        return html
    except Exception as e:
        return f"Erreur: {str(e)}"


@app.tool()
def rechercher_documentation(topic: str) -> str:
    """
    Recherche dans la documentation DSFR extraite.
    
    Args:
        topic: Sujet \u00e0 rechercher (ex: grille, couleurs, accessibilit\u00e9)
    
    Returns:
        R\u00e9sultats de recherche avec guidelines et exemples
    """
    try:
        results = {
            "topic": topic,
            "guidelines": design.get_guidelines(topic),
            "foundations": {},
            "utilities": []
        }
        
        # Rechercher dans les fondamentaux
        if "grille" in topic.lower() or "grid" in topic.lower():
            results["foundations"]["grid"] = design.get_foundations("grid")
        if "typo" in topic.lower():
            results["foundations"]["typography"] = design.get_foundations("typography_rules")
        if "couleur" in topic.lower() or "color" in topic.lower():
            results["utilities"] = design.get_css_utilities("colors")
        
        return json.dumps(results, indent=2, ensure_ascii=False)
    except Exception as e:
        return f"Erreur: {str(e)}"


@app.tool()
def obtenir_aide_assistant(query: str) -> str:
    """
    Obtient de l'aide de l'assistant DSFR.
    
    Args:
        query: Question ou demande d'aide
    
    Returns:
        Réponse de l'assistant
    """
    try:
        # L'assistant n'a pas de méthode help directe, on utilise analyze_needs
        # et on génère une réponse basée sur l'analyse
        query_lower = query.lower()
        
        # Réponses pré-définies pour les questions fréquentes
        if "formulaire" in query_lower and "accessible" in query_lower:
            return """
Pour rendre un formulaire accessible selon DSFR et RGAA 4.1 :

1. **Labels et associations** (RGAA 11.1)
   - Chaque champ doit avoir un <label> associé via l'attribut 'for'
   - Ou utiliser aria-label / aria-labelledby
   
2. **Champs obligatoires** (RGAA 11.9)
   - Indiquer visuellement avec un astérisque (*)
   - Ajouter aria-required="true"
   - Mentionner en début de formulaire : "Les champs marqués * sont obligatoires"

3. **Messages d'erreur** (RGAA 11.10-11.11)
   - Utiliser role="alert" pour les messages d'erreur
   - Positionner les erreurs près du champ concerné
   - Messages explicites : "Le format de l'email est invalide"

4. **Structure et navigation**
   - Grouper avec <fieldset> et <legend> pour les champs liés
   - Ordre de tabulation logique (éviter tabindex > 0)
   - Bouton submit accessible au clavier

5. **Classes DSFR recommandées**
   - fr-input-group : conteneur de champ
   - fr-label : pour les labels
   - fr-input : pour les champs
   - fr-error-text : pour les messages d'erreur
   - fr-valid-text : pour les messages de succès

Exemple :
<div class="fr-input-group">
    <label class="fr-label" for="email">
        Email *
    </label>
    <input class="fr-input" type="email" id="email" 
           name="email" required aria-required="true">
    <p class="fr-error-text" role="alert">
        Ce champ est obligatoire
    </p>
</div>
"""
        
        elif "composant" in query_lower and ("choisir" in query_lower or "quel" in query_lower):
            # Analyser les besoins pour suggérer des composants
            analysis = assistant.analyze_needs(query)
            suggestions = assistant.suggest_components(analysis)
            
            response = "Voici les composants DSFR recommandés :\n\n"
            for sugg in suggestions[:5]:
                response += f"• **{sugg['component']}** : {sugg['reason']}\n"
                if 'variant' in sugg:
                    response += f"  Variante recommandée : {sugg['variant']}\n"
            
            return response
        
        elif "couleur" in query_lower or "color" in query_lower:
            return """
Les couleurs DSFR officielles :

**Couleurs principales**
- Bleu France : #000091 (couleur principale)
- Bleu France hover : #1212ff

**Couleurs système**
- Succès : #18753c (vert)
- Erreur : #ce0500 (rouge)
- Avertissement : #b34000 (orange)
- Information : #0063cb (bleu)

**Règles d'usage**
- Toujours utiliser les variables CSS DSFR
- Respecter les ratios de contraste RGAA (4.5:1 minimum)
- Ne pas créer de nouvelles couleurs
- Utiliser les couleurs système pour les feedbacks

Exemple :
.mon-element {
    color: var(--text-default-grey);
    background-color: var(--background-default-grey);
}
"""
        
        else:
            # Analyse générale des besoins
            analysis = assistant.analyze_needs(query)
            suggestions = assistant.suggest_components(analysis)
            
            response = f"Analyse de votre demande : '{query}'\n\n"
            
            if suggestions:
                response += "Composants DSFR suggérés :\n"
                for sugg in suggestions[:3]:
                    response += f"• {sugg['component']} : {sugg['reason']}\n"
            
            response += "\nPour plus d'informations, consultez la documentation DSFR."
            
            return response
            
    except Exception as e:
        return f"Erreur: {str(e)}"


# ============================================================================
# RESOURCES MCP - Accès direct aux gabarits HTML
# ============================================================================

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


# ============================================================================
# PROMPTS MCP - Templates de demandes prédéfinies
# ============================================================================

@app.prompt("formulaire_accessible")
async def prompt_formulaire_accessible() -> dict:
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
async def prompt_tableau_responsive() -> dict:
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
async def prompt_page_complete() -> dict:
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
async def prompt_composant_carte() -> dict:
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
async def prompt_navigation_complexe() -> dict:
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


if __name__ == "__main__":
    # Lancer le serveur
    app.run()