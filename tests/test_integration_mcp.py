#!/usr/bin/env python3
"""
Tests d'intégration pour le serveur MCP DSFR.
Teste les appels complets end-to-end.
"""

import pytest
import asyncio
import json
from typing import Dict, Any
from pathlib import Path
import sys

# Ajouter le chemin parent
sys.path.insert(0, str(Path(__file__).parent.parent))

from mcp.dsfr_server import DSFRMCPServer
from mcp.server.models import CallToolRequest, TextContent
from src.services import get_generator, get_validator, get_audit_service


class TestMCPIntegration:
    """Tests d'intégration du serveur MCP."""
    
    @pytest.fixture
    def server(self):
        """Crée une instance du serveur MCP."""
        return DSFRMCPServer()
    
    @pytest.mark.asyncio
    async def test_generate_component_flow(self, server):
        """Test le flow complet de génération de composant."""
        # Préparer la requête
        request = CallToolRequest(
            method="tools/call",
            params={
                "name": "generate_component",
                "arguments": {
                    "component": "button",
                    "variant": "primary",
                    "options": {
                        "label": "Test Button",
                        "icon": "save-line"
                    }
                }
            }
        )
        
        # Appeler le handler
        result = await server._handle_generate(request)
        
        # Vérifications
        assert result is not None
        assert len(result.content) > 0
        
        content = result.content[0]
        assert isinstance(content, TextContent)
        assert "fr-btn" in content.text
        assert "Test Button" in content.text
        assert "save-line" in content.text
    
    @pytest.mark.asyncio
    async def test_validate_html_flow(self, server):
        """Test le flow de validation HTML/RGAA."""
        # HTML à valider
        test_html = """
        <button class="fr-btn fr-btn--primary">
            <span class="fr-icon-save-line fr-icon--left"></span>
            Sauvegarder
        </button>
        """
        
        request = CallToolRequest(
            method="tools/call",
            params={
                "name": "validate_html",
                "arguments": {
                    "html": test_html,
                    "component_type": "button"
                }
            }
        )
        
        result = await server._handle_validate(request)
        
        assert result is not None
        content = json.loads(result.content[0].text)
        assert "valid" in content
        assert "issues" in content
    
    @pytest.mark.asyncio
    async def test_list_components_flow(self, server):
        """Test la liste des composants disponibles."""
        request = CallToolRequest(
            method="tools/call",
            params={
                "name": "list_components",
                "arguments": {}
            }
        )
        
        result = await server._handle_list_components(request)
        
        assert result is not None
        content = json.loads(result.content[0].text)
        assert "components" in content
        assert len(content["components"]) > 0
        assert "button" in content["components"]
    
    @pytest.mark.asyncio
    async def test_cognitive_analysis_flow(self, server):
        """Test l'analyse cognitive Rumsfeld."""
        request = CallToolRequest(
            method="tools/call",
            params={
                "name": "cognitive_analysis",
                "arguments": {
                    "request": "Je veux créer un formulaire de contact simple",
                    "context": {
                        "deadline": "2 semaines",
                        "users": "grand public"
                    }
                }
            }
        )
        
        result = await server._handle_cognitive_analysis(request)
        
        assert result is not None
        content = json.loads(result.content[0].text)
        assert "known_knowns" in content
        assert "known_unknowns" in content
        assert "unknown_knowns" in content
        assert "unknown_unknowns" in content
    
    @pytest.mark.asyncio
    async def test_accessibility_audit_flow(self, server):
        """Test l'audit d'accessibilité RGAA."""
        test_html = """
        <div class="fr-card">
            <img src="test.jpg" alt="">
            <div class="fr-card__body">
                <h3>Titre sans niveau</h3>
                <p style="color: #666">Texte avec faible contraste</p>
            </div>
        </div>
        """
        
        request = CallToolRequest(
            method="tools/call",
            params={
                "name": "accessibility_audit",
                "arguments": {
                    "html": test_html,
                    "level": "AA"
                }
            }
        )
        
        result = await server._handle_accessibility_audit(request)
        
        assert result is not None
        content = json.loads(result.content[0].text)
        assert "score" in content
        assert "issues" in content
        assert "level" in content
        assert len(content["issues"]) > 0  # Devrait détecter des problèmes
    
    @pytest.mark.asyncio
    async def test_generate_tests_flow(self, server):
        """Test la génération de tests automatiques."""
        request = CallToolRequest(
            method="tools/call",
            params={
                "name": "generate_tests",
                "arguments": {
                    "component": "form",
                    "framework": "cypress",
                    "selector": ".fr-form"
                }
            }
        )
        
        result = await server._handle_generate_tests(request)
        
        assert result is not None
        content = result.content[0].text
        assert "describe" in content
        assert "it(" in content
        assert "cy." in content
        assert ".fr-form" in content
    
    @pytest.mark.asyncio
    async def test_error_handling(self, server):
        """Test la gestion d'erreurs."""
        # Composant inexistant
        request = CallToolRequest(
            method="tools/call",
            params={
                "name": "generate_component",
                "arguments": {
                    "component": "inexistant_component"
                }
            }
        )
        
        result = await server._handle_generate(request)
        
        assert result is not None
        content = result.content[0].text
        assert "error" in content.lower() or "n'existe pas" in content.lower()
    
    @pytest.mark.asyncio
    async def test_concurrent_requests(self, server):
        """Test plusieurs requêtes concurrentes."""
        requests = [
            CallToolRequest(
                method="tools/call",
                params={
                    "name": "generate_component",
                    "arguments": {
                        "component": "button",
                        "options": {"label": f"Button {i}"}
                    }
                }
            )
            for i in range(5)
        ]
        
        # Exécuter en parallèle
        results = await asyncio.gather(*[
            server._handle_generate(req) for req in requests
        ])
        
        # Vérifier tous les résultats
        assert len(results) == 5
        for i, result in enumerate(results):
            assert result is not None
            assert f"Button {i}" in result.content[0].text


