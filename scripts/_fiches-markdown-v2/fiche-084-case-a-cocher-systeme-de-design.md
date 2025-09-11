URL:
https://main--ds-gouv.netlify.app/example/component/checkbox/deprecated

Title:
Case à cocher - Système de design

Markdown:

Case à cocher - Système de design


DSFR v1.14.0


[Retour](../)


# Case à cocher (checkbox)


La case à cocher permet à l'utilisateur de sélectionner une ou plusieurs options dans une liste. Elle est utilisée pour effectuer des sélections multiples (de 0 à N éléments), ou bien pour permettre un choix binaire, lorsque l'utilisateur peut sélectionner ou désélectionner une seule option.
[Documentation](https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/case-a-cocher)


## Dépréciation


Les exemples suivants sont dépréciés, ne pas utiliser comme référence

Pour support des versions précédentes


### Ensemble de cases à cocher


Légende pour l'ensemble de champs


Libellé checkbox


Libellé checkbox


Libellé checkbox


###
Extrait de code


<div class="fr-form-group">
<fieldset class="fr-fieldset">
<legend class="fr-fieldset__legend fr-text--regular" id='checkboxes-legend'>
Légende pour l'ensemble de champs
</legend>
<div class="fr-fieldset__content">
<div class="fr-checkbox-group">
<input name="checkboxes-1" id="checkboxes-1" type="checkbox" aria-describedby="checkboxes-1-messages">
<label class="fr-label" for="checkboxes-1">
Libellé checkbox
</label>
<div class="fr-messages-group" id="checkboxes-1-messages" aria-live="polite">
</div>
</div>
<div class="fr-checkbox-group">
<input checked name="checkboxes-2" id="checkboxes-2" type="checkbox" aria-describedby="checkboxes-2-messages">
<label class="fr-label" for="checkboxes-2">
Libellé checkbox
</label>
<div class="fr-messages-group" id="checkboxes-2-messages" aria-live="polite">
</div>
</div>
<div class="fr-checkbox-group">
<input name="checkboxes-3" id="checkboxes-3" type="checkbox" aria-describedby="checkboxes-3-messages">
<label class="fr-label" for="checkboxes-3">
Libellé checkbox
</label>
<div class="fr-messages-group" id="checkboxes-3-messages" aria-live="polite">
</div>
</div>
</div>
</fieldset>
</div>


### Ensemble de cases à cocher, petite taille


Légende pour l'ensemble de champs


Libellé checkbox


Libellé checkbox


Libellé checkbox


###
Extrait de code


<div class="fr-form-group">
<fieldset class="fr-fieldset">
<legend class="fr-fieldset__legend fr-text--regular" id='checkboxes-small-legend'>
Légende pour l'ensemble de champs
</legend>
<div class="fr-fieldset__content">
<div class="fr-checkbox-group fr-checkbox-group--sm">
<input name="checkboxes-small-1" id="checkboxes-small-1" type="checkbox" aria-describedby="checkboxes-small-1-messages">
<label class="fr-label" for="checkboxes-small-1">
Libellé checkbox
</label>
<div class="fr-messages-group" id="checkboxes-small-1-messages" aria-live="polite">
</div>
</div>
<div class="fr-checkbox-group fr-checkbox-group--sm">
<input checked name="checkboxes-small-2" id="checkboxes-small-2" type="checkbox" aria-describedby="checkboxes-small-2-messages">
<label class="fr-label" for="checkboxes-small-2">
Libellé checkbox
</label>
<div class="fr-messages-group" id="checkboxes-small-2-messages" aria-live="polite">
</div>
</div>
<div class="fr-checkbox-group fr-checkbox-group--sm">
<input name="checkboxes-small-3" id="checkboxes-small-3" type="checkbox" aria-describedby="checkboxes-small-3-messages">
<label class="fr-label" for="checkboxes-small-3">
Libellé checkbox
</label>
<div class="fr-messages-group" id="checkboxes-small-3-messages" aria-live="polite">
</div>
</div>
</div>
</fieldset>
</div>


### Ensemble de cases à cocher désactivées


Légende pour l'ensemble de champs


Libellé checkbox


Libellé checkbox


Libellé checkbox


###
Extrait de code


