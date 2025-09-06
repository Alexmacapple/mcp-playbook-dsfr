#!/usr/bin/env python3
"""
Serveur MCP DSFR Final - Version qui fonctionne avec Claude Desktop
"""

import asyncio
import sys
from pathlib import Path

# Ajouter le chemin parent
sys.path.insert(0, str(Path(__file__).parent.parent))

from mcp.server.stdio import stdio_server
from mcp.server import Server
from mcp.server.models import InitializationOptions
from mcp.types import Tool, TextContent

from src.services import (
    get_generator, get_validator, get_assistant,
    get_cognitive_service, get_design_service,
    get_audit_service, get_test_generator
)
from src.data import get_registry
from src.errors.base import DSFRError
import json


# Créer le serveur
server = Server("mcp-playbook-dsfr")

# Services
generator = get_generator()
validator = get_validator()
assistant = get_assistant()
cognitive = get_cognitive_service()
design = get_design_service()
audit = get_audit_service()
test_gen = get_test_generator()
registry = get_registry()


@server.list_tools()
async def list_tools() -> list[Tool]:
    """Liste tous les outils disponibles."""
    return [
        Tool(
            name="generate_component",
            description="Génère un composant DSFR",
            inputSchema={
                "type": "object",
                "properties": {
                    "component": {
                        "type": "string",
                        "description": "Nom du composant (button, alert, form, etc.)"
                    },
                    "variant": {
                        "type": "string",
                        "description": "Variante du composant (optionnel)"
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
            name="validate_html",
            description="Valide du HTML selon les standards DSFR et RGAA",
            inputSchema={
                "type": "object",
                "properties": {
                    "html": {
                        "type": "string",
                        "description": "HTML à valider"
                    }
                },
                "required": ["html"]
            }
        )
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    """Appelle un outil spécifique."""
    
    try:
        if name == "generate_component":
            component = arguments.get("component")
            variant = arguments.get("variant")
            options = arguments.get("options", {})
            
            # Si variant est fourni, l'ajouter aux options
            if variant:
                options["variant"] = variant
            
            html = generator.generate(component, **options)
            return [TextContent(
                type="text",
                text=html
            )]
        
        elif name == "list_components":
            components = registry.list_components()
            result = {
                "components": components,
                "count": len(components),
                "categories": {
                    "navigation": ["header", "footer", "breadcrumb", "navigation", "sidemenu"],
                    "forms": ["form", "input", "select", "checkbox", "radio", "toggle"],
                    "content": ["accordion", "alert", "badge", "button", "card", "table"],
                    "feedback": ["modal", "notice", "callout", "highlight"],
                    "layout": ["grid", "container", "tile", "tabs"]
                }
            }
            return [TextContent(
                type="text",
                text=json.dumps(result, indent=2, ensure_ascii=False)
            )]
        
        elif name == "validate_html":
            html = arguments.get("html", "")
            validation_result = validator.validate(html)
            return [TextContent(
                type="text",
                text=json.dumps(validation_result, indent=2, ensure_ascii=False)
            )]
        
        else:
            return [TextContent(
                type="text",
                text=f"Erreur: Outil '{name}' non reconnu"
            )]
            
    except DSFRError as e:
        return [TextContent(
            type="text",
            text=f"Erreur DSFR: {e.message}\nCode: {e.code}\nDétails: {json.dumps(e.details)}"
        )]
    except Exception as e:
        return [TextContent(
            type="text",
            text=f"Erreur: {str(e)}"
        )]


async def main():
    """Lance le serveur MCP."""
    try:
        async with stdio_server() as (read_stream, write_stream):
            init_options = InitializationOptions(
                server_name="mcp-playbook-dsfr",
                server_version="2.0.0"
            )
            await server.run(read_stream, write_stream, init_options)
    except Exception as e:
        # Log en stderr pour débug
        import sys
        print(f"Erreur serveur: {e}", file=sys.stderr)
        raise


if __name__ == "__main__":
    asyncio.run(main())