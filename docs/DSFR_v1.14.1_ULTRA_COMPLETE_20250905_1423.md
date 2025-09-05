# 🇫🇷 DSFR v1.14.1 - DOCUMENTATION ULTRA COMPLÈTE

*Généré le 05/09/2025 14:23*

## 📊 SOURCES COMBINÉES

1. **GitHub** : Code source complet (SCSS, JS, Templates)
2. **Storybook** : Documentation interactive
3. **NPM** : Package officiel @gouvfr/dsfr

## 📦 INSTALLATION

```bash
# NPM
npm install @gouvfr/dsfr@1.14.1

# CDN
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@gouvfr/dsfr@1.14.1/dist/dsfr.min.css">
<script src="https://cdn.jsdelivr.net/npm/@gouvfr/dsfr@1.14.1/dist/dsfr.module.min.js"></script>
```

---

# 🎨 COMPOSANTS COMPLETS (52)


## 🧭 Navigation


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🔹 HEADER

### 📋 INFORMATIONS GÉNÉRALES

- **Classe CSS** : `fr-header`
- **Dossier GitHub** : `/src/dsfr/component/header/`

### 📄 EXEMPLE (index.ejs)

```html
<% const sample = getSample(include); %>

<style>
    @media (min-width: 62em) {
        .relative-sample\@lg {
            position: relative;
        }
    }
</style>

<%- sample('Header minimal', './sample/header.ejs', {header: { logo:{ title: 'Intitulé<br>officiel'}, navigation: 'min' }}, true, './layout');  %>

<%- sample('Header sans navigation', './sample/header.ejs', {header: { logo:{ title: 'Intitulé<br>officiel'}, service: true }}, true, './layout');  %>

<%- sample('Header sans navigation avec un seul raccourci', './sample/header.ejs', {header: { logo:{ title: 'Intitulé<br>officiel'}, links: { buttons: [{ url: '[url - à modifier]', label: 'Espace particulier', markup: 'a', classes: [`${prefix}-btn--account`]}] }, service: true}}, true, './layout');  %>

<%- sample('Header sans n
...
```

### 🔗 LIENS