<div class="fr-form-group">
<fieldset class="fr-fieldset">
<legend class="fr-fieldset__legend fr-text--regular" id='checkboxes-disabled-legend'>
Légende pour l'ensemble de champs
</legend>
<div class="fr-fieldset__content">
<div class="fr-checkbox-group">
<input disabled name="checkboxes-disabled-1" id="checkboxes-disabled-1" type="checkbox" aria-describedby="checkboxes-disabled-1-messages">
<label class="fr-label" for="checkboxes-disabled-1">
Libellé checkbox
</label>
<div class="fr-messages-group" id="checkboxes-disabled-1-messages" aria-live="polite">
</div>
</div>
<div class="fr-checkbox-group">
<input checked disabled name="checkboxes-disabled-2" id="checkboxes-disabled-2" type="checkbox" aria-describedby="checkboxes-disabled-2-messages">
<label class="fr-label" for="checkboxes-disabled-2">
Libellé checkbox
</label>
<div class="fr-messages-group" id="checkboxes-disabled-2-messages" aria-live="polite">
</div>
</div>
<div class="fr-checkbox-group">
<input disabled name="checkboxes-disabled-3" id="checkboxes-disabled-3" type="checkbox" aria-describedby="checkboxes-disabled-3-messages">
<label class="fr-label" for="checkboxes-disabled-3">
Libellé checkbox
</label>
<div class="fr-messages-group" id="checkboxes-disabled-3-messages" aria-live="polite">
</div>
</div>
</div>
</fieldset>
</div>


### Ensemble de cases à cocher en ligne


Légende pour l'ensemble de champs


Libellé checkbox


Libellé checkbox


Libellé checkbox


###
Extrait de code


<div class="fr-form-group">
<fieldset class="fr-fieldset fr-fieldset--inline">
<legend class="fr-fieldset__legend fr-text--regular" id='checkboxes-inline-legend'>
Légende pour l'ensemble de champs
</legend>
<div class="fr-fieldset__content">
<div class="fr-checkbox-group">
<input name="checkboxes-inline-1" id="checkboxes-inline-1" type="checkbox" aria-describedby="checkboxes-inline-1-messages">
<label class="fr-label" for="checkboxes-inline-1">
Libellé checkbox
</label>
<div class="fr-messages-group" id="checkboxes-inline-1-messages" aria-live="polite">
</div>
</div>
<div class="fr-checkbox-group">
<input name="checkboxes-inline-2" id="checkboxes-inline-2" type="checkbox" aria-describedby="checkboxes-inline-2-messages">
<label class="fr-label" for="checkboxes-inline-2">
Libellé checkbox
</label>
<div class="fr-messages-group" id="checkboxes-inline-2-messages" aria-live="polite">
</div>
</div>
<div class="fr-checkbox-group">
<input name="checkboxes-inline-3" id="checkboxes-inline-3" type="checkbox" aria-describedby="checkboxes-inline-3-messages">
<label class="fr-label" for="checkboxes-inline-3">
Libellé checkbox
</label>
<div class="fr-messages-group" id="checkboxes-inline-3-messages" aria-live="polite">
</div>
</div>
</div>
</fieldset>
</div>


### Ensemble de cases à cocher avec texte d'aide


Légende pour l'ensemble de champs


Libellé checkbox
Texte de description additionnel


Libellé checkbox
Texte de description additionnel


Libellé checkbox
Texte de description additionnel


###
Extrait de code


<div class="fr-form-group">
<fieldset class="fr-fieldset">
<legend class="fr-fieldset__legend fr-text--regular" id='checkboxes-hint-legend'>
Légende pour l'ensemble de champs
</legend>
<div class="fr-fieldset__content">
<div class="fr-checkbox-group">
<input name="checkboxes-hint-1" id="checkboxes-hint-1" type="checkbox" aria-describedby="checkboxes-hint-1-messages">
<label class="fr-label" for="checkboxes-hint-1">
Libellé checkbox
<span class="fr-hint-text">Texte de description additionnel</span>
</label>
<div class="fr-messages-group" id="checkboxes-hint-1-messages" aria-live="polite">
</div>
</div>
<div class="fr-checkbox-group">
<input name="checkboxes-hint-2" id="checkboxes-hint-2" type="checkbox" aria-describedby="checkboxes-hint-2-messages">
<label class="fr-label" for="checkboxes-hint-2">
Libellé checkbox
<span class="fr-hint-text">Texte de description additionnel</span>
</label>
<div class="fr-messages-group" id="checkboxes-hint-2-messages" aria-live="polite">
</div>
</div>
<div class="fr-checkbox-group">
<input name="checkboxes-hint-3" id="checkboxes-hint-3" type="checkbox" aria-describedby="checkboxes-hint-3-messages">
<label class="fr-label" for="checkboxes-hint-3">
Libellé checkbox
<span class="fr-hint-text">Texte de description additionnel</span>
</label>
<div class="fr-messages-group" id="checkboxes-hint-3-messages" aria-live="polite">
</div>
</div>
</div>
</fieldset>
</div>


