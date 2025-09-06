# Guide Utilisateur MCP DSFR

## Introduction

MCP DSFR est un serveur Model Context Protocol qui intègre le Design System de l'État français directement dans Claude Desktop. Il vous permet de générer, valider et auditer des composants DSFR conformes aux normes d'accessibilité RGAA 4.1.

### Comment ça fonctionne ?

Une fois le serveur MCP activé dans Claude Desktop, vous pouvez simplement demander à Claude d'utiliser les outils DSFR en langage naturel. Claude comprendra votre demande et utilisera automatiquement l'outil approprié.

## Les 8 outils disponibles

### 1. generer_composant

**Description** : Génère du code HTML pour n'importe quel composant DSFR.

**Exemples d'utilisation** :

```
"Génère un bouton DSFR primaire avec le texte Valider"
"Crée une carte DSFR avec titre et description"
"J'ai besoin d'un formulaire de connexion DSFR"
"Fais-moi un header DSFR avec navigation"
```

**Paramètres disponibles** :
- `component` : Le type de composant (button, card, form, etc.)
- `variant` : La variante du composant (primary, secondary, etc.)
- `options` : Options spécifiques (label, icon, size, etc.)

**Résultat attendu** : Code HTML complet et prêt à l'emploi avec toutes les classes CSS DSFR.

### 2. lister_composants

**Description** : Affiche la liste complète des 48 composants DSFR disponibles, organisés par catégories.

**Exemples d'utilisation** :

```
"Liste tous les composants DSFR disponibles"
"Quels composants DSFR puis-je utiliser ?"
"Montre-moi les composants de formulaire DSFR"
"Qu'est-ce qui est disponible pour la navigation ?"
```

**Résultat attendu** : Liste structurée avec catégories (Navigation, Formulaires, Actions, Contenu, etc.)

### 3. valider_html

**Description** : Vérifie que votre code HTML respecte les standards DSFR et RGAA.

**Exemples d'utilisation** :

```
"Valide ce code HTML : <button class='fr-btn'>Test</button>"
"Vérifie si mon formulaire est conforme DSFR"
"Est-ce que cette structure HTML est correcte pour DSFR ?"
"Analyse la conformité de ma page HTML"
```

**Résultat attendu** : Rapport de validation avec :
- Conformité DSFR (classes CSS correctes)
- Structure HTML valide
- Suggestions d'amélioration

### 4. audit_accessibilite

**Description** : Effectue un audit d'accessibilité selon les critères RGAA 4.1.

**Exemples d'utilisation** :

```
"Fais un audit RGAA de mon formulaire"
"Vérifie l'accessibilité niveau AA de ma page"
"Audit d'accessibilité complet de ce code HTML"
"Quels sont les problèmes d'accessibilité dans mon composant ?"
```

**Niveaux disponibles** :
- A : Niveau minimum
- AA : Niveau recommandé (par défaut)
- AAA : Niveau maximum

**Résultat attendu** : Rapport détaillé avec :
- Score par niveau (A, AA, AAA)
- Liste des problèmes identifiés
- Recommandations de correction
- Éléments à améliorer

### 5. analyser_cognitif

**Description** : Analyse les besoins d'un projet selon la matrice de Rumsfeld (Known/Unknown).

**Exemples d'utilisation** :

```
"Analyse les risques de mon projet de refonte"
"Identifie les zones d'incertitude dans mon cahier des charges"
"Quels sont les angles morts de mon projet ?"
"Analyse cognitive de mes besoins fonctionnels"
```

**Résultat attendu** : Matrice avec :
- Known Knowns : Ce qui est clair et défini
- Known Unknowns : Questions identifiées à résoudre
- Unknown Unknowns : Risques potentiels non identifiés
- Recommandations d'actions

### 6. obtenir_tokens_design

**Description** : Récupère les tokens de design DSFR (couleurs, espacements, typographie).

**Exemples d'utilisation** :

```
"Donne-moi les couleurs officielles DSFR"
"Quels sont les espacements DSFR ?"
"Liste les tokens de typographie DSFR"
"J'ai besoin des variables CSS pour les couleurs"
```

**Catégories disponibles** :
- `colors` : Palette de couleurs
- `spacing` : Espacements et marges
- `typography` : Polices et tailles
- `icons` : Icônes disponibles

**Résultat attendu** : Liste des tokens avec leurs valeurs CSS.

### 7. generer_tests

**Description** : Génère automatiquement des tests pour vos composants DSFR.

**Exemples d'utilisation** :

```
"Génère des tests Cypress pour mon bouton DSFR"
"Crée des tests unitaires Jest pour ce formulaire"
"J'ai besoin de tests e2e Playwright pour ma navigation"
"Écris des tests pour valider mon composant carte"
```

**Types de tests** :
- `unit` : Tests unitaires (Jest)
- `integration` : Tests d'intégration
- `e2e` : Tests end-to-end (Cypress, Playwright)

