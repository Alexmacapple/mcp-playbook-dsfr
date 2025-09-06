#!/usr/bin/env python3
"""
Script de test pour générer une page avec TOUS les composants DSFR.
Version 2.0 - Sans émojis - Aligné avec MCP DSFR
"""

import json
import os
from datetime import datetime
from pathlib import Path
import sys

# Ajouter le chemin parent
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.data import get_registry


def create_test_page():
    """Crée une page HTML de test avec tous les composants et génère un rapport."""
    
    # Créer le rapport de test
    output_dir = Path(__file__).parent / "resultats-test"
    output_dir.mkdir(parents=True, exist_ok=True)
    report_path = output_dir / "test_all_components_report.txt"
    
    report = []
    report.append("Test Page Complète - Tous les Composants DSFR")
    report.append("=" * 50)
    report.append(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report.append("Version: 2.0\n")
    
    try:
        # Obtenir le registre
        registry = get_registry()
        
        # Récupérer les statistiques
        stats = registry.get_stats()
        components = registry.list_components()
        
        report.append("STATISTIQUES:")
        report.append("-" * 30)
        report.append(f"  - Composants: {stats['components']}")
        report.append(f"  - Variantes: {stats['variants']}")
        report.append(f"  - Version DSFR: 1.14.1\n")
        
        # Créer le HTML de la page
        html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Test COMPLET - Tous les {stats['components']} composants DSFR</title>
    
    <!-- DSFR CSS -->
    <link rel="stylesheet" href="https://unpkg.com/@gouvfr/dsfr@1.14.1/dist/dsfr.min.css">
    <link rel="stylesheet" href="https://unpkg.com/@gouvfr/dsfr@1.14.1/dist/utility/utility.min.css">
    <link rel="stylesheet" href="https://unpkg.com/@gouvfr/dsfr@1.14.1/dist/utility/icons/icons.min.css">
    
    <style>
        .test-section {{
            margin: 4rem 0;
            padding: 2rem;
            border: 2px solid #e5e5e5;
            border-radius: 8px;
        }}
        .test-section h2 {{
            color: #000091;
            border-bottom: 3px solid #000091;
            padding-bottom: 1rem;
            margin-bottom: 2rem;
        }}
        .component-test {{
            margin: 2rem 0;
            padding: 1.5rem;
            background: #f6f8fa;
            border-left: 4px solid #000091;
        }}
        .variant-label {{
            font-weight: bold;
            color: #666;
            margin-bottom: 1rem;
            font-family: monospace;
        }}
        .component-wrapper {{
            padding: 1rem;
            background: white;
            border-radius: 4px;
            margin-top: 1rem;
        }}
        .stats-banner {{
            background: #000091;
            color: white;
            padding: 2rem;
            text-align: center;
            margin-bottom: 3rem;
        }}
        .stats-banner h1 {{
            margin: 0 0 1rem 0;
            color: #FFF;
        }}
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 1rem;
            max-width: 800px;
            margin: 0 auto;
        }}
        .stat {{
            background: rgba(255,255,255,0.1);
            padding: 1rem;
            border-radius: 4px;
        }}
        .stat-number {{
            font-size: 2rem;
            font-weight: bold;
        }}
        nav.test-nav {{
            position: sticky;
            top: 0;
            background: white;
            border-bottom: 2px solid #e5e5e5;
            padding: 1rem;
            z-index: 100;
            margin-bottom: 2rem;
        }}
        .nav-grid {{
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
        }}
        .nav-link {{
            padding: 0.25rem 0.5rem;
            background: #f0f0f0;
            text-decoration: none;
            border-radius: 4px;
            font-size: 0.875rem;
        }}
        .nav-link:hover {{
            background: #000091;
            color: white;
        }}
        .test-metadata {{
            background: #f0f8ff;
            padding: 1rem;
            border-radius: 4px;
            margin-bottom: 2rem;
            font-size: 0.9rem;
        }}
    </style>
</head>
<body>
    <!-- Header principal -->
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
                            <p class="fr-header__service-title">Test Complet DSFR</p>
                            <p class="fr-header__service-tagline">Tous les composants v1.14.1</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </header>

    <!-- Bannière de stats -->
    <div class="stats-banner">
        <h1>Page de test complète DSFR</h1>
        <div class="stats-grid">
            <div class="stat">
                <div class="stat-number">{stats['components']}</div>
                <div>Composants</div>
            </div>
            <div class="stat">
                <div class="stat-number">{stats['variants']}</div>
                <div>Variantes</div>
            </div>
            <div class="stat">
                <div class="stat-number">v1.14.1</div>
                <div>Version DSFR</div>
            </div>
        </div>
    </div>

    <main class="fr-container">
        <!-- Navigation rapide -->
        <nav class="test-nav" aria-label="Navigation rapide">
            <div class="nav-grid">
                {"".join(f'<a href="#{comp}" class="nav-link">{comp}</a>' for comp in sorted(components))}
            </div>
        </nav>

        <!-- Metadata -->
        <div class="test-metadata">
            <strong>Date de génération :</strong> {datetime.now().strftime("%d/%m/%Y à %H:%M:%S")}<br>
            <strong>Composants testés :</strong> {len(components)-1} / {len(components)}<br>
            <strong>Variantes totales :</strong> {stats['variants']}<br>
            <strong>Mode :</strong> Test de rendu complet<br>
            <strong>Note :</strong> Le composant 'consent' n'est pas affiché car il créerait un bandeau bloquant
        </div>
