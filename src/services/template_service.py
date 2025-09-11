"""
Service de templates et mod\u00e8les de pages DSFR.
G\u00e8re les mod\u00e8les de pages compl\u00e8tes (erreur, connexion, etc.).
"""

import json
from pathlib import Path
from typing import Dict, Any, Optional, List


class TemplateService:
    """
    Service pour les templates de pages DSFR.
    Responsabilit\u00e9 unique : G\u00e9rer les mod\u00e8les de pages compl\u00e8tes.
    """
    
    def __init__(self):
        """Initialise le service avec la documentation KB."""
        self.documentation_kb = self._load_documentation_kb()
        self.templates = self._extract_templates()
        self.page_structures = self._init_page_structures()
    
    def _load_documentation_kb(self) -> Dict[str, Any]:
        """
        Charge la Knowledge Base de documentation.
        """
        # Nouveau chemin dans src/data/knowledge_base/
        kb_path = Path(__file__).parent.parent / 'data' / 'knowledge_base' / 'documentation.json'
        if kb_path.exists():
            try:
                with open(kb_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                print(f"[WARNING] Impossible de charger la documentation KB: {e}")
        return {}
    
    def _extract_templates(self) -> Dict[str, List[Dict[str, Any]]]:
        """
        Extrait les templates depuis la documentation KB.
        """
        templates = {
            'error': [],
            'auth': [],
            'signup': [],
            'general': []
        }
        
        if not self.documentation_kb or 'templates' not in self.documentation_kb:
            return templates
        
        for template_type, template_list in self.documentation_kb['templates'].items():
            if isinstance(template_list, list):
                templates[template_type] = template_list
        
        return templates
    
    def _init_page_structures(self) -> Dict[str, str]:
        """
        Initialise les structures de pages de base.
        """
        return {
            'basic': """<!DOCTYPE html>
<html lang="fr" data-fr-theme>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>{title}</title>
    <link rel="stylesheet" href="/dist/dsfr/dsfr.min.css">
    <link rel="stylesheet" href="/dist/utility/utility.min.css">
</head>
<body>
    {header}
    <main role="main" id="main">
        <div class="fr-container">
            {content}
        </div>
    </main>
    {footer}
    <script type="module" src="/dist/dsfr/dsfr.module.min.js"></script>
    <script type="text/javascript" nomodule src="/dist/dsfr/dsfr.nomodule.min.js"></script>
</body>
</html>""",
            
            'error_404': """<div class="fr-container">
    <div class="fr-grid-row fr-grid-row--center">
        <div class="fr-col-12 fr-col-md-8 fr-col-lg-6">
            <div class="fr-error-page">
                <h1>404</h1>
                <p class="fr-h3">Page non trouv\u00e9e</p>
                <p class="fr-text--lg">La page que vous recherchez n'existe pas ou a \u00e9t\u00e9 d\u00e9plac\u00e9e.</p>
                <div class="fr-btns-group fr-btns-group--inline">
                    <a href="/" class="fr-btn">Retour \u00e0 l'accueil</a>
                </div>
            </div>
        </div>
    </div>
</div>""",
            
            'error_500': """<div class="fr-container">
    <div class="fr-grid-row fr-grid-row--center">
        <div class="fr-col-12 fr-col-md-8 fr-col-lg-6">
            <div class="fr-error-page">
                <h1>500</h1>
                <p class="fr-h3">Erreur inattendue</p>
                <p class="fr-text--lg">Une erreur inattendue s'est produite. Veuillez r\u00e9essayer plus tard.</p>
                <div class="fr-btns-group fr-btns-group--inline">
                    <a href="/" class="fr-btn">Retour \u00e0 l'accueil</a>
                </div>
            </div>
        </div>
    </div>
</div>""",
            
            'login': """<div class="fr-container">
    <div class="fr-grid-row fr-grid-row--center">
        <div class="fr-col-12 fr-col-md-8 fr-col-lg-6">
            <h1>Connexion</h1>
            <form action="/login" method="post">
                <div class="fr-input-group">
                    <label class="fr-label" for="email">Adresse email</label>
                    <input class="fr-input" type="email" id="email" name="email" required>
                </div>
                <div class="fr-input-group">
                    <label class="fr-label" for="password">Mot de passe</label>
                    <input class="fr-input" type="password" id="password" name="password" required>
                </div>
                <div class="fr-checkbox-group">
                    <input type="checkbox" id="remember" name="remember">
                    <label class="fr-label" for="remember">Se souvenir de moi</label>
                </div>
                <div class="fr-btns-group">
                    <button type="submit" class="fr-btn">Se connecter</button>
                </div>
            </form>
            <hr class="fr-hr">
            <div class="fr-connect-group">
                <button class="fr-connect">
                    <span class="fr-connect__login">S'identifier avec</span>
                    <span class="fr-connect__brand">FranceConnect</span>
                </button>
            </div>
        </div>
    </div>
</div>""",
            
            'signup': """<div class="fr-container">
    <div class="fr-grid-row fr-grid-row--center">
        <div class="fr-col-12 fr-col-md-8 fr-col-lg-6">
            <h1>Cr\u00e9er un compte</h1>
            <form action="/signup" method="post">
                <div class="fr-input-group">
                    <label class="fr-label" for="firstname">Pr\u00e9nom</label>
                    <input class="fr-input" type="text" id="firstname" name="firstname" required>
                </div>
                <div class="fr-input-group">
                    <label class="fr-label" for="lastname">Nom</label>
                    <input class="fr-input" type="text" id="lastname" name="lastname" required>
                </div>
                <div class="fr-input-group">
                    <label class="fr-label" for="email">Adresse email</label>
                    <input class="fr-input" type="email" id="email" name="email" required>
                </div>
                <div class="fr-input-group">
                    <label class="fr-label" for="password">Mot de passe</label>
                    <span class="fr-hint-text">8 caract\u00e8res minimum</span>
                    <input class="fr-input" type="password" id="password" name="password" required>
                </div>
                <div class="fr-input-group">
                    <label class="fr-label" for="password-confirm">Confirmer le mot de passe</label>
                    <input class="fr-input" type="password" id="password-confirm" name="password-confirm" required>
                </div>
                <div class="fr-checkbox-group">
                    <input type="checkbox" id="terms" name="terms" required>
                    <label class="fr-label" for="terms">
                        J'accepte les conditions g\u00e9n\u00e9rales d'utilisation
                    </label>
                </div>
                <div class="fr-btns-group">
                    <button type="submit" class="fr-btn">Cr\u00e9er mon compte</button>
                </div>
            </form>
        </div>
    </div>
</div>"""
        }
    
    def get_template(self, template_type: str, **kwargs) -> str:
        """
        R\u00e9cup\u00e8re et personnalise un template de page.
        
        Args:
            template_type: Type de template (error_404, error_500, login, signup, basic)
            **kwargs: Param\u00e8tres de personnalisation
            
        Returns:
            HTML du template personnalis\u00e9
        """
        if template_type not in self.page_structures:
            # Chercher dans la KB
            if template_type in self.templates and self.templates[template_type]:
                # Utiliser le premier template de ce type
                template_data = self.templates[template_type][0]
                if 'code_examples' in template_data and template_data['code_examples']:
                    return template_data['code_examples'][0]
            
            # Fallback sur le template basic
            template_type = 'basic'
        
        html = self.page_structures[template_type]
        
        # Remplacements personnalis\u00e9s
        for key, value in kwargs.items():
            placeholder = f'{{{key}}}'
            if placeholder in html:
                html = html.replace(placeholder, str(value))
        
        return html
    
    def create_page(self, 
                   title: str,
                   content: str,
                   template: str = 'basic',
                   header: Optional[str] = None,
                   footer: Optional[str] = None) -> str:
        """
        Cr\u00e9e une page compl\u00e8te avec header et footer.
        
        Args:
            title: Titre de la page
            content: Contenu principal
            template: Template de base \u00e0 utiliser
            header: HTML du header (optionnel)
            footer: HTML du footer (optionnel)
            
        Returns:
            HTML de la page compl\u00e8te
        """
        if not header:
            header = self._get_default_header()
        
        if not footer:
            footer = self._get_default_footer()
        
        return self.get_template(
            template,
            title=title,
            content=content,
            header=header,
            footer=footer
        )
    
    def _get_default_header(self) -> str:
        """G\u00e9n\u00e8re un header DSFR par d\u00e9faut."""
        return """
<header role="banner" class="fr-header">
    <div class="fr-header__body">
        <div class="fr-container">
            <div class="fr-header__body-row">
                <div class="fr-header__brand fr-enlarge-link">
                    <div class="fr-header__brand-top">
                        <div class="fr-header__logo">
                            <p class="fr-logo">
                                R\u00e9publique<br>Fran\u00e7aise
                            </p>
                        </div>
                    </div>
                    <div class="fr-header__service">
                        <a href="/" title="Accueil">
                            <p class="fr-header__service-title">Nom du service</p>
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</header>"""
    
    def _get_default_footer(self) -> str:
        """G\u00e9n\u00e8re un footer DSFR par d\u00e9faut."""
        return """
<footer class="fr-footer" role="contentinfo">
    <div class="fr-container">
        <div class="fr-footer__body">
            <div class="fr-footer__brand fr-enlarge-link">
                <p class="fr-logo">
                    R\u00e9publique<br>Fran\u00e7aise
                </p>
            </div>
            <div class="fr-footer__content">
                <p class="fr-footer__content-desc">
                    Service public num\u00e9rique
                </p>
                <ul class="fr-footer__content-list">
                    <li class="fr-footer__content-item">
                        <a class="fr-footer__content-link" href="/mentions-legales">Mentions l\u00e9gales</a>
                    </li>
                    <li class="fr-footer__content-item">
                        <a class="fr-footer__content-link" href="/donnees-personnelles">Donn\u00e9es personnelles</a>
                    </li>
                    <li class="fr-footer__content-item">
                        <a class="fr-footer__content-link" href="/accessibilite">Accessibilit\u00e9</a>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</footer>"""
    
    def get_available_templates(self) -> Dict[str, int]:
        """
        Liste les templates disponibles.
        
        Returns:
            Dictionnaire avec le nombre de templates par cat\u00e9gorie
        """
        available = {}
        
        # Templates pr\u00e9d\u00e9finis
        available['predefined'] = len(self.page_structures)
        
        # Templates depuis la KB
        for template_type, template_list in self.templates.items():
            available[f'kb_{template_type}'] = len(template_list)
        
        return available


# Singleton helper
_template_instance: Optional[TemplateService] = None

def get_template_service() -> TemplateService:
    """
    R\u00e9cup\u00e8re l'instance unique du service de templates.
    
    Returns:
        Instance de TemplateService
    """
    global _template_instance
    if _template_instance is None:
        _template_instance = TemplateService()
    return _template_instance