class TestServiceIntegration:
    """Tests d'intégration entre services."""
    
    def test_generator_validator_integration(self):
        """Test l'intégration générateur -> validateur."""
        generator = get_generator()
        validator = get_validator()
        
        # Générer un composant
        html = generator.generate(
            "alert",
            type="success",
            message="Test réussi"
        )
        
        # Valider le HTML généré
        result = validator.validate(html, "alert")
        
        assert result["valid"] is True
        assert len(result["issues"]) == 0
    
    def test_generator_audit_integration(self):
        """Test l'intégration générateur -> audit."""
        generator = get_generator()
        audit = get_audit_service()
        
        # Générer un formulaire
        html = generator.generate(
            "form",
            fields=[
                {"type": "text", "label": "Nom", "required": True},
                {"type": "email", "label": "Email", "required": True}
            ]
        )
        
        # Auditer l'accessibilité
        result = audit.audit(html, "AA")
        
        assert result["score"] > 80  # Devrait être accessible
        assert result["level"] == "AA"


@pytest.mark.asyncio
async def test_full_mcp_lifecycle():
    """Test le cycle de vie complet du serveur MCP."""
    server = DSFRMCPServer()
    
    # 1. Lister les outils disponibles
    tools = await server.server.list_tools()
    assert len(tools) >= 10
    
    # 2. Générer plusieurs composants
    components = ["button", "alert", "form", "card"]
    for comp in components:
        request = CallToolRequest(
            method="tools/call",
            params={
                "name": "generate_component",
                "arguments": {"component": comp}
            }
        )
        result = await server._handle_generate(request)
        assert result is not None
    
    print("✅ Tests d'intégration MCP réussis")


if __name__ == "__main__":
    # Lancer les tests
    pytest.main([__file__, "-v", "--asyncio-mode=auto"])