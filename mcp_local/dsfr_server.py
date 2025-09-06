#!/usr/bin/env python3
"""
MCP Server pour DSFR - Point d'entrée principal.
Architecture Clean Code avec principes SOLID.
"""

import asyncio
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

# Ajouter le chemin parent pour les imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from mcp import Server
from mcp.server import stdio_server
from mcp.types import (
    Tool,
    TextContent
)

from src.services import (
    get_generator, get_validator, get_assistant, get_cognitive_service, 
    get_design_service, get_audit_service, get_test_generator
)
from src.data import get_registry
from src.errors.base import DSFRError, is_dsfr_error


class DSFRMCPServer:
    """
    Serveur MCP pour DSFR.
    Responsabilité unique : Bridge entre MCP et nos services (S de SOLID).
    """
    
    def __init__(self):
        """Initialise le serveur avec tous les services."""
        self.server = Server("mcp-playbook-dsfr")
        self.generator = get_generator()
        self.validator = get_validator()
        self.assistant = get_assistant()
        self.cognitive = get_cognitive_service()
        self.design = get_design_service()
        self.audit = get_audit_service()
        self.test_gen = get_test_generator()
        self.registry = get_registry()
        
        # Enregistrer les handlers
        self._register_handlers()
        
    def _register_handlers(self):
        """
        Enregistre tous les handlers MCP.
        Open/Closed : Facile d'ajouter de nouveaux handlers.
        """
        
        @self.server.tool()
        async def list_tools() -> List[Tool]:
            """Liste tous les outils disponibles."""
            return [
                Tool(
                    name="generate_component",
                    description="Génère un composant DSFR avec les options spécifiées",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "component": {
                                "type": "string",
                                "description": "Nom du composant (button, alert, form, etc.)"
                            },
                            "variant": {
                                "type": "string", 
                                "description": "Variante du composant (primary, secondary, etc.)"
                            },
                            "options": {
                                "type": "object",
                                "description": "Options du composant (label, icon, etc.)"
                            }
                        },
                        "required": ["component"]
                    }
                ),
                Tool(
                    name="list_components",
                    description="Liste tous les composants DSFR disponibles",
                    inputSchema={
                        "type": "object",
                        "properties": {}
                    }
                ),
                Tool(
                    name="list_variants",
                    description="Liste les variantes d'un composant",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "component": {
                                "type": "string",
                                "description": "Nom du composant"
                            }
                        },
                        "required": ["component"]
                    }
                ),
                Tool(
                    name="validate_html",
                    description="Valide du HTML selon les standards DSFR et RGAA",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "html": {
                                "type": "string",
                                "description": "HTML à valider"
                            },
                            "component_type": {
                                "type": "string",
                                "description": "Type de composant (optionnel)"
                            }
                        },
                        "required": ["html"]
                    }
                ),
                Tool(
                    name="analyze_needs",
                    description="Analyse les besoins et suggère des composants DSFR",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "description": {
                                "type": "string",
                                "description": "Description du besoin"
                            }
                        },
                        "required": ["description"]
                    }
                ),
                Tool(
                    name="create_page",
                    description="Crée une page HTML complète avec plusieurs composants",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "title": {
                                "type": "string",
                                "description": "Titre de la page"
                            },
                            "components": {
                                "type": "array",
                                "description": "Liste des composants à inclure",
                                "items": {
                                    "type": "object"
                                }
                            }
                        },
                        "required": ["title", "components"]
                    }
                ),
                Tool(
                    name="get_component_info",
                    description="Récupère les informations détaillées d'un composant",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "component": {
                                "type": "string",
                                "description": "Nom du composant"
                            }
                        },
                        "required": ["component"]
                    }
                ),
                Tool(
                    name="cognitive_analysis",
                    description="Analyse cognitive profonde avec la matrice Connu-Inconnu de Rumsfeld",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "request": {
                                "type": "string",
                                "description": "Description du besoin à analyser"
                            },
                            "context": {
                                "type": "object",
                                "description": "Contexte additionnel (framework, deadline, etc.)"
                            }
                        },
                        "required": ["request"]
                    }
                ),
                Tool(
                    name="reveal_blind_spots",
                    description="Révèle les angles morts et risques cachés d'un projet",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "description": {
                                "type": "string",
                                "description": "Description du projet"
                            }
                        },
                        "required": ["description"]
                    }
                ),
                Tool(
                    name="get_dsfr_colors",
                    description="Récupère la palette de couleurs DSFR officielle",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "category": {
                                "type": "string",
                                "description": "Catégorie de couleurs (primary, system, grey, context, border)"
                            }
                        }
                    }
                ),
                Tool(
                    name="get_dsfr_icons",
                    description="Récupère les icônes DSFR disponibles (Remix Icon)",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "category": {
                                "type": "string",
                                "description": "Catégorie d'icônes (navigation, action, alert, etc.)"
                            },
                            "search": {
                                "type": "string",
                                "description": "Terme de recherche dans les noms d'icônes"
                            }
                        }
                    }
                ),
                Tool(
                    name="search_components",
                    description="Recherche des composants DSFR par mot-clé",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "query": {
                                "type": "string",
                                "description": "Terme de recherche"
                            },
                            "category": {
                                "type": "string",
                                "description": "Catégorie de composants (optionnel)"
                            }
                        },
                        "required": ["query"]
                    }
                ),
                Tool(
                    name="accessibility_audit",
                    description="Audit RGAA complet avec scores A/AA/AAA et corrections suggérées",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "html": {
                                "type": "string",
                                "description": "HTML à auditer"
                            },
                            "level": {
                                "type": "string",
                                "enum": ["A", "AA", "AAA"],
                                "description": "Niveau RGAA cible (défaut: AA)"
                            },
                            "generate_report": {
                                "type": "boolean",
                                "description": "Générer un rapport HTML (défaut: false)"
                            }
                        },
                        "required": ["html"]
                    }
                ),
                Tool(
                    name="generate_tests",
                    description="Génère des tests automatiques pour les composants DSFR",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "component": {
                                "type": "string",
                                "description": "Type de composant à tester"
                            },
                            "framework": {
                                "type": "string",
                                "enum": ["cypress", "playwright", "jest"],
                                "description": "Framework de test (défaut: cypress)"
                            },
                            "selector": {
                                "type": "string",
                                "description": "Sélecteur CSS du composant (optionnel)"
                            }
                        },
                        "required": ["component"]
                    }
                ),
                Tool(
                    name="generate_e2e_scenario",
                    description="Génère un scénario de test E2E multi-composants",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "components": {
                                "type": "array",
                                "description": "Liste des composants impliqués",
                                "items": {
                                    "type": "string"
                                }
                            },
                            "scenario": {
                                "type": "string",
                                "description": "Description du scénario utilisateur"
                            },
                            "framework": {
                                "type": "string",
                                "enum": ["cypress", "playwright"],
                                "description": "Framework de test (défaut: cypress)"
                            }
                        },
                        "required": ["components", "scenario"]
                    }
                )
            ]
        
        @self.server.tool()
        async def call_tool(name: str, arguments: dict) -> dict:
            """
            Dispatcher principal pour les appels d'outils.
            Factory Pattern : Route vers le bon handler.
            """
            tool_name = request.params.get("tool") or request.name
            
            handlers = {
                "generate_component": self._handle_generate,
                "list_components": self._handle_list_components,
                "list_variants": self._handle_list_variants,
                "validate_html": self._handle_validate,
                "analyze_needs": self._handle_analyze,
                "create_page": self._handle_create_page,
                "get_component_info": self._handle_component_info,
                "cognitive_analysis": self._handle_cognitive_analysis,
                "reveal_blind_spots": self._handle_reveal_blind_spots,
                "get_dsfr_colors": self._handle_get_colors,
                "get_dsfr_icons": self._handle_get_icons,
                "search_components": self._handle_search_components,
                "accessibility_audit": self._handle_accessibility_audit,
                "generate_tests": self._handle_generate_tests,
                "generate_e2e_scenario": self._handle_generate_e2e_scenario
            }
            
            handler = handlers.get(tool_name)
            if not handler:
                return CallToolResult(
                    content=[TextContent(text=f"Outil inconnu: {tool_name}")]
                )
            
            try:
                return await handler(request)
            except DSFRError as e:
                # Gestion élégante des erreurs DSFR
                return CallToolResult(
                    content=[TextContent(
                        text=f"Erreur DSFR [{e.code}]: {e.message}\n"
                             f"Détails: {json.dumps(e.details, indent=2)}"
                    )]
                )
            except Exception as e:
                # Erreurs non prévues
                return CallToolResult(
                    content=[TextContent(text=f"Erreur: {str(e)}")]
                )
    
    async def _handle_generate(self, request: CallToolRequest) -> CallToolResult:
        """Génère un composant DSFR."""
        component = request.params.get("component")
        variant = request.params.get("variant")
        options = request.params.get("options", {})
        
        if not component:
            return CallToolResult(
                content=[TextContent(text="Paramètre 'component' requis")]
            )
        
        # Fusionner variant dans options si fourni
        if variant:
            options["variant"] = variant
        
        # Générer le HTML
        html = self.generator.generate(component, **options)
        
        # Retourner le résultat
        return CallToolResult(
            content=[TextContent(
                text=f"```html\n{html}\n```\n\n"
                     f"✅ Composant '{component}' généré avec succès"
            )]
        )
    
    async def _handle_list_components(self, request: CallToolRequest) -> CallToolResult:
        """Liste tous les composants disponibles."""
        components = self.registry.list_components()
        stats = self.registry.get_stats()
        
        # Formatter la liste avec infos
        component_list = []
        for comp in components[:20]:  # Limiter pour la lisibilité
            variants = self.registry.list_variants(comp)
            component_list.append(f"• **{comp}** ({len(variants)} variantes)")
        
        if len(components) > 20:
            component_list.append(f"• ... et {len(components) - 20} autres")
        
        return CallToolResult(
            content=[TextContent(
                text=f"📦 **Composants DSFR disponibles** ({stats['components']} total)\n\n"
                     f"{chr(10).join(component_list)}\n\n"
                     f"📊 **Statistiques:**\n"
                     f"• Total composants: {stats['components']}\n"
                     f"• Total variantes: {stats['variants']}\n\n"
                     f"💡 Utilisez `list_variants` pour voir les variantes d'un composant"
            )]
        )
    
    async def _handle_list_variants(self, request: CallToolRequest) -> CallToolResult:
        """Liste les variantes d'un composant."""
        component = request.params.get("component")
        
        if not component:
            return CallToolResult(
                content=[TextContent(text="Paramètre 'component' requis")]
            )
        
        variants = self.registry.list_variants(component)
        metadata = self.registry.get_metadata(component)
        
        if not variants:
            return CallToolResult(
                content=[TextContent(
                    text=f"❌ Composant '{component}' non trouvé.\n"
                         f"Utilisez `list_components` pour voir la liste."
                )]
            )
        
        # Formatter les variantes
        variant_list = [f"• `{v}`" for v in variants]
        
        return CallToolResult(
            content=[TextContent(
                text=f"🎨 **Variantes pour '{component}':**\n\n"
                     f"{chr(10).join(variant_list)}\n\n"
                     f"📝 **Description:** {metadata.get('description', 'N/A')}\n"
                     f"♿ **Niveau RGAA:** {metadata.get('rgaa_level', 'AA')}\n\n"
                     f"💡 Exemple: `generate_component` avec component='{component}' et variant='{variants[0]}'"
            )]
        )
    
    async def _handle_validate(self, request: CallToolRequest) -> CallToolResult:
        """Valide du HTML DSFR."""
        html = request.params.get("html")
        component_type = request.params.get("component_type")
        
        if not html:
            return CallToolResult(
                content=[TextContent(text="Paramètre 'html' requis")]
            )
        
        # Valider
        result = self.validator.validate(html, component_type)
        
        # Formatter le résultat
        status = "✅ Valide" if result['valid'] else "❌ Invalide"
        
        message = f"**Validation DSFR/RGAA**\n\n"
        message += f"**Statut:** {status}\n"
        message += f"**Score:** {result['score']}/100\n\n"
        
        if result['errors']:
            message += "**❌ Erreurs:**\n"
            for error in result['errors']:
                message += f"• {error}\n"
            message += "\n"
        
        if result['warnings']:
            message += "**⚠️ Avertissements:**\n"
            for warning in result['warnings']:
                message += f"• {warning}\n"
        
        return CallToolResult(content=[TextContent(text=message)])
    
    async def _handle_analyze(self, request: CallToolRequest) -> CallToolResult:
        """Analyse les besoins et suggère des composants."""
        description = request.params.get("description")
        
        if not description:
            return CallToolResult(
                content=[TextContent(text="Paramètre 'description' requis")]
            )
        
        # Analyser
        analysis = self.assistant.analyze_needs(description)
        suggestions = self.assistant.suggest_components(analysis)
        
        # Formatter le résultat
        message = f"🧠 **Analyse des besoins**\n\n"
        message += f"**Description:** {description}\n\n"
        
        message += "**📊 Analyse (matrice Connu-Inconnu):**\n"
        if analysis['connus_connus']:
            message += f"• ✅ Explicite: {', '.join(analysis['connus_connus'])}\n"
        if analysis['inconnus_connus']:
            message += f"• 💡 Implicite détecté: {', '.join(analysis['inconnus_connus'])}\n"
        if analysis['inconnus_inconnus']:
            message += f"• ⚠️ À anticiper: {', '.join(analysis['inconnus_inconnus'])}\n"
        
        if suggestions:
            message += "\n**🎯 Composants suggérés:**\n"
            for sugg in suggestions:
                confidence_emoji = "🟢" if sugg['confidence'] == 'high' else "🟡"
                message += f"{confidence_emoji} **{sugg['component']}** "
                message += f"(variante: {sugg['variant']})\n"
                message += f"   → {sugg['reason']}\n"
        
        return CallToolResult(content=[TextContent(text=message)])
    
    async def _handle_create_page(self, request: CallToolRequest) -> CallToolResult:
        """Crée une page complète."""
        title = request.params.get("title", "Page DSFR")
        components = request.params.get("components", [])
        
        if not components:
            return CallToolResult(
                content=[TextContent(text="Paramètre 'components' requis (array)")]
            )
        
        # Générer la page
        html = self.assistant.generate_page(title, components)
        
        return CallToolResult(
            content=[TextContent(
                text=f"```html\n{html}\n```\n\n"
                     f"✅ Page créée avec {len(components)} composants"
            )]
        )
    
    async def _handle_component_info(self, request: CallToolRequest) -> CallToolResult:
        """Récupère les infos détaillées d'un composant."""
        component = request.params.get("component")
        
        if not component:
            return CallToolResult(
                content=[TextContent(text="Paramètre 'component' requis")]
            )
        
        info = self.generator.get_component_info(component)
        
        if not info:
            return CallToolResult(
                content=[TextContent(text=f"Composant '{component}' non trouvé")]
            )
        
        message = f"📦 **Composant: {component}**\n\n"
        message += f"**Description:** {info['metadata'].get('description', 'N/A')}\n"
        message += f"**Niveau RGAA:** {info['metadata'].get('rgaa_level', 'AA')}\n"
        message += f"**Variantes:** {', '.join(info['variants'])}\n\n"
        
        if info['metadata'].get('required_props'):
            message += f"**Props requises:** {', '.join(info['metadata']['required_props'])}\n"
        if info['metadata'].get('optional_props'):
            message += f"**Props optionnelles:** {', '.join(info['metadata']['optional_props'])}\n"
        
        return CallToolResult(content=[TextContent(text=message)])
    
    async def _handle_cognitive_analysis(self, request: CallToolRequest) -> CallToolResult:
        """Analyse cognitive avec la matrice Connu-Inconnu de Rumsfeld."""
        request_text = request.params.get("request")
        context = request.params.get("context", {})
        
        if not request_text:
            return CallToolResult(
                content=[TextContent(text="Paramètre 'request' requis")]
            )
        
        # Analyse cognitive profonde
        analysis = self.cognitive.analyze_request(request_text, context)
        
        # Formatter le résultat
        message = f"🧠 **Analyse Cognitive (Matrice de Rumsfeld)**\n\n"
        message += f"**Requête:** {request_text}\n\n"
        
        matrix = analysis['matrix']
        
        # Connus connus
        if matrix['connus_connus']:
            message += "**✅ Connus connus (besoins explicites):**\n"
            for insight in matrix['connus_connus']:
                message += f"• {insight.insight}\n"
                if insight.action_required:
                    message += f"  → Action: {insight.action_required}\n"
            message += "\n"
        
        # Inconnus connus
        if matrix['connus_inconnus']:
            message += "**🤔 Inconnus connus (questions à clarifier):**\n"
            for insight in matrix['connus_inconnus']:
                message += f"• {insight.insight}\n"
                if insight.action_required:
                    message += f"  → Action: {insight.action_required}\n"
            message += "\n"
        
        # Connus inconnus
        if matrix['inconnus_connus']:
            message += "**💡 Connus inconnus (besoins implicites détectés):**\n"
            for insight in matrix['inconnus_connus']:
                message += f"• {insight.insight}\n"
                if insight.action_required:
                    message += f"  → Action: {insight.action_required}\n"
            message += "\n"
        
        # Inconnus inconnus
        if matrix['inconnus_inconnus']:
            message += "**⚠️ Inconnus inconnus (angles morts anticipés):**\n"
            for insight in matrix['inconnus_inconnus']:
                risk_emoji = "🔴" if insight.risk_level == 'critical' else "🟡" if insight.risk_level == 'high' else "🟢"
                message += f"{risk_emoji} {insight.insight}\n"
                if insight.action_required:
                    message += f"  → Action: {insight.action_required}\n"
            message += "\n"
        
        # Risques identifiés
        if analysis.get('risks'):
            message += f"**⚠️ Risques identifiés:** {len(analysis['risks'])}\n\n"
        
        # Recommandations globales
        if analysis['recommendations']:
            message += "\n**🎯 Recommandations prioritaires:**\n"
            for idx, rec in enumerate(analysis['recommendations'][:5], 1):
                message += f"{idx}. {rec}\n"
        
        return CallToolResult(content=[TextContent(text=message)])
    
    async def _handle_reveal_blind_spots(self, request: CallToolRequest) -> CallToolResult:
        """Révèle les angles morts et risques cachés d'un projet."""
        description = request.params.get("description")
        
        if not description:
            return CallToolResult(
                content=[TextContent(text="Paramètre 'description' requis")]
            )
        
        # Analyser avec focus sur les inconnus inconnus
        context = {"focus": "blind_spots"}
        analysis = self.cognitive.analyze_request(description, context)
        
        # Formatter spécifiquement pour les angles morts
        message = f"🔍 **Révélation des angles morts**\n\n"
        message += f"**Projet:** {description}\n\n"
        
        # Focus sur les risques cachés
        blind_spots = analysis['matrix'].get('inconnus_inconnus', [])
        
        if blind_spots:
            message += "**⚠️ Angles morts détectés:**\n\n"
            
            # Grouper par catégorie de risque
            technical_risks = []
            security_risks = []
            ux_risks = []
            compliance_risks = []
            
            for spot in blind_spots:
                insight_text = spot.insight.lower()
                if any(term in insight_text for term in ['technique', 'performance', 'css', 'js']):
                    technical_risks.append(spot)
                elif any(term in insight_text for term in ['sécurité', 'rgpd', 'données']):
                    security_risks.append(spot)
                elif any(term in insight_text for term in ['utilisateur', 'ergonomie', 'accessibilité']):
                    ux_risks.append(spot)
                else:
                    compliance_risks.append(spot)
            
            if technical_risks:
                message += "**🔧 Risques techniques:**\n"
                for risk in technical_risks:
                    message += f"• {risk.insight}\n"
                    if risk.action_required:
                        message += f"  Mitigation: {risk.action_required}\n"
                message += "\n"
            
            if security_risks:
                message += "**🔒 Risques sécurité/conformité:**\n"
                for risk in security_risks:
                    message += f"• {risk.insight}\n"
                    if risk.action_required:
                        message += f"  Mitigation: {risk.action_required}\n"
                message += "\n"
            
            if ux_risks:
                message += "**👤 Risques UX/accessibilité:**\n"
                for risk in ux_risks:
                    message += f"• {risk.insight}\n"
                    if risk.action_required:
                        message += f"  Mitigation: {risk.action_required}\n"
                message += "\n"
            
            if compliance_risks:
                message += "**📋 Autres risques:**\n"
                for risk in compliance_risks:
                    message += f"• {risk.insight}\n"
                    if risk.action_required:
                        message += f"  Mitigation: {risk.action_required}\n"
                message += "\n"
        
        # Questions non anticipées
        unknowns = analysis['matrix'].get('connus_inconnus', [])
        if unknowns:
            message += "**❓ Questions à se poser:**\n"
            for unknown in unknowns[:5]:
                message += f"• {unknown.insight}\n"
            message += "\n"
        
        # Plan de mitigation
        message += "**📋 Plan de mitigation recommandé:**\n"
        message += "1. Audit technique préalable\n"
        message += "2. Revue sécurité/RGPD\n"
        message += "3. Tests accessibilité RGAA\n"
        message += "4. Tests de charge et performance\n"
        message += "5. Documentation des décisions d'architecture\n"
        
        return CallToolResult(content=[TextContent(text=message)])
    
    async def _handle_get_colors(self, request: CallToolRequest) -> CallToolResult:
        """Récupère la palette de couleurs DSFR."""
        category = request.params.get("category")
        
        colors = self.design.get_colors(category)
        
        message = f"🎨 **Palette de couleurs DSFR**\n\n"
        
        if category:
            message += f"**Catégorie:** {category}\n\n"
            for name, value in colors.items():
                message += f"• `{name}`: {value}\n"
        else:
            for cat_name, cat_colors in colors.items():
                message += f"**{cat_name.title()}:**\n"
                # Limiter à 5 couleurs par catégorie pour la lisibilité
                for i, (name, value) in enumerate(cat_colors.items()):
                    if i >= 5:
                        message += f"  ... et {len(cat_colors) - 5} autres\n"
                        break
                    message += f"  • `{name}`: {value}\n"
                message += "\n"
        
        message += "\n💡 **Utilisation:**\n"
        message += "```css\n"
        message += ".mon-element {\n"
        message += "  color: var(--text-default-grey);\n"
        message += "  background: var(--background-default-grey);\n"
        message += "}\n"
        message += "```"
        
        return CallToolResult(content=[TextContent(text=message)])
    
    async def _handle_get_icons(self, request: CallToolRequest) -> CallToolResult:
        """Récupère les icônes DSFR."""
        category = request.params.get("category")
        search = request.params.get("search")
        
        icons = self.design.get_icons(category, search)
        
        if not icons:
            return CallToolResult(
                content=[TextContent(text="❌ Aucune icône trouvée avec ces critères")]
            )
        
        message = f"🎯 **Icônes DSFR (Remix Icon)**\n\n"
        
        if search:
            message += f"**Recherche:** {search}\n"
        if category:
            message += f"**Catégorie:** {category}\n"
        
        message += f"**{len(icons)} icône(s) trouvée(s):**\n\n"
        
        # Grouper par catégorie
        categories = {}
        for name, data in icons.items():
            cat = data.get("category", "autre")
            if cat not in categories:
                categories[cat] = []
            categories[cat].append((name, data["class"]))
        
        for cat_name, cat_icons in categories.items():
            message += f"**{cat_name.title()}:**\n"
            for name, class_name in cat_icons[:10]:  # Limiter à 10 par catégorie
                message += f"• `{name}`: `{class_name}`\n"
            if len(cat_icons) > 10:
                message += f"  ... et {len(cat_icons) - 10} autres\n"
            message += "\n"
        
        message += "💡 **Utilisation:**\n"
        message += "```html\n"
        message += '<span class="fr-icon-search-line" aria-hidden="true"></span>\n'
        message += "```"
        
        return CallToolResult(content=[TextContent(text=message)])
    
    async def _handle_search_components(self, request: CallToolRequest) -> CallToolResult:
        """Recherche des composants DSFR."""
        query = request.params.get("query")
        category = request.params.get("category")
        
        if not query:
            return CallToolResult(
                content=[TextContent(text="Paramètre 'query' requis")]
            )
        
        # Recherche floue dans les composants
        query_lower = query.lower()
        all_components = self.registry.list_components()
        
        # Recherche exacte
        exact_matches = [c for c in all_components if query_lower == c.lower()]
        
        # Recherche partielle
        partial_matches = [
            c for c in all_components 
            if query_lower in c.lower() and c not in exact_matches
        ]
        
        # Recherche par mots-clés associés
        keyword_map = {
            "formulaire": ["form", "input", "select", "checkbox", "radio", "textarea"],
            "bouton": ["button", "btn"],
            "navigation": ["nav", "breadcrumb", "stepper", "tabs"],
            "alerte": ["alert", "notice", "message"],
            "carte": ["card", "tile"],
            "tableau": ["table"],
            "modal": ["modal", "dialog"],
            "menu": ["menu", "navigation", "sidemenu"]
        }
        
        keyword_matches = []
        for keyword, related in keyword_map.items():
            if query_lower in keyword:
                keyword_matches.extend([
                    c for c in all_components
                    if any(r in c.lower() for r in related)
                    and c not in exact_matches
                    and c not in partial_matches
                ])
        
        # Combiner les résultats
        results = exact_matches + partial_matches + keyword_matches
        
        if not results:
            # Suggestions alternatives
            suggestions = []
            if "form" in query_lower:
                suggestions = ["input", "select", "checkbox", "form"]
            elif "btn" in query_lower or "button" in query_lower:
                suggestions = ["button"]
            
            message = f"❌ Aucun composant trouvé pour '{query}'\n\n"
            if suggestions:
                message += "💡 **Essayez plutôt:**\n"
                for s in suggestions:
                    message += f"• {s}\n"
            return CallToolResult(content=[TextContent(text=message)])
        
        # Formatter les résultats
        message = f"🔍 **Résultats de recherche pour '{query}'**\n\n"
        message += f"**{len(results)} composant(s) trouvé(s):**\n\n"
        
        if exact_matches:
            message += "**✅ Correspondances exactes:**\n"
            for comp in exact_matches:
                variants = self.registry.list_variants(comp)
                message += f"• **{comp}** ({len(variants)} variantes)\n"
            message += "\n"
        
        if partial_matches:
            message += "**📝 Correspondances partielles:**\n"
            for comp in partial_matches[:5]:
                variants = self.registry.list_variants(comp)
                message += f"• **{comp}** ({len(variants)} variantes)\n"
            if len(partial_matches) > 5:
                message += f"• ... et {len(partial_matches) - 5} autres\n"
            message += "\n"
        
        if keyword_matches:
            message += "**🔗 Composants associés:**\n"
            for comp in keyword_matches[:3]:
                variants = self.registry.list_variants(comp)
                message += f"• **{comp}** ({len(variants)} variantes)\n"
            if len(keyword_matches) > 3:
                message += f"• ... et {len(keyword_matches) - 3} autres\n"
        
        message += "\n💡 Utilisez `get_component_info` pour plus de détails sur un composant"
        
        return CallToolResult(content=[TextContent(text=message)])
    
    async def _handle_accessibility_audit(self, request: CallToolRequest) -> CallToolResult:
        """Effectue un audit RGAA complet."""
        from src.services.audit_service import RGAALevel
        
        html = request.params.get("html")
        level_str = request.params.get("level", "AA")
        generate_report = request.params.get("generate_report", False)
        
        if not html:
            return CallToolResult(
                content=[TextContent(text="Paramètre 'html' requis")]
            )
        
        # Convertir le niveau
        level_map = {"A": RGAALevel.A, "AA": RGAALevel.AA, "AAA": RGAALevel.AAA}
        level = level_map.get(level_str, RGAALevel.AA)
        
        # Effectuer l'audit
        report = self.audit.audit(html, level)
        
        # Formatter le résultat
        message = f"🔍 **Audit RGAA - Niveau cible : {level_str}**\n\n"
        
        # Scores
        message += "**📊 Scores de conformité:**\n"
        score_emojis = {
            "A": "🟢" if report.score_a >= 80 else "🟡" if report.score_a >= 60 else "🔴",
            "AA": "🟢" if report.score_aa >= 80 else "🟡" if report.score_aa >= 60 else "🔴",
            "AAA": "🟢" if report.score_aaa >= 80 else "🟡" if report.score_aaa >= 60 else "🔴"
        }
        message += f"{score_emojis['A']} Niveau A : {report.score_a:.1f}%\n"
        message += f"{score_emojis['AA']} Niveau AA : {report.score_aa:.1f}%\n"
        message += f"{score_emojis['AAA']} Niveau AAA : {report.score_aaa:.1f}%\n\n"
        
        # Résumé des problèmes
        message += f"**⚠️ Problèmes détectés : {report.total_issues}**\n"
        if report.critical_issues > 0:
            message += f"• 🔴 Critiques : {report.critical_issues}\n"
        
        serious = len([i for i in report.issues if i.impact == "serious"])
        moderate = len([i for i in report.issues if i.impact == "moderate"])
        minor = len([i for i in report.issues if i.impact == "minor"])
        
        if serious > 0:
            message += f"• 🟠 Sérieux : {serious}\n"
        if moderate > 0:
            message += f"• 🟡 Modérés : {moderate}\n"
        if minor > 0:
            message += f"• 🟢 Mineurs : {minor}\n"
        
        message += "\n"
        
        # Top 5 problèmes critiques/sérieux
        critical_and_serious = [i for i in report.issues if i.impact in ["critical", "serious"]]
        if critical_and_serious:
            message += "**🚨 Problèmes prioritaires à corriger:**\n"
            for issue in critical_and_serious[:5]:
                message += f"\n**[{issue.criterion.value}] {issue.issue}**\n"
                message += f"• Impact : {issue.impact}\n"
                message += f"• Niveau : {issue.level.value}\n"
                if issue.suggestion:
                    message += f"• ✅ Suggestion : {issue.suggestion}\n"
                if issue.auto_fix:
                    message += f"• 🔧 Correction auto disponible\n"
        
        # Recommandations
        if report.recommendations:
            message += "\n**💡 Recommandations:**\n"
            for rec in report.recommendations:
                message += f"• {rec}\n"
        
        # Corrections automatiques disponibles
        if report.auto_fixes:
            message += f"\n**🔧 {len(report.auto_fixes)} corrections automatiques disponibles**\n"
            message += "Utilisez les suggestions pour corriger rapidement les problèmes.\n"
        
        # Génération du rapport HTML si demandé
        if generate_report:
            html_report = self.audit.generate_report_html(report)
            message += "\n**📄 Rapport HTML généré** (copiez le code ci-dessous) :\n"
            message += f"```html\n{html_report[:1000]}...\n```\n"
            message += "(Rapport tronqué - utilisez le code complet pour un fichier HTML)\n"
        
        return CallToolResult(content=[TextContent(text=message)])
    
    async def _handle_generate_tests(self, request: CallToolRequest) -> CallToolResult:
        """Génère des tests automatiques pour un composant."""
        from src.services.test_generator_service import TestFramework
        
        component = request.params.get("component")
        framework_str = request.params.get("framework", "cypress")
        selector = request.params.get("selector")
        
        if not component:
            return CallToolResult(
                content=[TextContent(text="Paramètre 'component' requis")]
            )
        
        # Convertir le framework
        framework_map = {
            "cypress": TestFramework.CYPRESS,
            "playwright": TestFramework.PLAYWRIGHT,
            "jest": TestFramework.JEST
        }
        framework = framework_map.get(framework_str, TestFramework.CYPRESS)
        
        # Options
        options = {"selector": selector} if selector else None
        
        # Générer les tests
        test_code = self.test_gen.generate_tests(component, framework, options)
        
        # Formatter le résultat
        message = f"🧪 **Tests générés pour '{component}' avec {framework_str.title()}**\n\n"
        
        # Informations sur les tests générés
        message += "**📋 Tests inclus:**\n"
        if component in ["button", "form", "accordion", "modal", "table"]:
            message += "• Test fonctionnel principal\n"
            message += "• Test d'accessibilité clavier\n"
            message += "• Test de conformité ARIA\n"
            message += "• Vérification des états\n"
        
        message += f"\n**💻 Code des tests:**\n"
        message += f"```javascript\n{test_code}\n```\n"
        
        # Instructions d'utilisation
        message += "\n**📝 Instructions:**\n"
        if framework == TestFramework.CYPRESS:
            message += "1. Sauvegarder dans `cypress/e2e/{component}.cy.js`\n"
            message += "2. Installer Cypress : `npm install --save-dev cypress`\n"
            message += "3. Lancer les tests : `npx cypress open`\n"
        elif framework == TestFramework.PLAYWRIGHT:
            message += "1. Sauvegarder dans `tests/{component}.spec.js`\n"
            message += "2. Installer Playwright : `npm install --save-dev @playwright/test`\n"
            message += "3. Lancer les tests : `npx playwright test`\n"
        elif framework == TestFramework.JEST:
            message += "1. Sauvegarder dans `__tests__/{component}.test.js`\n"
            message += "2. Installer Jest : `npm install --save-dev jest @testing-library/react`\n"
            message += "3. Lancer les tests : `npm test`\n"
        
        message += "\n💡 **Tip:** Adaptez les sélecteurs et assertions selon votre implémentation."
        
        return CallToolResult(content=[TextContent(text=message)])
    
    async def _handle_generate_e2e_scenario(self, request: CallToolRequest) -> CallToolResult:
        """Génère un scénario E2E complet."""
        from src.services.test_generator_service import TestFramework
        
        components = request.params.get("components", [])
        scenario = request.params.get("scenario")
        framework_str = request.params.get("framework", "cypress")
        
        if not components or not scenario:
            return CallToolResult(
                content=[TextContent(text="Paramètres 'components' et 'scenario' requis")]
            )
        
        # Convertir le framework
        framework = TestFramework.CYPRESS if framework_str == "cypress" else TestFramework.PLAYWRIGHT
        
        # Générer le scénario
        scenario_code = self.test_gen.generate_e2e_scenario(components, scenario, framework)
        
        # Formatter le résultat
        message = f"🎯 **Scénario E2E généré**\n\n"
        message += f"**📝 Scénario:** {scenario}\n"
        message += f"**🧩 Composants testés:** {', '.join(components)}\n"
        message += f"**🔧 Framework:** {framework_str.title()}\n\n"
        
        message += f"**💻 Code du scénario:**\n"
        message += f"```javascript\n{scenario_code}\n```\n"
        
        # Recommandations
        message += "\n**💡 Recommandations:**\n"
        message += "• Adaptez les sélecteurs à votre implémentation\n"
        message += "• Ajoutez des assertions spécifiques à votre logique métier\n"
        message += "• Utilisez des fixtures pour les données de test\n"
        message += "• Ajoutez des temps d'attente si nécessaire\n"
        
        return CallToolResult(content=[TextContent(text=message)])
    
    async def run(self):
        """Lance le serveur MCP."""
        async with stdio_server() as (read_stream, write_stream):
            await self.server.run(
                read_stream,
                write_stream,
                InitializationOptions(
                    server_name="mcp-playbook-dsfr",
                    server_version="2.0.0"
                )
            )


async def main():
    """Point d'entrée principal."""
    server = DSFRMCPServer()
    await server.run()


def start_server():
    """Helper pour démarrer le serveur (utilisé par le package)."""
    asyncio.run(main())


if __name__ == "__main__":
    asyncio.run(main())