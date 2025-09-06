#!/usr/bin/env python3
"""
Constructeur de bibliothèque HTML DSFR pour production
Génère des gabarits HTML prêts à l'emploi depuis le MCP
"""

import json
import os
import sys
from datetime import datetime
from typing import Dict, List, Any

# Ajouter le MCP au path si disponible
MCP_PATH = "/Users/alex/Desktop/mcp-dsfr"
if os.path.exists(MCP_PATH):
    sys.path.insert(0, MCP_PATH)

class DSFRProductionBuilder:
    """
    Constructeur de gabarits DSFR pour production
    Génère du HTML utilisable directement, pas des templates
    """
    
    def __init__(self):
        self.output_dir = "gabarits"
        self.components_db = {}
        self.html_snippets = {}
        
        # Composants DSFR complets avec exemples HTML
        self.production_templates = {
            "button": {
                "basic": """<button class="fr-btn">
    {label}
</button>""",
                "primary": """<button class="fr-btn">
    {label}
</button>""",
                "secondary": """<button class="fr-btn fr-btn--secondary">
    {label}
</button>""",
                "tertiary": """<button class="fr-btn fr-btn--tertiary">
    {label}
</button>""",
                "icon_left": """<button class="fr-btn fr-btn--icon-left {icon_class}">
    {label}
</button>""",
                "icon_right": """<button class="fr-btn fr-btn--icon-right {icon_class}">
    {label}
</button>""",
                "disabled": """<button class="fr-btn" disabled aria-disabled="true">
    {label}
</button>""",
                "sm": """<button class="fr-btn fr-btn--sm">
    {label}
</button>""",
                "lg": """<button class="fr-btn fr-btn--lg">
    {label}
</button>"""
            },
            
            "input": {
                "text": """<div class="fr-input-group">
    <label class="fr-label" for="{id}">
        {label}
        {hint}
    </label>
    <input class="fr-input" type="text" id="{id}" name="{name}"{required}{aria}>
    {error_msg}
</div>""",
                "email": """<div class="fr-input-group">
    <label class="fr-label" for="{id}">
        {label}
        <span class="fr-hint-text">Format : nom@domaine.fr</span>
    </label>
    <input class="fr-input" type="email" id="{id}" name="{name}"{required} aria-describedby="{id}-hint">
</div>""",
                "password": """<div class="fr-password" id="{id}-password">
    <label class="fr-label" for="{id}">
        {label}
    </label>
    <div class="fr-input-wrap">
        <input class="fr-password__input fr-input" type="password" id="{id}" name="{name}"{required}>
    </div>
    <div class="fr-password__checkbox fr-checkbox-group fr-checkbox-group--sm">
        <input type="checkbox" id="{id}-password-show" aria-label="Afficher le mot de passe">
        <label class="fr-password__checkbox-label" for="{id}-password-show">
            Afficher
        </label>
    </div>
</div>""",
                "with_error": """<div class="fr-input-group fr-input-group--error">
    <label class="fr-label" for="{id}">
        {label}
    </label>
    <input class="fr-input fr-input--error" type="text" id="{id}" name="{name}" aria-invalid="true" aria-describedby="{id}-error">
    <p id="{id}-error" class="fr-error-text">
        {error_message}
    </p>
</div>""",
                "with_success": """<div class="fr-input-group fr-input-group--valid">
    <label class="fr-label" for="{id}">
        {label}
    </label>
    <input class="fr-input fr-input--valid" type="text" id="{id}" name="{name}" aria-describedby="{id}-valid">
    <p id="{id}-valid" class="fr-valid-text">
        {success_message}
    </p>
</div>"""
            },
            
            "card": {
                "basic": """<div class="fr-card fr-enlarge-link">
    <div class="fr-card__body">
        <div class="fr-card__content">
            <h3 class="fr-card__title">
                <a href="{link}" class="fr-card__link">{title}</a>
            </h3>
            <p class="fr-card__desc">
                {description}
            </p>
            <p class="fr-card__detail">{detail}</p>
        </div>
    </div>
</div>""",
                "horizontal": """<div class="fr-card fr-card--horizontal fr-enlarge-link">
    <div class="fr-card__body">
        <div class="fr-card__content">
            <h3 class="fr-card__title">
                <a href="{link}" class="fr-card__link">{title}</a>
            </h3>
            <p class="fr-card__desc">
                {description}
            </p>
            <p class="fr-card__detail">{detail}</p>
        </div>
    </div>
    <div class="fr-card__header">
        <div class="fr-card__img">
            <img class="fr-responsive-img" src="{image}" alt="{image_alt}">
        </div>
    </div>
</div>""",
                "with_image": """<div class="fr-card fr-enlarge-link">
    <div class="fr-card__header">
        <div class="fr-card__img">
            <img class="fr-responsive-img" src="{image}" alt="{image_alt}">
        </div>
        <ul class="fr-badges-group">
            <li>
                <p class="fr-badge">{badge}</p>
            </li>
        </ul>
    </div>
    <div class="fr-card__body">
        <div class="fr-card__content">
            <h3 class="fr-card__title">
                <a href="{link}" class="fr-card__link">{title}</a>
            </h3>
            <p class="fr-card__desc">
                {description}
            </p>
            <p class="fr-card__detail">{detail}</p>
        </div>
    </div>
</div>"""
            },
            
            "alert": {
                "info": """<div class="fr-alert fr-alert--info">
    <h3 class="fr-alert__title">{title}</h3>
    <p>{message}</p>
</div>""",
                "success": """<div class="fr-alert fr-alert--success">
    <h3 class="fr-alert__title">{title}</h3>
    <p>{message}</p>
</div>""",
                "warning": """<div class="fr-alert fr-alert--warning">
    <h3 class="fr-alert__title">{title}</h3>
    <p>{message}</p>
</div>""",
                "error": """<div class="fr-alert fr-alert--error">
    <h3 class="fr-alert__title">{title}</h3>
    <p>{message}</p>
</div>""",
                "closable": """<div class="fr-alert fr-alert--{type}" role="alert">
    <h3 class="fr-alert__title">{title}</h3>
    <p>{message}</p>
    <button class="fr-btn--close fr-btn" title="Masquer le message" aria-label="Masquer le message">
        Masquer le message
    </button>
</div>"""
            },
            
            "modal": {
                "basic": """<dialog id="{id}" class="fr-modal" role="dialog" aria-labelledby="{id}-title" aria-modal="true">
    <div class="fr-container fr-container--fluid fr-container-md">
        <div class="fr-grid-row fr-grid-row--center">
            <div class="fr-col-12 fr-col-md-8 fr-col-lg-6">
                <div class="fr-modal__body">
                    <div class="fr-modal__header">
                        <button class="fr-btn--close fr-btn" title="Fermer la fenêtre modale" aria-controls="{id}">
                            Fermer
                        </button>
                    </div>
                    <div class="fr-modal__content">
                        <h1 id="{id}-title" class="fr-modal__title">
                            {title}
                        </h1>
                        <p>{content}</p>
                    </div>
                    <div class="fr-modal__footer">
                        <div class="fr-btns-group fr-btns-group--inline-lg">
                            <button class="fr-btn" data-fr-js-modal-button="true">
                                {action_primary}
                            </button>
                            <button class="fr-btn fr-btn--secondary" data-fr-js-modal-button="true">
                                {action_secondary}
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</dialog>""",
                "trigger": """<!-- Bouton déclencheur -->
<button class="fr-btn" data-fr-opened="false" aria-controls="{id}">
    {trigger_label}
</button>

<!-- Modale -->
<dialog id="{id}" class="fr-modal" role="dialog" aria-labelledby="{id}-title" aria-modal="true">
    <!-- Contenu de la modale -->
</dialog>"""
            },
            
            "accordion": {
                "single": """<section class="fr-accordion">
    <h3 class="fr-accordion__title">
        <button class="fr-accordion__btn" aria-expanded="false" aria-controls="{id}">
            {title}
        </button>
    </h3>
    <div class="fr-collapse" id="{id}">
        <div class="fr-accordion__inner">
            {content}
        </div>
    </div>
</section>""",
                "group": """<div class="fr-accordions-group">
    <section class="fr-accordion">
        <h3 class="fr-accordion__title">
            <button class="fr-accordion__btn" aria-expanded="false" aria-controls="{id}-1">
                {title1}
            </button>
        </h3>
        <div class="fr-collapse" id="{id}-1">
            <div class="fr-accordion__inner">
                {content1}
            </div>
        </div>
    </section>
    <section class="fr-accordion">
        <h3 class="fr-accordion__title">
            <button class="fr-accordion__btn" aria-expanded="false" aria-controls="{id}-2">
                {title2}
            </button>
        </h3>
        <div class="fr-collapse" id="{id}-2">
            <div class="fr-accordion__inner">
                {content2}
            </div>
        </div>
    </section>
</div>"""
            },
            
            "table": {
                "basic": """<div class="fr-table">
    <table>
        <caption>{caption}</caption>
        <thead>
            <tr>
                {headers}
            </tr>
        </thead>
        <tbody>
            {rows}
        </tbody>
    </table>
</div>""",
                "complex": """<div class="fr-table">
    <table>
        <caption>{caption}</caption>
        <thead>
            <tr>
                <th scope="col">Colonne 1</th>
                <th scope="col">Colonne 2</th>
                <th scope="col">Colonne 3</th>
                <th scope="col">Actions</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <th scope="row">Ligne 1</th>
                <td>Donnée 1.2</td>
                <td>Donnée 1.3</td>
                <td>
                    <button class="fr-btn fr-btn--sm fr-btn--tertiary-no-outline fr-btn--icon-left fr-icon-edit-line">
                        Modifier
                    </button>
                </td>
            </tr>
        </tbody>
    </table>
</div>"""
            },
            
            "form": {
                "contact": """<form action="{action}" method="post">
    <fieldset class="fr-fieldset" aria-labelledby="contact-fieldset-legend">
        <legend class="fr-fieldset__legend" id="contact-fieldset-legend">
            <h2>Formulaire de contact</h2>
        </legend>
        
        <div class="fr-input-group">
            <label class="fr-label" for="contact-name">
                Nom complet
                <span class="fr-hint-text">Prénom et nom</span>
            </label>
            <input class="fr-input" type="text" id="contact-name" name="name" required>
        </div>
        
        <div class="fr-input-group">
            <label class="fr-label" for="contact-email">
                Email
            </label>
            <input class="fr-input" type="email" id="contact-email" name="email" required>
        </div>
        
        <div class="fr-input-group">
            <label class="fr-label" for="contact-message">
                Message
            </label>
            <textarea class="fr-input" id="contact-message" name="message" rows="5" required></textarea>
        </div>
        
        <div class="fr-checkbox-group">
            <input type="checkbox" id="contact-consent" name="consent" required>
            <label class="fr-label" for="contact-consent">
                J'accepte que mes données soient utilisées pour traiter ma demande
            </label>
        </div>
        
        <div class="fr-btns-group">
            <button class="fr-btn" type="submit">
                Envoyer
            </button>
            <button class="fr-btn fr-btn--secondary" type="reset">
                Annuler
            </button>
        </div>
    </fieldset>
</form>""",
                "login": """<form action="{action}" method="post">
    <fieldset class="fr-fieldset" aria-labelledby="login-fieldset-legend">
        <legend class="fr-fieldset__legend" id="login-fieldset-legend">
            <h2>Connexion</h2>
        </legend>
        
        <div class="fr-input-group">
            <label class="fr-label" for="login-email">
                Adresse email
            </label>
            <input class="fr-input" type="email" id="login-email" name="email" required autocomplete="username">
        </div>
        
        <div class="fr-password" id="login-password">
            <label class="fr-label" for="login-pass">
                Mot de passe
            </label>
            <div class="fr-input-wrap">
                <input class="fr-password__input fr-input" type="password" id="login-pass" name="password" required autocomplete="current-password">
            </div>
            <div class="fr-password__checkbox fr-checkbox-group fr-checkbox-group--sm">
                <input type="checkbox" id="login-pass-show" aria-label="Afficher le mot de passe">
                <label class="fr-password__checkbox-label" for="login-pass-show">
                    Afficher
                </label>
            </div>
        </div>
        
        <div class="fr-checkbox-group">
            <input type="checkbox" id="login-remember" name="remember">
            <label class="fr-label" for="login-remember">
                Se souvenir de moi
            </label>
        </div>
        
        <div class="fr-btns-group">
            <button class="fr-btn" type="submit">
                Se connecter
            </button>
            <a class="fr-btn fr-btn--secondary" href="/forgot-password">
                Mot de passe oublié ?
            </a>
        </div>
    </fieldset>
</form>"""
            },
            
            "navigation": {
                "breadcrumb": """<nav role="navigation" class="fr-breadcrumb" aria-label="vous êtes ici :">
    <button class="fr-breadcrumb__button" aria-expanded="false" aria-controls="breadcrumb-{id}">
        Voir le fil d'Ariane
    </button>
    <div class="fr-collapse" id="breadcrumb-{id}">
        <ol class="fr-breadcrumb__list">
            <li>
                <a class="fr-breadcrumb__link" href="/">Accueil</a>
            </li>
            <li>
                <a class="fr-breadcrumb__link" href="/niveau1">Niveau 1</a>
            </li>
            <li>
                <a class="fr-breadcrumb__link" href="/niveau1/niveau2">Niveau 2</a>
            </li>
            <li>
                <a class="fr-breadcrumb__link" aria-current="page">Page actuelle</a>
            </li>
        </ol>
    </div>
</nav>""",
                "pagination": """<nav role="navigation" class="fr-pagination" aria-label="Pagination">
    <ul class="fr-pagination__list">
        <li>
            <a class="fr-pagination__link fr-pagination__link--first" href="/page-1" aria-label="Première page">
                Première page
            </a>
        </li>
        <li>
            <a class="fr-pagination__link fr-pagination__link--prev fr-pagination__link--lg-label" href="/page-2" aria-label="Page précédente">
                Page précédente
            </a>
        </li>
        <li>
            <a class="fr-pagination__link" href="/page-1" title="Page 1">
                1
            </a>
        </li>
        <li>
            <a class="fr-pagination__link" href="/page-2" title="Page 2">
                2
            </a>
        </li>
        <li>
            <a class="fr-pagination__link" aria-current="page" title="Page 3">
                3
            </a>
        </li>
        <li>
            <a class="fr-pagination__link" href="/page-4" title="Page 4">
                4
            </a>
        </li>
        <li>
            <a class="fr-pagination__link" href="/page-5" title="Page 5">
                5
            </a>
        </li>
        <li>
            <a class="fr-pagination__link fr-pagination__link--next fr-pagination__link--lg-label" href="/page-4" aria-label="Page suivante">
                Page suivante
            </a>
        </li>
        <li>
            <a class="fr-pagination__link fr-pagination__link--last" href="/page-10" aria-label="Dernière page">
                Dernière page
            </a>
        </li>
    </ul>
</nav>"""
            }
        }
    
    def build_html_library(self):
        """Construit la bibliothèque complète de gabarits HTML"""
        print("🏗️  Construction de la bibliothèque HTML DSFR de production...")
        
        os.makedirs(self.output_dir, exist_ok=True)
        
        # Créer les fichiers HTML pour chaque composant
        for component_name, variants in self.production_templates.items():
            component_dir = os.path.join(self.output_dir, component_name)
            os.makedirs(component_dir, exist_ok=True)
            
            print(f"  📦 {component_name}")
            
            # Créer un fichier pour chaque variante
            for variant_name, template in variants.items():
                filename = f"{component_name}_{variant_name}.html"
                filepath = os.path.join(component_dir, filename)
                
                # Nettoyer le template pour avoir du HTML prêt
                clean_html = self.prepare_template(template, component_name, variant_name)
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(clean_html)
                
                print(f"    [OK] {variant_name}")
        
        # Créer un index HTML pour naviguer
        self.create_index()
        
        # Créer un fichier JSON avec tous les snippets
        self.create_json_library()
        
        print(f"\n[INFO] Bibliothèque créée dans '{self.output_dir}/'")
        print(f"   {len(self.production_templates)} composants")
        print(f"   {sum(len(v) for v in self.production_templates.values())} variantes")
    
    def prepare_template(self, template: str, component: str, variant: str) -> str:
        """Prépare un template avec des valeurs par défaut"""
        
        # Valeurs par défaut selon le composant
        defaults = {
            # Génériques
            "label": "Libellé",
            "title": "Titre",
            "description": "Description du contenu",
            "content": "Contenu principal",
            "message": "Message d'information",
            "id": f"{component}-{variant}",
            "name": f"{component}_{variant}",
            
            # Spécifiques
            "link": "#",
            "action": "/submit",
            "image": "/placeholder.jpg",
            "image_alt": "Description de l'image",
            "detail": "Information détaillée",
            "badge": "Nouveau",
            "hint": '<span class="fr-hint-text">Texte d\'aide</span>',
            "required": ' required aria-required="true"',
            "aria": ' aria-describedby="input-hint"',
            "error_message": "Message d'erreur",
            "success_message": "Validation réussie",
            "error_msg": "",
            "icon_class": "fr-icon-save-line",
            "type": "info",
            "action_primary": "Valider",
            "action_secondary": "Annuler",
            "trigger_label": "Ouvrir",
            "caption": "Titre du tableau",
            "headers": "<th scope='col'>En-tête 1</th><th scope='col'>En-tête 2</th>",
            "rows": "<tr><td>Donnée 1</td><td>Donnée 2</td></tr>",
            "title1": "Section 1",
            "content1": "Contenu de la section 1",
            "title2": "Section 2", 
            "content2": "Contenu de la section 2"
        }
        
        # Remplacer les placeholders
        result = template
        for key, value in defaults.items():
            result = result.replace(f"{{{key}}}", value)
        
        # Ajouter un commentaire d'identification
        header = f"""<!-- DSFR v1.14.1 - Composant: {component} - Variante: {variant} -->
<!-- Généré le {datetime.now().strftime('%Y-%m-%d %H:%M')} -->
"""
        
        return header + result
    
    def create_index(self):
        """Crée une page d'index pour naviguer dans les gabarits"""
        
        html = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bibliothèque DSFR - Gabarits de production</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@gouvfr/dsfr@1.14.0/dist/dsfr.min.css">
    <style>
        .component-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 1rem;
            margin: 2rem 0;
        }
        .variant-list {
            list-style: none;
            padding: 0;
            margin: 0.5rem 0;
        }
        .variant-list li {
            margin: 0.25rem 0;
        }
        pre {
            background: #f6f8fa;
            padding: 1rem;
            border-radius: 4px;
            overflow-x: auto;
        }
    </style>
