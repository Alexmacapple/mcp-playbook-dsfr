# 📚 CAHIER DE TEST EXHAUSTIF - MCP DSFR v2.0

## 📋 Vue d'ensemble
- **Projet** : MCP Playbook DSFR
- **Version** : 2.0.0
- **Date** : 2025-09-05
- **Outils testés** : 8 outils MCP
- **Environnement** : Claude Desktop + Python 3.13

---

## 🧪 TESTS PAR OUTIL

### 1️⃣ OUTIL : `generate_component`
**Description** : Génère des composants DSFR

#### Test 1.1 : Bouton simple
```
Génère un bouton DSFR avec le label "Cliquer ici"
```
**Résultat attendu** :
```html
<button class="fr-btn">
    Cliquer ici
</button>
```

#### Test 1.2 : Bouton avec variante
```
Génère un bouton secondaire avec le label "Annuler"
```
**Résultat attendu** :
```html
<button class="fr-btn fr-btn--secondary">
    Annuler
</button>
```

#### Test 1.3 : Bouton avec icône
```
Génère un bouton avec icône "arrow-right" et label "Suivant"
```
**Résultat attendu** :
```html
<button class="fr-btn fr-icon-arrow-right-line fr-btn--icon-right">
    Suivant
</button>
```

#### Test 1.4 : Alerte info
```
Génère une alerte info avec le message "Opération réussie"
```
**Résultat attendu** :
```html
<div class="fr-alert fr-alert--info">
    <h3 class="fr-alert__title">Information</h3>
    <p>Opération réussie</p>
</div>
```

#### Test 1.5 : Alerte erreur
```
Génère une alerte erreur avec le message "Une erreur est survenue"
```
**Résultat attendu** :
```html
<div class="fr-alert fr-alert--error">
    <h3 class="fr-alert__title">Erreur</h3>
    <p>Une erreur est survenue</p>
</div>
```

#### Test 1.6 : Badge
```
Génère un badge avec le texte "Nouveau"
```
**Résultat attendu** :
```html
<p class="fr-badge">Nouveau</p>
```

#### Test 1.7 : Carte (Card)
```
Génère une carte avec titre "Ma carte" et description "Contenu de la carte"
```
**Résultat attendu** :
```html
<div class="fr-card">
    <div class="fr-card__body">
        <h3 class="fr-card__title">Ma carte</h3>
        <p class="fr-card__desc">Contenu de la carte</p>
    </div>
</div>
```

#### Test 1.8 : Accordéon
```
Génère un accordéon avec titre "Section 1" et contenu "Contenu dépliable"
```
**Résultat attendu** :
```html
<section class="fr-accordion">
    <h3 class="fr-accordion__title">
        <button class="fr-accordion__btn" aria-expanded="false" aria-controls="accordion-1">
            Section 1
        </button>
    </h3>
    <div class="fr-collapse" id="accordion-1">
        <p>Contenu dépliable</p>
    </div>
</section>
```

#### Test 1.9 : Modale
```
Génère une modale avec titre "Confirmation" et contenu "Êtes-vous sûr ?"
```
**Résultat attendu** :
```html
<dialog class="fr-modal" id="modal-1" aria-labelledby="modal-1-title">
    <div class="fr-container fr-container--fluid fr-container-md">
        <div class="fr-grid-row fr-grid-row--center">
            <div class="fr-col-12 fr-col-md-8 fr-col-lg-6">
                <div class="fr-modal__body">
                    <div class="fr-modal__header">
                        <button class="fr-btn--close fr-btn" aria-controls="modal-1">Fermer</button>
                    </div>
                    <div class="fr-modal__content">
                        <h1 id="modal-1-title" class="fr-modal__title">Confirmation</h1>
                        <p>Êtes-vous sûr ?</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</dialog>
```

#### Test 1.10 : Formulaire complet
```
Génère un formulaire avec champs email et mot de passe
```
**Résultat attendu** :
```html
<form>
    <div class="fr-input-group">
        <label class="fr-label" for="email">Email</label>
        <input class="fr-input" type="email" id="email" name="email">
    </div>
    <div class="fr-input-group">
        <label class="fr-label" for="password">Mot de passe</label>
        <input class="fr-input" type="password" id="password" name="password">
    </div>
</form>
```

---

### 2️⃣ OUTIL : `list_components`
**Description** : Liste tous les composants DSFR disponibles

#### Test 2.1 : Liste simple
```
Liste tous les composants DSFR disponibles
```
**Résultat attendu** :
- 48 composants listés
- Catégories : navigation, forms, content, feedback, layout
- Format JSON structuré

#### Test 2.2 : Vérification du count
```
Combien de composants DSFR sont disponibles ?
```
**Résultat attendu** :
- count: 48

---

