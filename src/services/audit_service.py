"""
Service d'audit RGAA approfondi.
Analyse, score et corrections automatiques pour l'accessibilité.
Clean Code : SOLID, DRY, KISS
"""

from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass
from enum import Enum
import re
from bs4 import BeautifulSoup, Tag


class RGAALevel(Enum):
    """Niveaux de conformité RGAA/WCAG."""
    A = "A"
    AA = "AA" 
    AAA = "AAA"


class RGAACriterion(Enum):
    """Critères RGAA principaux."""
    # Images
    IMG_ALT = "1.1"  # Images avec alternative textuelle
    IMG_DECORATIVE = "1.2"  # Images décoratives
    IMG_CAPTION = "1.3"  # Images avec légende
    
    # Cadres
    IFRAME_TITLE = "2.1"  # Cadres avec titre
    
    # Couleurs
    COLOR_CONTRAST = "3.2"  # Contraste des couleurs
    COLOR_INFO = "3.1"  # Information par la couleur
    
    # Multimédia
    VIDEO_CAPTION = "4.1"  # Vidéos avec sous-titres
    AUDIO_TRANSCRIPT = "4.2"  # Audio avec transcription
    
    # Tableaux
    TABLE_HEADER = "5.1"  # En-têtes de tableaux
    TABLE_CAPTION = "5.4"  # Titre de tableau
    
    # Liens
    LINK_CONTEXT = "6.1"  # Liens explicites
    LINK_TITLE = "6.2"  # Liens avec titre si nécessaire
    
    # Scripts
    SCRIPT_ALTERNATIVE = "7.1"  # Alternative aux scripts
    SCRIPT_KEYBOARD = "7.3"  # Scripts utilisables au clavier
    
    # Éléments obligatoires
    LANG = "8.3"  # Langue de la page
    TITLE = "8.5"  # Titre de page
    LANDMARKS = "9.2"  # Landmarks ARIA
    
    # Navigation
    NAV_CONSISTENT = "9.3"  # Navigation cohérente
    SKIP_LINKS = "9.7"  # Liens d'évitement
    
    # Présentation
    CSS_DISABLED = "10.2"  # Lisible sans CSS
    ZOOM_200 = "10.4"  # Zoom à 200%
    
    # Formulaires
    FORM_LABEL = "11.1"  # Labels de formulaires
    FORM_ERROR = "11.10"  # Messages d'erreur
    FORM_REQUIRED = "11.9"  # Champs obligatoires
    
    # Navigation
    FOCUS_VISIBLE = "12.7"  # Focus visible
    TAB_ORDER = "12.8"  # Ordre de tabulation


@dataclass
class AuditIssue:
    """Représente un problème d'accessibilité détecté."""
    criterion: RGAACriterion
    level: RGAALevel
    element: str
    issue: str
    impact: str  # "critical", "serious", "moderate", "minor"
    suggestion: Optional[str] = None
    auto_fix: Optional[str] = None
    line_number: Optional[int] = None


@dataclass
class AuditReport:
    """Rapport d'audit complet."""
    score_a: float
    score_aa: float
    score_aaa: float
    total_issues: int
    critical_issues: int
    issues: List[AuditIssue]
    passed_criteria: List[RGAACriterion]
    recommendations: List[str]
    auto_fixes: Dict[str, str]


