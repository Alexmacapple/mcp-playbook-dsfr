#!/usr/bin/env python3
"""
MCP Server pour DSFR - Version correcte avec protocole JSON-RPC.
"""

import sys
import json
import asyncio
from pathlib import Path

# Ajouter le chemin parent pour les imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.services import (
    get_generator, get_validator, get_assistant, get_cognitive_service,
    get_design_service, get_audit_service, get_test_generator
)
from src.data import get_registry
from src.errors.base import DSFRError


class MCPServer:
    """Serveur MCP compatible avec le protocole JSON-RPC."""
    
    def __init__(self):
        self.generator = get_generator()
        self.validator = get_validator()
        self.assistant = get_assistant()
        self.cognitive = get_cognitive_service()
        self.design = get_design_service()
        self.audit = get_audit_service()
        self.test_gen = get_test_generator()
        self.registry = get_registry()
    
    async def handle_request(self, request):
        """Traite une requête JSON-RPC."""
        method = request.get("method")
        params = request.get("params", {})
        request_id = request.get("id")
        
        try:
            if method == "initialize":
                result = {
                    "capabilities": {
                        "tools": {
                            "supported": True
                        }
                    },
                    "serverInfo": {
                        "name": "mcp-playbook-dsfr",
                        "version": "2.0.0"
                    }
                }
            
            elif method == "tools/list":
                result = {
                    "tools": [
                        {
                            "name": "generate_component",
                            "description": "Génère un composant DSFR",
                            "inputSchema": {
                                "type": "object",
                                "properties": {
                                    "component": {"type": "string"},
                                    "options": {"type": "object"}
                                },
                                "required": ["component"]
                            }
                        },
                        {
                            "name": "list_components",
                            "description": "Liste tous les composants DSFR",
                            "inputSchema": {
                                "type": "object",
                                "properties": {}
                            }
                        },
                        {
                            "name": "validate_html",
                            "description": "Valide du HTML selon DSFR/RGAA",
                            "inputSchema": {
                                "type": "object",
                                "properties": {
                                    "html": {"type": "string"}
                                },
                                "required": ["html"]
                            }
                        }
                    ]
                }
            
            elif method == "tools/call":
                tool_name = params.get("name")
                arguments = params.get("arguments", {})
                
                if tool_name == "generate_component":
                    component = arguments.get("component")
                    options = arguments.get("options", {})
                    html = self.generator.generate(component, **options)
                    result = {
                        "content": [
                            {
                                "type": "text",
                                "text": html
                            }
                        ]
                    }
                
                elif tool_name == "list_components":
                    components = self.registry.list_components()
                    result = {
                        "content": [
                            {
                                "type": "text",
                                "text": json.dumps({
                                    "components": components,
                                    "count": len(components)
                                }, indent=2)
                            }
                        ]
                    }
                
                elif tool_name == "validate_html":
                    html = arguments.get("html", "")
                    validation = self.validator.validate(html)
                    result = {
                        "content": [
                            {
                                "type": "text",
                                "text": json.dumps(validation, indent=2)
                            }
                        ]
                    }
                
                else:
                    raise ValueError(f"Unknown tool: {tool_name}")
            
            else:
                raise ValueError(f"Unknown method: {method}")
            
            return {
                "jsonrpc": "2.0",
                "result": result,
                "id": request_id
            }
            
        except Exception as e:
            return {
                "jsonrpc": "2.0",
                "error": {
                    "code": -32603,
                    "message": str(e)
                },
                "id": request_id
            }
    
    async def run(self):
        """Lance le serveur en mode stdio."""
        while True:
            try:
                # Lire depuis stdin
                line = await asyncio.get_event_loop().run_in_executor(None, sys.stdin.readline)
                if not line:
                    break
                
                # Parser la ligne Content-Length
                if line.startswith("Content-Length:"):
                    content_length = int(line.split(":")[1].strip())
                    
                    # Lire la ligne vide
                    await asyncio.get_event_loop().run_in_executor(None, sys.stdin.readline)
                    
                    # Lire le contenu JSON
                    content = await asyncio.get_event_loop().run_in_executor(
                        None, sys.stdin.read, content_length
                    )
                    
                    # Parser la requête
                    request = json.loads(content)
                    
                    # Traiter la requête
                    response = await self.handle_request(request)
                    
                    # Envoyer la réponse
                    response_str = json.dumps(response)
                    response_bytes = response_str.encode('utf-8')
                    
                    sys.stdout.write(f"Content-Length: {len(response_bytes)}\r\n\r\n")
                    sys.stdout.write(response_str)
                    sys.stdout.flush()
                    
            except Exception as e:
                # Log erreur vers stderr pour debug
                print(f"Error: {e}", file=sys.stderr)
                sys.stderr.flush()


async def main():
    """Point d'entrée principal."""
    server = MCPServer()
    await server.run()


if __name__ == "__main__":
    asyncio.run(main())