### Ensemble de cases à cocher avec erreur


Légende pour l'ensemble de champs


Libellé checkbox


Libellé checkbox


Libellé checkbox


Texte d'erreur obligatoire


###
Extrait de code


<div class="fr-form-group">
<fieldset class="fr-fieldset fr-fieldset--error" aria-labelledby="checkboxes-error-legend checkboxes-error-desc-error" role="group">
<legend class="fr-fieldset__legend fr-text--regular" id='checkboxes-error-legend'>
Légende pour l'ensemble de champs
</legend>
<div class="fr-fieldset__content">
<div class="fr-checkbox-group">
<input name="checkboxes-error-1" id="checkboxes-error-1" type="checkbox" aria-describedby="checkboxes-error-1-messages">
<label class="fr-label" for="checkboxes-error-1">
Libellé checkbox
</label>
<div class="fr-messages-group" id="checkboxes-error-1-messages" aria-live="polite">
</div>
</div>
<div class="fr-checkbox-group">
<input name="checkboxes-error-2" id="checkboxes-error-2" type="checkbox" aria-describedby="checkboxes-error-2-messages">
<label class="fr-label" for="checkboxes-error-2">
Libellé checkbox
</label>
<div class="fr-messages-group" id="checkboxes-error-2-messages" aria-live="polite">
</div>
</div>
<div class="fr-checkbox-group">
<input name="checkboxes-error-3" id="checkboxes-error-3" type="checkbox" aria-describedby="checkboxes-error-3-messages">
<label class="fr-label" for="checkboxes-error-3">
Libellé checkbox
</label>
<div class="fr-messages-group" id="checkboxes-error-3-messages" aria-live="polite">
</div>
</div>
</div>
<p id="checkboxes-error-desc-error" class="fr-error-text">
Texte d'erreur obligatoire
</p>
</fieldset>
</div>


### Ensemble de cases à cocher validées


Légende pour l'ensemble de champs


Libellé checkbox


Libellé checkbox


Libellé checkbox


Texte de validation


###
Extrait de code


<div class="fr-form-group">
<fieldset class="fr-fieldset fr-fieldset--valid" aria-labelledby="checkboxes-valid-legend checkboxes-valid-desc-valid" role="group">
<legend class="fr-fieldset__legend fr-text--regular" id='checkboxes-valid-legend'>
Légende pour l'ensemble de champs
</legend>
<div class="fr-fieldset__content">
<div class="fr-checkbox-group">
<input name="checkboxes-valid-1" id="checkboxes-valid-1" type="checkbox" aria-describedby="checkboxes-valid-1-messages">
<label class="fr-label" for="checkboxes-valid-1">
Libellé checkbox
</label>
<div class="fr-messages-group" id="checkboxes-valid-1-messages" aria-live="polite">
</div>
</div>
<div class="fr-checkbox-group">
<input name="checkboxes-valid-2" id="checkboxes-valid-2" type="checkbox" aria-describedby="checkboxes-valid-2-messages">
<label class="fr-label" for="checkboxes-valid-2">
Libellé checkbox
</label>
<div class="fr-messages-group" id="checkboxes-valid-2-messages" aria-live="polite">
</div>
</div>
<div class="fr-checkbox-group">
<input name="checkboxes-valid-3" id="checkboxes-valid-3" type="checkbox" aria-describedby="checkboxes-valid-3-messages">
<label class="fr-label" for="checkboxes-valid-3">
Libellé checkbox
</label>
<div class="fr-messages-group" id="checkboxes-valid-3-messages" aria-live="polite">
</div>
</div>
</div>
<p id="checkboxes-valid-desc-valid" class="fr-valid-text">
Texte de validation
</p>
</fieldset>
</div>


