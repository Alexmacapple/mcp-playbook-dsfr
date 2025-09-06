#!/usr/bin/env python3
"""
Script de test de non-régression après optimisations.
Vérifie que toutes les fonctionnalités essentielles fonctionnent.
"""

import sys
import json
import time
from pathlib import Path

# Ajouter le chemin du projet (parent du dossier tests/)
sys.path.insert(0, str(Path(__file__).parent.parent))

def test_imports():
    """Test que tous les imports fonctionnent."""
    print("\n📦 Test des imports...")
    try:
        from mcp_local.server import app
        from src.services import (
            get_generator, get_validator, get_assistant,
            get_cognitive_service, get_design_service,
            get_audit_service, get_test_generator
        )
        from src.data import get_registry
        from src.errors.base import DSFRError
        print("✅ Tous les imports OK")
        return True
    except Exception as e:
        print(f"❌ Erreur d'import: {e}")
        return False

def test_generator_service():
    """Test le service de génération."""
    print("\n🔨 Test du GeneratorService...")
    try:
        from src.services import get_generator
        generator = get_generator()
        
        # Test bouton
        html = generator.generate('button', label='Test', variant='primary')
        assert 'fr-btn' in html
        assert 'Test' in html
        
        # Test input
        html = generator.generate('input', label='Email', type='email')
        assert 'fr-input' in html
        
        # Test alert
        html = generator.generate('alert', message='Info', variant='info')
        assert 'fr-alert' in html
        
        print("✅ GeneratorService OK")
        return True
    except Exception as e:
        print(f"❌ GeneratorService: {e}")
        return False

def test_validator_service():
    """Test le service de validation."""
    print("\n✔️ Test du ValidatorService...")
    try:
        from src.services import get_validator
        validator = get_validator()
        
        # HTML valide
        result = validator.validate('<button class="fr-btn">OK</button>')
        assert result['valid'] == True
        
        # HTML avec erreur
        result = validator.validate('<div><span></div>')
        assert result['valid'] == False
        
        print("✅ ValidatorService OK")
        return True
    except Exception as e:
        print(f"❌ ValidatorService: {e}")
        return False

def test_audit_service():
    """Test le service d'audit."""
    print("\n🔍 Test du AuditService...")
    try:
        from src.services import get_audit_service
        from src.services.audit_service import RGAALevel
        
        audit = get_audit_service()
        
        # Audit simple
        html = '<img src="test.jpg" alt="Description">'
        report = audit.audit(html, level=RGAALevel.AA)
        assert report.score_a > 0
        
        print("✅ AuditService OK")
        return True
    except Exception as e:
        print(f"❌ AuditService: {e}")
        return False

def test_security_module():
    """Test le module de sécurité simplifié."""
    print("\n🔒 Test du module Security...")
    try:
        from src.utils.security import (
            validate_and_sanitize_html,
            validate_component_request,
            InputValidator,
            HTMLSanitizer
        )
        
        # Test validation composant
        result = validate_component_request('button', 'primary', {'label': 'Test'})
        assert result['component'] == 'button'
        
        # Test sanitization HTML - rejet du HTML dangereux
        dirty = '<script>alert("XSS")</script><div class="fr-btn">OK</div>'
        try:
            clean = validate_and_sanitize_html(dirty)
            assert False, "Devrait rejeter le HTML dangereux"
        except ValueError:
            pass  # C'est le comportement attendu
        
        # Test avec HTML sûr
        safe = '<div class="fr-btn">OK</div>'
        clean = validate_and_sanitize_html(safe)
        assert 'fr-btn' in clean
        
        print("✅ Security module OK")
        return True
    except Exception as e:
        print(f"❌ Security module: {e}")
        return False

def test_logger_module():
    """Test le module de logging simplifié."""
    print("\n📝 Test du module Logger...")
    try:
        from src.utils.logger import (
            get_logger,
            log_mcp_call,
            log_error,
            log_audit,
            log_performance
        )
        
        # Test logger creation
        logger = get_logger('test')
        assert logger is not None
        
        # Test log methods (ne doivent pas planter)
        log_mcp_call('test_tool', {'param': 'value'}, 100)
        log_audit('button', 'AA', 95.0, 2)
        log_performance('generate', 50.5)
        
        print("✅ Logger module OK")
        return True
    except Exception as e:
        print(f"❌ Logger module: {e}")
        return False

def test_mcp_tools():
    """Test tous les outils MCP."""
    print("\n🛠️ Test des outils MCP...")
    try:
        from mcp_local.server import (
            generer_composant,
            lister_composants,
            valider_html,
            audit_accessibilite,
            analyser_cognitif,
            obtenir_tokens_design,
            generer_tests,
            obtenir_aide_assistant
        )
        
        # Test génération
        html = generer_composant('button', variant='primary', options={'label': 'Test'})
        assert 'fr-btn' in html
        
        # Test liste
        result = json.loads(lister_composants())
        assert result['count'] == 48
        
        # Test validation
        result = json.loads(valider_html('<div class="fr-btn">Test</div>'))
        assert 'valid' in result
        
        # Test audit
        result = json.loads(audit_accessibilite('<button>Test</button>', 'AA'))
        assert 'scores' in result
        
        # Test analyse cognitive
        result = json.loads(analyser_cognitif('Créer un formulaire de contact'))
        assert 'matrix' in result or 'insights' in result
        
        # Test tokens
        result = json.loads(obtenir_tokens_design('colors'))
        assert len(result) > 0
        
        # Test génération tests
        tests = generer_tests('button', 'unit')
        assert 'describe' in tests or 'test' in tests
        
        # Test assistant
        help_text = obtenir_aide_assistant('Comment rendre un formulaire accessible?')
        assert 'accessible' in help_text.lower() or 'rgaa' in help_text.lower()
        
        print("✅ Tous les outils MCP OK")
        return True
    except Exception as e:
        print(f"❌ Outils MCP: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_performance():
    """Test de performance basique."""
    print("\n⚡ Test de performance...")
    try:
        from src.services import get_generator
        generator = get_generator()
        
        start = time.time()
        for _ in range(100):
            generator.generate('button', label='Test')
        duration = time.time() - start
        
        ops_per_sec = 100 / duration
        print(f"✅ Performance: {ops_per_sec:.1f} générations/seconde")
        
        if ops_per_sec < 50:
            print("⚠️ Performance dégradée (< 50 ops/sec)")
            return False
        
        return True
    except Exception as e:
        print(f"❌ Test performance: {e}")
        return False

def main():
    """Lance tous les tests de non-régression."""
    print("=" * 50)
    print("🧪 TESTS DE NON-RÉGRESSION MCP DSFR")
    print("=" * 50)
    
    tests = [
        test_imports,
        test_generator_service,
        test_validator_service,
        test_audit_service,
        test_security_module,
        test_logger_module,
        test_mcp_tools,
        test_performance
    ]
    
    results = []
    for test in tests:
        try:
            results.append(test())
        except Exception as e:
            print(f"❌ Erreur inattendue dans {test.__name__}: {e}")
            results.append(False)
    
    # Résumé
    print("\n" + "=" * 50)
    print("📊 RÉSUMÉ DES TESTS")
    print("=" * 50)
    
    passed = sum(results)
    total = len(results)
    
    if passed == total:
        print(f"✅ SUCCÈS: {passed}/{total} tests passés")
        print("🎉 Aucune régression détectée !")
        return 0
    else:
        print(f"❌ ÉCHEC: {passed}/{total} tests passés")
        print("⚠️ Des régressions ont été détectées")
        return 1

if __name__ == "__main__":
    sys.exit(main())