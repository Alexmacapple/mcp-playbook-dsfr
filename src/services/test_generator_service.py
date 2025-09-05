"""
Service de génération automatique de tests.
Génère des tests Cypress et Playwright pour les composants DSFR.
Clean Code : SOLID, DRY, KISS
"""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from enum import Enum


class TestFramework(Enum):
    """Frameworks de test supportés."""
    CYPRESS = "cypress"
    PLAYWRIGHT = "playwright"
    JEST = "jest"


@dataclass 
class TestCase:
    """Représente un cas de test."""
    name: str
    description: str
    steps: List[str]
    assertions: List[str]
    data: Optional[Dict[str, Any]] = None


class TestGeneratorService:
    """
    Service de génération de tests automatiques.
    Responsabilité unique : Générer des tests pour les composants (S de SOLID).
    """
    
    def __init__(self):
        """Initialise le service de génération de tests."""
        self.test_patterns = self._init_test_patterns()
        self.assertions = self._init_assertions()
    
    def _init_test_patterns(self) -> Dict[str, List[TestCase]]:
        """Initialise les patterns de test par composant."""
        return {
            "button": [
                TestCase(
                    name="should be clickable and trigger action",
                    description="Vérifie que le bouton est cliquable",
                    steps=[
                        "Localiser le bouton",
                        "Cliquer sur le bouton",
                        "Vérifier l'action déclenchée"
                    ],
                    assertions=[
                        "Le bouton est visible",
                        "Le bouton n'est pas désactivé", 
                        "L'action est déclenchée après le clic"
                    ]
                ),
                TestCase(
                    name="should be keyboard accessible",
                    description="Vérifie l'accessibilité clavier",
                    steps=[
                        "Naviguer au bouton avec Tab",
                        "Activer avec Entrée ou Espace"
                    ],
                    assertions=[
                        "Le bouton reçoit le focus",
                        "Le focus est visible",
                        "Entrée/Espace déclenche l'action"
                    ]
                )
            ],
            "form": [
                TestCase(
                    name="should validate required fields",
                    description="Vérifie la validation des champs requis",
                    steps=[
                        "Laisser les champs requis vides",
                        "Soumettre le formulaire",
                        "Vérifier les messages d'erreur"
                    ],
                    assertions=[
                        "Le formulaire n'est pas soumis",
                        "Les messages d'erreur sont affichés",
                        "Les champs en erreur sont identifiés"
                    ]
                ),
                TestCase(
                    name="should submit with valid data",
                    description="Vérifie la soumission avec données valides",
                    steps=[
                        "Remplir tous les champs requis",
                        "Soumettre le formulaire"
                    ],
                    assertions=[
                        "Le formulaire est soumis",
                        "Pas de messages d'erreur",
                        "Confirmation affichée ou redirection"
                    ]
                )
            ],
            "accordion": [
                TestCase(
                    name="should expand and collapse sections",
                    description="Vérifie l'ouverture/fermeture des sections",
                    steps=[
                        "Cliquer sur un titre de section",
                        "Vérifier l'expansion",
                        "Cliquer à nouveau"
                    ],
                    assertions=[
                        "Le contenu s'affiche à l'ouverture",
                        "Le contenu se masque à la fermeture",
                        "L'état ARIA est mis à jour"
                    ]
                )
            ],
            "modal": [
                TestCase(
                    name="should open and close correctly",
                    description="Vérifie l'ouverture/fermeture de la modale",
                    steps=[
                        "Cliquer sur le déclencheur",
                        "Vérifier l'ouverture",
                        "Fermer avec bouton/ESC"
                    ],
                    assertions=[
                        "La modale s'ouvre",
                        "Le focus est piégé dans la modale",
                        "ESC ferme la modale",
                        "Le focus retourne au déclencheur"
                    ]
                )
            ],
            "table": [
                TestCase(
                    name="should be sortable",
                    description="Vérifie le tri des colonnes",
                    steps=[
                        "Cliquer sur un en-tête de colonne",
                        "Vérifier le tri ascendant",
                        "Cliquer à nouveau"
                    ],
                    assertions=[
                        "Les données sont triées en ascendant",
                        "Les données sont triées en descendant",
                        "L'indicateur de tri est visible"
                    ]
                )
            ]
        }
    
    def _init_assertions(self) -> Dict[str, List[str]]:
        """Initialise les assertions communes."""
        return {
            "visibility": [
                "exists()",
                "isVisible()",
                "isNotHidden()"
            ],
            "interaction": [
                "isEnabled()",
                "isClickable()",
                "isFocusable()"
            ],
            "accessibility": [
                "hasRole()",
                "hasAriaLabel()",
                "hasAriaDescribedBy()"
            ],
            "validation": [
                "hasError()",
                "hasSuccessMessage()",
                "isInvalid()"
            ]
        }
    
    def generate_tests(
        self,
        component: str,
        framework: TestFramework = TestFramework.CYPRESS,
        options: Optional[Dict[str, Any]] = None
    ) -> str:
        """
        Génère les tests pour un composant.
        
        Args:
            component: Type de composant
            framework: Framework de test
            options: Options spécifiques
            
        Returns:
            Code des tests générés
        """
        if framework == TestFramework.CYPRESS:
            return self._generate_cypress_tests(component, options)
        elif framework == TestFramework.PLAYWRIGHT:
            return self._generate_playwright_tests(component, options)
        elif framework == TestFramework.JEST:
            return self._generate_jest_tests(component, options)
        else:
            raise ValueError(f"Framework non supporté : {framework}")
    
    def _generate_cypress_tests(self, component: str, options: Optional[Dict] = None) -> str:
        """Génère des tests Cypress."""
        test_cases = self.test_patterns.get(component, [])
        selector = options.get('selector', f'.fr-{component}') if options else f'.fr-{component}'
        
        code = f"""// Tests Cypress pour composant DSFR : {component}
// Généré automatiquement par TestGeneratorService

describe('DSFR {component.title()} Component', () => {{
    beforeEach(() => {{
        cy.visit('/page-with-{component}');
    }});
"""
        
        for test_case in test_cases:
            code += f"""
    it('{test_case.name}', () => {{
        // {test_case.description}
"""
            
            # Générer les étapes selon le composant
            if component == "button":
                code += f"""
        cy.get('{selector}').should('be.visible');
        cy.get('{selector}').should('not.be.disabled');
        
        // Test du clic
        cy.get('{selector}').click();
        
        // Vérifier l'action (adapter selon le contexte)
        // cy.url().should('include', '/expected-path');
        // ou
        // cy.get('.success-message').should('be.visible');
"""
            elif component == "form":
                code += f"""
        // Test de validation
        cy.get('{selector}').within(() => {{
            // Soumettre sans remplir
            cy.get('button[type="submit"]').click();
            
            // Vérifier les erreurs
            cy.get('.fr-error-text').should('be.visible');
            cy.get('.fr-input--error').should('exist');
        }});
        
        // Test de soumission valide
        cy.get('{selector}').within(() => {{
            cy.get('input[name="email"]').type('test@example.fr');
            cy.get('input[name="password"]').type('MotDePasse123!');
            cy.get('button[type="submit"]').click();
        }});
        
        // Vérifier le succès
        cy.get('.fr-alert--success').should('be.visible');
"""
            elif component == "accordion":
                code += f"""
        // Test d'expansion/collapse
        cy.get('{selector} .fr-accordion__btn').first().as('firstButton');
        
        // État initial fermé
        cy.get('@firstButton').should('have.attr', 'aria-expanded', 'false');
        
        // Ouvrir
        cy.get('@firstButton').click();
        cy.get('@firstButton').should('have.attr', 'aria-expanded', 'true');
        cy.get('@firstButton').next('.fr-collapse').should('be.visible');
        
        // Fermer
        cy.get('@firstButton').click();
        cy.get('@firstButton').should('have.attr', 'aria-expanded', 'false');
"""
            elif component == "modal":
                code += f"""
        // Test d'ouverture
        cy.get('[data-fr-opened="false"]').click();
        cy.get('{selector}').should('be.visible');
        cy.get('{selector} .fr-modal__body').should('be.visible');
        
        // Test du piège de focus
        cy.focused().should('be.within', cy.get('{selector}'));
        
        // Test de fermeture avec ESC
        cy.get('body').type('{{esc}}');
        cy.get('{selector}').should('not.be.visible');
        
        // Test de fermeture avec bouton
        cy.get('[data-fr-opened="false"]').click();
        cy.get('{selector} .fr-btn--close').click();
        cy.get('{selector}').should('not.be.visible');
"""
            elif component == "table":
                code += f"""
        // Test de tri
        cy.get('{selector} th[data-sortable]').first().as('sortHeader');
        
        // Tri ascendant
        cy.get('@sortHeader').click();
        cy.get('@sortHeader').should('have.attr', 'aria-sort', 'ascending');
        
        // Vérifier l'ordre (adapter selon les données)
        cy.get('{selector} tbody tr').first().should('contain', 'A');
        
        // Tri descendant
        cy.get('@sortHeader').click();
        cy.get('@sortHeader').should('have.attr', 'aria-sort', 'descending');
        cy.get('{selector} tbody tr').first().should('contain', 'Z');
"""
            
            code += """    });
"""
        
        # Ajouter les tests d'accessibilité
        code += f"""
    it('should be accessible', () => {{
        // Test d'accessibilité automatique
        cy.injectAxe();
        cy.checkA11y('{selector}', {{
            runOnly: {{
                type: 'tag',
                values: ['wcag2a', 'wcag2aa']
            }}
        }});
        
        // Navigation clavier
        cy.get('{selector}').first().focus();
        cy.focused().should('have.class', 'fr-{component}');
        
        // Test avec lecteur d'écran simulé
        cy.get('{selector}').should('have.attr', 'role');
        cy.get('{selector}').should('have.attr', 'aria-label');
    }});
}});
"""
        
        return code
    
    def _generate_playwright_tests(self, component: str, options: Optional[Dict] = None) -> str:
        """Génère des tests Playwright."""
        test_cases = self.test_patterns.get(component, [])
        selector = options.get('selector', f'.fr-{component}') if options else f'.fr-{component}'
        
        code = f"""// Tests Playwright pour composant DSFR : {component}
// Généré automatiquement par TestGeneratorService

import {{ test, expect }} from '@playwright/test';

test.describe('DSFR {component.title()} Component', () => {{
    test.beforeEach(async ({{ page }}) => {{
        await page.goto('/page-with-{component}');
    }});
"""
        
        for test_case in test_cases:
            code += f"""
    test('{test_case.name}', async ({{ page }}) => {{
        // {test_case.description}
"""
            
            if component == "button":
                code += f"""
        const button = page.locator('{selector}');
        await expect(button).toBeVisible();
        await expect(button).toBeEnabled();
        
        // Test du clic
        await button.click();
        
        // Vérifier l'action (adapter selon le contexte)
        // await expect(page).toHaveURL(/.*expected-path/);
        // ou
        // await expect(page.locator('.success-message')).toBeVisible();
"""
            elif component == "form":
                code += f"""
        const form = page.locator('{selector}');
        
        // Test de validation
        await form.locator('button[type="submit"]').click();
        await expect(form.locator('.fr-error-text')).toBeVisible();
        
        // Test de soumission valide
        await form.locator('input[name="email"]').fill('test@example.fr');
        await form.locator('input[name="password"]').fill('MotDePasse123!');
        await form.locator('button[type="submit"]').click();
        
        // Vérifier le succès
        await expect(page.locator('.fr-alert--success')).toBeVisible();
"""
            elif component == "accordion":
                code += f"""
        const accordion = page.locator('{selector}');
        const firstButton = accordion.locator('.fr-accordion__btn').first();
        
        // État initial
        await expect(firstButton).toHaveAttribute('aria-expanded', 'false');
        
        // Ouvrir
        await firstButton.click();
        await expect(firstButton).toHaveAttribute('aria-expanded', 'true');
        
        // Fermer
        await firstButton.click();
        await expect(firstButton).toHaveAttribute('aria-expanded', 'false');
"""
            elif component == "modal":
                code += f"""
        // Ouvrir la modale
        await page.locator('[data-fr-opened="false"]').click();
        const modal = page.locator('{selector}');
        await expect(modal).toBeVisible();
        
        // Fermer avec ESC
        await page.keyboard.press('Escape');
        await expect(modal).not.toBeVisible();
        
        // Fermer avec bouton
        await page.locator('[data-fr-opened="false"]').click();
        await modal.locator('.fr-btn--close').click();
        await expect(modal).not.toBeVisible();
"""
            
            code += """    });
"""
        
        # Tests d'accessibilité
        code += f"""
    test('should be accessible', async ({{ page }}) => {{
        // Snapshot d'accessibilité
        const accessibilitySnapshot = await page.accessibility.snapshot();
        expect(accessibilitySnapshot).toBeDefined();
        
        // Navigation clavier
        await page.locator('{selector}').first().focus();
        const focused = await page.evaluate(() => document.activeElement?.className);
        expect(focused).toContain('fr-{component}');
        
        // Vérifier les attributs ARIA
        const element = page.locator('{selector}').first();
        await expect(element).toHaveAttribute('role', /.+/);
    }});
}});
"""
        
        return code
    
    def _generate_jest_tests(self, component: str, options: Optional[Dict] = None) -> str:
        """Génère des tests Jest pour composants React/Vue."""
        code = f"""// Tests Jest pour composant DSFR : {component}
// Généré automatiquement par TestGeneratorService

import {{ render, screen, fireEvent, waitFor }} from '@testing-library/react';
import '@testing-library/jest-dom';
import {component.title()}Component from './components/{component.title()}Component';

describe('DSFR {component.title()} Component', () => {{
"""
        
        if component == "button":
            code += """
    test('renders and handles click', () => {
        const handleClick = jest.fn();
        render(<ButtonComponent onClick={handleClick}>Cliquer ici</ButtonComponent>);
        
        const button = screen.getByRole('button', { name: /cliquer ici/i });
        expect(button).toBeInTheDocument();
        expect(button).toBeEnabled();
        
        fireEvent.click(button);
        expect(handleClick).toHaveBeenCalledTimes(1);
    });
    
    test('is keyboard accessible', () => {
        const handleClick = jest.fn();
        render(<ButtonComponent onClick={handleClick}>Test</ButtonComponent>);
        
        const button = screen.getByRole('button');
        button.focus();
        expect(button).toHaveFocus();
        
        fireEvent.keyDown(button, { key: 'Enter' });
        expect(handleClick).toHaveBeenCalled();
    });
"""
        elif component == "form":
            code += """
    test('validates required fields', async () => {
        const handleSubmit = jest.fn();
        render(<FormComponent onSubmit={handleSubmit} />);
        
        const submitButton = screen.getByRole('button', { name: /soumettre/i });
        fireEvent.click(submitButton);
        
        expect(handleSubmit).not.toHaveBeenCalled();
        expect(screen.getByText(/ce champ est requis/i)).toBeInTheDocument();
    });
    
    test('submits with valid data', async () => {
        const handleSubmit = jest.fn();
        render(<FormComponent onSubmit={handleSubmit} />);
        
        const emailInput = screen.getByLabelText(/email/i);
        const passwordInput = screen.getByLabelText(/mot de passe/i);
        
        fireEvent.change(emailInput, { target: { value: 'test@example.fr' } });
        fireEvent.change(passwordInput, { target: { value: 'Password123!' } });
        
        const submitButton = screen.getByRole('button', { name: /soumettre/i });
        fireEvent.click(submitButton);
        
        await waitFor(() => {
            expect(handleSubmit).toHaveBeenCalledWith({
                email: 'test@example.fr',
                password: 'Password123!'
            });
        });
    });
"""
        
        code += """
    test('meets accessibility standards', () => {
        const { container } = render(<""" + component.title() + """Component />);
        
        // Vérifier les labels
        const inputs = container.querySelectorAll('input');
        inputs.forEach(input => {
            if (input.type !== 'hidden') {
                expect(input).toHaveAccessibleName();
            }
        });
        
        // Vérifier les rôles ARIA
        expect(container.firstChild).toHaveAttribute('role');
    });
});
"""
        
        return code
    
    def generate_e2e_scenario(
        self,
        components: List[str],
        scenario: str,
        framework: TestFramework = TestFramework.CYPRESS
    ) -> str:
        """
        Génère un scénario E2E complet.
        
        Args:
            components: Liste des composants impliqués
            scenario: Description du scénario
            framework: Framework de test
            
        Returns:
            Code du scénario E2E
        """
        if framework == TestFramework.CYPRESS:
            code = f"""// Scénario E2E : {scenario}
// Composants testés : {', '.join(components)}

describe('E2E: {scenario}', () => {{
    it('should complete the full user journey', () => {{
        cy.visit('/');
        
"""
            
            if "form" in components and "modal" in components:
                code += """        // Ouvrir le formulaire dans une modale
        cy.get('[data-test="open-form"]').click();
        cy.get('.fr-modal').should('be.visible');
        
        // Remplir et soumettre le formulaire
        cy.get('.fr-modal').within(() => {
            cy.get('input[name="email"]').type('user@example.fr');
            cy.get('input[name="name"]').type('Jean Dupont');
            cy.get('button[type="submit"]').click();
        });
        
        // Vérifier la fermeture de la modale et le message de succès
        cy.get('.fr-modal').should('not.be.visible');
        cy.get('.fr-alert--success').should('contain', 'Inscription réussie');
"""
            
            code += """    });
});
"""
        
        return code


# Singleton
_instance: Optional[TestGeneratorService] = None

def get_test_generator() -> TestGeneratorService:
    """Retourne l'instance singleton du TestGeneratorService."""
    global _instance
    if _instance is None:
        _instance = TestGeneratorService()
    return _instance