**Résultat attendu** : Code de test complet et exécutable.

### 8. obtenir_aide_assistant

**Description** : Obtient de l'aide contextuelle et des bonnes pratiques DSFR.

**Exemples d'utilisation** :

```
"Comment rendre un formulaire accessible ?"
"Aide-moi à choisir le bon composant DSFR"
"Quelles sont les bonnes pratiques pour les boutons ?"
"Explique-moi les couleurs système DSFR"
```

**Résultat attendu** : Conseils personnalisés avec exemples de code.

## Cas d'usage courants

### Créer un formulaire de contact complet

```
Claude, j'ai besoin d'un formulaire de contact DSFR avec :
- Champs nom, email, message
- Bouton d'envoi
- Messages d'erreur accessibles
```

Claude utilisera automatiquement `generer_composant` plusieurs fois et assemblera le tout.

### Construire une page d'accueil

```
Aide-moi à créer une page d'accueil avec :
- Un header DSFR avec navigation
- Des cartes pour présenter les services
- Un footer avec liens légaux
```

### Valider et corriger du code existant

```
Voici mon code HTML actuel : [votre code]
Peux-tu :
1. Valider la conformité DSFR
2. Faire un audit d'accessibilité
3. Me proposer les corrections
```

### Migrer vers DSFR

```
J'ai ce formulaire Bootstrap : [code]
Peux-tu le convertir en DSFR tout en gardant la même fonctionnalité ?
```

## Bonnes pratiques

### Comment formuler vos demandes

**Préférez** :
- Des demandes claires et spécifiques
- Mentionner le contexte d'usage
- Préciser les variantes souhaitées

**Évitez** :
- Les demandes trop vagues ("fais-moi un truc DSFR")
- D'oublier les contraintes d'accessibilité
- De mélanger plusieurs frameworks CSS

### Optimisation des résultats

1. **Commencez simple** : Demandez d'abord un composant basique, puis ajoutez des options
2. **Validez régulièrement** : Utilisez `valider_html` après chaque génération importante
3. **Pensez accessibilité** : Faites un audit RGAA avant la mise en production
4. **Documentez** : Demandez à Claude d'expliquer les choix de composants

### Erreurs courantes à éviter

- **Ne pas mélanger** DSFR avec Bootstrap, Tailwind, etc.
- **Ne pas oublier** d'inclure les CSS et JS DSFR dans votre page
- **Ne pas ignorer** les recommandations d'accessibilité
- **Ne pas surcharger** les classes DSFR avec du CSS custom

## Référence rapide

### Les 48 composants disponibles

| Catégorie | Composants |
|-----------|------------|
| **Navigation** | header, footer, breadcrumb, navigation, sidemenu, pagination |
| **Formulaires** | form, input, select, checkbox, radio, toggle, upload, password, search, range |
| **Actions** | button, button-group, link, download, share |
| **Contenu** | accordion, alert, badge, card, table, quote, callout, summary, highlight |
| **Feedback** | modal, notice, tag, stepper, tooltip, transcription |
| **Layout** | grid, container, tile, tabs |
| **Autres** | logo, consent, connect, translate, follow, back-to-top, version |

### Variantes courantes

| Composant | Variantes disponibles |
|-----------|----------------------|
| **button** | primary, secondary, tertiary, ghost |
| **alert** | info, success, warning, error |
| **badge** | success, error, warning, info, new |
| **card** | horizontal, vertical, download, article |
| **input** | text, email, password, number, date, search |

### Exemples de code rapides

**Bouton simple** :
```
"Génère un bouton DSFR primaire"
```

**Formulaire avec validation** :
```
"Crée un champ email DSFR avec message d'erreur"
```

**Navigation complète** :
```
"Génère un header DSFR avec menu et recherche"
```

**Carte de contenu** :
```
"Fais une carte DSFR horizontale avec image"
```

## Support et ressources

### Documentation officielle
- [Système de Design de l'État](https://www.systeme-de-design.gouv.fr)
- [Référentiel RGAA 4.1](https://www.numerique.gouv.fr/publications/rgaa-accessibilite/)

### Commandes utiles
- Vérifier la version DSFR : `python3 check_dsfr_version.py`
- Lancer les tests : `./run_tests.sh`
- Voir tous les gabarits : `ls gabarits/`

### En cas de problème
1. Vérifiez que le serveur MCP est bien connecté (icône dans Claude Desktop)
2. Consultez les logs : `tail -f mcp.log`
3. Relancez Claude Desktop si nécessaire
4. Consultez la documentation technique dans `/README.md`

## Conclusion

MCP DSFR simplifie considérablement l'implémentation du Design System de l'État. N'hésitez pas à expérimenter avec les différents outils et à combiner leurs fonctionnalités pour créer des interfaces conformes et accessibles.

Pour toute question technique, consultez la documentation complète dans le README principal du projet.