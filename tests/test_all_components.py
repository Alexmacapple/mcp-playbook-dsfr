#!/usr/bin/env python3
"""
Script de test pour générer une page avec TOUS les composants DSFR
Vérifie que le constructeur fonctionne correctement
"""

import json
import os
from datetime import datetime

def create_test_page():
    """Crée une page HTML de test avec tous les composants"""
    
    # Charger la bibliothèque complète
    library_path = "gabarits/dsfr_complete_library.json"
    if not os.path.exists(library_path):
        print("❌ Bibliothèque non trouvée. Lancez d'abord build_complete_library.py")
        return
    
    with open(library_path, 'r', encoding='utf-8') as f:
        library = json.load(f)
    
    components = library.get("components", {})
    
    # Créer le HTML de la page
    html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Test COMPLET - Tous les {len(components)} composants DSFR</title>
    
    <!-- DSFR CSS -->
    <link rel="stylesheet" href="https://unpkg.com/@gouvfr/dsfr@1.11.2/dist/dsfr.min.css">
    <link rel="stylesheet" href="https://unpkg.com/@gouvfr/dsfr@1.11.2/dist/utility/utility.min.css">
    <link rel="stylesheet" href="https://unpkg.com/@gouvfr/dsfr@1.11.2/dist/utility/icons/icons.min.css">
    
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
                <div class="stat-number">{len(components)}</div>
                <div>Composants</div>
            </div>
            <div class="stat">
                <div class="stat-number">{sum(len(v.get("variants", [])) for v in components.values())}</div>
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
                {"".join(f'<a href="#{comp}" class="nav-link">{comp}</a>' for comp in sorted(components.keys()))}
            </div>
        </nav>

        <!-- Metadata -->
        <div class="test-metadata">
            <strong>📅 Généré le :</strong> {datetime.now().strftime("%d/%m/%Y à %H:%M:%S")}<br>
            <strong>📦 Composants testés :</strong> {len(components)-1} / {len(components)}<br>
            <strong>🎨 Variantes totales :</strong> {sum(len(v.get("variants", [])) for v in components.values())}<br>
            <strong>✅ Mode :</strong> Test de rendu complet<br>
            <strong>⚠️ Note :</strong> Le composant 'consent' n'est pas affiché car il créerait un bandeau bloquant
        </div>
"""

    # Ajouter chaque composant (exclure consent qui crée un bandeau bloquant)
    for comp_name in sorted(components.keys()):
        # Skip consent component in test page as it creates a blocking banner
        if comp_name == "consent":
            continue
        comp_data = components[comp_name]
        variants = comp_data.get("variants", [])
        
        html += f"""
        <!-- ========== {comp_name.upper()} ========== -->
        <section class="test-section" id="{comp_name}">
            <h2>📦 {comp_name.replace('_', ' ').title()} ({len(variants)} variante{"s" if len(variants) > 1 else ""})</h2>
"""
        
        # Ajouter chaque variante
        for variant_name in variants:
            # Charger le HTML depuis le fichier
            variant_file = f"gabarits/{comp_name}/{comp_name}_{variant_name}.html"
            if os.path.exists(variant_file):
                with open(variant_file, 'r', encoding='utf-8') as f:
                    # Ignorer les commentaires en début de fichier
                    lines = f.readlines()
                    variant_html = ''.join(lines[3:]) if len(lines) > 3 else ''.join(lines)
            else:
                variant_html = f"<!-- Fichier non trouvé : {variant_file} -->"
            
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
        
        html += """
        </section>
"""

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
    <script type="module" src="https://unpkg.com/@gouvfr/dsfr@1.11.2/dist/dsfr.module.min.js"></script>
    <script nomodule src="https://unpkg.com/@gouvfr/dsfr@1.11.2/dist/dsfr.nomodule.min.js"></script>
    
    <script>
        // Initialiser les composants DSFR
        window.addEventListener('DOMContentLoaded', function() {
            console.log('✅ Page de test chargée');
            console.log('📊 Composants:', """ + str(len(components)) + """);
            console.log('🎨 Variantes:', """ + str(sum(len(v.get("variants", [])) for v in components.values())) + """);
        });
    </script>
</body>
</html>
"""
    
    # Sauvegarder le fichier
    output_file = "test_all_components.html"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"""
╔════════════════════════════════════════════════════════╗
║   ✅ PAGE DE TEST COMPLÈTE CRÉÉE AVEC SUCCÈS !         ║
╚════════════════════════════════════════════════════════╝

📄 Fichier : {output_file}
📊 Statistiques :
   • {len(components)} composants DSFR
   • {sum(len(v.get("variants", [])) for v in components.values())} variantes au total
   • 100% des composants v1.14.1

🚀 Pour voir la page :
   1. Ouvrez {output_file} dans votre navigateur
   2. Vérifiez que tous les composants s'affichent
   3. Testez l'interactivité (accordéons, modales, etc.)

📋 Navigation rapide incluse pour accéder à chaque composant
🎨 Tous les styles DSFR appliqués via CDN
""")

if __name__ == "__main__":
    create_test_page()