### 3️⃣ OUTIL : `validate_html`
**Description** : Valide du HTML selon DSFR et standards web

#### Test 3.1 : HTML valide
```
Valide : <button class="fr-btn">Test</button>
```
**Résultat attendu** :
- valid: true
- score: 100
- errors: []

#### Test 3.2 : HTML invalide - balises croisées
```
Valide : <div><span></div></span>
```
**Résultat attendu** :
- valid: false
- score: 20
- errors: ["Erreur d'imbrication", "Balises croisées"]

#### Test 3.3 : Bouton sans classe DSFR
```
Valide : <button>Test</button>
```
**Résultat attendu** :
- valid: true (structure valide)
- warnings: ["Classe fr-btn recommandée"]

#### Test 3.4 : Balise non fermée
```
Valide : <div><p>Test</div>
```
**Résultat attendu** :
- valid: false
- errors: ["Balise <p> non fermée"]

#### Test 3.5 : HTML vide
```
Valide : ""
```
**Résultat attendu** :
- valid: true
- score: 100

---

### 4️⃣ OUTIL : `audit_accessibility`
**Description** : Audit RGAA 4.1

#### Test 4.1 : Image sans alt
```
Audit : <img src="logo.png">
```
**Résultat attendu** :
- critical_issues: 1
- issues: ["Image sans attribut alt"]
- scores: {A: ~66%, AA: ~75%, AAA: ~75%}

#### Test 4.2 : Image avec alt
```
Audit : <img src="logo.png" alt="Logo">
```
**Résultat attendu** :
- critical_issues: 0
- scores: {A: 100%, AA: 100%, AAA: ~90%}

#### Test 4.3 : Formulaire sans labels
```
Audit : <input type="text" id="name"><input type="email" id="email">
```
**Résultat attendu** :
- critical_issues: 2
- issues: ["Champ sans label" x2]

#### Test 4.4 : Formulaire accessible
```
Audit : <label for="name">Nom</label><input type="text" id="name">
```
**Résultat attendu** :
- critical_issues: 0
- scores: {A: 100%, AA: ~95%}

#### Test 4.5 : Tableau sans en-têtes
```
Audit : <table><tr><td>A</td><td>B</td></tr></table>
```
**Résultat attendu** :
- issues: ["Tableau sans <th>", "Tableau sans <caption>"]

#### Test 4.6 : Lien vide
```
Audit : <a href="/page"></a>
```
**Résultat attendu** :
- issues: ["Lien sans texte ni aria-label"]

#### Test 4.7 : Contraste insuffisant (simulation)
```
Audit : <p style="color:#999;background:#aaa">Texte</p>
```
**Note** : Test de détection des patterns problématiques

---

### 5️⃣ OUTIL : `analyze_cognitive`
**Description** : Analyse selon la matrice de Rumsfeld

#### Test 5.1 : Système d'authentification
```
Analyse : "Nous devons créer un système d'authentification mais nous ne connaissons pas les contraintes de sécurité"
```
**Résultat attendu** :
- Known Unknowns : contraintes de sécurité non définies
- Unknown Unknowns : évolutions RGPD, attaques futures

#### Test 5.2 : Formulaire simple
```
Analyse : "Juste un petit formulaire basique rapidement"
```
**Résultat attendu** :
- Unknown Knowns : complexité sous-estimée (mots "juste", "basique", "rapidement")
- Recommendations : explorer les besoins réels

#### Test 5.3 : Multi-utilisateurs
```
Analyse : "Interface pour différents types d'utilisateurs"
```
**Résultat attendu** :
- Unknown Knowns : besoins différenciés par persona
- Recommendations : définir les personas

#### Test 5.4 : Évolution future
```
Analyse : "Composant qui devra évoluer plus tard"
```
**Résultat attendu** :
- Unknown Unknowns : changements non anticipés
- Recommendations : architecture flexible

#### Test 5.5 : Projet clair
```
Analyse : "Bouton bleu avec le texte Valider"
```
**Résultat attendu** :
- Known Knowns : spécifications claires
- Peu d'Unknown Unknowns

---

### 6️⃣ OUTIL : `get_design_tokens`
**Description** : Récupère les tokens de design DSFR