class AuditService:
    """
    Service d'audit RGAA/WCAG approfondi.
    Responsabilité unique : Auditer l'accessibilité (S de SOLID).
    """
    
    def __init__(self):
        """Initialise le service d'audit."""
        self.criteria_weights = self._init_criteria_weights()
        self.contrast_ratios = {
            "normal_AA": 4.5,
            "normal_AAA": 7.0,
            "large_AA": 3.0,
            "large_AAA": 4.5
        }
        
    def _init_criteria_weights(self) -> Dict[RGAACriterion, Dict[str, Any]]:
        """Initialise les poids et niveaux des critères."""
        return {
            # Niveau A - Essentiel
            RGAACriterion.IMG_ALT: {"level": RGAALevel.A, "weight": 3, "impact": "critical"},
            RGAACriterion.FORM_LABEL: {"level": RGAALevel.A, "weight": 3, "impact": "critical"},
            RGAACriterion.LANG: {"level": RGAALevel.A, "weight": 2, "impact": "serious"},
            RGAACriterion.TITLE: {"level": RGAALevel.A, "weight": 2, "impact": "serious"},
            RGAACriterion.LINK_CONTEXT: {"level": RGAALevel.A, "weight": 2, "impact": "serious"},
            RGAACriterion.TABLE_HEADER: {"level": RGAALevel.A, "weight": 2, "impact": "serious"},
            RGAACriterion.IFRAME_TITLE: {"level": RGAALevel.A, "weight": 1, "impact": "moderate"},
            
            # Niveau AA - Recommandé
            RGAACriterion.COLOR_CONTRAST: {"level": RGAALevel.AA, "weight": 3, "impact": "serious"},
            RGAACriterion.FOCUS_VISIBLE: {"level": RGAALevel.AA, "weight": 3, "impact": "serious"},
            RGAACriterion.SKIP_LINKS: {"level": RGAALevel.AA, "weight": 2, "impact": "moderate"},
            RGAACriterion.FORM_ERROR: {"level": RGAALevel.AA, "weight": 2, "impact": "moderate"},
            RGAACriterion.ZOOM_200: {"level": RGAALevel.AA, "weight": 2, "impact": "moderate"},
            RGAACriterion.VIDEO_CAPTION: {"level": RGAALevel.AA, "weight": 2, "impact": "moderate"},
            
            # Niveau AAA - Excellence
            RGAACriterion.LANDMARKS: {"level": RGAALevel.AAA, "weight": 1, "impact": "minor"},
            RGAACriterion.NAV_CONSISTENT: {"level": RGAALevel.AAA, "weight": 1, "impact": "minor"},
            RGAACriterion.CSS_DISABLED: {"level": RGAALevel.AAA, "weight": 1, "impact": "minor"}
        }
    
    def audit(self, html: str, level: RGAALevel = RGAALevel.AA) -> AuditReport:
        """
        Effectue un audit RGAA complet.
        
        Args:
            html: HTML à auditer
            level: Niveau cible (A, AA, AAA)
            
        Returns:
            Rapport d'audit détaillé
        """
        soup = BeautifulSoup(html, 'html.parser')
        issues = []
        passed = []
        
        # Audit des images
        issues.extend(self._audit_images(soup))
        
        # Audit des formulaires
        issues.extend(self._audit_forms(soup))
        
        # Audit de la structure
        issues.extend(self._audit_structure(soup))
        
        # Audit des liens
        issues.extend(self._audit_links(soup))
        
        # Audit des tableaux
        issues.extend(self._audit_tables(soup))
        
        # Audit des couleurs/contrastes
        issues.extend(self._audit_colors(soup))
        
        # Audit de la navigation
        issues.extend(self._audit_navigation(soup))
        
        # Calcul des scores
        scores = self._calculate_scores(issues, passed)
        
        # Génération des corrections automatiques
        auto_fixes = self._generate_auto_fixes(issues, soup)
        
        # Recommandations
        recommendations = self._generate_recommendations(issues, level)
        
        return AuditReport(
            score_a=scores['A'],
            score_aa=scores['AA'],
            score_aaa=scores['AAA'],
            total_issues=len(issues),
            critical_issues=len([i for i in issues if i.impact == "critical"]),
            issues=issues,
            passed_criteria=passed,
            recommendations=recommendations,
            auto_fixes=auto_fixes
        )
    
    def _audit_images(self, soup: BeautifulSoup) -> List[AuditIssue]:
        """Audit des images."""
        issues = []
        
        for img in soup.find_all('img'):
            # Vérifier l'attribut alt
            if not img.get('alt'):
                if not img.get('role') == 'presentation':
                    issues.append(AuditIssue(
                        criterion=RGAACriterion.IMG_ALT,
                        level=RGAALevel.A,
                        element=str(img)[:100],
                        issue="Image sans attribut alt",
                        impact="critical",
                        suggestion="Ajouter un alt descriptif ou alt='' si décorative",
                        auto_fix=f'<img alt="[Description de l\'image]" {self._copy_attributes(img)}/>'
                    ))
            
            # Vérifier si l'image est dans un figure avec figcaption
            parent = img.parent
            if parent and parent.name == 'figure':
                if not parent.find('figcaption'):
                    issues.append(AuditIssue(
                        criterion=RGAACriterion.IMG_CAPTION,
                        level=RGAALevel.A,
                        element=str(parent)[:100],
                        issue="Figure sans figcaption",
                        impact="moderate",
                        suggestion="Ajouter une légende avec <figcaption>"
                    ))
        
        return issues
    
    def _audit_forms(self, soup: BeautifulSoup) -> List[AuditIssue]:
        """Audit des formulaires."""
        issues = []
        
        # Vérifier les labels
        for input_elem in soup.find_all(['input', 'select', 'textarea']):
            if input_elem.get('type') not in ['hidden', 'submit', 'button', 'reset']:
                input_id = input_elem.get('id')
                
                # Chercher un label associé
                has_label = False
                if input_id:
                    label = soup.find('label', {'for': input_id})
                    if label:
                        has_label = True
                
                # Vérifier aria-label ou aria-labelledby
                if not has_label:
                    if not input_elem.get('aria-label') and not input_elem.get('aria-labelledby'):
                        issues.append(AuditIssue(
                            criterion=RGAACriterion.FORM_LABEL,
                            level=RGAALevel.A,
                            element=str(input_elem)[:100],
                            issue="Champ de formulaire sans label",
                            impact="critical",
                            suggestion="Ajouter un <label> ou aria-label",
                            auto_fix=f'<label for="{input_id or "field-id"}">[Libellé]</label>'
                        ))
                
                # Vérifier les champs obligatoires
                if input_elem.get('required'):
                    if not input_elem.get('aria-required'):
                        issues.append(AuditIssue(
                            criterion=RGAACriterion.FORM_REQUIRED,
                            level=RGAALevel.AA,
                            element=str(input_elem)[:100],
                            issue="Champ requis sans aria-required",
                            impact="moderate",
                            suggestion="Ajouter aria-required='true'",
                            auto_fix=self._add_attribute(input_elem, 'aria-required', 'true')
                        ))
        
        # Vérifier les messages d'erreur
        for elem in soup.find_all(class_=re.compile(r'error|erreur|invalid')):
            if not elem.get('role') == 'alert':
                issues.append(AuditIssue(
                    criterion=RGAACriterion.FORM_ERROR,
                    level=RGAALevel.AA,
                    element=str(elem)[:100],
                    issue="Message d'erreur sans role='alert'",
                    impact="moderate",
                    suggestion="Ajouter role='alert' aux messages d'erreur",
                    auto_fix=self._add_attribute(elem, 'role', 'alert')
                ))
        
        return issues
    
    def _audit_structure(self, soup: BeautifulSoup) -> List[AuditIssue]:
        """Audit de la structure du document."""
        issues = []
        
        # Vérifier la langue
        html_tag = soup.find('html')
        if html_tag and not html_tag.get('lang'):
            issues.append(AuditIssue(
                criterion=RGAACriterion.LANG,
                level=RGAALevel.A,
                element="<html>",
                issue="Langue du document non spécifiée",
                impact="serious",
                suggestion="Ajouter lang='fr' à la balise <html>",
                auto_fix='<html lang="fr">'
            ))
        
        # Vérifier le titre
        title_tag = soup.find('title')
        if not title_tag or not title_tag.string:
            issues.append(AuditIssue(
                criterion=RGAACriterion.TITLE,
                level=RGAALevel.A,
                element="<head>",
                issue="Titre de page manquant ou vide",
                impact="serious",
                suggestion="Ajouter un <title> descriptif",
                auto_fix='<title>Titre de la page - Site DSFR</title>'
            ))
        
        # Vérifier les landmarks ARIA
        main_tag = soup.find(['main', '[role="main"]'])
        if not main_tag:
            issues.append(AuditIssue(
                criterion=RGAACriterion.LANDMARKS,
                level=RGAALevel.AAA,
                element="<body>",
                issue="Pas de landmark <main>",
                impact="minor",
                suggestion="Ajouter <main> ou role='main'",
                auto_fix='<main role="main">'
            ))
        
        # Vérifier les liens d'évitement
        skip_link = soup.find('a', href='#main') or soup.find('a', href='#content')
        if not skip_link:
            issues.append(AuditIssue(
                criterion=RGAACriterion.SKIP_LINKS,
                level=RGAALevel.AA,
                element="<body>",
                issue="Pas de lien d'évitement",
                impact="moderate",
                suggestion="Ajouter un lien 'Aller au contenu principal'",
                auto_fix='<a href="#main" class="fr-link">Aller au contenu principal</a>'
            ))
        
        return issues
    
    def _audit_links(self, soup: BeautifulSoup) -> List[AuditIssue]:
        """Audit des liens."""
        issues = []
        
        for link in soup.find_all('a', href=True):
            link_text = link.get_text(strip=True)
            
            # Vérifier les liens vides
            if not link_text and not link.get('aria-label'):
                issues.append(AuditIssue(
                    criterion=RGAACriterion.LINK_CONTEXT,
                    level=RGAALevel.A,
                    element=str(link)[:100],
                    issue="Lien sans texte ni aria-label",
                    impact="serious",
                    suggestion="Ajouter du texte ou aria-label au lien",
                    auto_fix=self._add_attribute(link, 'aria-label', '[Description du lien]')
                ))
            
            # Vérifier les liens génériques
            generic_texts = ['cliquez ici', 'ici', 'lire plus', 'plus', 'suite']
            if link_text.lower() in generic_texts:
                issues.append(AuditIssue(
                    criterion=RGAACriterion.LINK_CONTEXT,
                    level=RGAALevel.A,
                    element=str(link)[:100],
                    issue=f"Lien avec texte non explicite : '{link_text}'",
                    impact="moderate",
                    suggestion="Utiliser un texte de lien plus descriptif"
                ))
            
            # Vérifier les liens externes
            if link['href'].startswith('http') and 'gov.fr' not in link['href']:
                if 'external' not in str(link.get('class', [])):
                    issues.append(AuditIssue(
                        criterion=RGAACriterion.LINK_TITLE,
                        level=RGAALevel.AA,
                        element=str(link)[:100],
                        issue="Lien externe sans indication",
                        impact="minor",
                        suggestion="Ajouter une indication de lien externe",
                        auto_fix=self._add_attribute(link, 'title', f'{link_text} - nouvelle fenêtre')
                    ))
        
        return issues
    
    def _audit_tables(self, soup: BeautifulSoup) -> List[AuditIssue]:
        """Audit des tableaux."""
        issues = []
        
        for table in soup.find_all('table'):
            # Vérifier les en-têtes
            if not table.find('th'):
                issues.append(AuditIssue(
                    criterion=RGAACriterion.TABLE_HEADER,
                    level=RGAALevel.A,
                    element=str(table)[:100],
                    issue="Tableau sans en-têtes <th>",
                    impact="serious",
                    suggestion="Ajouter des <th> avec scope approprié"
                ))
            
            # Vérifier le caption
            if not table.find('caption'):
                issues.append(AuditIssue(
                    criterion=RGAACriterion.TABLE_CAPTION,
                    level=RGAALevel.A,
                    element=str(table)[:100],
                    issue="Tableau sans <caption>",
                    impact="moderate",
                    suggestion="Ajouter un <caption> descriptif",
                    auto_fix='<caption>Titre du tableau</caption>'
                ))
            
            # Vérifier les scopes
            for th in table.find_all('th'):
                if not th.get('scope'):
                    issues.append(AuditIssue(
                        criterion=RGAACriterion.TABLE_HEADER,
                        level=RGAALevel.A,
                        element=str(th)[:100],
                        issue="En-tête sans attribut scope",
                        impact="moderate",
                        suggestion="Ajouter scope='col' ou scope='row'",
                        auto_fix=self._add_attribute(th, 'scope', 'col')
                    ))
        
        return issues
    
    def _audit_colors(self, soup: BeautifulSoup) -> List[AuditIssue]:
        """Audit des couleurs et contrastes."""
        issues = []
        
        # Note: L'audit complet des contrastes nécessiterait l'analyse CSS
        # Ici on vérifie juste les patterns problématiques connus
        
        # Vérifier les textes sur images sans ombre
        for elem in soup.find_all(style=re.compile(r'background-image')):
            if elem.get_text(strip=True):
                if 'text-shadow' not in str(elem.get('style', '')):
                    issues.append(AuditIssue(
                        criterion=RGAACriterion.COLOR_CONTRAST,
                        level=RGAALevel.AA,
                        element=str(elem)[:100],
                        issue="Texte sur image sans ombre portée",
                        impact="serious",
                        suggestion="Ajouter text-shadow ou fond semi-transparent"
                    ))
        
        return issues
    
    def _audit_navigation(self, soup: BeautifulSoup) -> List[AuditIssue]:
        """Audit de la navigation au clavier."""
        issues = []
        
        # Vérifier les éléments focusables
        for elem in soup.find_all(['a', 'button', 'input', 'select', 'textarea']):
            # Vérifier tabindex négatif (sauf si volontaire)
            tabindex = elem.get('tabindex')
            if tabindex and int(tabindex) < -1:
                issues.append(AuditIssue(
                    criterion=RGAACriterion.TAB_ORDER,
                    level=RGAALevel.AA,
                    element=str(elem)[:100],
                    issue=f"tabindex={tabindex} empêche la navigation clavier",
                    impact="serious",
                    suggestion="Utiliser tabindex='0' ou '-1' uniquement"
                ))
        
        # Vérifier les événements mouse-only
        for elem in soup.find_all(onmouseover=True):
            if not elem.get('onfocus'):
                issues.append(AuditIssue(
                    criterion=RGAACriterion.SCRIPT_KEYBOARD,
                    level=RGAALevel.A,
                    element=str(elem)[:100],
                    issue="Événement onmouseover sans équivalent clavier",
                    impact="serious",
                    suggestion="Ajouter onfocus pour l'accessibilité clavier"
                ))
        
        return issues
    
    def _calculate_scores(self, issues: List[AuditIssue], passed: List[RGAACriterion]) -> Dict[str, float]:
        """Calcule les scores par niveau."""
        scores = {'A': 100.0, 'AA': 100.0, 'AAA': 100.0}
        
        # Regrouper les issues par niveau
        issues_by_level = {'A': [], 'AA': [], 'AAA': []}
        for issue in issues:
            issues_by_level[issue.level.value].append(issue)
        
        # Calculer les pénalités
        for level in ['A', 'AA', 'AAA']:
            total_weight = 0
            penalty = 0
            
            for criterion, info in self.criteria_weights.items():
                if info['level'].value == level or (level == 'AA' and info['level'].value == 'A') or (level == 'AAA'):
                    total_weight += info['weight']
                    
                    # Compter les issues pour ce critère
                    criterion_issues = [i for i in issues if i.criterion == criterion]
                    if criterion_issues:
                        penalty += info['weight']
            
            if total_weight > 0:
                scores[level] = max(0, 100 * (1 - penalty / total_weight))
        
        return scores
    
    def _generate_auto_fixes(self, issues: List[AuditIssue], soup: BeautifulSoup) -> Dict[str, str]:
        """Génère les corrections automatiques."""
        fixes = {}
        
        for issue in issues:
            if issue.auto_fix:
                key = f"{issue.criterion.value}_{issue.element[:30]}"
                fixes[key] = issue.auto_fix
        
        return fixes
    
    def _generate_recommendations(self, issues: List[AuditIssue], target_level: RGAALevel) -> List[str]:
        """Génère les recommandations prioritaires."""
        recommendations = []
        
        # Compter les issues par impact
        critical_count = len([i for i in issues if i.impact == "critical"])
        serious_count = len([i for i in issues if i.impact == "serious"])
        
        if critical_count > 0:
            recommendations.append(
                f"🔴 Corriger en priorité les {critical_count} problèmes critiques "
                f"(principalement labels de formulaires et alternatives d'images)"
            )
        
        if serious_count > 0:
            recommendations.append(
                f"🟠 Traiter les {serious_count} problèmes sérieux "
                f"(contrastes, langue du document, navigation clavier)"
            )
        
        # Recommandations spécifiques par pattern
        form_issues = [i for i in issues if 'form' in i.criterion.value.lower()]
        if len(form_issues) > 5:
            recommendations.append(
                "📝 Réviser l'accessibilité des formulaires : "
                "ajouter labels, messages d'erreur et indications des champs requis"
            )
        
        img_issues = [i for i in issues if i.criterion == RGAACriterion.IMG_ALT]
        if img_issues:
            recommendations.append(
                "🖼️ Ajouter des alternatives textuelles à toutes les images informatives"
            )
        
        # Recommandation niveau cible
        if target_level == RGAALevel.AAA:
            recommendations.append(
                "⭐ Pour atteindre le niveau AAA : ajouter landmarks ARIA, "
                "améliorer la navigation cohérente et tester sans CSS"
            )
        
        return recommendations
    
    def _copy_attributes(self, elem: Tag) -> str:
        """Copie les attributs d'un élément."""
        attrs = []
        for key, value in elem.attrs.items():
            if key != 'alt':
                attrs.append(f'{key}="{value}"')
        return ' '.join(attrs)
    
    def _add_attribute(self, elem: Tag, attr: str, value: str) -> str:
        """Ajoute un attribut à un élément."""
        elem_copy = str(elem)
        if elem.name:
            return elem_copy.replace(f'<{elem.name}', f'<{elem.name} {attr}="{value}"', 1)
        return elem_copy
    
    def generate_report_html(self, report: AuditReport) -> str:
        """
        Génère un rapport HTML formaté.
        
        Args:
            report: Rapport d'audit
            
        Returns:
            HTML du rapport
        """
        html = f"""
        <!DOCTYPE html>
        <html lang="fr">
        <head>
            <meta charset="UTF-8">
            <title>Rapport d'audit RGAA</title>
            <link rel="stylesheet" href="https://unpkg.com/@gouvfr/dsfr/dist/dsfr.min.css">
        </head>
        <body>
            <div class="fr-container">
                <h1>Rapport d'audit RGAA</h1>
                
                <div class="fr-grid-row fr-grid-row--gutters">
                    <div class="fr-col-4">
                        <div class="fr-tile">
                            <div class="fr-tile__body">
                                <h3 class="fr-tile__title">Score niveau A</h3>
                                <p class="fr-tile__desc">{report.score_a:.1f}%</p>
                            </div>
                        </div>
                    </div>
                    <div class="fr-col-4">
                        <div class="fr-tile">
                            <div class="fr-tile__body">
                                <h3 class="fr-tile__title">Score niveau AA</h3>
                                <p class="fr-tile__desc">{report.score_aa:.1f}%</p>
                            </div>
                        </div>
                    </div>
                    <div class="fr-col-4">
                        <div class="fr-tile">
                            <div class="fr-tile__body">
                                <h3 class="fr-tile__title">Score niveau AAA</h3>
                                <p class="fr-tile__desc">{report.score_aaa:.1f}%</p>
                            </div>
                        </div>
                    </div>
                </div>
                
                <h2>Problèmes détectés ({report.total_issues})</h2>
                
                <div class="fr-table">
                    <table>
                        <caption>Liste des problèmes d'accessibilité</caption>
                        <thead>
                            <tr>
                                <th scope="col">Critère</th>
                                <th scope="col">Niveau</th>
                                <th scope="col">Impact</th>
                                <th scope="col">Description</th>
                                <th scope="col">Suggestion</th>
                            </tr>
                        </thead>
                        <tbody>
        """
        
        for issue in report.issues[:20]:  # Limiter à 20 pour l'exemple
            html += f"""
                            <tr>
                                <td>{issue.criterion.value}</td>
                                <td>{issue.level.value}</td>
                                <td><span class="fr-badge fr-badge--{'error' if issue.impact == 'critical' else 'warning'}">{issue.impact}</span></td>
                                <td>{issue.issue}</td>
                                <td>{issue.suggestion or '-'}</td>
                            </tr>
            """
        
        html += """
                        </tbody>
                    </table>
                </div>
                
                <h2>Recommandations</h2>
                <ul>
        """
        
        for rec in report.recommendations:
            html += f"<li>{rec}</li>"
        
        html += """
                </ul>
            </div>
        </body>
        </html>
        """
        
        return html


# Singleton
_instance: Optional[AuditService] = None

def get_audit_service() -> AuditService:
    """Retourne l'instance singleton du AuditService."""
    global _instance
    if _instance is None:
        _instance = AuditService()
    return _instance