</head>
<body>
    <header role="banner" class="fr-header">
        <div class="fr-header__body">
            <div class="fr-container">
                <div class="fr-header__body-row">
                    <div class="fr-header__brand fr-enlarge-link">
                        <div class="fr-header__brand-top">
                            <div class="fr-header__logo">
                                <p class="fr-logo">République<br>Française</p>
                            </div>
                        </div>
                        <div class="fr-header__service">
                            <p class="fr-header__service-title">
                                Bibliothèque DSFR - Gabarits de production
                            </p>
                            <p class="fr-header__service-tagline">
                                HTML prêt à l'emploi pour vos projets
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </header>
    
    <main id="main" role="main" class="fr-container fr-py-8w">
        <h1>Gabarits HTML DSFR v1.14.1</h1>
        
        <div class="fr-alert fr-alert--info">
            <p class="fr-alert__title">Mode d'emploi</p>
            <p>
                Ces gabarits sont du HTML pur, prêt à copier-coller dans vos projets.
                Chaque variante est un fichier HTML autonome avec les bonnes classes et structure DSFR.
            </p>
        </div>
        
        <div class="component-grid">
"""
        
        # Ajouter les composants
        for component_name in sorted(self.production_templates.keys()):
            variants = self.production_templates[component_name]
            
            html += f"""
            <div class="fr-card">
                <div class="fr-card__body">
                    <div class="fr-card__content">
                        <h3 class="fr-card__title">{component_name.upper()}</h3>
                        <p class="fr-card__desc">{len(variants)} variantes disponibles</p>
                        <ul class="variant-list">
