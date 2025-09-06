#!/usr/bin/env python3
"""
CE TEST EST DEPRECATED
======================
La fonctionnalité reveal_blind_spots est déjà couverte par:
- cognitive_service.analyze_request() qui détecte les "unknown_unknowns"
- Le test test-mcp-dsfr-cognitive.py qui teste cette fonctionnalité

Pour détecter les angles morts, utilisez:
cognitive_service.analyze_request(description, {"focus": "blind_spots"})

Ce test a été conservé pour référence historique uniquement.
"""
print("Test déprécié - Utilisez test-mcp-dsfr-cognitive.py à la place")
exit(0)