### Ensemble de cases à cocher avec erreur, en ligne


Légende pour l'ensemble de champs


Libellé checkbox


Libellé checkbox


Libellé checkbox


Texte d'erreur obligatoire


###
Extrait de code


<div class="fr-form-group">
<fieldset class="fr-fieldset fr-fieldset--inline fr-fieldset--error" aria-labelledby="checkboxes-error-inline-legend checkboxes-error-inline-desc-error" role="group">
<legend class="fr-fieldset__legend fr-text--regular" id='checkboxes-error-inline-legend'>
Légende pour l'ensemble de champs
</legend>
<div class="fr-fieldset__content">
<div class="fr-checkbox-group">
<input name="checkboxes-error-inline-1" id="checkboxes-error-inline-1" type="checkbox" aria-describedby="checkboxes-error-inline-1-messages">
<label class="fr-label" for="checkboxes-error-inline-1">
Libellé checkbox
</label>
<div class="fr-messages-group" id="checkboxes-error-inline-1-messages" aria-live="polite">
</div>
</div>
<div class="fr-checkbox-group">
<input name="checkboxes-error-inline-2" id="checkboxes-error-inline-2" type="checkbox" aria-describedby="checkboxes-error-inline-2-messages">
<label class="fr-label" for="checkboxes-error-inline-2">
Libellé checkbox
</label>
<div class="fr-messages-group" id="checkboxes-error-inline-2-messages" aria-live="polite">
</div>
</div>
<div class="fr-checkbox-group">
<input name="checkboxes-error-inline-3" id="checkboxes-error-inline-3" type="checkbox" aria-describedby="checkboxes-error-inline-3-messages">
<label class="fr-label" for="checkboxes-error-inline-3">
Libellé checkbox
</label>
<div class="fr-messages-group" id="checkboxes-error-inline-3-messages" aria-live="polite">
</div>
</div>
</div>
<p id="checkboxes-error-inline-desc-error" class="fr-error-text">
Texte d'erreur obligatoire
</p>
</fieldset>
</div>


### Ensemble de cases à cocher validées, en ligne


Légende pour l'ensemble de champs


Libellé checkbox


Libellé checkbox


Libellé checkbox


Texte de validation


###
Extrait de code


<div class="fr-form-group">
<fieldset class="fr-fieldset fr-fieldset--inline fr-fieldset--valid" aria-labelledby="checkboxes-valid-inline-legend checkboxes-valid-inline-desc-valid" role="group">
<legend class="fr-fieldset__legend fr-text--regular" id='checkboxes-valid-inline-legend'>
Légende pour l'ensemble de champs
</legend>
<div class="fr-fieldset__content">
<div class="fr-checkbox-group">
<input name="checkboxes-valid-inline-1" id="checkboxes-valid-inline-1" type="checkbox" aria-describedby="checkboxes-valid-inline-1-messages">
<label class="fr-label" for="checkboxes-valid-inline-1">
Libellé checkbox
</label>
<div class="fr-messages-group" id="checkboxes-valid-inline-1-messages" aria-live="polite">
</div>
</div>
<div class="fr-checkbox-group">
<input name="checkboxes-valid-inline-2" id="checkboxes-valid-inline-2" type="checkbox" aria-describedby="checkboxes-valid-inline-2-messages">
<label class="fr-label" for="checkboxes-valid-inline-2">
Libellé checkbox
</label>
<div class="fr-messages-group" id="checkboxes-valid-inline-2-messages" aria-live="polite">
</div>
</div>
<div class="fr-checkbox-group">
<input name="checkboxes-valid-inline-3" id="checkboxes-valid-inline-3" type="checkbox" aria-describedby="checkboxes-valid-inline-3-messages">
<label class="fr-label" for="checkboxes-valid-inline-3">
Libellé checkbox
</label>
<div class="fr-messages-group" id="checkboxes-valid-inline-3-messages" aria-live="polite">
</div>
</div>
</div>
<p id="checkboxes-valid-inline-desc-valid" class="fr-valid-text">
Texte de validation
</p>
</fieldset>
</div>


### Ensemble de cases à cocher avec texte d'aide spécifique


Légende pour l'ensemble de champs


