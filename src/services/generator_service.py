"""
Service de génération de composants DSFR.
Implémente le Factory Pattern pour éviter les switch/case (O de SOLID).
"""

import re
from typing import Dict, Any, Optional, Callable, List
from functools import lru_cache
from src.data import get_registry
from src.errors.components import (
    ComponentNotFoundError,
    InvalidVariantError,
    MissingPropertyError
)


class GeneratorService:
    """
    Service de génération HTML pour les composants DSFR.
    
    Factory Pattern : Map de générateurs au lieu de if/elif.
    Open/Closed Principle : Extensible sans modification du core.
    
    Example:
        >>> generator = GeneratorService()
        >>> html = generator.generate('button', label='Valider', variant='primary')
    """
    
    def __init__(self):
        """Initialise le service avec le registre de composants."""
        self.registry = get_registry()
        self._generators = self._init_generators()
    
    def _init_generators(self) -> Dict[str, Callable]:
        """
        Initialise la factory de générateurs.
        KISS : Map simple fonction -> composant.
        
        Returns:
            Dictionnaire des générateurs par composant
        """
        return {
            'button': self._generate_button,
            'input': self._generate_input,
            'form': self._generate_form,
            'alert': self._generate_alert,
            'card': self._generate_card,
            'modal': self._generate_modal,
            'table': self._generate_table,
            'accordion': self._generate_accordion,
            # Générateur par défaut pour les autres composants
            '__default__': self._generate_default
        }
    
    def generate(self, component: str, **kwargs) -> str:
        """
        Génère le HTML d'un composant avec les options données.
        
        Args:
            component: Nom du composant DSFR
            **kwargs: Options du composant (variant, label, etc.)
            
        Returns:
            HTML généré
            
        Raises:
            ComponentNotFoundError: Si le composant n'existe pas
            InvalidVariantError: Si la variante n'est pas valide
            
        Example:
            >>> html = generator.generate('button', 
            ...                          variant='primary',
            ...                          label='Envoyer',
            ...                          icon='send')
        """
        # Vérifier que le composant existe
        if not self.registry.get_component(component):
            available = self.registry.list_components()
            raise ComponentNotFoundError(component, available)
        
        # Utiliser le générateur spécifique ou le défaut
        if component in self._generators:
            generator = self._generators[component]
        else:
            generator = self._generators['__default__']
        
        # Générer le HTML
        html = generator(component, **kwargs)
        
        return html
    
    def _generate_button(self, component: str, **kwargs) -> str:
        """
        Générateur spécialisé pour les boutons.
        Gère les variantes, icônes, tailles, etc.
        """
        variant = kwargs.get('variant', 'basic')
        label = kwargs.get('label', 'Bouton')
        icon = kwargs.get('icon')
        size = kwargs.get('size')
        disabled = kwargs.get('disabled', False)
        
        # Récupérer le template de base
        html = self.registry.get_variant_html('button', variant)
        if not html:
            raise InvalidVariantError('button', variant, 
                                    self.registry.list_variants('button'))
        
        # Remplacer les placeholders
        html = self._replace_placeholder(html, 'Label bouton', label)
        html = self._replace_placeholder(html, 'Libellé', label)
        
        # Ajouter les modifications
        if icon:
            html = self._add_icon_to_button(html, icon)
        if size:
            html = self._add_size_to_button(html, size)
        if disabled:
            html = self._add_disabled_to_button(html)
        
        return html
    
    def _generate_input(self, component: str, **kwargs) -> str:
        """
        Générateur pour les champs de formulaire.
        """
        input_type = kwargs.get('type', 'text')
        label = kwargs.get('label', 'Champ')
        name = kwargs.get('name', 'input')
        required = kwargs.get('required', False)
        hint = kwargs.get('hint')
        error = kwargs.get('error')
        
        # Déterminer la variante selon le type
        variant_map = {
            'email': 'email',
            'password': 'password',
            'text': 'text',
            'error': 'with_error'
        }
        variant = variant_map.get(input_type, 'text')
        if error:
            variant = 'with_error'
        
        html = self.registry.get_variant_html('input', variant)
        if not html:
            html = self.registry.get_variant_html('input', 'text')
        
        # Remplacements
        html = self._replace_placeholder(html, 'Libellé', label)
        html = self._replace_placeholder(html, 'name="input_', f'name="{name}_')
        html = self._replace_placeholder(html, 'id="input-', f'id="{name}-')
        html = self._replace_placeholder(html, 'for="input-', f'for="{name}-')
        
        if hint:
            html = self._add_hint_to_input(html, hint)
        if error:
            html = self._add_error_to_input(html, error)
        if required:
            html = html.replace('<input', '<input required aria-required="true"')
        
        return html
    
    def _generate_form(self, component: str, **kwargs) -> str:
        """
        Générateur pour les formulaires complets.
        """
        variant = kwargs.get('variant', 'contact')
        action = kwargs.get('action', '/submit')
        method = kwargs.get('method', 'post')
        fields = kwargs.get('fields', [])
        
        html = self.registry.get_variant_html('form', variant)
        if not html:
            raise InvalidVariantError('form', variant,
                                    self.registry.list_variants('form'))
        
        # Personnalisation de base
        html = html.replace('action="/contact"', f'action="{action}"')
        html = html.replace('action="/submit"', f'action="{action}"')
        html = html.replace('method="post"', f'method="{method}"')
        
        # Si des champs custom sont fournis
        if fields:
            # TODO: Générer les champs dynamiquement (YAGNI pour l'instant)
            pass
        
        return html
    
    def _generate_alert(self, component: str, **kwargs) -> str:
        """
        Générateur pour les alertes.
        """
        alert_type = kwargs.get('type', 'info')
        variant = kwargs.get('variant', alert_type)
        title = kwargs.get('title')
        message = kwargs.get('message', 'Message d\'alerte')
        closable = kwargs.get('closable', False)
        
        html = self.registry.get_variant_html('alert', variant)
        if not html:
            html = self.registry.get_variant_html('alert', 'info')
        
        # Remplacements
        if title:
            html = re.sub(r'<p class="fr-alert__title">.*?</p>',
                         f'<p class="fr-alert__title">{title}</p>',
                         html, flags=re.DOTALL)
        
        # Remplacer le message
        html = re.sub(r'<p>.*?</p>(?!.*<p>)',
                     f'<p>{message}</p>',
                     html, count=1)
        
        if closable and 'fr-alert--close' not in html:
            html = html.replace('fr-alert', 'fr-alert fr-alert--close', 1)
        
        return html
    
    def _generate_card(self, component: str, **kwargs) -> str:
        """
        Générateur pour les cartes.
        """
        variant = kwargs.get('variant', 'basic')
        title = kwargs.get('title', 'Titre de la carte')
        description = kwargs.get('description', 'Description')
        link = kwargs.get('link')
        image = kwargs.get('image')
        
        html = self.registry.get_variant_html('card', variant)
        if not html:
            html = self.registry.get_variant_html('card', 'basic')
        
        # Remplacements basiques
        html = self._replace_placeholder(html, 'Titre de la carte', title)
        html = self._replace_placeholder(html, 'Description de la carte', description)
        
        if link:
            html = html.replace('href="#"', f'href="{link}"')
        
        if image:
            html = self._add_image_to_card(html, image)
        
        return html
    
    def _generate_modal(self, component: str, **kwargs) -> str:
        """
        Générateur pour les modales.
        """
        variant = kwargs.get('variant', 'basic')
        title = kwargs.get('title', 'Titre de la modale')
        content = kwargs.get('content', 'Contenu de la modale')
        modal_id = kwargs.get('id', 'modal-1')
        
        html = self.registry.get_variant_html('modal', variant)
        if not html:
            html = self.registry.get_variant_html('modal', 'basic')
        
        # Remplacements
        html = html.replace('id="modal-', f'id="{modal_id}-')
        html = html.replace('#modal-', f'#{modal_id}-')
        html = self._replace_placeholder(html, 'Titre de la modale', title)
        html = self._replace_placeholder(html, 'Contenu de la modale', content)
        
        return html
    
    def _generate_table(self, component: str, **kwargs) -> str:
        """
        Générateur pour les tableaux.
        """
        variant = kwargs.get('variant', 'basic')
        headers = kwargs.get('headers', ['Colonne 1', 'Colonne 2'])
        rows = kwargs.get('rows', [])
        caption = kwargs.get('caption')
        
        html = self.registry.get_variant_html('table', variant)
        if not html:
            html = self.registry.get_variant_html('table', 'basic')
        
        # TODO: Génération dynamique des lignes (YAGNI pour l'instant)
        # Pour l'instant on retourne le template de base
        
        if caption:
            html = f'<table class="fr-table">\n<caption>{caption}</caption>' + \
                   html.split('<table class="fr-table">')[1] if '<table' in html else html
        
        return html
    
    def _generate_accordion(self, component: str, **kwargs) -> str:
        """
        Générateur pour les accordéons.
        """
        variant = kwargs.get('variant', 'single')
        title = kwargs.get('title', 'Titre de l\'accordéon')
        content = kwargs.get('content', 'Contenu de l\'accordéon')
        expanded = kwargs.get('expanded', False)
        accordion_id = kwargs.get('id', 'accordion-1')
        
        html = self.registry.get_variant_html('accordion', variant)
        if not html:
            html = self.registry.get_variant_html('accordion', 'single')
        
        # Remplacements
        html = html.replace('id="accordion-', f'id="{accordion_id}-')
        html = html.replace('"accordion-', f'"{accordion_id}-')
        html = self._replace_placeholder(html, 'Titre de l\'accordéon', title)
        html = self._replace_placeholder(html, 'Contenu de l\'accordéon', content)
        
        if expanded:
            html = html.replace('aria-expanded="false"', 'aria-expanded="true"')
        
        return html
    
    def _generate_default(self, component: str, **kwargs) -> str:
        """
        Générateur par défaut pour les composants sans logique spéciale.
        KISS : Retourne le template avec remplacements basiques.
        """
        variant = kwargs.get('variant', 'basic')
        
        html = self.registry.get_variant_html(component, variant)
        if not html:
            # Essayer de récupérer la première variante disponible
            variants = self.registry.list_variants(component)
            if variants:
                html = self.registry.get_variant_html(component, variants[0])
            else:
                raise ComponentNotFoundError(component)
        
        # Remplacements génériques pour les kwargs fournis
        for key, value in kwargs.items():
            if key not in ['variant', 'component']:
                # Essayer plusieurs patterns de remplacement
                html = self._replace_placeholder(html, f'{{{key}}}', str(value))
                html = self._replace_placeholder(html, f'${key}', str(value))
        
        return html
    
    # Méthodes utilitaires (DRY)
    
    def _replace_placeholder(self, html: str, placeholder: str, value: str) -> str:
        """Remplace un placeholder de manière sûre."""
        return html.replace(placeholder, value)
    
    def _add_icon_to_button(self, html: str, icon: str) -> str:
        """Ajoute une icône à un bouton."""
        icon_class = f'fr-icon-{icon}-line'
        if 'fr-btn--icon-left' not in html:
            html = html.replace('fr-btn', f'fr-btn fr-btn--icon-left {icon_class}', 1)
        return html
    
    def _add_size_to_button(self, html: str, size: str) -> str:
        """Ajoute une taille à un bouton."""
        size_class = f'fr-btn--{size}'
        if size_class not in html:
            html = html.replace('fr-btn', f'fr-btn {size_class}', 1)
        return html
    
    def _add_disabled_to_button(self, html: str) -> str:
        """Rend un bouton disabled."""
        return html.replace('<button', '<button disabled', 1)
    
    def _add_hint_to_input(self, html: str, hint: str) -> str:
        """Ajoute un texte d'aide à un input."""
        hint_html = f'<span class="fr-hint-text">{hint}</span>'
        return html.replace('</label>', f'{hint_html}</label>', 1)
    
    def _add_error_to_input(self, html: str, error: str) -> str:
        """Ajoute un message d'erreur à un input."""
        error_html = f'<p class="fr-error-text">{error}</p>'
        return html.replace('</div>', f'{error_html}</div>', 1)
    
    def _add_image_to_card(self, html: str, image: str) -> str:
        """Ajoute une image à une carte."""
        img_html = f'<img src="{image}" alt="" class="fr-responsive-img">'
        return html.replace('<div class="fr-card__body">', 
                           f'<div class="fr-card__img">{img_html}</div>\n<div class="fr-card__body">')
    
    @lru_cache(maxsize=256)
    def get_component_info(self, component: str) -> Dict[str, Any]:
        """
        Récupère les infos d'un composant (avec cache).
        
        Returns:
            Métadonnées et variantes du composant
        """
        return {
            'name': component,
            'variants': self.registry.list_variants(component),
            'metadata': self.registry.get_metadata(component)
        }


# Singleton helper (KISS)
_generator_instance: Optional[GeneratorService] = None

def get_generator() -> GeneratorService:
    """
    Récupère l'instance unique du générateur.
    
    Returns:
        Instance de GeneratorService
        
    Example:
        >>> generator = get_generator()
        >>> html = generator.generate('button', label='OK')
    """
    global _generator_instance
    if _generator_instance is None:
        _generator_instance = GeneratorService()
    return _generator_instance