"""

        # Compteurs pour le rapport
        components_processed = 0
        variants_processed = 0
        errors = []
        
        # Ajouter chaque composant (exclure consent qui crée un bandeau bloquant)
        for comp_name in sorted(components):
            # Skip consent component in test page as it creates a blocking banner
            if comp_name == "consent":
                continue
            
            try:
                variants = registry.list_variants(comp_name)
                if not variants:
                    variants = ["default"]
                
                html += f"""
        <!-- ========== {comp_name.upper()} ========== -->
        <section class="test-section" id="{comp_name}">
            <h2>{comp_name.replace('_', ' ').title()} ({len(variants)} variante{"s" if len(variants) > 1 else ""})</h2>
"""
                
                # Ajouter chaque variante
                for variant_name in variants:
                    try:
                        variant_html = registry.get_variant_html(comp_name, variant_name)
                        if not variant_html:
                            variant_html = f"<!-- Variante non trouvée : {comp_name}/{variant_name} -->"
                        
                        html += f"""
            <div class="component-test">
                <div class="variant-label">
                    Variante : <code>{variant_name}</code>
                </div>
                <div class="component-wrapper">
                    {variant_html}
                </div>
            </div>
"""
                        variants_processed += 1
                    except Exception as e:
                        errors.append(f"Erreur variante {comp_name}/{variant_name}: {str(e)}")
                
                html += """
        </section>
"""
                components_processed += 1
                
            except Exception as e:
                errors.append(f"Erreur composant {comp_name}: {str(e)}")

        # Footer
        html += """
    </main>

    <!-- Footer DSFR -->
    <footer class="fr-footer" role="contentinfo">
        <div class="fr-container">
            <div class="fr-footer__body">
                <div class="fr-footer__brand">
                    <p class="fr-logo">République<br>Française</p>
                </div>
                <div class="fr-footer__content">
                    <p class="fr-footer__content-desc">
                        Page de test générée automatiquement pour vérifier le rendu de tous les composants DSFR
                    </p>
                    <ul class="fr-footer__content-list">
                        <li class="fr-footer__content-item">
                            <a class="fr-footer__content-link" href="#">Test DSFR v1.14.1</a>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </footer>

    <!-- DSFR JS -->
    <script type="module" src="https://unpkg.com/@gouvfr/dsfr@1.14.1/dist/dsfr.module.min.js"></script>
    <script nomodule src="https://unpkg.com/@gouvfr/dsfr@1.14.1/dist/dsfr.nomodule.min.js"></script>
    
    <script>
        // Initialiser les composants DSFR
        window.addEventListener('DOMContentLoaded', function() {
            console.log('[OK] Page de test chargée');
            console.log('Composants:', """ + str(stats['components']) + """);
            console.log('Variantes:', """ + str(stats['variants']) + """);
        });
    </script>
</body>
</html>
"""
        
        # Sauvegarder le fichier HTML dans le bon répertoire
        output_dir = Path(__file__).parent / "html_outputs"
        output_dir.mkdir(parents=True, exist_ok=True)
        output_file = output_dir / "test_all_components.html"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html)
        
        # Créer le rapport
        report.append("RESULTATS DE GENERATION:")
        report.append("-" * 30)
        report.append(f"  - Composants traités: {components_processed}/{len(components)-1}")
        report.append(f"  - Variantes traitées: {variants_processed}")
        report.append(f"  - Fichier HTML: {output_file}")
        report.append(f"  - Taille HTML: {len(html)} caractères\n")
        
        if errors:
            report.append("ERREURS RENCONTREES:")
            report.append("-" * 30)
            for error in errors[:10]:  # Limiter à 10 erreurs
                report.append(f"  - {error}")
            if len(errors) > 10:
                report.append(f"  ... et {len(errors) - 10} autres erreurs")
        else:
            report.append("AUCUNE ERREUR DETECTEE")
        
        report.append("\n" + "=" * 50)
        
        if components_processed == len(components) - 1:  # -1 pour consent
            report.append("STATUT: PAGE DE TEST GENEREE AVEC SUCCES")
        else:
            report.append("STATUT: GENERATION PARTIELLE")
        
        report.append("=" * 50)
        
        # Sauvegarder le rapport
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(report))
        
        # Afficher le résumé
        print('\n'.join(report))
        print(f"\nRapport sauvegardé dans: {report_path}")
        print(f"Page HTML générée: {output_file}")
        
        return components_processed == len(components) - 1
        
    except Exception as e:
        error_msg = f"[ERREUR CRITIQUE] Impossible de générer la page de test: {str(e)}"
        report.append(error_msg)
        
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(report))
        
        print(error_msg)
        return False


def main():
    """Point d'entrée principal."""
    success = create_test_page()
    return 0 if success else 1


if __name__ == "__main__":
    exit(main())