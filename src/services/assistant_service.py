"""
Service d'assistant intelligent DSFR.
Analyse les besoins et suggère les composants appropriés.
"""

from typing import Dict, List, Any, Optional
from src.services.generator_service import get_generator
from src.data import get_registry


class AssistantService:
    """
    Assistant intelligent pour DSFR.
    
    Utilise la matrice Connu-Inconnu pour analyser les besoins
    et suggérer les meilleurs composants.
    """
    
    def __init__(self):
        """Initialise l'assistant avec les services nécessaires."""
        self.generator = get_generator()
        self.registry = get_registry()
        self.keywords = self._init_keywords()
    
    def _init_keywords(self) -> Dict[str, List[str]]:
        """
        Initialise les mots-clés pour la détection de besoins.
        KISS : Mapping simple mot-clé -> composant.
        """
        return {
            'button': ['bouton', 'button', 'valider', 'envoyer', 'submit', 'action'],
            'form': ['formulaire', 'form', 'saisie', 'inscription', 'contact'],
            'alert': ['alerte', 'alert', 'message', 'notification', 'avertissement'],
            'modal': ['popup', 'modal', 'dialog', 'fenêtre', 'dialogue'],
            'table': ['tableau', 'table', 'liste', 'données', 'grille'],
            'card': ['carte', 'card', 'tuile', 'vignette', 'fiche'],
            'accordion': ['accordéon', 'accordion', 'collapse', 'déroulant'],
            'navigation': ['menu', 'navigation', 'nav', 'breadcrumb', 'fil'],
            'input': ['champ', 'input', 'field', 'saisie', 'texte']
        }
    
    def analyze_needs(self, description: str) -> Dict[str, Any]:
        """
        Analyse les besoins selon la matrice Connu-Inconnu.
        
        Args:
            description: Description du besoin utilisateur
            
        Returns:
            Analyse structurée des besoins
        """
        description_lower = description.lower()
        
        analysis = {
            'connus_connus': [],      # Ce que l'utilisateur sait qu'il veut
            'connus_inconnus': [],    # Ce qu'il sait qu'il ne sait pas
            'inconnus_connus': [],    # Ce qu'il ne réalise pas qu'il sait
            'inconnus_inconnus': []   # Ce qu'il ne sait pas qu'il ne sait pas
        }
        
        # Détecter les composants explicites
        for component, keywords in self.keywords.items():
            if any(keyword in description_lower for keyword in keywords):
                analysis['connus_connus'].append(component)
        
        # Détecter les besoins implicites
        if 'formulaire' in description_lower or 'form' in description_lower:
            analysis['inconnus_connus'].extend(['validation', 'error_handling'])
            if 'contact' in description_lower:
                analysis['inconnus_connus'].append('consent_checkbox')
        
        if 'accessible' in description_lower or 'rgaa' in description_lower:
            analysis['inconnus_connus'].extend(['aria_labels', 'keyboard_nav'])
        
        # Anticiper les besoins non exprimés
        if 'form' in analysis['connus_connus']:
            analysis['inconnus_inconnus'].extend(['csrf_protection', 'validation_js'])
        
        if 'modal' in analysis['connus_connus']:
            analysis['inconnus_inconnus'].extend(['focus_trap', 'escape_handler'])
        
        return analysis
    
    def suggest_components(self, analysis: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Suggère des composants basés sur l'analyse.
        
        Args:
            analysis: Résultat de analyze_needs
            
        Returns:
            Liste de suggestions avec confiance
        """
        suggestions = []
        
        # Suggestions directes (haute confiance)
        for component in analysis['connus_connus']:
            if self.registry.get_component(component):
                suggestions.append({
                    'component': component,
                    'variant': self._get_best_variant(component, analysis),
                    'reason': f"Composant {component} explicitement demandé",
                    'confidence': 'high'
                })
        
        # Suggestions indirectes (confiance moyenne)
        if 'validation' in analysis['inconnus_connus']:
            suggestions.append({
                'component': 'input',
                'variant': 'with_error',
                'reason': "Gestion des erreurs recommandée",
                'confidence': 'medium'
            })
        
        if 'consent_checkbox' in analysis['inconnus_connus']:
            suggestions.append({
                'component': 'checkbox',
                'variant': 'basic',
                'reason': "Consentement RGPD nécessaire",
                'confidence': 'high'
            })
        
        return suggestions
    
    def _get_best_variant(self, component: str, analysis: Dict) -> str:
        """
        Détermine la meilleure variante selon le contexte.
        KISS : Logique simple de sélection.
        """
        context = ' '.join(str(v) for v in analysis.values())
        
        if component == 'button':
            if 'principal' in context or 'important' in context:
                return 'primary'
            elif 'secondaire' in context:
                return 'secondary'
            else:
                return 'basic'
        
        elif component == 'alert':
            if 'erreur' in context or 'error' in context:
                return 'error'
            elif 'succès' in context or 'success' in context:
                return 'success'
            else:
                return 'info'
        
        elif component == 'form':
            if 'connexion' in context or 'login' in context:
                return 'login'
            elif 'contact' in context:
                return 'contact'
            else:
                return 'basic'
        
        # Par défaut, première variante disponible
        variants = self.registry.list_variants(component)
        return variants[0] if variants else 'basic'
    
    def generate_page(self, title: str, components: List[str]) -> str:
        """
        Génère une page complète avec plusieurs composants.
        
        Args:
            title: Titre de la page
            components: Liste des composants à inclure
            
        Returns:
            HTML complet de la page
        """
        # Header de page DSFR
        html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{title}</title>
    <link rel="stylesheet" href="https://unpkg.com/@gouvfr/dsfr@1.11.2/dist/dsfr.min.css">
</head>
<body>
    <div class="fr-container">
        <h1>{title}</h1>
"""
        
        # Ajouter chaque composant
        for comp_spec in components:
            if isinstance(comp_spec, dict):
                comp_html = self.generator.generate(**comp_spec)
            else:
                comp_html = self.generator.generate(comp_spec)
            
            html += f"""
        <div class="fr-my-3w">
            {comp_html}
        </div>
"""
        
        # Footer
        html += """
    </div>
    <script src="https://unpkg.com/@gouvfr/dsfr@1.11.2/dist/dsfr.module.js"></script>
</body>
</html>"""
        
        return html


# Singleton
_assistant_instance: Optional[AssistantService] = None

def get_assistant() -> AssistantService:
    """Récupère l'instance unique de l'assistant."""
    global _assistant_instance
    if _assistant_instance is None:
        _assistant_instance = AssistantService()
    return _assistant_instance