"""
            
            for variant in sorted(variants.keys()):
                file_path = f"{component_name}/{component_name}_{variant}.html"
                html += f"""                            <li>
                                <a href="{file_path}" class="fr-link">
                                    {variant.replace('_', ' ').title()}
                                </a>
                            </li>
"""
            
            html += """                        </ul>
                    </div>
                </div>
            </div>
"""
        
        html += """        </div>
        
        <h2>Utilisation</h2>
        
        <div class="fr-highlight">
            <p>Pour utiliser un gabarit :</p>
            <ol>
                <li>Choisissez le composant et la variante</li>
                <li>Copiez le code HTML</li>
                <li>Remplacez les valeurs par défaut par vos données</li>
                <li>Intégrez dans votre projet avec les CSS/JS DSFR</li>
            </ol>
        </div>
        
        <h2>Intégration DSFR</h2>
        
        <pre><code>&lt;!-- CSS DSFR --&gt;
&lt;link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@gouvfr/dsfr@1.14.0/dist/dsfr.min.css"&gt;

&lt;!-- JS DSFR --&gt;
&lt;script type="module" src="https://cdn.jsdelivr.net/npm/@gouvfr/dsfr@1.14.0/dist/dsfr.module.min.js"&gt;&lt;/script&gt;
&lt;script nomodule src="https://cdn.jsdelivr.net/npm/@gouvfr/dsfr@1.14.0/dist/dsfr.nomodule.min.js"&gt;&lt;/script&gt;</code></pre>
    </main>
    
    <footer class="fr-footer" role="contentinfo">
        <div class="fr-container">
            <div class="fr-footer__body">
                <div class="fr-footer__brand fr-enlarge-link">
                    <p class="fr-logo">République<br>Française</p>
                </div>
                <div class="fr-footer__content">
                    <p class="fr-footer__content-desc">
                        Gabarits DSFR de production - Générés automatiquement
                    </p>
                </div>
            </div>
        </div>
    </footer>
</body>
</html>"""
        
        with open(os.path.join(self.output_dir, "index.html"), 'w', encoding='utf-8') as f:
            f.write(html)
    
    def create_json_library(self):
        """Crée un fichier JSON avec tous les snippets pour usage programmatique"""
        
        library = {
            "version": "1.14.1",
            "generated": datetime.now().isoformat(),
            "components": {}
        }
        
        for component_name, variants in self.production_templates.items():
            library["components"][component_name] = {
                "variants": variants,
                "count": len(variants)
            }
        
        with open(os.path.join(self.output_dir, "dsfr_library.json"), 'w', encoding='utf-8') as f:
            json.dump(library, f, indent=2, ensure_ascii=False)
        
        print(f"  📄 Bibliothèque JSON créée : dsfr_library.json")

def main():
    builder = DSFRProductionBuilder()
    builder.build_html_library()
    
    print("\n[CIBLE] Assistant DSFR de production prêt !")
    print("   Ouvrez 'gabarits/index.html' pour naviguer dans les templates")

if __name__ == "__main__":
    main()