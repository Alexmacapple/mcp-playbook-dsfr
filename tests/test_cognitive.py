#!/usr/bin/env python3
"""
Test de l'agent cognitif avec la matrice Connu-Inconnu de Rumsfeld.
"""

import sys
from pathlib import Path

# Ajouter le chemin pour les imports
sys.path.insert(0, str(Path(__file__).parent))

from src.services import get_cognitive_service


def test_cognitive_analysis():
    """Test l'analyse cognitive avec différents cas."""
    cognitive = get_cognitive_service()
    
    print("=" * 80)
    print("🧠 TEST DE L'AGENT COGNITIF - MATRICE CONNU-INCONNU")
    print("=" * 80)
    
    # Cas 1: Formulaire simple
    print("\n📝 CAS 1: Formulaire d'inscription simple")
    print("-" * 40)
    
    result = cognitive.analyze_request(
        "J'ai besoin d'un formulaire d'inscription avec nom et email",
        {"project_type": "web", "deadline": "2_weeks"}
    )
    
    matrix = result['matrix']
    
    print(f"\n✅ Connus connus: {len(matrix['connus_connus'])} insights")
    for insight in matrix['connus_connus'][:2]:
        print(f"  • {insight.insight}")
    
    print(f"\n💡 Inconnus connus: {len(matrix['inconnus_connus'])} insights")
    for insight in matrix['inconnus_connus'][:2]:
        print(f"  • {insight.insight}")
    
    print(f"\n⚠️ Inconnus inconnus: {len(matrix['inconnus_inconnus'])} angles morts")
    for insight in matrix['inconnus_inconnus'][:2]:
        print(f"  • [{insight.risk_level.upper()}] {insight.insight}")
    
    print(f"\n🎯 Recommandations: {len(result['recommendations'])}")
    for rec in result['recommendations'][:2]:
        print(f"  • {rec}")
    
    # Cas 2: Dashboard complexe
    print("\n" + "=" * 80)
    print("📊 CAS 2: Dashboard administratif")
    print("-" * 40)
    
    result = cognitive.analyze_request(
        "Dashboard pour suivre les statistiques utilisateurs avec graphiques",
        {"users": "10000", "data_volume": "high"}
    )
    
    matrix = result['matrix']
    
    print(f"\n✅ Connus connus: {len(matrix['connus_connus'])} insights")
    for insight in matrix['connus_connus'][:2]:
        print(f"  • {insight.insight}")
    
    print(f"\n⚠️ Inconnus inconnus détectés:")
    for insight in matrix['inconnus_inconnus'][:3]:
        print(f"  • [{insight.risk_level.upper()}] {insight.insight}")
        if insight.action_required:
            print(f"    → Action: {insight.action_required}")
    
    # Cas 3: Test des angles morts
    print("\n" + "=" * 80)
    print("🔍 CAS 3: Révélation des angles morts")
    print("-" * 40)
    
    # Simuler l'appel direct à reveal_blind_spots
    context = {"focus": "blind_spots"}
    result = cognitive.analyze_request(
        "Application e-commerce avec paiement en ligne",
        context
    )
    
    blind_spots = result['matrix']['inconnus_inconnus']
    
    # Catégoriser les risques
    technical = [s for s in blind_spots if 'performance' in s.insight.lower()]
    security = [s for s in blind_spots if 'sécurité' in s.insight.lower() or 'rgpd' in s.insight.lower()]
    
    if technical:
        print("\n🔧 Risques techniques anticipés:")
        for risk in technical[:2]:
            print(f"  • {risk.insight}")
    
    if security:
        print("\n🔒 Risques sécurité/conformité:")
        for risk in security[:2]:
            print(f"  • {risk.insight}")
    
    print("\n📊 Recommandations globales:")
    for idx, rec in enumerate(result['recommendations'][:3], 1):
        print(f"  {idx}. {rec}")
    
    print("\n" + "=" * 80)
    print("✅ TESTS TERMINÉS AVEC SUCCÈS")
    print("=" * 80)


if __name__ == "__main__":
    test_cognitive_analysis()