Libellé checkbox
Texte de description additionnel


Libellé checkbox
Texte de description additionnel


Libellé checkbox
Texte de description additionnel


###
Extrait de code


<div class="fr-form-group">
<fieldset class="fr-fieldset">
<legend class="fr-fieldset__legend fr-text--regular" id='checkboxes-hint-element-legend'>
Légende pour l'ensemble de champs
</legend>
<div class="fr-fieldset__content">
<div class="fr-checkbox-group">
<input name="checkboxes-hint-element-1" id="checkboxes-hint-element-1" type="checkbox" aria-describedby="checkboxes-hint-element-1-messages">
<label class="fr-label" for="checkboxes-hint-element-1">
Libellé checkbox
<span class="fr-hint-text">Texte de description additionnel</span>
</label>
<div class="fr-messages-group" id="checkboxes-hint-element-1-messages" aria-live="polite">
</div>
</div>
<div class="fr-checkbox-group">
<input name="checkboxes-hint-element-2" id="checkboxes-hint-element-2" type="checkbox" aria-describedby="checkboxes-hint-element-2-messages">
<label class="fr-label" for="checkboxes-hint-element-2">
Libellé checkbox
<span class="fr-hint-text">Texte de description additionnel</span>
</label>
<div class="fr-messages-group" id="checkboxes-hint-element-2-messages" aria-live="polite">
</div>
</div>
<div class="fr-checkbox-group">
<input name="checkboxes-hint-element-3" id="checkboxes-hint-element-3" type="checkbox" aria-describedby="checkboxes-hint-element-3-messages">
<label class="fr-label" for="checkboxes-hint-element-3">
Libellé checkbox
<span class="fr-hint-text">Texte de description additionnel</span>
</label>
<div class="fr-messages-group" id="checkboxes-hint-element-3-messages" aria-live="polite">
</div>
</div>
</div>
</fieldset>
</div>


### Ensemble de cases à cocher avec texte d'aide spécifique, petite taille


Légende pour l'ensemble de champs


Libellé checkbox
Texte de description additionnel


Libellé checkbox
Texte de description additionnel


Libellé checkbox
Texte de description additionnel


###
Extrait de code


<div class="fr-form-group">
<fieldset class="fr-fieldset">
<legend class="fr-fieldset__legend fr-text--regular" id='checkboxes-hint-el-sm-legend'>
Légende pour l'ensemble de champs
</legend>
<div class="fr-fieldset__content">
<div class="fr-checkbox-group fr-checkbox-group--sm">
<input name="checkboxes-hint-el-sm-1" id="checkboxes-hint-el-sm-1" type="checkbox" aria-describedby="checkboxes-hint-el-sm-1-messages">
<label class="fr-label" for="checkboxes-hint-el-sm-1">
Libellé checkbox
<span class="fr-hint-text">Texte de description additionnel</span>
</label>
<div class="fr-messages-group" id="checkboxes-hint-el-sm-1-messages" aria-live="polite">
</div>
</div>
<div class="fr-checkbox-group fr-checkbox-group--sm">
<input name="checkboxes-hint-el-sm-2" id="checkboxes-hint-el-sm-2" type="checkbox" aria-describedby="checkboxes-hint-el-sm-2-messages">
<label class="fr-label" for="checkboxes-hint-el-sm-2">
Libellé checkbox
<span class="fr-hint-text">Texte de description additionnel</span>
</label>
<div class="fr-messages-group" id="checkboxes-hint-el-sm-2-messages" aria-live="polite">
</div>
</div>
<div class="fr-checkbox-group fr-checkbox-group--sm">
<input name="checkboxes-hint-el-sm-3" id="checkboxes-hint-el-sm-3" type="checkbox" aria-describedby="checkboxes-hint-el-sm-3-messages">
<label class="fr-label" for="checkboxes-hint-el-sm-3">
Libellé checkbox
<span class="fr-hint-text">Texte de description additionnel</span>
</label>
<div class="fr-messages-group" id="checkboxes-hint-el-sm-3-messages" aria-live="polite">
</div>
</div>
</div>
</fieldset>
</div>


Libellé bouton


Fermer


##
Paramètres d'affichage


Choisissez un thème pour personnaliser l'apparence du site.


Thème clair


Thème sombre


Système
Utilise les paramètres système
