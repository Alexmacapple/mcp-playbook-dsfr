"""
Services métier pour DSFR MCP.
Chaque service a une responsabilité unique (S de SOLID).
"""

from .generator_service import GeneratorService, get_generator
from .validator_service import ValidatorService, get_validator
from .assistant_service import AssistantService, get_assistant
from .cognitive_service import CognitiveService, get_cognitive_service
from .design_service import DesignService, get_design_service
from .audit_service import AuditService, get_audit_service
from .test_generator_service import TestGeneratorService, get_test_generator

__all__ = [
    'GeneratorService', 
    'get_generator',
    'ValidatorService',
    'get_validator',
    'AssistantService',
    'get_assistant',
    'CognitiveService',
    'get_cognitive_service',
    'DesignService',
    'get_design_service',
    'AuditService',
    'get_audit_service',
    'TestGeneratorService',
    'get_test_generator'
]