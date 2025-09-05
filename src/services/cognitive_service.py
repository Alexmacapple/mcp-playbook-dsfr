"""
Service d'analyse cognitive basé sur la matrice Connu-Inconnu de Rumsfeld.
Révèle les besoins cachés et anticipe les problèmes non identifiés.
Clean Code : SOLID, DRY, KISS, YAGNI
"""

from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass
from enum import Enum
import re


class KnowledgeQuadrant(Enum):
    """Les 4 quadrants de la matrice de Rumsfeld."""
    KNOWN_KNOWNS = "connus_connus"          # Ce qu'on sait qu'on sait
    KNOWN_UNKNOWNS = "connus_inconnus"      # Ce qu'on sait qu'on ne sait pas
    UNKNOWN_KNOWNS = "inconnus_connus"      # Ce qu'on ne réalise pas qu'on sait
    UNKNOWN_UNKNOWNS = "inconnus_inconnus"  # Ce qu'on ne sait pas qu'on ne sait pas


@dataclass
class CognitiveInsight:
    """Représente une découverte cognitive."""
    quadrant: KnowledgeQuadrant
    insight: str
    confidence: float  # 0.0 à 1.0
    action_required: Optional[str] = None
    risk_level: str = "low"  # low, medium, high, critical


class CognitiveService:
    """
    Service d'analyse cognitive pour révéler les besoins cachés.
    
    Applique la matrice Connu-Inconnu pour :
    - Identifier les besoins non exprimés
    - Détecter les risques cachés
    - Suggérer des améliorations proactives
    - Anticiper les problèmes futurs
    """
    
    def __init__(self):
        """Initialise le service avec les patterns de détection."""
        self.patterns = self._init_detection_patterns()
        self.risk_indicators = self._init_risk_indicators()
        self.clarifying_questions = self._init_questions()
        
    def _init_detection_patterns(self) -> Dict[str, List[str]]:
        """
        Patterns pour détecter les besoins implicites.
        DRY : Centralisation des patterns de détection.
        """
        return {
            # Patterns qui révèlent des Inconnus Connus
            'resistance_patterns': [
                'simple', 'basique', 'juste', 'rapidement',
                'pas besoin', 'pas important', 'peu importe'
            ],
            
            # Patterns qui signalent des complexités cachées
            'complexity_indicators': [
                'utilisateurs', 'clients', 'équipe', 'plusieurs',
                'différents', 'types', 'variés', 'multiples'
            ],
            
            # Patterns d'incertitude (Known Unknowns)
            'uncertainty_markers': [
                'peut-être', 'probablement', 'je pense',
                'environ', 'à peu près', 'genre', 'style'
            ],
            
            # Patterns temporels (futurs Unknown Unknowns)
            'temporal_markers': [
                'plus tard', 'futur', 'évolution', 'migration',
                'mise à jour', 'changement', 'croissance'
            ]
        }
    
    def _init_risk_indicators(self) -> Dict[str, Dict[str, Any]]:
        """
        Indicateurs de risques par contexte.
        KISS : Structure simple pour l'évaluation des risques.
        """
        return {
            'accessibility': {
                'keywords': ['accessible', 'rgaa', 'handicap', 'senior'],
                'missing_often': ['contraste', 'clavier', 'lecteur écran'],
                'risk_level': 'high'
            },
            'performance': {
                'keywords': ['mobile', 'lent', 'performance', 'rapide'],
                'missing_often': ['lazy loading', 'optimisation', 'cache'],
                'risk_level': 'medium'
            },
            'security': {
                'keywords': ['formulaire', 'données', 'connexion', 'paiement'],
                'missing_often': ['csrf', 'validation', 'sanitization'],
                'risk_level': 'critical'
            },
            'maintenance': {
                'keywords': ['équipe', 'évolutif', 'modulaire', 'réutilisable'],
                'missing_often': ['documentation', 'tests', 'patterns'],
                'risk_level': 'medium'
            }
        }
    
    def _init_questions(self) -> Dict[KnowledgeQuadrant, List[str]]:
        """
        Questions de clarification par quadrant.
        S de SOLID : Chaque quadrant a ses propres questions.
        """
        return {
            KnowledgeQuadrant.KNOWN_UNKNOWNS: [
                "Quel est le nombre d'utilisateurs attendu ?",
                "Quelle est la deadline du projet ?",
                "Y a-t-il des contraintes techniques spécifiques ?",
                "Quel est le niveau d'accessibilité requis (A, AA, AAA) ?"
            ],
            
            KnowledgeQuadrant.UNKNOWN_KNOWNS: [
                "Avez-vous déjà rencontré des problèmes similaires dans le passé ?",
                "Y a-t-il des aspects que vous préférez éviter de mentionner ?",
                "Quelle est votre plus grande préoccupation non exprimée ?",
                "Qu'est-ce qui vous a surpris dans vos projets précédents ?"
            ],
            
            KnowledgeQuadrant.UNKNOWN_UNKNOWNS: [
                "Comment ce composant pourrait-il évoluer dans 6 mois ?",
                "Qui d'autre pourrait utiliser ce composant ?",
                "Quelles intégrations futures sont possibles ?",
                "Quels changements réglementaires pourraient impacter ce projet ?"
            ]
        }
    
    def analyze_request(self, request: str, context: Optional[Dict] = None) -> Dict[str, Any]:
        """
        Analyse une requête selon la matrice Connu-Inconnu.
        
        Args:
            request: Description du besoin
            context: Contexte additionnel
            
        Returns:
            Analyse complète avec insights par quadrant
        """
        request_lower = request.lower()
        context = context or {}
        
        # Analyse par quadrant
        analysis = {
            'matrix': {
                KnowledgeQuadrant.KNOWN_KNOWNS.value: self._extract_known_knowns(request, context),
                KnowledgeQuadrant.KNOWN_UNKNOWNS.value: self._identify_known_unknowns(request, context),
                KnowledgeQuadrant.UNKNOWN_KNOWNS.value: self._reveal_unknown_knowns(request, context),
                KnowledgeQuadrant.UNKNOWN_UNKNOWNS.value: self._predict_unknown_unknowns(request, context)
            },
            'insights': [],
            'risks': [],
            'recommendations': [],
            'questions': []
        }
        
        # Générer les insights
        analysis['insights'] = self._generate_insights(analysis['matrix'])
        
        # Évaluer les risques
        analysis['risks'] = self._evaluate_risks(request, analysis['matrix'])
        
        # Générer les recommandations
        analysis['recommendations'] = self._generate_recommendations(analysis)
        
        # Questions de clarification
        analysis['questions'] = self._select_clarifying_questions(analysis)
        
        return analysis
    
    def _extract_known_knowns(self, request: str, context: Dict) -> List[CognitiveInsight]:
        """
        Extrait ce qui est explicitement connu et maîtrisé.
        KISS : Extraction simple des éléments explicites.
        """
        insights = []
        request_lower = request.lower()
        
        # Composants explicitement demandés
        explicit_components = [
            'formulaire', 'bouton', 'tableau', 'navigation',
            'alerte', 'modal', 'carte', 'accordéon'
        ]
        
        for component in explicit_components:
            if component in request_lower:
                insights.append(CognitiveInsight(
                    quadrant=KnowledgeQuadrant.KNOWN_KNOWNS,
                    insight=f"Composant {component} explicitement demandé",
                    confidence=1.0,
                    risk_level="low"
                ))
        
        # Contraintes explicites
        if 'accessible' in request_lower or 'rgaa' in request_lower:
            insights.append(CognitiveInsight(
                quadrant=KnowledgeQuadrant.KNOWN_KNOWNS,
                insight="Accessibilité requise et identifiée",
                confidence=1.0,
                risk_level="low"
            ))
        
        return insights
    
    def _identify_known_unknowns(self, request: str, context: Dict) -> List[CognitiveInsight]:
        """
        Identifie ce qu'on sait ne pas savoir.
        O de SOLID : Extensible pour nouveaux patterns.
        """
        insights = []
        request_lower = request.lower()
        
        # Détection des incertitudes
        for marker in self.patterns['uncertainty_markers']:
            if marker in request_lower:
                insights.append(CognitiveInsight(
                    quadrant=KnowledgeQuadrant.KNOWN_UNKNOWNS,
                    insight=f"Incertitude détectée : présence de '{marker}'",
                    confidence=0.8,
                    action_required="Clarifier les spécifications exactes",
                    risk_level="medium"
                ))
        
        # Questions manquantes évidentes
        if 'formulaire' in request_lower and 'validation' not in request_lower:
            insights.append(CognitiveInsight(
                quadrant=KnowledgeQuadrant.KNOWN_UNKNOWNS,
                insight="Règles de validation non spécifiées",
                confidence=0.9,
                action_required="Définir les règles de validation",
                risk_level="medium"
            ))
        
        return insights
    
    def _reveal_unknown_knowns(self, request: str, context: Dict) -> List[CognitiveInsight]:
        """
        Révèle ce qu'on sait sans le réaliser ou qu'on refuse d'admettre.
        Détecte les biais cognitifs et résistances.
        """
        insights = []
        request_lower = request.lower()
        
        # Détection de minimisation (résistance cognitive)
        for pattern in self.patterns['resistance_patterns']:
            if pattern in request_lower:
                insights.append(CognitiveInsight(
                    quadrant=KnowledgeQuadrant.UNKNOWN_KNOWNS,
                    insight=f"Minimisation détectée ('{pattern}') - complexité probablement sous-estimée",
                    confidence=0.7,
                    action_required="Explorer les besoins réels non exprimés",
                    risk_level="high"
                ))
        
        # Expériences passées non mentionnées
        if 'refaire' in request_lower or 'comme avant' in request_lower:
            insights.append(CognitiveInsight(
                quadrant=KnowledgeQuadrant.UNKNOWN_KNOWNS,
                insight="Référence à une expérience passée non détaillée",
                confidence=0.8,
                action_required="Analyser les leçons du projet précédent",
                risk_level="medium"
            ))
        
        # Complexité multi-utilisateurs souvent sous-estimée
        if any(word in request_lower for word in ['utilisateurs', 'équipe', 'clients']):
            insights.append(CognitiveInsight(
                quadrant=KnowledgeQuadrant.UNKNOWN_KNOWNS,
                insight="Contexte multi-utilisateurs : besoins différenciés probables",
                confidence=0.75,
                action_required="Définir les personas et leurs besoins spécifiques",
                risk_level="medium"
            ))
        
        return insights
    
    def _predict_unknown_unknowns(self, request: str, context: Dict) -> List[CognitiveInsight]:
        """
        Anticipe ce qu'on ne sait pas qu'on ne sait pas.
        Prédiction des angles morts et surprises potentielles.
        """
        insights = []
        request_lower = request.lower()
        
        # Évolutions futures non anticipées
        if 'formulaire' in request_lower:
            insights.append(CognitiveInsight(
                quadrant=KnowledgeQuadrant.UNKNOWN_UNKNOWNS,
                insight="Évolution RGPD : nouvelles obligations de consentement possibles",
                confidence=0.6,
                action_required="Prévoir une architecture flexible pour les consentements",
                risk_level="medium"
            ))
        
        # Problèmes de performance non visibles
        if 'tableau' in request_lower or 'liste' in request_lower:
            insights.append(CognitiveInsight(
                quadrant=KnowledgeQuadrant.UNKNOWN_UNKNOWNS,
                insight="Performance avec grands volumes : pagination/virtualisation nécessaire",
                confidence=0.7,
                action_required="Implémenter lazy loading dès le début",
                risk_level="high"
            ))
        
        # Intégrations futures
        if 'api' not in request_lower and 'données' in request_lower:
            insights.append(CognitiveInsight(
                quadrant=KnowledgeQuadrant.UNKNOWN_UNKNOWNS,
                insight="Intégration API future probable mais non mentionnée",
                confidence=0.65,
                action_required="Prévoir une couche d'abstraction pour les données",
                risk_level="medium"
            ))
        
        # Conflits CSS potentiels
        if context.get('framework') or 'bootstrap' in request_lower or 'tailwind' in request_lower:
            insights.append(CognitiveInsight(
                quadrant=KnowledgeQuadrant.UNKNOWN_UNKNOWNS,
                insight="Conflits CSS possibles avec frameworks existants",
                confidence=0.7,
                action_required="Isoler les styles DSFR avec namespace",
                risk_level="high"
            ))
        
        # Accessibilité mobile souvent oubliée
        if 'mobile' not in request_lower and 'responsive' not in request_lower:
            insights.append(CognitiveInsight(
                quadrant=KnowledgeQuadrant.UNKNOWN_UNKNOWNS,
                insight="Utilisation mobile non mentionnée mais probable (60% du trafic)",
                confidence=0.8,
                action_required="Tester sur appareils mobiles et tactiles",
                risk_level="high"
            ))
        
        return insights
    
    def _evaluate_risks(self, request: str, matrix: Dict) -> List[Dict[str, Any]]:
        """
        Évalue les risques identifiés dans l'analyse.
        KISS : Évaluation simple mais efficace.
        """
        risks = []
        request_lower = request.lower()
        
        for risk_type, indicators in self.risk_indicators.items():
            # Vérifier si le contexte match
            if any(keyword in request_lower for keyword in indicators['keywords']):
                # Vérifier ce qui manque souvent
                for missing in indicators['missing_often']:
                    if missing not in request_lower:
                        risks.append({
                            'type': risk_type,
                            'description': f"{missing} non mentionné mais critique pour {risk_type}",
                            'level': indicators['risk_level'],
                            'mitigation': f"Implémenter {missing} dès le début"
                        })
        
        # Risques basés sur les Unknown Unknowns
        unknown_unknowns = matrix.get(KnowledgeQuadrant.UNKNOWN_UNKNOWNS.value, [])
        for insight in unknown_unknowns:
            if insight.risk_level in ['high', 'critical']:
                risks.append({
                    'type': 'blind_spot',
                    'description': insight.insight,
                    'level': insight.risk_level,
                    'mitigation': insight.action_required
                })
        
        return sorted(risks, key=lambda x: {'low': 0, 'medium': 1, 'high': 2, 'critical': 3}.get(x['level'], 0), reverse=True)
    
    def _generate_insights(self, matrix: Dict) -> List[str]:
        """
        Génère des insights actionnables depuis la matrice.
        DRY : Centralisation de la génération d'insights.
        """
        insights = []
        
        # Analyser la distribution dans la matrice
        quadrant_counts = {q: len(items) for q, items in matrix.items()}
        
        # Insight sur la clarté du besoin
        if quadrant_counts[KnowledgeQuadrant.KNOWN_KNOWNS.value] < 2:
            insights.append("⚠️ Besoin peu détaillé : nécessite clarification")
        
        # Insight sur les risques cachés
        if quadrant_counts[KnowledgeQuadrant.UNKNOWN_UNKNOWNS.value] > 3:
            insights.append("🚨 Nombreux angles morts détectés : approche prudente recommandée")
        
        # Insight sur la résistance cognitive
        if quadrant_counts[KnowledgeQuadrant.UNKNOWN_KNOWNS.value] > 2:
            insights.append("💭 Résistances ou biais détectés : exploration empathique nécessaire")
        
        return insights
    
    def _generate_recommendations(self, analysis: Dict) -> List[Dict[str, str]]:
        """
        Génère des recommandations basées sur l'analyse complète.
        YAGNI : Recommandations pragmatiques et actionnables.
        """
        recommendations = []
        
        # Recommandations par niveau de risque
        high_risks = [r for r in analysis['risks'] if r['level'] in ['high', 'critical']]
        
        for risk in high_risks[:3]:  # Top 3 risques
            recommendations.append({
                'priority': 'high',
                'action': risk['mitigation'],
                'reason': risk['description'],
                'impact': f"Réduit le risque {risk['type']}"
            })
        
        # Recommandations basées sur les Unknown Unknowns
        uu_count = len(analysis['matrix'][KnowledgeQuadrant.UNKNOWN_UNKNOWNS.value])
        if uu_count > 2:
            recommendations.append({
                'priority': 'medium',
                'action': "Implémenter une architecture flexible et modulaire",
                'reason': f"{uu_count} inconnues détectées",
                'impact': "Facilite les adaptations futures"
            })
        
        # Recommandation sur l'accessibilité si non mentionnée
        if not any('accessible' in str(i).lower() for i in analysis['matrix'][KnowledgeQuadrant.KNOWN_KNOWNS.value]):
            recommendations.append({
                'priority': 'high',
                'action': "Appliquer les standards RGAA niveau AA minimum",
                'reason': "Accessibilité non explicitement mentionnée",
                'impact': "Évite les problèmes légaux et élargit l'audience"
            })
        
        return recommendations
    
    def _select_clarifying_questions(self, analysis: Dict) -> List[str]:
        """
        Sélectionne les questions de clarification pertinentes.
        KISS : Maximum 3 questions pour ne pas surcharger.
        """
        questions = []
        
        # Prioriser les questions par quadrant critique
        quadrant_priority = [
            KnowledgeQuadrant.UNKNOWN_UNKNOWNS,
            KnowledgeQuadrant.UNKNOWN_KNOWNS,
            KnowledgeQuadrant.KNOWN_UNKNOWNS
        ]
        
        for quadrant in quadrant_priority:
            if len(questions) >= 3:
                break
            
            # Sélectionner une question pertinente pour ce quadrant
            if quadrant in self.clarifying_questions:
                quadrant_questions = self.clarifying_questions[quadrant]
                if quadrant_questions and len(questions) < 3:
                    # Prendre la première question non encore posée
                    questions.append(quadrant_questions[0])
        
        return questions
    
    def generate_report(self, analysis: Dict) -> str:
        """
        Génère un rapport formaté de l'analyse.
        Clean Code : Présentation claire et structurée.
        """
        report = ["## 🧠 Analyse Cognitive (Matrice Connu-Inconnu)\n"]
        
        # Résumé executif
        report.append("### 📊 Résumé")
        total_insights = sum(len(items) for items in analysis['matrix'].values())
        high_risks = len([r for r in analysis['risks'] if r['level'] in ['high', 'critical']])
        report.append(f"- **{total_insights}** insights détectés")
        report.append(f"- **{high_risks}** risques élevés identifiés")
        report.append(f"- **{len(analysis['recommendations'])}** recommandations prioritaires\n")
        
        # Matrice détaillée
        report.append("### 🗂️ Matrice d'Analyse\n")
        
        quadrant_emojis = {
            KnowledgeQuadrant.KNOWN_KNOWNS.value: "✅",
            KnowledgeQuadrant.KNOWN_UNKNOWNS.value: "❓",
            KnowledgeQuadrant.UNKNOWN_KNOWNS.value: "💭",
            KnowledgeQuadrant.UNKNOWN_UNKNOWNS.value: "⚫"
        }
        
        for quadrant, insights in analysis['matrix'].items():
            emoji = quadrant_emojis.get(quadrant, "•")
            report.append(f"#### {emoji} {quadrant.replace('_', ' ').title()}")
            
            if insights:
                for insight in insights[:3]:  # Limiter à 3 par quadrant
                    confidence_bar = "█" * int(insight.confidence * 5)
                    report.append(f"- {insight.insight} [{confidence_bar}]")
                    if insight.action_required:
                        report.append(f"  → Action: {insight.action_required}")
            else:
                report.append("- Aucun élément identifié")
            report.append("")
        
        # Risques principaux
        if analysis['risks']:
            report.append("### ⚠️ Risques Identifiés\n")
            for risk in analysis['risks'][:3]:
                emoji = {"critical": "🔴", "high": "🟠", "medium": "🟡", "low": "🟢"}.get(risk['level'], "⚪")
                report.append(f"{emoji} **{risk['type'].upper()}**: {risk['description']}")
                report.append(f"   → Mitigation: {risk['mitigation']}\n")
        
        # Recommandations
        if analysis['recommendations']:
            report.append("### 💡 Recommandations\n")
            for i, rec in enumerate(analysis['recommendations'][:3], 1):
                priority_emoji = {"high": "🔥", "medium": "⚡", "low": "💫"}.get(rec['priority'], "•")
                report.append(f"{i}. {priority_emoji} {rec['action']}")
                report.append(f"   - Raison: {rec['reason']}")
                report.append(f"   - Impact: {rec['impact']}\n")
        
        # Questions de clarification
        if analysis['questions']:
            report.append("### ❓ Questions de Clarification\n")
            for q in analysis['questions']:
                report.append(f"- {q}")
        
        return "\n".join(report)


# Singleton pour accès global (DRY)
_cognitive_instance: Optional[CognitiveService] = None

def get_cognitive_service() -> CognitiveService:
    """
    Récupère l'instance unique du service cognitif.
    Pattern Singleton pour cohérence globale.
    """
    global _cognitive_instance
    if _cognitive_instance is None:
        _cognitive_instance = CognitiveService()
    return _cognitive_instance