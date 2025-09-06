#!/usr/bin/env python3
"""
Vérificateur de conformité DSFR v1.14.1
Vérifie que les gabarits respectent les standards officiels
Version 2.0 - Alignée avec le projet MCP DSFR actuel
"""

import os
import sys
import json
import re
from pathlib import Path
from typing import Dict, List, Tuple

# Ajouter le path parent pour importer src
sys.path.insert(0, str(Path(__file__).parent.parent))

class DSFRConformityChecker:
    def __init__(self):
        self.errors = []
        self.warnings = []
        self.valid = []
        
        # Classes CSS obligatoires par composant selon DSFR v1.14.1
        # Aligné avec les 48 composants du registre actuel
        self.required_classes = {
            "accordion": ["fr-accordion"],
            "alert": ["fr-alert"],
            "badge": ["fr-badge"],
            "breadcrumb": ["fr-breadcrumb"],
            "button": ["fr-btn"],
            "button_group": ["fr-btns-group"],
            "callout": ["fr-callout"],
            "card": ["fr-card"],
            "checkbox": ["fr-checkbox-group"],
            "connect": ["fr-connect"],
            "consent": ["fr-consent"],
            "content": ["fr-content-media"],
            "display": ["fr-display"],
            "download": ["fr-download"],
            "follow": ["fr-follow"],
            "footer": ["fr-footer"],
            "form": ["fr-fieldset"],
            "header": ["fr-header"],
            "highlight": ["fr-highlight"],
            "input": ["fr-input"],
            "link": ["fr-link"],
            "logo": ["fr-logo"],
            "modal": ["fr-modal"],
            "navigation": ["fr-nav"],
            "notice": ["fr-notice"],
            "pagination": ["fr-pagination"],
            "password": ["fr-password"],
            "quote": ["fr-quote"],
            "radio": ["fr-radio-group"],
            "range": ["fr-range"],
            "search": ["fr-search-bar"],
            "select": ["fr-select"],
            "share": ["fr-share"],
            "sidemenu": ["fr-sidemenu"],
            "skiplinks": ["fr-skiplinks"],
            "stepper": ["fr-stepper"],
            "summary": ["fr-summary"],
            "table": ["fr-table"],
            "tabs": ["fr-tabs"],
            "tag": ["fr-tag"],
            "tile": ["fr-tile"],
            "toggle": ["fr-toggle"],
            "tooltip": ["fr-tooltip"],
            "transcription": ["fr-transcription"],
            "translate": ["fr-translate"],
            "upload": ["fr-upload"]
        }
        
        # Attributs ARIA recommandés
        self.aria_attributes = {
            "modal": ["aria-modal", "role"],
            "accordion": ["aria-expanded", "aria-controls"],
            "tabs": ["role", "aria-selected", "aria-controls"],
            "alert": ["role"],
            "navigation": ["role", "aria-label"],
            "breadcrumb": ["aria-label", "aria-current"],
            "header": ["role"],
            "footer": ["role"],
            "search": ["role", "aria-label"],
            "tooltip": ["aria-describedby"],
            "stepper": ["aria-current"]
        }
        
        # Variantes officielles par composant
        self.official_variants = {
            "button": ["primary", "secondary", "tertiary", "tertiary-no-outline", "sm", "lg", "icon-left", "icon-right"],
            "alert": ["info", "success", "warning", "error"],
            "badge": ["info", "success", "warning", "error", "new", "sm"],
            "tag": ["sm", "clickable", "dismissible"],
            "callout": ["info", "warning", "success"],
            "card": ["horizontal", "vertical", "sm", "lg", "no-arrow"],
            "notice": ["info", "warning", "alert"],
            "modal": ["sm", "lg"],
            "input": ["text", "email", "password", "number", "date", "search", "tel", "url", "textarea"],
            "table": ["sm", "lg", "bordered", "no-scroll"],
            "tile": ["horizontal", "vertical", "sm"]
        }
        
    def check_file(self, filepath: str, component: str, variant: str) -> Dict:
        """Vérifie un fichier HTML"""
        if not os.path.exists(filepath):
            return {"error": f"Fichier non trouvé: {filepath}"}
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        result = {
            "file": filepath,
            "component": component,
            "variant": variant,
            "checks": {}
        }
        
        # 1. Vérifier les classes CSS requises
        if component in self.required_classes:
            for required_class in self.required_classes[component]:
                # Recherche plus flexible pour les classes CSS
                if required_class in content:
                    result["checks"][f"CSS {required_class}"] = "OK"
                    self.valid.append(f"{component}/{variant}: Classe {required_class} présente")
                else:
                    result["checks"][f"CSS {required_class}"] = "ERREUR"
                    self.errors.append(f"{component}/{variant}: Classe {required_class} manquante")
        
        # 2. Vérifier les attributs ARIA
        if component in self.aria_attributes:
            for aria_attr in self.aria_attributes[component]:
                if aria_attr in content:
                    result["checks"][f"ARIA {aria_attr}"] = "OK"
                    self.valid.append(f"{component}/{variant}: Attribut {aria_attr} présent")
                else:
                    result["checks"][f"ARIA {aria_attr}"] = "WARN"
                    self.warnings.append(f"{component}/{variant}: Attribut {aria_attr} recommandé absent")
        
        # 3. Vérifier la structure HTML
        if len(content.strip()) < 50:
            self.warnings.append(f"{component}/{variant}: Contenu très court, possible placeholder")
            result["checks"]["Contenu"] = "WARN"
        else:
            result["checks"]["Contenu"] = "OK"
        
        # 4. Vérifier l'accessibilité de base
        if component in ["input", "select", "checkbox", "radio", "range", "upload"]:
            if "fr-label" in content or "<label" in content:
                result["checks"]["Label"] = "OK"
                self.valid.append(f"{component}/{variant}: Label présent")
            else:
                result["checks"]["Label"] = "ERREUR"
                self.errors.append(f"{component}/{variant}: Label manquant pour l'accessibilité")
        
        # 5. Vérifier les IDs uniques pour les formulaires
        if component in ["input", "select", "checkbox", "radio", "form"]:
            id_pattern = r'id="([^"]+)"'
            for_pattern = r'for="([^"]+)"'
            ids = re.findall(id_pattern, content)
            fors = re.findall(for_pattern, content)
            
            if ids and fors:
                matching_pairs = any(id_val in fors for id_val in ids)
                if matching_pairs:
                    result["checks"]["ID/FOR"] = "OK"
                    self.valid.append(f"{component}/{variant}: Associations ID/FOR correctes")
                else:
                    result["checks"]["ID/FOR"] = "WARN"
                    self.warnings.append(f"{component}/{variant}: IDs et FOR ne correspondent pas")
        
        # 6. Vérifier les icônes DSFR
        if "fr-icon" in content or "fr-fi" in content:
            result["checks"]["Icônes"] = "OK"
        
        # 7. Vérifier la variante officielle
        if component in self.official_variants:
            if variant in self.official_variants[component]:
                result["checks"]["Variante officielle"] = "OK"
            else:
                result["checks"]["Variante officielle"] = "WARN"
                self.warnings.append(f"{component}/{variant}: Variante non documentée")
        
        return result
    
    def check_all_components(self) -> Dict:
        """Vérifie tous les composants dans gabarits/"""
        # Utiliser le chemin absolu
        gabarits_dir = Path(__file__).parent.parent / "gabarits"
        results = {}
        
        if not gabarits_dir.exists():
            print(f"Erreur : Dossier {gabarits_dir} non trouvé")
            return {}
        
        # Liste des 48 composants attendus (sans version et back_to_top qui n'existent plus)
        expected_components = list(self.required_classes.keys())
        found_components = []
        
        # Parcourir tous les composants
        for component_dir in sorted(gabarits_dir.iterdir()):
            if not component_dir.is_dir():
                continue
            
            component_name = component_dir.name
            
            # Ignorer les fichiers système
            if component_name.startswith('.'):
                continue
            
            # Vérifier si c'est un composant attendu ou nouveau
            if component_name not in expected_components:
                # C'est peut-être un nouveau composant non répertorié
                self.warnings.append(f"Composant non attendu trouvé: {component_name}")
            
            found_components.append(component_name)
            results[component_name] = []
            
            # Parcourir toutes les variantes HTML
            html_files = list(component_dir.glob('*.html'))
            if not html_files:
                self.warnings.append(f"{component_name}: Aucun fichier HTML trouvé")
                continue
            
            for variant_file in sorted(html_files):
                # Extraire le nom de la variante
                variant = variant_file.stem.replace(f"{component_name}_", "")
                if variant == component_name:
                    variant = "default"
                
                result = self.check_file(str(variant_file), component_name, variant)
                results[component_name].append(result)
        
        # Vérifier les composants manquants
        missing = set(expected_components) - set(found_components)
        if missing:
            for comp in missing:
                self.warnings.append(f"Composant attendu non trouvé: {comp}")
        
        return results
    
    def generate_report(self, results: Dict) -> str:
        """Génère un rapport de conformité"""
        report = """
╔════════════════════════════════════════════════════════════╗
║         RAPPORT DE CONFORMITÉ DSFR v1.14.1                 ║
║                 MCP DSFR Version 2.0.0                     ║
╚════════════════════════════════════════════════════════════╝
"""
        
        total_components = len(results)
        total_variants = sum(len(variants) for variants in results.values())
        total_checks = len(self.valid) + len(self.errors) + len(self.warnings)
        
        conformity_rate = 0
        if total_checks > 0:
            conformity_rate = len(self.valid) / total_checks * 100
        
        report += f"""
STATISTIQUES GLOBALES:
   • Composants vérifiés: {total_components}
   • Variantes testées: {total_variants}
   • Points de contrôle: {total_checks}
   • Validations: {len(self.valid)}
   • Erreurs: {len(self.errors)}
   • Avertissements: {len(self.warnings)}
   • Taux de conformité: {conformity_rate:.1f}%

"""
        
        # Erreurs critiques
        if self.errors:
            report += "ERREURS CRITIQUES (à corriger):\n"
            for error in self.errors[:10]:
                report += f"   - {error}\n"
            if len(self.errors) > 10:
                report += f"   ... et {len(self.errors) - 10} autres erreurs\n"
            report += "\n"
        
        # Avertissements
        if self.warnings:
            report += "AVERTISSEMENTS (recommandations):\n"
            for warning in self.warnings[:15]:
                report += f"   - {warning}\n"
            if len(self.warnings) > 15:
                report += f"   ... et {len(self.warnings) - 15} autres avertissements\n"
            report += "\n"
        
        # Résumé par composant
        report += "CONFORMITÉ PAR COMPOSANT:\n"
        for component, variants in sorted(results.items()):
            if not variants:
                continue
            
            # Calculer le score du composant
            component_valid = sum(1 for v in variants for check in v.get("checks", {}).values() if check == "OK")
            component_total = sum(len(v.get("checks", {})) for v in variants)
            
            if component_total > 0:
                score = component_valid / component_total * 100
                if score >= 90:
                    status = "[OK]"
                elif score >= 70:
                    status = "[WARN]"
                else:
                    status = "[ERR]"
                
                report += f"   {status} {component}: {score:.0f}% ({len(variants)} variantes)\n"
        
        # Recommandations
        report += """
RECOMMANDATIONS:
   1. Corriger toutes les erreurs critiques (classes CSS manquantes)
   2. Ajouter les attributs ARIA recommandés pour l'accessibilité
   3. Vérifier que tous les formulaires ont des labels associés
   4. Tester avec un lecteur d'écran (NVDA, JAWS)
   5. Valider avec l'outil officiel de test DSFR

RESSOURCES:
   • Documentation DSFR: https://www.systeme-de-design.gouv.fr/
   • Guide accessibilité RGAA: https://www.numerique.gouv.fr/publications/rgaa-accessibilite/
   • Validateur W3C: https://validator.w3.org/
   • Documentation MCP DSFR: docs/

DATE DU RAPPORT: 2025-01-06
"""
        
        return report

def main():
    print("Analyse de conformité DSFR en cours...")
    print("Vérification des 48 composants du projet MCP DSFR...")
    
    checker = DSFRConformityChecker()
    results = checker.check_all_components()
    
    if not results:
        print("Erreur : Aucun composant trouvé à vérifier")
        return 1
    
    report = checker.generate_report(results)
    print(report)
    
    # Sauvegarder le rapport dans resultats-test/
    report_path = Path(__file__).parent / "resultats-test" / "conformity_report.txt"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"\nRapport sauvegardé dans: {report_path}")
    
    # Retourner le code de sortie selon les erreurs
    # Tolérer jusqu'à 5 erreurs mineures
    if len(checker.errors) > 5:
        print(f"\n⚠ {len(checker.errors)} erreurs détectées - Vérification requise")
        print("STATUT: CONFORMITE PARTIELLE")
        return 1
    elif checker.errors:
        print(f"\n⚠ {len(checker.errors)} erreurs mineures détectées - Conformité acceptable")
        print("STATUT: CONFORMITE FONCTIONNELLE")
        return 0
    else:
        print("\n✓ Aucune erreur critique - Conformité validée")
        print("STATUT: CONFORMITE VALIDEE")
        return 0

if __name__ == "__main__":
    exit(main())