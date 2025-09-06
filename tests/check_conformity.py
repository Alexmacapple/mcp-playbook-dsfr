#!/usr/bin/env python3
"""
Vérificateur de conformité DSFR v1.14.1
Vérifie que les gabarits respectent les standards officiels
"""

import os
import json
import re
from typing import Dict, List, Tuple

class DSFRConformityChecker:
    def __init__(self):
        self.errors = []
        self.warnings = []
        self.valid = []
        
        # Classes CSS obligatoires par composant selon DSFR v1.14.1
        self.required_classes = {
            "button": ["fr-btn"],
            "input": ["fr-input", "fr-input-group", "fr-label"],
            "alert": ["fr-alert"],
            "card": ["fr-card"],
            "modal": ["fr-modal"],
            "accordion": ["fr-accordion"],
            "table": ["fr-table"],
            "form": ["fr-fieldset"],
            "navigation": ["fr-nav"],
            "breadcrumb": ["fr-breadcrumb"],
            "badge": ["fr-badge"],
            "tag": ["fr-tag"],
            "toggle": ["fr-toggle"],
            "checkbox": ["fr-checkbox-group"],
            "radio": ["fr-radio-group"],
            "select": ["fr-select", "fr-select-group"],
            "header": ["fr-header"],
            "footer": ["fr-footer"],
            "callout": ["fr-callout"],
            "highlight": ["fr-highlight"],
            "quote": ["fr-quote"],
            "tile": ["fr-tile"],
            "tabs": ["fr-tabs"],
            "stepper": ["fr-stepper"],
            "summary": ["fr-summary"],
            "link": ["fr-link"],
            "password": ["fr-input", "fr-password"],
            "range": ["fr-range"],
            "search": ["fr-search-bar"],
            "upload": ["fr-upload"],
            "notice": ["fr-notice"],
            "content": ["fr-content"],
            "pagination": ["fr-pagination"],
            "sidemenu": ["fr-sidemenu"],
            "skiplinks": ["fr-skiplinks"],
            "tooltip": ["fr-tooltip"],
            "transcription": ["fr-transcription"],
            "consent": ["fr-consent-banner"],
            "share": ["fr-share"],
            "follow": ["fr-follow"],
            "connect": ["fr-connect"],
            "translate": ["fr-translate"],
            "download": ["fr-download"],
            "display": ["fr-display"],
            "logo": ["fr-logo"],
            "version": ["fr-version"],
            "back_to_top": ["fr-btn--top"]
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
            "search": ["role", "aria-label"]
        }
        
        # Variantes officielles par composant
        self.official_variants = {
            "button": ["primary", "secondary", "tertiary", "tertiary-no-outline"],
            "alert": ["info", "success", "warning", "error"],
            "badge": ["info", "success", "warning", "error", "new"],
            "tag": ["sm", "md", "lg", "clickable", "dismiss"],
            "callout": ["info", "warning", "success"],
            "card": ["horizontal", "vertical", "tile"],
            "notice": ["info", "warning", "alert"]
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
                pattern = f'class="[^"]*{required_class}[^"]*"'
                if re.search(pattern, content):
                    result["checks"][f"CSS {required_class}"] = "✅"
                    self.valid.append(f"{component}/{variant}: Classe {required_class} présente")
                else:
                    result["checks"][f"CSS {required_class}"] = "❌"
                    self.errors.append(f"{component}/{variant}: Classe {required_class} manquante")
        
        # 2. Vérifier les attributs ARIA
        if component in self.aria_attributes:
            for aria_attr in self.aria_attributes[component]:
                if aria_attr in content:
                    result["checks"][f"ARIA {aria_attr}"] = "✅"
                    self.valid.append(f"{component}/{variant}: Attribut {aria_attr} présent")
                else:
                    result["checks"][f"ARIA {aria_attr}"] = "⚠️"
                    self.warnings.append(f"{component}/{variant}: Attribut {aria_attr} recommandé absent")
        
        # 3. Vérifier la structure HTML
        # Vérifier que ce n'est pas juste un placeholder
        if len(content.strip()) < 50:
            self.warnings.append(f"{component}/{variant}: Contenu très court, possible placeholder")
            result["checks"]["Contenu"] = "⚠️"
        else:
            result["checks"]["Contenu"] = "✅"
        
        # 4. Vérifier l'accessibilité de base
        # Labels pour les inputs
        if component in ["input", "select", "checkbox", "radio", "range"]:
            if "fr-label" in content or "<label" in content:
                result["checks"]["Label"] = "✅"
                self.valid.append(f"{component}/{variant}: Label présent")
            else:
                result["checks"]["Label"] = "❌"
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
                    result["checks"]["ID/FOR"] = "✅"
                    self.valid.append(f"{component}/{variant}: Associations ID/FOR correctes")
                else:
                    result["checks"]["ID/FOR"] = "⚠️"
                    self.warnings.append(f"{component}/{variant}: IDs et FOR ne correspondent pas")
        
        # 6. Vérifier les icônes DSFR
        if "fr-icon" in content or "fr-fi" in content:
            result["checks"]["Icônes"] = "✅"
        
        # 7. Vérifier la variante officielle
        if component in self.official_variants:
            if variant in self.official_variants[component]:
                result["checks"]["Variante officielle"] = "✅"
            else:
                result["checks"]["Variante officielle"] = "⚠️"
                self.warnings.append(f"{component}/{variant}: Variante non officielle (custom)")
        
        return result
    
    def check_all_components(self) -> Dict:
        """Vérifie tous les composants dans gabarits/"""
        gabarits_dir = "gabarits"
        results = {}
        
        if not os.path.exists(gabarits_dir):
            print("❌ Dossier gabarits/ non trouvé")
            return {}
        
        # Parcourir tous les composants
        for component_dir in sorted(os.listdir(gabarits_dir)):
            component_path = os.path.join(gabarits_dir, component_dir)
            
            if not os.path.isdir(component_path):
                continue
            
            results[component_dir] = []
            
            # Parcourir toutes les variantes
            for variant_file in sorted(os.listdir(component_path)):
                if not variant_file.endswith('.html'):
                    continue
                
                # Extraire le nom de la variante
                variant = variant_file.replace(f"{component_dir}_", "").replace(".html", "")
                filepath = os.path.join(component_path, variant_file)
                
                result = self.check_file(filepath, component_dir, variant)
                results[component_dir].append(result)
        
        return results
    
    def generate_report(self, results: Dict) -> str:
        """Génère un rapport de conformité"""
        report = """
╔════════════════════════════════════════════════════════════╗
║        📋 RAPPORT DE CONFORMITÉ DSFR v1.14.1               ║
╚════════════════════════════════════════════════════════════╝
"""
        
        total_components = len(results)
        total_variants = sum(len(variants) for variants in results.values())
        total_checks = len(self.valid) + len(self.errors) + len(self.warnings)
        
        report += f"""
📊 STATISTIQUES GLOBALES:
   • Composants vérifiés: {total_components}
   • Variantes testées: {total_variants}
   • Points de contrôle: {total_checks}
   • ✅ Validations: {len(self.valid)}
   • ❌ Erreurs: {len(self.errors)}
   • ⚠️ Avertissements: {len(self.warnings)}
   • Taux de conformité: {len(self.valid) / total_checks * 100:.1f}%

"""
        
        # Erreurs critiques
        if self.errors:
            report += "🚨 ERREURS CRITIQUES (à corriger):\n"
            for error in self.errors[:10]:  # Limiter à 10 erreurs
                report += f"   ❌ {error}\n"
            if len(self.errors) > 10:
                report += f"   ... et {len(self.errors) - 10} autres erreurs\n"
            report += "\n"
        
        # Avertissements
        if self.warnings:
            report += "⚠️ AVERTISSEMENTS (recommandations):\n"
            for warning in self.warnings[:10]:  # Limiter à 10 warnings
                report += f"   ⚠️ {warning}\n"
            if len(self.warnings) > 10:
                report += f"   ... et {len(self.warnings) - 10} autres avertissements\n"
            report += "\n"
        
        # Résumé par composant
        report += "📦 CONFORMITÉ PAR COMPOSANT:\n"
        for component, variants in results.items():
            if not variants:
                continue
            
            # Calculer le score du composant
            component_valid = sum(1 for v in variants for check in v.get("checks", {}).values() if check == "✅")
            component_total = sum(len(v.get("checks", {})) for v in variants)
            
            if component_total > 0:
                score = component_valid / component_total * 100
                if score >= 90:
                    status = "✅"
                elif score >= 70:
                    status = "⚠️"
                else:
                    status = "❌"
                
                report += f"   {status} {component}: {score:.0f}% ({len(variants)} variantes)\n"
        
        # Recommandations
        report += """
📌 RECOMMANDATIONS:
   1. Corriger toutes les erreurs critiques (classes CSS manquantes)
   2. Ajouter les attributs ARIA recommandés pour l'accessibilité
   3. Vérifier que tous les formulaires ont des labels associés
   4. Tester avec un lecteur d'écran (NVDA, JAWS)
   5. Valider avec l'outil officiel de test DSFR

🔗 RESSOURCES:
   • Documentation DSFR: https://www.systeme-de-design.gouv.fr/
   • Guide accessibilité RGAA: https://www.numerique.gouv.fr/publications/rgaa-accessibilite/
   • Validateur W3C: https://validator.w3.org/
"""
        
        return report

def main():
    print("🔍 Analyse de conformité DSFR en cours...")
    
    checker = DSFRConformityChecker()
    results = checker.check_all_components()
    
    if not results:
        print("❌ Aucun composant trouvé à vérifier")
        return
    
    report = checker.generate_report(results)
    print(report)
    
    # Sauvegarder le rapport
    with open("conformity_report.txt", 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"\n💾 Rapport sauvegardé dans: conformity_report.txt")
    
    # Retourner le code de sortie selon les erreurs
    if checker.errors:
        return 1  # Il y a des erreurs
    return 0  # Tout est OK

if __name__ == "__main__":
    exit(main())