- [GitHub](https://github.com/GouvernementFR/dsfr/tree/main/src/dsfr/component/header)
- [Site officiel](https://www.systeme-de-design.gouv.fr/elements-d-interface/header)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🔹 FOOTER

### 📋 INFORMATIONS GÉNÉRALES

- **Classe CSS** : `fr-footer`
- **Dossier GitHub** : `/src/dsfr/component/footer/`

📖 [Documentation interactive](https://www.systeme-de-design.gouv.fr/v1.14/storybook/?path=/docs/composants-pied-de-page-footer--docs)

### 📄 EXEMPLE (index.ejs)

```html
<% const sample = getSample(include); %>

<%- sample('Pied de page minimal', './sample/footer-minimal.ejs', {}, true); %>

<%- sample('Pied de page avec navigation', './sample/footer-total.ejs', {}, true); %>

<%- sample('Pied de page avec logo opérateur', './sample/footer-operator.ejs', {}, true); %>

<%- sample('Pied de page avec logos partenaires', './sample/footer-partners.ejs', {footer: {partners: {mainPartner: true, subPartners: true}}}, true); %>

<%- sample('Pied de page avec logo partenaire primaire uniquement', './sample/footer-partners.ejs', {footer: {partners: {mainPartner: true}}}, true); %>

<%- sample('Pied de page avec logos partenaires secondaires uniquement', './sample/footer-partners.ejs', {footer: {partners: {subPartners: true}}}, true); %>

<%- sample('Pied de page com
...
```

### 🔗 LIENS

- [GitHub](https://github.com/GouvernementFR/dsfr/tree/main/src/dsfr/component/footer)
- [Storybook](https://www.systeme-de-design.gouv.fr/v1.14/storybook/?path=/docs/composants-pied-de-page-footer--docs)
- [Site officiel](https://www.systeme-de-design.gouv.fr/elements-d-interface/footer)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🔹 NAVIGATION

### 📋 INFORMATIONS GÉNÉRALES

- **Classe CSS** : `fr-navigation`
- **Dossier GitHub** : `/src/dsfr/component/navigation/`

📖 [Documentation interactive](https://www.systeme-de-design.gouv.fr/v1.14/storybook/?path=/docs/composants-navigation-navigation--docs)

### 📄 EXEMPLE (index.ejs)

```html
<% const sample = getSample(include); %>

<%- sample('Navigation Principale', './sample/navigation', {}, true, './layout'); %>


```

### 🔗 LIENS

- [GitHub](https://github.com/GouvernementFR/dsfr/tree/main/src/dsfr/component/navigation)
- [Storybook](https://www.systeme-de-design.gouv.fr/v1.14/storybook/?path=/docs/composants-navigation-navigation--docs)
- [Site officiel](https://www.systeme-de-design.gouv.fr/elements-d-interface/navigation)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🔹 BREADCRUMB

### 📋 INFORMATIONS GÉNÉRALES

- **Classe CSS** : `fr-breadcrumb`
- **Dossier GitHub** : `/src/dsfr/component/breadcrumb/`

📖 [Documentation interactive](https://www.systeme-de-design.gouv.fr/v1.14/storybook/?path=/docs/composants-fil-d-ariane-breadcrumb--docs)

### 📄 EXEMPLE (index.ejs)

```html
<% const sample = getSample(include); %>

<%- sample('Fil d’Ariane avec liens', './sample/sample-a', { }, true); %>

```

### 🔗 LIENS

- [GitHub](https://github.com/GouvernementFR/dsfr/tree/main/src/dsfr/component/breadcrumb)
- [Storybook](https://www.systeme-de-design.gouv.fr/v1.14/storybook/?path=/docs/composants-fil-d-ariane-breadcrumb--docs)
- [Site officiel](https://www.systeme-de-design.gouv.fr/elements-d-interface/breadcrumb)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🔹 SIDEMENU

### 📋 INFORMATIONS GÉNÉRALES

- **Classe CSS** : `fr-sidemenu`
- **Dossier GitHub** : `/src/dsfr/component/sidemenu/`

### 📄 EXEMPLE (index.ejs)

```html
<% const sample = getSample(include); %>

<%- sample('Navigation latérale de base', './sample/sidemenu', {}, true, './layout'); %>

<%- sample('Navigation latérale sticky', './sample/sidemenu', {sidemenu: {modifier:'sticky'}}, true, './layout'); %>

<%- sample('Navigation latérale sticky et sur toute la hauteur', './sample/sidemenu', {sidemenu: {modifier:'sticky-full-height'}}, true, './layout'); %>

<%- sample('Navigation latérale à droite', './sample/sidemenu', {sidemenu: {modifier:'right'}}, true, './layout', {right:true}); %>

<!-- Exemple de navigation latérale sans collapse -->
<!-- <%- sample('Navigation latérale de base ouverte', './sample/sidemenu', {models: [ 'LLOLL', 'LOLLOLL', 'LLLLLL' ]}, true, './layout'); %> -->

```

### 🔗 LIENS

- [GitHub](https://github.com/GouvernementFR/dsfr/tree/main/src/dsfr/component/sidemenu)
- [Site officiel](https://www.systeme-de-design.gouv.fr/elements-d-interface/sidemenu)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🔹 SKIPLINK

### 📋 INFORMATIONS GÉNÉRALES

- **Classe CSS** : `fr-skiplink`
- **Dossier GitHub** : `/src/dsfr/component/skiplink/`

### 📄 EXEMPLE (index.ejs)

```html
<% const sample = getSample(include); %>

<div class="<%= prefix %>-container">
  <div class="<%= prefix %>-grid-row <%= prefix %>-grid-row--center" >
    <div class="<%= prefix %>-col-md-8 <%= prefix %>-col-12" id="content">
      <%- sample('Liens d’évitement', './sample/skiplinks.ejs', {}, true, './layout'); %>
      <% for (let i = 0; i < 10; i++) { %>
      <p><%- lorem() %></p>
      <% } %>
    </div>
  </div>
</div>

<%- include('../../footer/example/sample/footer-minimal.ejs', { footer: {id: 'footer' }}); %>

```

### 🔗 LIENS

- [GitHub](https://github.com/GouvernementFR/dsfr/tree/main/src/dsfr/component/skiplink)
- [Site officiel](https://www.systeme-de-design.gouv.fr/elements-d-interface/skiplink)


## 📝 Formulaires


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🔹 INPUT

### 📋 INFORMATIONS GÉNÉRALES

- **Classe CSS** : `fr-input`
- **Dossier GitHub** : `/src/dsfr/component/input/`

📖 [Documentation interactive](https://www.systeme-de-design.gouv.fr/v1.14/storybook/?path=/docs/composants-champ-de-saisie-input--docs)

### 📄 EXEMPLE (index.ejs)

```html
<% const sample = getSample(include); %>

<%
  const dateSubtitle = 'Préférez l\'utilisation du modèle de bloc de <a href="../../../pattern/date/">Date unique</a>';
  const passwordSubtitle = 'Préférez l\'utilisation du composant <a href="../../password/">Mot de passe</a>';
%>

<%- sample(getText('sample.text', 'input'), './sample/input-text.ejs', {input: { id:'text-input-text'}}, true); %>

<%- sample(getText('sample.number', 'input'), './sample/input-number.ejs', {input: { id:'text-input-number'}}, true); %>

<%- sample(getText('sample.search', 'input'), './sample/input-search.ejs', {input: { id:'text-input-search'}}, true); %>

<%- sample({title: getText('sample.date', 'input'), subtitle: dateSubtitle}, './sample/input-date.ejs', {input: { id:'text-input-date' }}, true); %>

<%- sample(
...
```

### 🔗 LIENS

- [GitHub](https://github.com/GouvernementFR/dsfr/tree/main/src/dsfr/component/input)
- [Storybook](https://www.systeme-de-design.gouv.fr/v1.14/storybook/?path=/docs/composants-champ-de-saisie-input--docs)
- [Site officiel](https://www.systeme-de-design.gouv.fr/elements-d-interface/input)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🔹 SELECT

### 📋 INFORMATIONS GÉNÉRALES

- **Classe CSS** : `fr-select`
- **Dossier GitHub** : `/src/dsfr/component/select/`

### 📄 EXEMPLE (index.ejs)

```html
<% const sample = getSample(include); %>

<%- sample('Liste déroulante par défaut', './sample/select', {select: { id:'select'}}, true); %>

<%- sample('Liste déroulante désactivée', './sample/select', {select: { id:'select-disabled', disabled:true}}, true); %>

<%- sample('Liste déroulante avec texte de description', './sample/select', {select: { id:'select-hint', hint: true}}, true); %>

<%- sample('Liste déroulante valide', './sample/select', {select: { id:'select-valid', valid: true}}, true); %>

<%- sample('Liste déroulante erreur', './sample/select', {select: { id:'select-error', error: true}}, true); %>

<%- sample('Liste déroulante avec groupe d\'options', './sample/option-group', {select: { id:'select-group'}}, true); %>

```

### 🔗 LIENS

- [GitHub](https://github.com/GouvernementFR/dsfr/tree/main/src/dsfr/component/select)
- [Site officiel](https://www.systeme-de-design.gouv.fr/elements-d-interface/select)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🔹 CHECKBOX

### 📋 INFORMATIONS GÉNÉRALES

- **Classe CSS** : `fr-checkbox`
- **Dossier GitHub** : `/src/dsfr/component/checkbox/`

### 📄 EXEMPLE (index.ejs)

```html
<% const sample = getSample(include); %>

<%- sample('Case à cocher seule', './sample/checkbox.ejs', {checkbox: {id:'checkbox'}}, true); %>

<%- sample('Case à cocher seule, exemple avec indice et exposant', './sample/checkbox.ejs', {checkbox: {id:'checkbox-sup-sub', label:'<span>Libellé checkbox <sub>sub</sub> et <sup>sup</sup></span>'}}, true); %>

<%- sample('Case à cocher avec texte d‘aide', './sample/checkbox.ejs', {checkbox: {id:'checkbox-hint', hint:true}}, true); %>

<%- sample('Case à cocher seule, validée', './sample/checkbox.ejs', {checkbox: {id:'checkbox-valid', valid:true}}, true); %>

<%- sample('Case à cocher seule avec erreur', './sample/checkbox.ejs', {checkbox: {id:'checkbox-error', error:true}}, true); %>

<%- sample('Ensemble de cases à cocher', './sample/checkboxes.ejs
...
```

### 🔗 LIENS

- [GitHub](https://github.com/GouvernementFR/dsfr/tree/main/src/dsfr/component/checkbox)
- [Site officiel](https://www.systeme-de-design.gouv.fr/elements-d-interface/checkbox)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🔹 RADIO

### 📋 INFORMATIONS GÉNÉRALES

- **Classe CSS** : `fr-radio`
- **Dossier GitHub** : `/src/dsfr/component/radio/`

📖 [Documentation interactive](https://www.systeme-de-design.gouv.fr/v1.14/storybook/?path=/docs/composants-boutons-radio-radio--docs)

### 📄 EXEMPLE (index.ejs)

```html
<% const sample = getSample(include); %>

<%- section('Bouton radio simple', null, 0); %>

<%- sample('Ensemble de boutons radio', './sample/radios.ejs', { radios: { id:'radio', checked: true } }, true); %>

<%- sample('Ensemble de boutons radio, petite taille', './sample/radios.ejs', { radios: { id:'radio-small', checked: true }, radio: { size:'sm' } }, true); %>

<%- sample('Ensemble de boutons radio désactivées', './sample/radios.ejs', { radios: { id:'radio-disabled', checked: true }, radio: { disabled:true } }, true); %>

<%- sample('Ensemble de boutons radio en ligne', './sample/radios.ejs', { radios: { id:'radio-inline', inline: true } }, true); %>

<%- sample('Ensemble de boutons radio avec texte d‘aide', './sample/radios.ejs', { radios: { id:'radio-hint', hint: true }, radio: {} },
...
```

### 🔗 LIENS

- [GitHub](https://github.com/GouvernementFR/dsfr/tree/main/src/dsfr/component/radio)
- [Storybook](https://www.systeme-de-design.gouv.fr/v1.14/storybook/?path=/docs/composants-boutons-radio-radio--docs)
- [Site officiel](https://www.systeme-de-design.gouv.fr/elements-d-interface/radio)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🔹 TOGGLE

### 📋 INFORMATIONS GÉNÉRALES

- **Classe CSS** : `fr-toggle`
- **Dossier GitHub** : `/src/dsfr/component/toggle/`

📖 [Documentation interactive](https://www.systeme-de-design.gouv.fr/v1.14/storybook/?path=/docs/composants-interrupteur-toggle--docs)

### 📄 EXEMPLE (index.ejs)

```html
<% const sample = getSample(include); %>

<%- sample('Toggle simple avec bouton', './sample/toggle-default.ejs', {toggle: {state: false}}, true, './layout'); %>

<%- sample('Toggle simple avec bouton + texte d’aide', './sample/toggle-default.ejs', {toggle: {state: false, hint: true}}, true, './layout'); %>

<%- sample('Toggle simple avec bouton + état', './sample/toggle-default.ejs', {toggle: {state: true}}, true, './layout'); %>

<%- sample('Toggle simple avec bouton + état + texte d’aide', './sample/toggle-default.ejs', {toggle: {state: true, hint: true}}, true, './layout'); %>

<%- sample('Toggle simple avec bouton + état + séparateur', './sample/toggle-default.ejs', {toggle: {state: true, border: true}}, true, './layout'); %>

<%- sample('Toggle simple avec bouton + état + séparateur +
...
```

### 🔗 LIENS

- [GitHub](https://github.com/GouvernementFR/dsfr/tree/main/src/dsfr/component/toggle)
- [Storybook](https://www.systeme-de-design.gouv.fr/v1.14/storybook/?path=/docs/composants-interrupteur-toggle--docs)
- [Site officiel](https://www.systeme-de-design.gouv.fr/elements-d-interface/toggle)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🔹 SEARCH

### 📋 INFORMATIONS GÉNÉRALES

- **Classe CSS** : `fr-search`
- **Dossier GitHub** : `/src/dsfr/component/search/`

📖 [Documentation interactive](https://www.systeme-de-design.gouv.fr/v1.14/storybook/?path=/docs/composants-barre-de-recherche-search--docs)

### 📄 EXEMPLE (index.ejs)

```html
<% const sample = getSample(include); %>

<%- sample('Barre de recherche MD (par défaut)', './sample/search-default.ejs', {}, true); %>

<%- sample('Barre de recherche LG', './sample/search-lg.ejs', {}, true); %>

```

### 🔗 LIENS

- [GitHub](https://github.com/GouvernementFR/dsfr/tree/main/src/dsfr/component/search)
- [Storybook](https://www.systeme-de-design.gouv.fr/v1.14/storybook/?path=/docs/composants-barre-de-recherche-search--docs)
- [Site officiel](https://www.systeme-de-design.gouv.fr/elements-d-interface/search)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🔹 UPLOAD

### 📋 INFORMATIONS GÉNÉRALES

- **Classe CSS** : `fr-upload`
- **Dossier GitHub** : `/src/dsfr/component/upload/`

📖 [Documentation interactive](https://www.systeme-de-design.gouv.fr/v1.14/storybook/?path=/docs/composants-ajout-de-fichier-upload--docs)

### 📄 EXEMPLE (index.ejs)

```html
<% const sample = getSample(include); %>

<%- sample(getText('sample.default', 'upload'), './sample/upload.ejs', { upload: {id:'file-upload'}}, true); %>

<%- sample(getText('sample.error', 'upload'), './sample/upload.ejs', { upload: {id:'file-upload-with-error', error: true }}, true); %>

<%- sample(getText('sample.multiple', 'upload'), './sample/upload-multiple.ejs', { upload: {id:'file-upload-multiple' }}, true); %>

<%- sample(getText('sample.disabled', 'upload'), './sample/upload.ejs', { upload: {id:'file-upload-disabled', disabled: true }}, true); %>


```

### 🔗 LIENS

- [GitHub](https://github.com/GouvernementFR/dsfr/tree/main/src/dsfr/component/upload)
- [Storybook](https://www.systeme-de-design.gouv.fr/v1.14/storybook/?path=/docs/composants-ajout-de-fichier-upload--docs)
- [Site officiel](https://www.systeme-de-design.gouv.fr/elements-d-interface/upload)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🔹 RANGE

### 📋 INFORMATIONS GÉNÉRALES

- **Classe CSS** : `fr-range`
- **Dossier GitHub** : `/src/dsfr/component/range/`

📖 [Documentation interactive](https://www.systeme-de-design.gouv.fr/v1.14/storybook/?path=/docs/composants-curseur-range--docs)

### 📄 EXEMPLE (index.ejs)

```html
<% const sample = getSample(include); %>

<%- sample(getText('sample.default', 'range'), './sample/range.ejs', { range: {min: 0, max: 100, value: 50}}, true); %>

<%- sample(getText('sample.sm', 'range'), './sample/range.ejs', { range: {size: 'sm', min: 0, max: 100, value: 50}}, true); %>

<%- sample(getText('sample.no-indicators', 'range'), './sample/range.ejs', { range: {indicators: false, min: 0, max: 100, value: 50}}, true); %>

<%- sample(getText('sample.step', 'range'), './sample/range-step.ejs', { range: {min: 0, max: 100, step: 10, value: 50}}, true); %>

<%- sample(getText('sample.step-sm', 'range'), './sample/range-step.ejs', { range: {size: 'sm', min: 0, max: 100, step: 10, value: 50}}, true); %>

<%- sample(getText('sample.double', 'range'), './sample/range-double.ejs', { range
...
```

### 🔗 LIENS

- [GitHub](https://github.com/GouvernementFR/dsfr/tree/main/src/dsfr/component/range)
- [Storybook](https://www.systeme-de-design.gouv.fr/v1.14/storybook/?path=/docs/composants-curseur-range--docs)
- [Site officiel](https://www.systeme-de-design.gouv.fr/elements-d-interface/range)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🔹 PASSWORD

### 📋 INFORMATIONS GÉNÉRALES

- **Classe CSS** : `fr-password`
- **Dossier GitHub** : `/src/dsfr/component/password/`

📖 [Documentation interactive](https://www.systeme-de-design.gouv.fr/v1.14/storybook/?path=/docs/composants-mot-de-passe-password--docs)

### 📄 EXEMPLE (index.ejs)

```html
<% const sample = getSample(include); %>

<%- sample('Mot de passe', './sample/password-register.ejs', {}, true); %>

<%- sample('Mot de passe avec description', './sample/sample-description.ejs', {}, true); %>

<%- sample('Mot de passe après validation', './sample/sample-validate.ejs', {}, true); %>

<%- sample('Mot de passe de connexion', './sample/password-login.ejs', {}, true); %>

```

### 🔗 LIENS

- [GitHub](https://github.com/GouvernementFR/dsfr/tree/main/src/dsfr/component/password)
- [Storybook](https://www.systeme-de-design.gouv.fr/v1.14/storybook/?path=/docs/composants-mot-de-passe-password--docs)
- [Site officiel](https://www.systeme-de-design.gouv.fr/elements-d-interface/password)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🔹 FORM

### 📋 INFORMATIONS GÉNÉRALES

- **Classe CSS** : `fr-form`
- **Dossier GitHub** : `/src/dsfr/component/form/`

📖 [Documentation interactive](https://www.systeme-de-design.gouv.fr/v1.14/storybook/?path=/docs/composants-formulaire-form--docs)

### 📄 EXEMPLE (index.ejs)

```html
<script>
  function preventSubmit(e) {
    e.preventDefault();
    return false;
  }
</script>

<form onsubmit="return preventSubmit(event)">

<% const sample = getSample(include); %>

<%- sample('Ensemble de champs de saisie', '../../input/example/sample/inputs', { inputs: { id:'text' }}, true);  %>

<%- sample('Ensemble de boutons radio', '../../radio/example/sample/radios', { radios: { id:'radio' }}, true);  %>

<%- sample('Ensemble de cases à cocher', '../../checkbox/example/sample/checkboxes', { checkboxes: { id:'checkbox' }}, true);  %>

<%- sample('Ensemble de boutons radio, en ligne', '../../radio/example/sample/radios', { radios: { id:'radio-inline', inline:true }}, true);  %>

<%- sample('Ensemble de cases à cocher, en ligne', '../../checkbox/example/sample/checkboxes', { checkbo
...
```

### 🔗 LIENS

- [GitHub](https://github.com/GouvernementFR/dsfr/tree/main/src/dsfr/component/form)
- [Storybook](https://www.systeme-de-design.gouv.fr/v1.14/storybook/?path=/docs/composants-formulaire-form--docs)
- [Site officiel](https://www.systeme-de-design.gouv.fr/elements-d-interface/form)


## 🔘 Boutons et Actions


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🔹 BUTTON

### 📋 INFORMATIONS GÉNÉRALES

- **Classe CSS** : `fr-button`
- **Dossier GitHub** : `/src/dsfr/component/button/`

📖 [Documentation interactive](https://www.systeme-de-design.gouv.fr/v1.14/storybook/?path=/docs/composants-bouton-button--docs)

### 📄 EXEMPLE (index.ejs)

```html
<% const sample = getSample(include); %>

<%- section('Bouton primaire', null, 0) %>
<%- sample('Bouton simple', './sample/button-default', {}, true); %>

<%- sample('Bouton simple SM', './sample/button-default', {button: {label: 'Libellé bouton SM', size:'sm'}}, true); %>

<%- sample('Bouton simple LG', './sample/button-default', {button: {label: 'Libellé bouton LG', size:'lg'}}, true); %>

<%- sample('Bouton désactivé', './sample/button-default', {button: {disabled:true}}, true); %>

<%- sample('Bouton icon à gauche', './sample/button-default', {button: {icon :'checkbox-circle-line', iconPlace:'left'}}, true); %>

<%- sample('Bouton icon à droite', './sample/button-default', {button: {icon :'checkbox-circle-line', iconPlace:'right'}}, true); %>

<%- sample('Bouton icon seule', './sample/
...
```

### 🔗 LIENS

- [GitHub](https://github.com/GouvernementFR/dsfr/tree/main/src/dsfr/component/button)
- [Storybook](https://www.systeme-de-design.gouv.fr/v1.14/storybook/?path=/docs/composants-bouton-button--docs)
- [Site officiel](https://www.systeme-de-design.gouv.fr/elements-d-interface/button)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🔹 LINK

### 📋 INFORMATIONS GÉNÉRALES

- **Classe CSS** : `fr-link`
- **Dossier GitHub** : `/src/dsfr/component/link/`

📖 [Documentation interactive](https://www.systeme-de-design.gouv.fr/v1.14/storybook/?path=/docs/composants-lien-link--docs)

### 📄 EXEMPLE (index.ejs)

```html
<% const sample = getSample(include); %>

<%- sample('Lien seul', './sample/link-default', {}, true); %>

<%- sample('Lien icon à gauche', './sample/link-default', {link: {iconPlace: 'left', icon: 'arrow-left-line'}}, true); %>

<%- sample('Lien icon à droite', './sample/link-default', {link: {iconPlace: 'right', icon: 'arrow-right-line'}}, true); %>

<%- sample('Lien seul SM', './sample/link-sm', {}, true); %>

<%- sample('Lien seul LG', './sample/link-lg', {}, true); %>

<%- sample('Lien seul désactivé', './sample/link-default', {link: {disabled: true}}, true); %>

<%- sample('Lien externe', './sample/link-default', {link: { title: getBlankTitle('[À MODIFIER - Intitulé] - nouvelle fenêtre'), blank: true}}, true); %>

<%- section('Groupe de liens', 'Lorsque que l\'on a plus d\'un lien, il
...
```

### 🔗 LIENS

- [GitHub](https://github.com/GouvernementFR/dsfr/tree/main/src/dsfr/component/link)
- [Storybook](https://www.systeme-de-design.gouv.fr/v1.14/storybook/?path=/docs/composants-lien-link--docs)
- [Site officiel](https://www.systeme-de-design.gouv.fr/elements-d-interface/link)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🔹 DOWNLOAD

### 📋 INFORMATIONS GÉNÉRALES

- **Classe CSS** : `fr-download`
- **Dossier GitHub** : `/src/dsfr/component/download/`

### 📄 EXEMPLE (index.ejs)

```html
<%- section('Nouvelles versions', null, 0) %>

<ul>
  <li>
    <a href="../card/download/"><%- getText('subdir.download', 'card') %></a>
  </li>
  <li>
    <a href="../link/download/"><%- getText('subdir.download', 'link') %></a>
  </li>
</ul>

```

### 🔗 LIENS

- [GitHub](https://github.com/GouvernementFR/dsfr/tree/main/src/dsfr/component/download)
- [Site officiel](https://www.systeme-de-design.gouv.fr/elements-d-interface/download)


## 📊 Affichage


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🔹 ACCORDION

### 📋 INFORMATIONS GÉNÉRALES

- **Classe CSS** : `fr-accordion`
- **Dossier GitHub** : `/src/dsfr/component/accordion/`

### 📄 EXEMPLE (index.ejs)

```html
<% const sample = getSample(include, 888); %>

<%- sample('Accordéon', './sample/accordion', {}, true); %>

<%- sample('Groupe d‘accordéons', './sample/accordions-group', {}, true); %>

<%- sample('Groupe d‘accordéons ouvert au chargement', './sample/accordions-group', {accordionsGroup: {isExpanded: true}}, true); %>

<%- sample('Groupe d‘accordéons dissociés', './sample/accordions-group', {accordionsGroup: {group: false}}, true); %>

<%- sample('Groupe d‘accordéons dissociés ouvert au chargement', './sample/accordions-group', {accordionsGroup: {group: false, isExpanded: true}}, true); %>

```

### 🔗 LIENS

- [GitHub](https://github.com/GouvernementFR/dsfr/tree/main/src/dsfr/component/accordion)
- [Site officiel](https://www.systeme-de-design.gouv.fr/elements-d-interface/accordion)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🔹 ALERT

### 📋 INFORMATIONS GÉNÉRALES

- **Classe CSS** : `fr-alert`
- **Dossier GitHub** : `/src/dsfr/component/alert/`

📖 [Documentation interactive](https://www.systeme-de-design.gouv.fr/v1.14/storybook/?path=/docs/composants-alerte-alert--docs)

### 📄 EXEMPLE (layout-dynamic.ejs)

```html
<% eval(include('../../../core/index.ejs')); %>

<% if (locals.title !== undefined && locals.title.length) { %>
  <h4><%= title %></h4>
  <% } %>
  <div class="<%= prefix %>-mb-6v" >
    <button type="button" class="fr-btn" id="button-add" onclick="const component = document.createElement('div'); component.className = 'fr-my-8v'; component.innerHTML = decodeURIComponent('<%- encodeURIComponent(component) %>'); this.after(component);">Bouton d'ajout</button>

</div>
  <% if (locals.snippet !== undefined) { %>
  <div class="<%= prefix %>-mb-12v" >
      <%- snippet %>
  </div>
  <% } %>


```

### 🔗 LIENS

- [GitHub](https://github.com/GouvernementFR/dsfr/tree/main/src/dsfr/component/alert)
- [Storybook](https://www.systeme-de-design.gouv.fr/v1.14/storybook/?path=/docs/composants-alerte-alert--docs)
- [Site officiel](https://www.systeme-de-design.gouv.fr/elements-d-interface/alert)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🔹 BADGE

### 📋 INFORMATIONS GÉNÉRALES

- **Classe CSS** : `fr-badge`
- **Dossier GitHub** : `/src/dsfr/component/badge/`

📖 [Documentation interactive](https://www.systeme-de-design.gouv.fr/v1.14/storybook/?path=/docs/composants-badge-badge--docs)

### 📄 EXEMPLE (index.ejs)

```html
<% const sample = getSample(include); %>

<%- sample('Badge seul', './sample/badge-default', {}, true); %>

<p>Il est conseillé d'ajouter une balise span avec la classe fr-ellipsis à l'interieur du badge pour que celui ci reste sur une seule ligne, avec le texte coupé par des points de suspensions.</p>
<%- sample('Badge sur une seule ligne - ellipsis', './sample/badge-ellipsis', {}, true); %>

<%- sample('Badge - succès', './sample/badge-default', {badge: {type: 'success'}}, true); %>
<%- sample('Badge - succès sans icone', './sample/badge-default', {badge: {type: 'success', icon: false}}, true); %>
<%- sample('Badge - erreur', './sample/badge-default', {badge: {type: 'error'}}, true); %>
<%- sample('Badge - erreur sans icone', './sample/badge-default', {badge: {type: 'error', icon: false}
...
```

### 🔗 LIENS

- [GitHub](https://github.com/GouvernementFR/dsfr/tree/main/src/dsfr/component/badge)
- [Storybook](https://www.systeme-de-design.gouv.fr/v1.14/storybook/?path=/docs/composants-badge-badge--docs)
- [Site officiel](https://www.systeme-de-design.gouv.fr/elements-d-interface/badge)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🔹 CALLOUT

### 📋 INFORMATIONS GÉNÉRALES

- **Classe CSS** : `fr-callout`
- **Dossier GitHub** : `/src/dsfr/component/callout/`

📖 [Documentation interactive](https://www.systeme-de-design.gouv.fr/v1.14/storybook/?path=/docs/composants-mise-en-avant-callout--docs)

### 📄 EXEMPLE (index.ejs)

```html
<%
const sample = getSample(include);
let title = 'Titre mise en avant';
let buttonTpl = '../../../button/example/sample/button-default';
let icon = 'info-line';
%>

<%- sample('Mise en avant avec texte seul', './sample/callout-default', {}, true); %>

<%- sample('Mise en avant avec titre et texte', './sample/callout-default', {callout: {title:title}}, true); %>

<%- sample('Mise en avant avec titre, bouton et texte', './sample/callout-default', {callout: {title:title, buttonTpl:buttonTpl}}, true); %>

<%- sample('Mise en avant avec titre, bouton, icône et texte', './sample/callout-default', {callout: {title:title, buttonTpl:buttonTpl, icon: icon}}, true); %>

<%- sample('Mise en avant accentué', './sample/callout-default', {callout: {title:title, accent:'green-emeraude'}}, true); %>

```

### 🔗 LIENS

- [GitHub](https://github.com/GouvernementFR/dsfr/tree/main/src/dsfr/component/callout)
- [Storybook](https://www.systeme-de-design.gouv.fr/v1.14/storybook/?path=/docs/composants-mise-en-avant-callout--docs)
- [Site officiel](https://www.systeme-de-design.gouv.fr/elements-d-interface/callout)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🔹 CARD

### 📋 INFORMATIONS GÉNÉRALES

- **Classe CSS** : `fr-card`
- **Dossier GitHub** : `/src/dsfr/component/card/`

📖 [Documentation interactive](https://www.systeme-de-design.gouv.fr/v1.14/storybook/?path=/docs/composants-carte-card--docs)

### 📄 EXEMPLE (index.ejs)

```html
<% const sample = getSample(include); %>

<%
  const elements = [
    {
      title: 'Tailles',
      path: 'sample-sizes'
    },
    {
      title: 'Icône',
      path: 'sample-icon'
    },
    {
      title: 'Variations',
      path: 'sample-variations'
    },
    {
      title: 'Markup button',
      path: 'sample-button'
    },
    {
      title: 'Sans image',
      path: 'sample-no-img'
    },
    {
      title: 'Image et ratio',
      path: 'sample-img'
    },
    {
      title: 'En-tête',
      path: 'sample-header'
    },
    {
      title: 'Contenu',
      path: 'sample-content'
    },
    {
      title: 'Sans lien',
      path: 'sample-no-link'
    },
    {
      title: 'Sans lien étendu',
      path: 'sample-enlarge'
    },
    {
      title: 'Desactivée',
      path: 'sample-di
...
```

### 🔗 LIENS

- [GitHub](https://github.com/GouvernementFR/dsfr/tree/main/src/dsfr/component/card)
- [Storybook](https://www.systeme-de-design.gouv.fr/v1.14/storybook/?path=/docs/composants-carte-card--docs)
- [Site officiel](https://www.systeme-de-design.gouv.fr/elements-d-interface/card)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🔹 MODAL

### 📋 INFORMATIONS GÉNÉRALES

- **Classe CSS** : `fr-modal`
- **Dossier GitHub** : `/src/dsfr/component/modal/`

📖 [Documentation interactive](https://www.systeme-de-design.gouv.fr/v1.14/storybook/?path=/docs/composants-modale-modal--docs)

### 📄 EXEMPLE (index.ejs)

```html
<%
const sample = getSample(include);

let dataText = {
    title: 'Titre de la modale',
    icon: 'arrow-right-line',
    body: include('sample/body/text')
}

let dataForm = {
    title: 'Titre de la modale',
    icon: 'arrow-right-line',
    body: include('sample/body/form')
}

let dataFooterButtons = {
    title: 'Titre de la modale',
    icon: 'arrow-right-line',
    body: include('sample/body/text', { text: { paragraphs: 6 } }),
    footer: include('../example/sample/footer/buttons')
}

let dataTable = {
    title: 'Titre de la modale',
    icon: 'arrow-right-line',
    body: include('sample/body/table'),
    footer: include('../example/sample/footer/buttons')
}
%>

<%- sample('Modale simple', './sample/modal-default', {modal: { ...dataText, label: 'Modale simple'}}, true ); %>

<%- s
...
```

### 🔗 LIENS

- [GitHub](https://github.com/GouvernementFR/dsfr/tree/main/src/dsfr/component/modal)
- [Storybook](https://www.systeme-de-design.gouv.fr/v1.14/storybook/?path=/docs/composants-modale-modal--docs)
- [Site officiel](https://www.systeme-de-design.gouv.fr/elements-d-interface/modal)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🔹 TABLE

### 📋 INFORMATIONS GÉNÉRALES

- **Classe CSS** : `fr-table`
- **Dossier GitHub** : `/src/dsfr/component/table/`

📖 [Documentation interactive](https://www.systeme-de-design.gouv.fr/v1.14/storybook/?path=/docs/composants-tableau-table--docs)

### 📄 EXEMPLE (index.ejs)

```html

<%
const sample = getSample(include);
const cellMultilineData = JSON.parse(include('./data/data-lorem.json.ejs'));
cellMultilineData.tbodies[0][1][1] = {
  content: `<b>${lorem(null, 200)}</b>`,
  attributes: {
    class: `${prefix}-cell--multiline`
  }
};
const complexData = JSON.parse(include('./data/data-complex.json.ejs'));
%>

<%-
  sample(getText('sample.default', 'table'), './sample/table-simple', {table: {table: {id: 'table-md', caption: getText('data.caption.default', 'table')}}}, true);
%>

<%-
  sample(getText('sample.sm', 'table'), './sample/table-simple', {table: {size: 'sm', table: {id: 'table-sm', caption: getText('data.caption.default', 'table')}}}, true);
%>

<%-
  sample(getText('sample.lg', 'table'), './sample/table-simple', {table: {size: 'lg', table: {id: 'table-lg', 
...
```

### 🔗 LIENS

- [GitHub](https://github.com/GouvernementFR/dsfr/tree/main/src/dsfr/component/table)
- [Storybook](https://www.systeme-de-design.gouv.fr/v1.14/storybook/?path=/docs/composants-tableau-table--docs)
- [Site officiel](https://www.systeme-de-design.gouv.fr/elements-d-interface/table)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🔹 TAB

### 📋 INFORMATIONS GÉNÉRALES

- **Classe CSS** : `fr-tab`
- **Dossier GitHub** : `/src/dsfr/component/tab/`

📖 [Documentation interactive](https://www.systeme-de-design.gouv.fr/v1.14/storybook/?path=/docs/composants-onglets-tabs--docs)

### 📄 EXEMPLE (index.ejs)

```html
<% const sample = getSample(include, 44719); %>

<%- sample('Onglets 4 éléments', './sample/tabs-default', {tabs: { tabsCount: 4, icon: 'checkbox-circle-line' }}, true); %>

<%- sample('Onglets 2 éléments', './sample/tabs-default', { tabs: {tabsCount: 2 }}, true); %>

<%- sample('Onglets dans onglets', './sample/tabs-in-tabs', {}, true); %>

<%- sample('Accordéon dans onglets', './sample/tabs-accordions', { tabs: {tabsCount: 2 }}, true); %>

<%- sample('Onglets 100% largeur du viewport en mobile', './sample/tabs-default', { tabs: {tabsCount: 2, viewportWidth: true} }, true); %>

```

### 🔗 LIENS

- [GitHub](https://github.com/GouvernementFR/dsfr/tree/main/src/dsfr/component/tab)
- [Storybook](https://www.systeme-de-design.gouv.fr/v1.14/storybook/?path=/docs/composants-onglets-tabs--docs)
- [Site officiel](https://www.systeme-de-design.gouv.fr/elements-d-interface/tab)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🔹 TAG

### 📋 INFORMATIONS GÉNÉRALES

- **Classe CSS** : `fr-tag`
- **Dossier GitHub** : `/src/dsfr/component/tag/`

📖 [Documentation interactive](https://www.systeme-de-design.gouv.fr/v1.14/storybook/?path=/docs/composants-tag-tag--docs)

### 📄 EXEMPLE (index.ejs)

```html
<% const sample = getSample(include); %>

<%- section('Tag non cliquable', 'Tag simple sans interaction', 0) %>
<%- sample('Tag non cliquable sans icône', './sample/tag-default', {}, true); %>
<%- sample('Tag non cliquable icône à gauche', './sample/tag-default', {tag:{iconPlace: 'left', icon: 'arrow-left-line'}}, true); %>
<%- sample('Tag non cliquable taille SM', './sample/tag-sm', {}, true); %>

<%- section('Tag cliquable', 'La balise utilisée pour le tag cliquable est un "a" s\'il s\'agit d\'un lien (href), si pas de href utiliser "button".') %>
<%- sample('Tag cliquable', './sample/tag-clickable', {}, true); %>
<%- sample('Tag cliquable avec icône', './sample/tag-clickable', {tag:{iconPlace: 'left', icon: 'arrow-left-line'}}, true); %>
<%- sample('Tag cliquable SM', './sample/tag-clic
...
```

### 🔗 LIENS

- [GitHub](https://github.com/GouvernementFR/dsfr/tree/main/src/dsfr/component/tag)
- [Storybook](https://www.systeme-de-design.gouv.fr/v1.14/storybook/?path=/docs/composants-tag-tag--docs)
- [Site officiel](https://www.systeme-de-design.gouv.fr/elements-d-interface/tag)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🔹 TILE

### 📋 INFORMATIONS GÉNÉRALES

- **Classe CSS** : `fr-tile`
- **Dossier GitHub** : `/src/dsfr/component/tile/`

📖 [Documentation interactive](https://www.systeme-de-design.gouv.fr/v1.14/storybook/?path=/docs/composants-tuile-tile--docs)

### 📄 EXEMPLE (index.ejs)

```html
<% const sample = getSample(include); %>

<%
  const elements = [
    {
      title: 'Tailles',
      path: 'sample-sizes'
    },
    {
      title: 'Sans image',
      path: 'sample-no-img'
    },
    {
      title: 'Contenu',
      path: 'sample-content'
    },
    {
      title: 'Variantes',
      path: 'sample-variations'
    },
    {
      title: 'Markup button',
      path: 'sample-button'
    },
    {
      title: 'Sans lien',
      path: 'sample-no-link'
    },
    {
      title: 'Sans lien étendu',
      path: 'sample-enlarge'
    },
    {
      title: 'Désactivée',
      path: 'sample-disabled'
    },
    {
      title: 'Icône',
      path: 'sample-icon'
    },
    {
      title: 'Tuile horizontale',
      path: 'sample-horizontal'
    },
    {
      title: 'Grille de tuiles vert
...
```

### 🔗 LIENS

- [GitHub](https://github.com/GouvernementFR/dsfr/tree/main/src/dsfr/component/tile)
- [Storybook](https://www.systeme-de-design.gouv.fr/v1.14/storybook/?path=/docs/composants-tuile-tile--docs)
- [Site officiel](https://www.systeme-de-design.gouv.fr/elements-d-interface/tile)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🔹 TOOLTIP

### 📋 INFORMATIONS GÉNÉRALES

- **Classe CSS** : `fr-tooltip`
- **Dossier GitHub** : `/src/dsfr/component/tooltip/`

📖 [Documentation interactive](https://www.systeme-de-design.gouv.fr/v1.14/storybook/?path=/docs/composants-infobulle-tooltip--docs)

### 📄 EXEMPLE (index.ejs)

```html
<% const sample = getSample(include); %>

<%- sample({title: getText('sample', 'tooltip'), subtitle: getText('sample.hover', 'tooltip')}, './sample/tooltip-hover.ejs', {}, true);  %>

<%- sample({title: getText('sample.tooltip', 'tooltip'), subtitle: getText('sample.click', 'tooltip')}, './sample/tooltip-button.ejs', {}, true);  %>

<%- sample(getText('sample.grid.left', 'tooltip'), './sample/tooltip-grid.ejs', {}, true);  %>

<%- sample(getText('sample.grid.right', 'tooltip'), './sample/tooltip-grid.ejs', {tooltip: {position: 'right'}}, true);  %>

<%- sample(getText('sample.list', 'tooltip'), './sample/tooltip-list.ejs', {}, true);  %>

<%- sample(getText('sample.table', 'tooltip'), './sample/tooltip-table.ejs', {}, true);  %>

```

### 🔗 LIENS

- [GitHub](https://github.com/GouvernementFR/dsfr/tree/main/src/dsfr/component/tooltip)
- [Storybook](https://www.systeme-de-design.gouv.fr/v1.14/storybook/?path=/docs/composants-infobulle-tooltip--docs)
- [Site officiel](https://www.systeme-de-design.gouv.fr/elements-d-interface/tooltip)


## 📄 Contenu


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🔹 CONTENT

### 📋 INFORMATIONS GÉNÉRALES

- **Classe CSS** : `fr-content`
- **Dossier GitHub** : `/src/dsfr/component/content/`

📖 [Documentation interactive](https://www.systeme-de-design.gouv.fr/v1.14/storybook/?path=/docs/composants-gestionnaire-de-contenu-content--docs)

### 📄 EXEMPLE (index.ejs)

```html
<% const sample = getSample(include, 666); %>

<%- sample('Média image edito', './sample/media-img', {}, true); %>

<%- sample('Média image edito, petite taille', './sample/media-img', { content: { size:'sm' } }, true); %>

<%- sample('Média image edito, grande taille', './sample/media-img', { content: { size:'lg' } }, true); %>

<%- sample('Média image edito ratio 32x9', './sample/media-img', { content: { ratio:'32x9' } }, true); %>

<%- sample('Média image edito ratio 16x9', './sample/media-img', { content: { ratio:'16x9' } }, true); %>

<%- sample('Média image edito ratio 3x2', './sample/media-img', { content: { ratio:'3x2' } }, true); %>

<%- sample('Média image edito ratio 4x3', './sample/media-img', { content: { ratio:'4x3' } }, true); %>

<%- sample('Média image edito ratio 1x1', '.
...
```

### 🔗 LIENS

- [GitHub](https://github.com/GouvernementFR/dsfr/tree/main/src/dsfr/component/content)
- [Storybook](https://www.systeme-de-design.gouv.fr/v1.14/storybook/?path=/docs/composants-gestionnaire-de-contenu-content--docs)
- [Site officiel](https://www.systeme-de-design.gouv.fr/elements-d-interface/content)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🔹 HIGHLIGHT

### 📋 INFORMATIONS GÉNÉRALES

- **Classe CSS** : `fr-highlight`
- **Dossier GitHub** : `/src/dsfr/component/highlight/`

📖 [Documentation interactive](https://www.systeme-de-design.gouv.fr/v1.14/storybook/?path=/docs/composants-mise-en-exergue-highlight--docs)

### 📄 EXEMPLE (index.ejs)

```html
<% const sample = getSample(include); %>

<%- sample('Exergue taille sm', './sample/highlight-sm', {}, true); %>

<%- sample('Exergue taille md', './sample/highlight-default', {}, true); %>

<%- sample('Exergue taille lg', './sample/highlight-lg', {}, true); %>

<%- sample('Exergue accentué', './sample/highlight-default', {highlight:{accent:'green-emeraude'}}, true); %>


```

### 🔗 LIENS

- [GitHub](https://github.com/GouvernementFR/dsfr/tree/main/src/dsfr/component/highlight)
- [Storybook](https://www.systeme-de-design.gouv.fr/v1.14/storybook/?path=/docs/composants-mise-en-exergue-highlight--docs)
- [Site officiel](https://www.systeme-de-design.gouv.fr/elements-d-interface/highlight)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🔹 QUOTE

### 📋 INFORMATIONS GÉNÉRALES

- **Classe CSS** : `fr-quote`
- **Dossier GitHub** : `/src/dsfr/component/quote/`

📖 [Documentation interactive](https://www.systeme-de-design.gouv.fr/v1.14/storybook/?path=/docs/composants-citation-quote--docs)

### 📄 EXEMPLE (index.ejs)

```html
<%
const sample = getSample(include);
%>

<%- sample('Citation par défaut (texte taille xl)', './sample/quote-default', {}, true); %>

<%- sample('Citation taille lg', './sample/quote-default', {quote:{size:'lg', sources: ['<a target="_blank" href="' + contentPlaceholder('Lien vers la sources ou des infos complémentaires') + '">Un seul détail</a>']}}, true); %>

<%- sample('Citation avec image', './sample/quote-with-image', {}, true); %>

<%- sample('Citation accentuée', './sample/quote-default', { quote: {accent:'green-emeraude'} }, true); %>

```

### 🔗 LIENS

- [GitHub](https://github.com/GouvernementFR/dsfr/tree/main/src/dsfr/component/quote)
- [Storybook](https://www.systeme-de-design.gouv.fr/v1.14/storybook/?path=/docs/composants-citation-quote--docs)
- [Site officiel](https://www.systeme-de-design.gouv.fr/elements-d-interface/quote)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🔹 SUMMARY

### 📋 INFORMATIONS GÉNÉRALES

- **Classe CSS** : `fr-summary`
- **Dossier GitHub** : `/src/dsfr/component/summary/`

📖 [Documentation interactive](https://www.systeme-de-design.gouv.fr/v1.14/storybook/?path=/docs/composants-sommaire-summary--docs)

### 📄 EXEMPLE (index.ejs)

```html
<% const sample = getSample(include); %>

<%
const getContent = (id) => {
    return `<div id="anchor-${id}">
        <h2>Contenu ${id}</h2>
    <p>${lorem()}</p>
</div>`;
}

const links = [12, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 12];
let data = {list:[]};
let content = '';

for (let i = 0; i < links.length; i++) {
    let id = i + 1
    content += getContent(id);

    if (links[i]) {
        for (let j = 0; j < links[i]; j++) {
            id = `${i + 1}.${j + 1}`;
            content += getContent(id);
        }
    }
}

%>

<%- sample('Sommaire', './sample/summary', {summary: {links: links}}, true); %>

<%- content; %>

```

### 🔗 LIENS

- [GitHub](https://github.com/GouvernementFR/dsfr/tree/main/src/dsfr/component/summary)
- [Storybook](https://www.systeme-de-design.gouv.fr/v1.14/storybook/?path=/docs/composants-sommaire-summary--docs)
- [Site officiel](https://www.systeme-de-design.gouv.fr/elements-d-interface/summary)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🔹 TRANSCRIPTION

### 📋 INFORMATIONS GÉNÉRALES

- **Classe CSS** : `fr-transcription`
- **Dossier GitHub** : `/src/dsfr/component/transcription/`

📖 [Documentation interactive](https://www.systeme-de-design.gouv.fr/v1.14/storybook/?path=/docs/composants-transcription-transcription--docs)

### 📄 EXEMPLE (index.ejs)

```html
<% const sample = getSample(include, 234); %>

<%- sample(getText('sample', 'transcription'), './sample/transcription-default.ejs', {}, true);  %>

```

### 🔗 LIENS

- [GitHub](https://github.com/GouvernementFR/dsfr/tree/main/src/dsfr/component/transcription)
- [Storybook](https://www.systeme-de-design.gouv.fr/v1.14/storybook/?path=/docs/composants-transcription-transcription--docs)
- [Site officiel](https://www.systeme-de-design.gouv.fr/elements-d-interface/transcription)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🔹 NOTICE

### 📋 INFORMATIONS GÉNÉRALES

- **Classe CSS** : `fr-notice`
- **Dossier GitHub** : `/src/dsfr/component/notice/`

📖 [Documentation interactive](https://www.systeme-de-design.gouv.fr/v1.14/storybook/?path=/docs/composants-bandeau-d-information-importante-notice--docs)

### 📄 EXEMPLE (index.ejs)

```html
<% const sample = getSample(include); %>

<%
  const elements = [
    {
      title: 'Contenu',
      path: 'sample-content'
    },
    {
      title: 'Bandeaux génériques',
      path: 'sample-generic'
    },
    {
      title: 'Bandeaux météo',
      path: 'sample-meteo'
    },
    {
      title: 'Bandeaux d\'alertes',
      path: 'sample-alert'
    },
    {
      title: 'Mise en situation',
      path: 'sample-header'
    },
  ];

  const accordions = [];

  for (let element of elements) { %>
    <%- include(`./sample/${element.path}`); %>
    <br><br><br><br>
  <%  }
%>

```

### 🔗 LIENS

- [GitHub](https://github.com/GouvernementFR/dsfr/tree/main/src/dsfr/component/notice)
- [Storybook](https://www.systeme-de-design.gouv.fr/v1.14/storybook/?path=/docs/composants-bandeau-d-information-importante-notice--docs)
- [Site officiel](https://www.systeme-de-design.gouv.fr/elements-d-interface/notice)


## 🔧 Utilitaires


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🔹 CONSENT

### 📋 INFORMATIONS GÉNÉRALES

- **Classe CSS** : `fr-consent`
- **Dossier GitHub** : `/src/dsfr/component/consent/`

📖 [Documentation interactive](https://www.systeme-de-design.gouv.fr/v1.14/storybook/?path=/docs/composants-gestionnaire-de-consentement-consent--docs)

### 📄 EXEMPLE (index.ejs)

```html
<% const sample = getSample(include, 123); %>

<%- sample('Gestionnaire de consentement', './sample/banner.ejs', {}, true); %>

<%- sample('Panneau de gestion des cookies', './sample/modal.ejs', {}, true ); %>

<%- sample('Placeholder cookies désactivés standard', './sample/placeholder.ejs', {}, true); %>

<%- sample('Placeholder dans un bloc vidéo responsive grande taille', '../../content/example/sample/media-vid-1x1', {content: {service: "Youtube", size:'lg', consent: { title: '**Nom du service** est désactivé', body: 'Autorisez le dépôt de cookies pour accèder à cette fonctionnalité.', button: {size: 'md', label: "Autoriser"}}, transcription: {id: uniqueId('transcription'), title: getText('modal.title', 'transcription'), content: randomContent(['text', 'list']), fullscreen: getText('but
...
```

### 🔗 LIENS

- [GitHub](https://github.com/GouvernementFR/dsfr/tree/main/src/dsfr/component/consent)
- [Storybook](https://www.systeme-de-design.gouv.fr/v1.14/storybook/?path=/docs/composants-gestionnaire-de-consentement-consent--docs)
- [Site officiel](https://www.systeme-de-design.gouv.fr/elements-d-interface/consent)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🔹 DISPLAY

### 📋 INFORMATIONS GÉNÉRALES

- **Classe CSS** : `fr-display`
- **Dossier GitHub** : `/src/dsfr/component/display/`

### 📄 EXEMPLE (index.ejs)

```html
<%
const sample = getSample(include);

const attrModal = {};
attrModal['aria-controls'] = prefix + '-theme-modal';
attrModal[`data-${prefix}-opened`] = false;

const links = {
  buttons: [
    {
      label: 'Paramètres d\'affichage',
      classes: [`${prefix}-btn--display`],
      attributes: {...attrModal},
      markup: 'button'
    }
  ]
};

let dataModal = {
  id: prefix + "-theme-modal",
  title: 'Paramètres d’affichage',
  body: include('../../display/example/sample/body'),
  size: "sm"
}

let dataFooter = {
    id: uniqueId('footer'),
    brand: {
      logo: {
          title: 'république<br>française',
      },
    },
    content: {
      desc: lorem(),
      links: [
        {label: 'info.gouv.fr', href: 'https://info.gouv.fr', blank: true, attributes: { title: getBlankTitle('i
...
```

### 🔗 LIENS

- [GitHub](https://github.com/GouvernementFR/dsfr/tree/main/src/dsfr/component/display)
- [Site officiel](https://www.systeme-de-design.gouv.fr/elements-d-interface/display)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🔹 FOLLOW

### 📋 INFORMATIONS GÉNÉRALES

- **Classe CSS** : `fr-follow`
- **Dossier GitHub** : `/src/dsfr/component/follow/`

### 📄 EXEMPLE (index.ejs)

```html
<% const sample = getSample(include); %>

<%- section('Réseaux sociaux seuls', 'Les icones réseaux sociaux disponibles pour ce composant sont définies dans :', 0, true); %>

<div class="fr-container">
    <%
    const accordion = {
        label: 'src/component/follow/style/_setting.scss',
        id: uniqueId('snippet'),
        content: '<pre class=" language-scss"><code>' + include('../style/_setting.scss') + '</code></pre>'
    };
    %>
    <div class="<%= prefix %>-mb-4v" >
        <%- include(root + 'src/dsfr/component/accordion/template/ejs/accordion', {accordion: accordion}); %>
    </div>


    <%- section(null, 'Il est aussi possible d\'appliquer une classe utilitaire sur un bouton pour utiliser une icone du dsfr (ex: "fr-icon-rss-line")', 0); %>

</div>

<%- sample('', './sampl
...
```

### 🔗 LIENS

- [GitHub](https://github.com/GouvernementFR/dsfr/tree/main/src/dsfr/component/follow)
- [Site officiel](https://www.systeme-de-design.gouv.fr/elements-d-interface/follow)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🔹 PAGINATION

### 📋 INFORMATIONS GÉNÉRALES

- **Classe CSS** : `fr-pagination`
- **Dossier GitHub** : `/src/dsfr/component/pagination/`

📖 [Documentation interactive](https://www.systeme-de-design.gouv.fr/v1.14/storybook/?path=/docs/composants-pagination-pagination--docs)

### 📄 EXEMPLE (index.ejs)

```html
<% const sample = getSample(include); %>

<%- sample('Élément de navigation icône seule (par défaut)', './sample/modifiers', {}, true); %>

<%- sample('Élément de navigation avec libellés', './sample/modifiers', {pagination: { hasLabel: true }}, true); %>

<%- sample('Élément de navigation avec libellés à partir du breakpoint LG', './sample/modifiers', {pagination: { hasLgLabel: true }}, true); %>

<%- sample('Pagination première page', './sample/pagination', {pagination: {index:0}}, true); %>

<%- sample('Pagination deuxième page', './sample/pagination', {pagination: {index:1}}, true); %>

<%- sample('Pagination dernière page', './sample/pagination', {pagination: {index:6}}, true); %>




```

### 🔗 LIENS

- [GitHub](https://github.com/GouvernementFR/dsfr/tree/main/src/dsfr/component/pagination)
- [Storybook](https://www.systeme-de-design.gouv.fr/v1.14/storybook/?path=/docs/composants-pagination-pagination--docs)
- [Site officiel](https://www.systeme-de-design.gouv.fr/elements-d-interface/pagination)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🔹 SHARE

### 📋 INFORMATIONS GÉNÉRALES

- **Classe CSS** : `fr-share`
- **Dossier GitHub** : `/src/dsfr/component/share/`

📖 [Documentation interactive](https://www.systeme-de-design.gouv.fr/v1.14/storybook/?path=/docs/composants-partage-share--docs)

### 📄 EXEMPLE (index.ejs)

```html
<% const sample = getSample(include); %>

<%- section('Méta données', 'Données à insérer dans la partie <code>< head ></code> de la page, pour fournir un aperçu de la page aux applications tierces lors du partage.', 0); %>

<%- sample('', './sample/meta-share', {}, true); %>

<%- section('Boutons de partage par défaut', 'Les icones réseaux sociaux disponibles pour ce composant sont définies dans :', 0); %>

<%
const accordion = {
    label: 'src/component/share/style/_setting.scss',
    id: uniqueId('snippet'),
    content: '<pre class=" language-scss"><code>' + include('../style/_setting.scss') + '</code></pre>'
};
%>
<div class="<%= prefix %>-mb-4v" >
    <%- include(root + 'src/dsfr/component/accordion/template/ejs/accordion', {accordion: accordion}); %>
</div>
<%- section(null, 'Il est
...
```

### 🔗 LIENS

- [GitHub](https://github.com/GouvernementFR/dsfr/tree/main/src/dsfr/component/share)
- [Storybook](https://www.systeme-de-design.gouv.fr/v1.14/storybook/?path=/docs/composants-partage-share--docs)
- [Site officiel](https://www.systeme-de-design.gouv.fr/elements-d-interface/share)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🔹 STEPPER

### 📋 INFORMATIONS GÉNÉRALES

- **Classe CSS** : `fr-stepper`
- **Dossier GitHub** : `/src/dsfr/component/stepper/`

### 📄 EXEMPLE (index.ejs)

```html
<%
const sample = getSample(include);
%>

<%- section('Informations générales', 'L\'indicateur d\'étape peut contenir de 2 à 8 étapes.<br> Il doit être placé dans un conteneur de 6 à 8 colonnes de large en desktop, et 100% (12 colonnes) en mobile.<br> Le niveau de titre h2 peut être modifié suivant le contexte', 0); %>

<%- sample('Exemple d\'indicateur d\'étape 1 sur 3', './sample/stepper-default', {}, true); %>

<%- sample('Exemple d\'indicateur d\'étape 2 sur 8', './sample/stepper-default', {stepper: {currentStep: 2, stepCount: 8}}, true); %>

```

### 🔗 LIENS

- [GitHub](https://github.com/GouvernementFR/dsfr/tree/main/src/dsfr/component/stepper)
- [Site officiel](https://www.systeme-de-design.gouv.fr/elements-d-interface/stepper)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🔹 TRANSLATE

### 📋 INFORMATIONS GÉNÉRALES

- **Classe CSS** : `fr-translate`
- **Dossier GitHub** : `/src/dsfr/component/translate/`

### 📄 EXEMPLE (index.ejs)

```html
<% const sample = getSample(include); %>

<%- sample(getText('sample', 'translate'), './sample/translate-default.ejs', {}, true);  %>

<%- sample(getText('sample.no-outline', 'translate'), './sample/translate-default.ejs', {translate: {button: {kind:4}}}, true);  %>

<%- sample(getText('sample.column', 'translate'), './sample/translate-big.ejs', {translate: {col: 3}}, true);  %>

```

### 🔗 LIENS

- [GitHub](https://github.com/GouvernementFR/dsfr/tree/main/src/dsfr/component/translate)
- [Site officiel](https://www.systeme-de-design.gouv.fr/elements-d-interface/translate)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# 📚 RESSOURCES COMPLÈTES

## 🔗 Liens officiels

- **Site web** : https://www.systeme-de-design.gouv.fr/
- **GitHub** : https://github.com/GouvernementFR/dsfr
- **NPM** : https://www.npmjs.com/package/@gouvfr/dsfr
- **Storybook** : https://www.systeme-de-design.gouv.fr/storybook/
- **Figma** : https://www.figma.com/community/file/1039777231080123654

## 📖 Documentation

- [Guide de démarrage](https://www.systeme-de-design.gouv.fr/utilisation-et-organisation/developpeurs/prise-en-main)
- [Accessibilité RGAA](https://www.systeme-de-design.gouv.fr/utilisation-et-organisation/accessibilite-et-rgaa)
- [Marque État](https://www.systeme-de-design.gouv.fr/utilisation-et-organisation/charte-graphique)

## 🛠️ Outils

- [Générateur de thème](https://www.systeme-de-design.gouv.fr/utilisation-et-organisation/developpeurs/personnalisation)
- [Migration guide](https://github.com/GouvernementFR/dsfr/blob/main/MIGRATION.md)
- [Changelog](https://github.com/GouvernementFR/dsfr/blob/main/CHANGELOG.md)

---

*Documentation ULTRA COMPLÈTE générée automatiquement*
*Combinaison de : GitHub + Storybook + NPM*