#### Test 6.1 : Couleurs
```
Récupère les design tokens pour "colors"
```
**Résultat attendu** :
- primary: {blue-france: #000091, ...}
- system: {success: #18753c, error: #ce0500, ...}
- grey: {palette complète}

#### Test 6.2 : Espacements
```
Récupère les design tokens pour "spacing"
```
**Résultat attendu** :
- Valeurs d'espacement DSFR (0.5rem, 1rem, 1.5rem, etc.)

#### Test 6.3 : Typographie
```
Récupère les design tokens pour "typography"
```
**Résultat attendu** :
- font-family: Marianne
- Tailles: xs, sm, md, lg, xl
- Line-heights correspondants

#### Test 6.4 : Icônes
```
Récupère les design tokens pour "icons"
```
**Résultat attendu** :
- navigation: {arrow-left, arrow-right, ...}
- action: {add, edit, delete, ...}
- system: {check, close, ...}

#### Test 6.5 : Tous les tokens
```
Récupère tous les design tokens (sans catégorie)
```
**Résultat attendu** :
- Object avec toutes les catégories

---

### 7️⃣ OUTIL : `generate_tests`
**Description** : Génère des tests automatiques

#### Test 7.1 : Tests unitaires Jest
```
Génère des tests unitaires pour "button"
```
**Résultat attendu** :
```javascript
import { render, screen, fireEvent } from '@testing-library/react';
test('renders and handles click', () => { ... })
test('keyboard accessible', () => { ... })
```

#### Test 7.2 : Tests d'intégration Cypress
```
Génère des tests d'intégration pour "form"
```
**Résultat attendu** :
```javascript
describe('DSFR Form', () => {
  it('validates required fields', () => { ... })
  it('submits with valid data', () => { ... })
})
```

#### Test 7.3 : Tests E2E
```
Génère des tests e2e pour "modal"
```
**Résultat attendu** :
- Scénario complet d'ouverture/fermeture
- Tests d'accessibilité clavier
- Focus trap

#### Test 7.4 : Composant inconnu
```
Génère des tests pour "composant_inexistant"
```
**Résultat attendu** :
- Tests génériques ou message d'erreur approprié

---

### 8️⃣ OUTIL : `get_assistant_help`
**Description** : Assistant DSFR pour aide contextuelle

#### Test 8.1 : Accessibilité formulaire
```
Comment rendre un formulaire accessible ?
```
**Résultat attendu** :
- Guide complet RGAA 11.1 à 11.11
- Labels, aria-required, messages d'erreur
- Exemples de code

#### Test 8.2 : Choix de composants
```
Quel composant choisir pour afficher des notifications ?
```
**Résultat attendu** :
- Suggestions : alert, notice, toast
- Raisons pour chaque choix

#### Test 8.3 : Couleurs DSFR
```
Quelles sont les couleurs officielles ?
```
**Résultat attendu** :
- Bleu France : #000091
- Couleurs système
- Règles d'usage

#### Test 8.4 : Question générale
```
Comment créer une page d'accueil ?
```
**Résultat attendu** :
- Analyse des besoins
- Composants suggérés
- Structure recommandée

#### Test 8.5 : Question technique
```
Comment implémenter le dark mode ?
```
**Résultat attendu** :
- Réponse sur les variables CSS DSFR
- Ou indication que ce n'est pas encore supporté

---

## 🔄 TESTS DE ROBUSTESSE

### Test R1 : Entrées vides
```
generate_component("", "")
validate_html("")
audit_accessibility("")
```
**Attendu** : Gestion gracieuse, pas de crash

### Test R2 : HTML malformé extrême
```
validate_html("<<><>>><<div<>")
```
**Attendu** : Erreurs détaillées, pas de crash

### Test R3 : Caractères spéciaux
```
generate_component("button", options={"label": "Test & < > \" '"})
```
**Attendu** : Échappement correct

### Test R4 : Injection
```
validate_html("<script>alert('XSS')</script>")
```
**Attendu** : Validation correcte, pas d'exécution

### Test R5 : Unicode
```
generate_component("alert", options={"message": "测试 🎉 émojis"})
```
**Attendu** : Support Unicode complet

### Test R6 : Très long contenu
```
validate_html("<p>" + "A" * 10000 + "</p>")
```
**Attendu** : Performance acceptable

### Test R7 : Composant inexistant
```
generate_component("nexistepas")
```
**Attendu** : Message d'erreur clair

### Test R8 : Paramètres manquants
```
audit_accessibility() // sans HTML
```
**Attendu** : Message d'erreur approprié

---

## 🎯 TESTS DE PERFORMANCE

### Test P1 : Temps de réponse
- Chaque outil doit répondre en < 2 secondes
- Mesurer avec : `time echo '...' | python3 server.py`

### Test P2 : Charge
```bash
# Lancer 10 requêtes en parallèle
for i in {1..10}; do
  (echo '{"method":"tools/call"...}' | python3 server.py) &
done
```

### Test P3 : Mémoire
```bash
# Monitorer la mémoire
ps aux | grep python3
```

### Test P4 : Session longue
- Laisser le serveur actif 1 heure
- Vérifier qu'il n'y a pas de fuite mémoire

---

## 📊 TESTS D'INTÉGRATION CLAUDE DESKTOP

### Test I1 : Connexion initiale
1. Démarrer Claude Desktop
2. Vérifier l'icône 🔌 MCP
3. Pas d'erreur "Server disconnected"

### Test I2 : Séquence complète
```
1. Liste les composants disponibles
2. Génère un formulaire avec 3 champs
3. Valide le HTML généré
4. Fait un audit d'accessibilité
5. Génère des tests pour le formulaire
```

### Test I3 : Multi-outils
```
En une seule requête :
- Génère un bouton ET valide-le ET audite-le
```

### Test I4 : Erreur et récupération
1. Provoquer une erreur (composant inexistant)
2. Vérifier que le serveur continue
3. Faire une requête valide ensuite

### Test I5 : Redémarrage
1. Tuer le processus Python
2. Claude Desktop doit détecter la déconnexion
3. Redémarrer et reconnecter

---

## ✅ CRITÈRES DE VALIDATION

### Fonctionnels
- [ ] 100% des tests nominaux passent
- [ ] Tous les outils répondent correctement
- [ ] Pas d'erreur dans les logs

### Robustesse
- [ ] Aucun crash sur entrées invalides
- [ ] Messages d'erreur explicites
- [ ] Récupération après erreur

### Performance
- [ ] Temps de réponse < 2s
- [ ] Pas de fuite mémoire
- [ ] Support de charge normale

### Intégration
- [ ] Fonctionne dans Claude Desktop
- [ ] Reconnexion automatique
- [ ] Expérience fluide

---

## 📈 MATRICE DE COUVERTURE

| Outil | Tests nominaux | Robustesse | Performance | Intégration | TOTAL |
|-------|---------------|------------|-------------|-------------|--------|
| generate_component | 10/10 | ✅ | ✅ | ✅ | 100% |
| list_components | 2/2 | ✅ | ✅ | ✅ | 100% |
| validate_html | 5/5 | ✅ | ✅ | ✅ | 100% |
| audit_accessibility | 7/7 | ✅ | ✅ | ✅ | 100% |
| analyze_cognitive | 5/5 | ✅ | ✅ | ✅ | 100% |
| get_design_tokens | 5/5 | ✅ | ✅ | ✅ | 100% |
| generate_tests | 4/4 | ✅ | ✅ | ✅ | 100% |
| get_assistant_help | 5/5 | ✅ | ✅ | ✅ | 100% |

**COUVERTURE TOTALE : 43 tests nominaux + 8 robustesse + 4 performance + 5 intégration = 60 TESTS**

---

## 🚀 SCRIPT DE TEST AUTOMATISÉ

```bash
#!/bin/bash
# test_mcp.sh - Script de test automatisé

echo "🧪 Test MCP DSFR - Démarrage"

# Configuration
SERVER="/Users/alex/Desktop/mcp-playbook-dsfr/mcp_local/server.py"
PYTHON="/Users/alex/Desktop/mcp-playbook-dsfr/venv/bin/python3"

# Fonction de test
test_tool() {
    local name=$1
    local args=$2
    local expected=$3
    
    result=$(echo "{\"jsonrpc\":\"2.0\",\"id\":1,\"method\":\"tools/call\",\"params\":{\"name\":\"$name\",\"arguments\":$args}}" | $PYTHON $SERVER 2>&1 | tail -1)
    
    if [[ $result == *"$expected"* ]]; then
        echo "✅ $name : PASS"
        return 0
    else
        echo "❌ $name : FAIL"
        echo "   Attendu: $expected"
        echo "   Reçu: $result"
        return 1
    fi
}

# Tests
echo "📋 Tests nominaux"
test_tool "list_components" "{}" "48"
test_tool "generate_component" "{\"component\":\"button\",\"options\":{\"label\":\"Test\"}}" "fr-btn"
test_tool "validate_html" "{\"html\":\"<div></div>\"}" "valid.*true"

echo "🔨 Tests robustesse"
test_tool "validate_html" "{\"html\":\"<div><span></div></span>\"}" "valid.*false"
test_tool "generate_component" "{\"component\":\"inexistant\"}" "Erreur"

echo "✅ Tests terminés"
```

---

## 📝 RAPPORT DE TEST

**Date** : ___________
**Testeur** : ___________
**Version** : 2.0.0

### Résultats
- Tests réussis : ___/60
- Tests échoués : ___/60
- Taux de réussite : ___%

### Problèmes identifiés
1. _______________________
2. _______________________
3. _______________________

### Recommandations
1. _______________________
2. _______________________
3. _______________________

### Validation finale
- [ ] Prêt pour production
- [ ] Corrections nécessaires
- [ ] Tests supplémentaires requis

---

## 📚 DOCUMENTATION COMPLÉMENTAIRE

- **CLAUDE.md** : Documentation technique
- **TEST_MCP.md** : Tests rapides
- **README.md** : Guide d'installation
- **DEPLOYMENT.md** : Guide de déploiement

---

**FIN DU CAHIER DE TEST EXHAUSTIF**