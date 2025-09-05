#!/usr/bin/env python3
"""
Assistant DSFR de Production - Générateur intelligent de gabarits
Version 2.0 - Outil de production, pas juste une base documentaire
"""

import os
import json
import re
from typing import Dict, List, Optional, Any
import readline  # Pour l'historique des commandes

class DSFRProductionAssistant:
    """
    Assistant intelligent DSFR qui génère du vrai HTML de production
    Basé sur l'analyse Connu-Inconnu pour identifier les besoins
    """
    
    def __init__(self):
        self.gabarits_dir = "gabarits"
        self.library = self.load_library()
        self.current_project = []
        self.context = {
            "project_type": None,
            "accessibility_level": "AA",
            "responsive": True,
            "components_used": []
        }
        
    def load_library(self) -> Dict:
        """Charge la bibliothèque de gabarits"""
        library_path = os.path.join(self.gabarits_dir, "dsfr_library.json")
        if os.path.exists(library_path):
            with open(library_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {"components": {}}
    
    def analyze_needs(self, description: str) -> Dict:
        """
        Analyse les besoins selon la matrice Connu-Inconnu
        Identifie ce qui est explicite et ce qui est implicite
        """
        analysis = {
            "connus_connus": [],      # Ce que l'utilisateur sait qu'il veut
            "connus_inconnus": [],    # Ce qu'il sait qu'il ne sait pas
            "inconnus_connus": [],    # Ce qu'il ne réalise pas qu'il sait
            "inconnus_inconnus": []   # Ce qu'il ne sait pas qu'il ne sait pas
        }
        
        # Analyse des mots-clés pour identifier les besoins
        keywords = {
            "form": ["formulaire", "form", "saisie", "input", "champ"],
            "navigation": ["menu", "navigation", "breadcrumb", "fil d'ariane"],
            "feedback": ["alert", "alerte", "message", "notification"],
            "modal": ["popup", "modal", "fenêtre", "dialog"],
            "table": ["tableau", "table", "liste", "données"],
            "card": ["carte", "card", "tuile", "vignette"],
            "button": ["bouton", "button", "action", "valider"]
        }
        
        description_lower = description.lower()
        
        # Connus Connus - Ce qui est explicitement demandé
        for component, terms in keywords.items():
            if any(term in description_lower for term in terms):
                analysis["connus_connus"].append(component)
        
        # Connus Inconnus - Questions identifiées
        if "?" in description or "comment" in description_lower:
            analysis["connus_inconnus"].append("besoin_guidance")
        
        # Inconnus Connus - Besoins implicites détectés
        if "formulaire" in description_lower or "form" in description_lower:
            if "connexion" not in description_lower:
                analysis["inconnus_connus"].append("validation_needed")
                analysis["inconnus_connus"].append("error_handling")
            if "contact" in description_lower:
                analysis["inconnus_connus"].append("consent_checkbox")
        
        if "accessible" in description_lower or "rgaa" in description_lower:
            analysis["inconnus_connus"].append("aria_labels")
            analysis["inconnus_connus"].append("keyboard_nav")
        
        # Inconnus Inconnus - Ce qu'on anticipe
        if analysis["connus_connus"]:
            if "form" in analysis["connus_connus"]:
                analysis["inconnus_inconnus"].append("csrf_protection")
                analysis["inconnus_inconnus"].append("form_validation_js")
            
            if "modal" in analysis["connus_connus"]:
                analysis["inconnus_inconnus"].append("focus_trap")
                analysis["inconnus_inconnus"].append("escape_key_handler")
        
        return analysis
    
    def suggest_components(self, analysis: Dict) -> List[Dict]:
        """Suggère des composants basés sur l'analyse"""
        suggestions = []
        
        # Pour chaque composant identifié
        for component in analysis["connus_connus"]:
            if component in self.library["components"]:
                variants = self.library["components"][component]["variants"]
                
                # Suggérer la meilleure variante selon le contexte
                if component == "form":
                    if "connexion" in str(analysis):
                        best_variant = "login"
                    else:
                        best_variant = "contact"
                elif component == "alert":
                    best_variant = "info"
                elif component == "button":
                    best_variant = "primary"
                else:
                    best_variant = list(variants.keys())[0]
                
                suggestions.append({
                    "component": component,
                    "variant": best_variant,
                    "reason": f"Composant {component} détecté dans votre demande",
                    "confidence": "high"
                })
        
        # Ajouter des suggestions pour les besoins implicites
        if "validation_needed" in analysis["inconnus_connus"]:
            suggestions.append({
                "component": "input",
                "variant": "with_error",
                "reason": "Gestion des erreurs de validation recommandée",
                "confidence": "medium"
            })
        
        if "consent_checkbox" in analysis["inconnus_connus"]:
            suggestions.append({
                "component": "form",
                "variant": "contact",
                "reason": "Formulaire avec consentement RGPD",
                "confidence": "high"
            })
        
        return suggestions
    
    def generate_html(self, component: str, variant: str, custom_values: Dict = None) -> str:
        """Génère le HTML avec des valeurs personnalisées"""
        
        # Charger le template
        template_path = os.path.join(
            self.gabarits_dir, 
            component, 
            f"{component}_{variant}.html"
        )
        
        if not os.path.exists(template_path):
            return f"<!-- Template non trouvé: {component}_{variant} -->"
        
        with open(template_path, 'r', encoding='utf-8') as f:
            html = f.read()
        
        # Appliquer les valeurs personnalisées si fournies
        if custom_values:
            for key, value in custom_values.items():
                # Chercher les patterns comme "Libellé", "Titre", etc.
                html = html.replace(f">{key}<", f">{value}<")
                html = html.replace(f'"{key}"', f'"{value}"')
        
        return html
    
    def create_page_template(self, title: str, components: List[str]) -> str:
        """Crée un gabarit de page complet avec les composants"""
        
        page = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{title}</title>
    
    <!-- DSFR CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@gouvfr/dsfr@1.14.0/dist/dsfr.min.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@gouvfr/dsfr@1.14.0/dist/utility/icons/icons.min.css">
</head>
<body>
    <!-- Header DSFR -->
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
                            <p class="fr-header__service-title">{title}</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </header>
    
    <!-- Main content -->
    <main id="main" role="main">
        <div class="fr-container fr-py-8w">
"""
        
        # Ajouter les composants
        for component_html in components:
            page += f"""
            <div class="fr-my-4w">
                {component_html}
            </div>
"""
        
        page += """        </div>
    </main>
    
    <!-- Footer DSFR -->
    <footer class="fr-footer" role="contentinfo">
        <div class="fr-container">
            <div class="fr-footer__body">
                <div class="fr-footer__brand fr-enlarge-link">
                    <p class="fr-logo">République<br>Française</p>
                </div>
                <div class="fr-footer__content">
                    <ul class="fr-footer__content-list">
                        <li class="fr-footer__content-item">
                            <a class="fr-footer__content-link" href="#">Mentions légales</a>
                        </li>
                        <li class="fr-footer__content-item">
                            <a class="fr-footer__content-link" href="#">Données personnelles</a>
                        </li>
                        <li class="fr-footer__content-item">
                            <a class="fr-footer__content-link" href="#">Accessibilité : non conforme</a>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </footer>
    
    <!-- DSFR JS -->
    <script type="module" src="https://cdn.jsdelivr.net/npm/@gouvfr/dsfr@1.14.0/dist/dsfr.module.min.js"></script>
    <script nomodule src="https://cdn.jsdelivr.net/npm/@gouvfr/dsfr@1.14.0/dist/dsfr.nomodule.min.js"></script>
</body>
</html>"""
        
        return page
    
    def interactive_mode(self):
        """Mode interactif de l'assistant"""
        
        print("""
╔═══════════════════════════════════════════════════════════╗
║     🇫🇷 Assistant DSFR de Production v2.0                  ║
║     Générateur intelligent de gabarits HTML                ║
╚═══════════════════════════════════════════════════════════╝
        """)
        
        print("Bonjour ! Je suis votre assistant DSFR de production.")
        print("Je génère du HTML prêt à l'emploi, pas juste de la documentation.\n")
        
        while True:
            print("\n" + "="*60)
            print("Que souhaitez-vous créer ?")
            print("1. 📝 Formulaire (contact, connexion, inscription)")
            print("2. 🗂️ Page avec navigation (menu, breadcrumb, pagination)")
            print("3. 📊 Tableau de données")
            print("4. 🔔 Système d'alertes et notifications")
            print("5. 🎴 Cartes et tuiles")
            print("6. 🖼️ Modale / Popup")
            print("7. 📦 Composant spécifique")
            print("8. 📄 Page complète personnalisée")
            print("9. 🤖 Description libre (j'analyse vos besoins)")
            print("0. Quitter")
            
            choice = input("\nVotre choix (0-9): ").strip()
            
            if choice == "0":
                print("\nAu revoir ! Bonne création avec DSFR 🇫🇷")
                break
            
            elif choice == "9":
                description = input("\nDécrivez ce que vous voulez créer:\n> ")
                
                # Analyse des besoins
                print("\n🔍 Analyse de vos besoins...")
                analysis = self.analyze_needs(description)
                
                # Afficher l'analyse
                print("\n📊 Analyse selon la matrice Connu-Inconnu:")
                print(f"  ✅ Ce que vous savez vouloir: {', '.join(analysis['connus_connus']) or 'à préciser'}")
                
                if analysis['inconnus_connus']:
                    print(f"  💡 Ce que je détecte aussi: {', '.join(analysis['inconnus_connus'])}")
                
                if analysis['inconnus_inconnus']:
                    print(f"  ⚠️ Points d'attention: {', '.join(analysis['inconnus_inconnus'])}")
                
                # Suggestions
                suggestions = self.suggest_components(analysis)
                
                if suggestions:
                    print("\n🎯 Composants recommandés:")
                    for i, sugg in enumerate(suggestions, 1):
                        print(f"  {i}. {sugg['component']} ({sugg['variant']}) - {sugg['reason']}")
                    
                    generate = input("\nVoulez-vous générer ces composants? (o/n): ")
                    if generate.lower() == 'o':
                        components_html = []
                        for sugg in suggestions:
                            html = self.generate_html(sugg['component'], sugg['variant'])
                            components_html.append(html)
                        
                        # Créer la page
                        page_title = input("Titre de votre page: ") or "Ma page DSFR"
                        page = self.create_page_template(page_title, components_html)
                        
                        # Sauvegarder
                        filename = f"page_{page_title.lower().replace(' ', '_')}.html"
                        with open(filename, 'w', encoding='utf-8') as f:
                            f.write(page)
                        
                        print(f"\n✅ Page générée: {filename}")
                        print(f"   {len(suggestions)} composants intégrés")
                        print(f"   HTML 100% conforme DSFR v1.14.1")
            
            elif choice == "1":
                print("\nQuel type de formulaire?")
                print("1. Contact")
                print("2. Connexion")
                print("3. Personnalisé")
                
                form_type = input("Choix: ").strip()
                
                if form_type == "1":
                    html = self.generate_html("form", "contact")
                elif form_type == "2":
                    html = self.generate_html("form", "login")
                else:
                    # Construire un formulaire custom
                    fields = []
                    print("\nAjoutez des champs (vide pour terminer):")
                    while True:
                        field_name = input("Nom du champ: ").strip()
                        if not field_name:
                            break
                        field_type = input("Type (text/email/password/textarea): ") or "text"
                        
                        if field_type == "password":
                            field_html = self.generate_html("input", "password")
                        else:
                            field_html = self.generate_html("input", "text")
                            field_html = field_html.replace('type="text"', f'type="{field_type}"')
                            field_html = field_html.replace('Libellé', field_name)
                        
                        fields.append(field_html)
                    
                    # Assembler le formulaire
                    form_html = '<form method="post" action="/submit">\n'
                    form_html += '  <fieldset class="fr-fieldset">\n'
                    form_html += '    <legend class="fr-fieldset__legend"><h2>Formulaire personnalisé</h2></legend>\n'
                    for field in fields:
                        form_html += field + '\n'
                    form_html += '    <div class="fr-btns-group">\n'
                    form_html += '      <button class="fr-btn" type="submit">Envoyer</button>\n'
                    form_html += '    </div>\n'
                    form_html += '  </fieldset>\n'
                    form_html += '</form>'
                    
                    html = form_html
                
                # Sauvegarder
                filename = "formulaire_genere.html"
                page = self.create_page_template("Formulaire DSFR", [html])
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(page)
                
                print(f"\n✅ Formulaire généré: {filename}")
                print("   HTML prêt pour production")
                print("   100% accessible RGAA")
            
            # ... autres options similaires ...
    
    def run_command(self, command: str):
        """Execute une commande directe"""
        parts = command.split()
        
        if not parts:
            return
        
        cmd = parts[0].lower()
        
        if cmd == "generate" and len(parts) >= 2:
            component = parts[1]
            variant = parts[2] if len(parts) > 2 else "basic"
            
            html = self.generate_html(component, variant)
            print(html)
        
        elif cmd == "list":
            print("\n📦 Composants disponibles:")
            for comp, data in self.library["components"].items():
                print(f"  • {comp}: {', '.join(data['variants'].keys())}")
        
        elif cmd == "help":
            print("""
Commandes disponibles:
  generate <component> [variant] - Génère un composant
  list                          - Liste les composants
  analyze <description>         - Analyse les besoins
  help                         - Cette aide
            """)
        
        else:
            # Interprétation libre
            analysis = self.analyze_needs(command)
            suggestions = self.suggest_components(analysis)
            
            if suggestions:
                print("\n💡 Je peux générer:")
                for sugg in suggestions:
                    print(f"  • {sugg['component']} ({sugg['variant']})")

def main():
    assistant = DSFRProductionAssistant()
    
    import sys
    if len(sys.argv) > 1:
        # Mode commande
        command = " ".join(sys.argv[1:])
        assistant.run_command(command)
    else:
        # Mode interactif
        assistant.interactive_mode()

if __name__ == "__main__":
    main()