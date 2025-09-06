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


if __name__ == "__main__":
    # Lancer le serveur
    app.run()