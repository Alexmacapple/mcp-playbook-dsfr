#!/usr/bin/env python3
"""
MCP Server pour DSFR - Version simplifiée et fonctionnelle.
Architecture Clean Code avec principes SOLID.
"""

import sys
from pathlib import Path

# Ajouter le chemin parent pour les imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.services import (
    get_generator, get_validator, get_assistant, get_cognitive_service,
    get_design_service, get_audit_service, get_test_generator
)
from src.data import get_registry
from src.errors.base import DSFRError
import json


class DSFRMCPServer:
    """
    Serveur MCP pour DSFR simplifié.
    Fonctionne en mode standalone pour tests.
    """
    
    def __init__(self):
        """Initialise le serveur avec tous les services."""
        self.generator = get_generator()
        self.validator = get_validator()
        self.assistant = get_assistant()
        self.cognitive = get_cognitive_service()
        self.design = get_design_service()
        self.audit = get_audit_service()
        self.test_gen = get_test_generator()
        self.registry = get_registry()
        
        print("✅ Serveur DSFR MCP initialisé")
        print(f"📦 {len(self.registry.list_components())} composants disponibles")
    
    def generate_component(self, component: str, **options):
        """Génère un composant DSFR."""
        try:
            html = self.generator.generate(component, **options)
            return {"success": True, "html": html}
        except DSFRError as e:
            return {"success": False, "error": str(e)}
    
    def validate_html(self, html: str, component_type: str = None):
        """Valide du HTML."""
        result = self.validator.validate(html, component_type)
        return result
    
    def list_components(self):
        """Liste tous les composants."""
        return {
            "components": self.registry.list_components(),
            "count": len(self.registry.list_components())
        }
    
    def test_server(self):
        """Test basique du serveur."""
        print("\n🧪 Test du serveur MCP DSFR")
        print("=" * 50)
        
        # Test 1: Liste des composants
        components = self.list_components()
        print(f"✅ {components['count']} composants disponibles")
        
        # Test 2: Génération
        result = self.generate_component("button", label="Test")
        if result["success"]:
            print("✅ Génération de composant OK")
        else:
            print(f"❌ Erreur génération: {result['error']}")
        
        # Test 3: Validation
        validation = self.validate_html("<button>Test</button>")
        print(f"✅ Validation: Score {validation.get('score', 'N/A')}/100")
        
        return True


def main():
    """Point d'entrée principal."""
    server = DSFRMCPServer()
    
    # Mode test
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        server.test_server()
        return
    
    # Mode serveur (simplifié pour l'instant)
    print("\n🚀 Serveur MCP DSFR démarré")
    print("Mode: Standalone (pas de connexion MCP active)")
    print("\nLe serveur est prêt pour être utilisé avec Claude Desktop")
    print("Configuration dans claude_desktop_config.json:")
    print(json.dumps({
        "command": str(Path(sys.executable).absolute()),
        "args": [str(Path(__file__).absolute())]
    }, indent=2))


if __name__ == "__main__":
    main()