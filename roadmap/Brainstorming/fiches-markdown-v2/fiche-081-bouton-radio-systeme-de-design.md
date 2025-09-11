URL:
https://main--ds-gouv.netlify.app/example/component/radio/deprecated

Title:
Bouton radio - Système de design

Markdown:

Bouton radio - Système de design


DSFR v1.14.0


[Retour](../)


# Bouton radio (radio)


Le bouton radio permettent à l'utilisateur de sélectionner une seule option dans une liste.

##### Documentation


-
[Bouton radio](https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/bouton-radio)


-
[Bouton radio riche](https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/bouton-radio-riche)


## Dépréciation


Les exemples suivants sont dépréciés, ne pas utiliser comme référence

Pour support des versions précédentes


## Bouton radio simple


### Ensemble de boutons radio


Légende pour l'ensemble de champs


Libellé radio


Libellé radio


Libellé radio


###
Extrait de code


<div class="fr-form-group">
<fieldset class="fr-fieldset">
<legend class="fr-fieldset__legend fr-text--regular" id='radio-legend'>
Légende pour l'ensemble de champs
</legend>
<div class="fr-fieldset__content">
<div class="fr-radio-group">
<input type="radio" id="radio-1" name="radio">
<label class="fr-label" for="radio-1">
Libellé radio
</label>
</div>
<div class="fr-radio-group">
<input checked type="radio" id="radio-2" name="radio">
<label class="fr-label" for="radio-2">
Libellé radio
</label>
</div>
<div class="fr-radio-group">
<input type="radio" id="radio-3" name="radio">
<label class="fr-label" for="radio-3">
Libellé radio
</label>
</div>
</div>
</fieldset>
</div>


### Ensemble de boutons radio, petite taille


Légende pour l'ensemble de champs


Libellé radio


Libellé radio


Libellé radio


###
Extrait de code


<div class="fr-form-group">
<fieldset class="fr-fieldset">
<legend class="fr-fieldset__legend fr-text--regular" id='radio-small-legend'>
Légende pour l'ensemble de champs
</legend>
<div class="fr-fieldset__content">
<div class="fr-radio-group fr-radio-group--sm">
<input type="radio" id="radio-small-1" name="radio-small">
<label class="fr-label" for="radio-small-1">
Libellé radio
</label>
</div>
<div class="fr-radio-group fr-radio-group--sm">
<input checked type="radio" id="radio-small-2" name="radio-small">
<label class="fr-label" for="radio-small-2">
Libellé radio
</label>
</div>
<div class="fr-radio-group fr-radio-group--sm">
<input type="radio" id="radio-small-3" name="radio-small">
<label class="fr-label" for="radio-small-3">
Libellé radio
</label>
</div>
</div>
</fieldset>
</div>


### Ensemble de boutons radio désactivées


Légende pour l'ensemble de champs


Libellé radio


Libellé radio


Libellé radio


###
Extrait de code


<div class="fr-form-group">
<fieldset class="fr-fieldset">
<legend class="fr-fieldset__legend fr-text--regular" id='radio-disabled-legend'>
Légende pour l'ensemble de champs
</legend>
<div class="fr-fieldset__content">
<div class="fr-radio-group">
<input disabled type="radio" id="radio-disabled-1" name="radio-disabled">
<label class="fr-label" for="radio-disabled-1">
Libellé radio
</label>
</div>
<div class="fr-radio-group">
<input disabled checked type="radio" id="radio-disabled-2" name="radio-disabled">
<label class="fr-label" for="radio-disabled-2">
Libellé radio
</label>
</div>
<div class="fr-radio-group">
<input disabled type="radio" id="radio-disabled-3" name="radio-disabled">
<label class="fr-label" for="radio-disabled-3">
Libellé radio
</label>
</div>
</div>
</fieldset>
</div>


### Ensemble de boutons radio en ligne


Légende pour l'ensemble de champs


Libellé radio


Libellé radio


Libellé radio


###
Extrait de code


<div class="fr-form-group">
<fieldset class="fr-fieldset fr-fieldset--inline">
<legend class="fr-fieldset__legend fr-text--regular" id='radio-inline-legend'>
Légende pour l'ensemble de champs
</legend>
<div class="fr-fieldset__content">
<div class="fr-radio-group">
<input type="radio" id="radio-inline-1" name="radio-inline">
<label class="fr-label" for="radio-inline-1">
Libellé radio
</label>
</div>
<div class="fr-radio-group">
<input type="radio" id="radio-inline-2" name="radio-inline">
<label class="fr-label" for="radio-inline-2">
Libellé radio
</label>
</div>
<div class="fr-radio-group">
<input type="radio" id="radio-inline-3" name="radio-inline">
<label class="fr-label" for="radio-inline-3">
Libellé radio
</label>
</div>
</div>
</fieldset>
</div>


### Ensemble de boutons radio avec texte d'aide


Légende pour l'ensemble de champs


Libellé radio
Texte de description additionnel


Libellé radio
Texte de description additionnel


Libellé radio
Texte de description additionnel


###
Extrait de code


<div class="fr-form-group">
<fieldset class="fr-fieldset">
<legend class="fr-fieldset__legend fr-text--regular" id='radio-hint-legend'>
Légende pour l'ensemble de champs
</legend>
<div class="fr-fieldset__content">
<div class="fr-radio-group">
<input type="radio" id="radio-hint-1" name="radio-hint">
<label class="fr-label" for="radio-hint-1">
Libellé radio
<span class="fr-hint-text">Texte de description additionnel</span>
</label>
</div>
<div class="fr-radio-group">
<input type="radio" id="radio-hint-2" name="radio-hint">
<label class="fr-label" for="radio-hint-2">
Libellé radio
<span class="fr-hint-text">Texte de description additionnel</span>
</label>
</div>
<div class="fr-radio-group">
<input type="radio" id="radio-hint-3" name="radio-hint">
<label class="fr-label" for="radio-hint-3">
Libellé radio
<span class="fr-hint-text">Texte de description additionnel</span>
</label>
</div>
</div>
</fieldset>
</div>


### Ensemble de boutons radio avec erreur


Légende pour l'ensemble de champs


Libellé radio


Libellé radio


Libellé radio


Texte d'erreur obligatoire


###
Extrait de code


<div class="fr-form-group">
<fieldset class="fr-fieldset fr-fieldset--error" aria-labelledby="radio-error-legend radio-error-desc-error" role="group">
<legend class="fr-fieldset__legend fr-text--regular" id='radio-error-legend'>
Légende pour l'ensemble de champs
</legend>
<div class="fr-fieldset__content">
<div class="fr-radio-group">
<input type="radio" id="radio-error-1" name="radio-error">
<label class="fr-label" for="radio-error-1">
Libellé radio
</label>
</div>
<div class="fr-radio-group">
<input type="radio" id="radio-error-2" name="radio-error">
<label class="fr-label" for="radio-error-2">
Libellé radio
</label>
</div>
<div class="fr-radio-group">
<input type="radio" id="radio-error-3" name="radio-error">
<label class="fr-label" for="radio-error-3">
Libellé radio
</label>
</div>
</div>
<p id="radio-error-desc-error" class="fr-error-text">
Texte d'erreur obligatoire
</p>
</fieldset>
</div>


### Ensemble de boutons radio avec erreur, en ligne


Légende pour l'ensemble de champs


Libellé radio


Libellé radio


Libellé radio


Texte d'erreur obligatoire


###
Extrait de code


<div class="fr-form-group">
<fieldset class="fr-fieldset fr-fieldset--inline fr-fieldset--error" aria-labelledby="radio-error-inline-legend radio-error-inline-desc-error" role="group">
<legend class="fr-fieldset__legend fr-text--regular" id='radio-error-inline-legend'>
Légende pour l'ensemble de champs
</legend>
<div class="fr-fieldset__content">
<div class="fr-radio-group">
<input type="radio" id="radio-error-inline-1" name="radio-error-inline">
<label class="fr-label" for="radio-error-inline-1">
Libellé radio
</label>
</div>
<div class="fr-radio-group">
<input type="radio" id="radio-error-inline-2" name="radio-error-inline">
<label class="fr-label" for="radio-error-inline-2">
Libellé radio
</label>
</div>
<div class="fr-radio-group">
<input type="radio" id="radio-error-inline-3" name="radio-error-inline">
<label class="fr-label" for="radio-error-inline-3">
Libellé radio
</label>
</div>
</div>
<p id="radio-error-inline-desc-error" class="fr-error-text">
Texte d'erreur obligatoire
</p>
</fieldset>
</div>


### Ensemble de boutons radio validés


Légende pour l'ensemble de champs


Libellé radio


Libellé radio


Libellé radio


Texte de validation


###
Extrait de code


<div class="fr-form-group">
<fieldset class="fr-fieldset fr-fieldset--valid" aria-labelledby="radio-valid-legend radio-valid-desc-valid" role="group">
<legend class="fr-fieldset__legend fr-text--regular" id='radio-valid-legend'>
Légende pour l'ensemble de champs
</legend>
<div class="fr-fieldset__content">
<div class="fr-radio-group">
<input type="radio" id="radio-valid-1" name="radio-valid">
<label class="fr-label" for="radio-valid-1">
Libellé radio
</label>
</div>
<div class="fr-radio-group">
<input type="radio" id="radio-valid-2" name="radio-valid">
<label class="fr-label" for="radio-valid-2">
Libellé radio
</label>
</div>
<div class="fr-radio-group">
<input type="radio" id="radio-valid-3" name="radio-valid">
<label class="fr-label" for="radio-valid-3">
Libellé radio
</label>
</div>
</div>
<p id="radio-valid-desc-valid" class="fr-valid-text">
Texte de validation
</p>
</fieldset>
</div>


### Ensemble de boutons radio validés, en ligne


Légende pour l'ensemble de champs


Libellé radio


Libellé radio


Libellé radio


Texte de validation


###
Extrait de code


<div class="fr-form-group">
<fieldset class="fr-fieldset fr-fieldset--inline fr-fieldset--valid" aria-labelledby="radio-valid-inline-legend radio-valid-inline-desc-valid" role="group">
<legend class="fr-fieldset__legend fr-text--regular" id='radio-valid-inline-legend'>
Légende pour l'ensemble de champs
</legend>
<div class="fr-fieldset__content">
<div class="fr-radio-group">
<input type="radio" id="radio-valid-inline-1" name="radio-valid-inline">
<label class="fr-label" for="radio-valid-inline-1">
Libellé radio
</label>
</div>
<div class="fr-radio-group">
<input type="radio" id="radio-valid-inline-2" name="radio-valid-inline">
<label class="fr-label" for="radio-valid-inline-2">
Libellé radio
</label>
</div>
<div class="fr-radio-group">
<input type="radio" id="radio-valid-inline-3" name="radio-valid-inline">
<label class="fr-label" for="radio-valid-inline-3">
Libellé radio
</label>
</div>
</div>
<p id="radio-valid-inline-desc-valid" class="fr-valid-text">
Texte de validation
</p>
</fieldset>
</div>


### Ensemble de boutons radio avec texte d'aide spécifique


Légende pour l'ensemble de champs


Libellé radio
Texte de description additionnel


Libellé radio
Texte de description additionnel


Libellé radio
Texte de description additionnel


###
Extrait de code


<div class="fr-form-group">
<fieldset class="fr-fieldset">
<legend class="fr-fieldset__legend fr-text--regular" id='radio-hint-element-legend'>
Légende pour l'ensemble de champs
</legend>
<div class="fr-fieldset__content">
<div class="fr-radio-group">
<input type="radio" id="radio-hint-element-1" name="radio-hint-element">
<label class="fr-label" for="radio-hint-element-1">
Libellé radio
<span class="fr-hint-text">Texte de description additionnel</span>
</label>
</div>
<div class="fr-radio-group">
<input type="radio" id="radio-hint-element-2" name="radio-hint-element">
<label class="fr-label" for="radio-hint-element-2">
Libellé radio
<span class="fr-hint-text">Texte de description additionnel</span>
</label>
</div>
<div class="fr-radio-group">
<input type="radio" id="radio-hint-element-3" name="radio-hint-element">
<label class="fr-label" for="radio-hint-element-3">
Libellé radio
<span class="fr-hint-text">Texte de description additionnel</span>
</label>
</div>
</div>
</fieldset>
</div>


### Ensemble de boutons radio avec texte d'aide spécifique, petite taille


Légende pour l'ensemble de champs


Libellé radio
Texte de description additionnel


Libellé radio
Texte de description additionnel


Libellé radio
Texte de description additionnel


###
Extrait de code


<div class="fr-form-group">
<fieldset class="fr-fieldset">
<legend class="fr-fieldset__legend fr-text--regular" id='radio-hint-el-sm-legend'>
Légende pour l'ensemble de champs
</legend>
<div class="fr-fieldset__content">
<div class="fr-radio-group fr-radio-group--sm">
<input type="radio" id="radio-hint-el-sm-1" name="radio-hint-el-sm">
<label class="fr-label" for="radio-hint-el-sm-1">
Libellé radio
<span class="fr-hint-text">Texte de description additionnel</span>
</label>
</div>
<div class="fr-radio-group fr-radio-group--sm">
<input type="radio" id="radio-hint-el-sm-2" name="radio-hint-el-sm">
<label class="fr-label" for="radio-hint-el-sm-2">
Libellé radio
<span class="fr-hint-text">Texte de description additionnel</span>
</label>
</div>
<div class="fr-radio-group fr-radio-group--sm">
<input type="radio" id="radio-hint-el-sm-3" name="radio-hint-el-sm">
<label class="fr-label" for="radio-hint-el-sm-3">
Libellé radio
<span class="fr-hint-text">Texte de description additionnel</span>
</label>
</div>
</div>
</fieldset>
</div>


### Ensemble de boutons radio, libellé en indice et exposant


Légende pour l'ensemble de champs


Libellé radio sup
sub


Libellé radio sup
sub


Libellé radio sup
sub


###
Extrait de code


<div class="fr-form-group">
<fieldset class="fr-fieldset">
<legend class="fr-fieldset__legend fr-text--regular" id='radio-sub-legend'>
Légende pour l'ensemble de champs
</legend>
<div class="fr-fieldset__content">
<div class="fr-radio-group">
<input type="radio" id="radio-sub-1" name="radio-sub">
<label class="fr-label" for="radio-sub-1">
<span>Libellé radio <sup>sup</sup>
<sub>sub</sub>
</span>
</label>
</div>
<div class="fr-radio-group">
<input type="radio" id="radio-sub-2" name="radio-sub">
<label class="fr-label" for="radio-sub-2">
<span>Libellé radio <sup>sup</sup>
<sub>sub</sub>
</span>
</label>
</div>
<div class="fr-radio-group">
<input type="radio" id="radio-sub-3" name="radio-sub">
<label class="fr-label" for="radio-sub-3">
<span>Libellé radio <sup>sup</sup>
<sub>sub</sub>
</span>
</label>
</div>
</div>
</fieldset>
</div>


## Bouton radio riche


### Ensemble de boutons radio riches, simple


Légende pour l'ensemble de champs


Libellé radio


Libellé radio


Libellé radio


###
Extrait de code


<div class="fr-form-group">
<fieldset class="fr-fieldset">
<legend class="fr-fieldset__legend fr-text--regular" id='radio-rich-legend'>
Légende pour l'ensemble de champs
</legend>
<div class="fr-fieldset__content">
<div class="fr-radio-group fr-radio-rich">
<input type="radio" id="radio-rich-1" name="radio-rich">
<label class="fr-label" for="radio-rich-1">
Libellé radio
</label>
<div class="fr-radio-rich__img">
<svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
<use class="fr-artwork-decorative" href="../../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
<use class="fr-artwork-minor" href="../../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
<use class="fr-artwork-major" href="../../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
</svg>
</div>
</div>
<div class="fr-radio-group fr-radio-rich">
<input checked type="radio" id="radio-rich-2" name="radio-rich">
<label class="fr-label" for="radio-rich-2">
Libellé radio
</label>
<div class="fr-radio-rich__img">
<svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
<use class="fr-artwork-decorative" href="../../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
<use class="fr-artwork-minor" href="../../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
<use class="fr-artwork-major" href="../../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
</svg>
</div>
</div>
<div class="fr-radio-group fr-radio-rich">
<input type="radio" id="radio-rich-3" name="radio-rich">
<label class="fr-label" for="radio-rich-3">
Libellé radio
</label>
<div class="fr-radio-rich__img">
<svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
<use class="fr-artwork-decorative" href="../../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
<use class="fr-artwork-minor" href="../../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
<use class="fr-artwork-major" href="../../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
</svg>
</div>
</div>
</div>
</fieldset>
</div>


### Ensemble de boutons radio riches, en ligne, simple


Légende pour l'ensemble de champs


Libellé radio


Libellé radio


Libellé radio


###
Extrait de code


<div class="fr-form-group">
<fieldset class="fr-fieldset fr-fieldset--inline">
<legend class="fr-fieldset__legend fr-text--regular" id='radio-rich-inline-legend'>
Légende pour l'ensemble de champs
</legend>
<div class="fr-fieldset__content">
<div class="fr-radio-group fr-radio-rich">
<input type="radio" id="radio-rich-inline-1" name="radio-rich-inline">
<label class="fr-label" for="radio-rich-inline-1">
Libellé radio
</label>
<div class="fr-radio-rich__img">
<svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
<use class="fr-artwork-decorative" href="../../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
<use class="fr-artwork-minor" href="../../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
<use class="fr-artwork-major" href="../../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
</svg>
</div>
</div>
<div class="fr-radio-group fr-radio-rich">
<input type="radio" id="radio-rich-inline-2" name="radio-rich-inline">
<label class="fr-label" for="radio-rich-inline-2">
Libellé radio
</label>
<div class="fr-radio-rich__img">
<svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
<use class="fr-artwork-decorative" href="../../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
<use class="fr-artwork-minor" href="../../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
<use class="fr-artwork-major" href="../../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
</svg>
</div>
</div>
<div class="fr-radio-group fr-radio-rich">
<input type="radio" id="radio-rich-inline-3" name="radio-rich-inline">
<label class="fr-label" for="radio-rich-inline-3">
Libellé radio
</label>
<div class="fr-radio-rich__img">
<svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
<use class="fr-artwork-decorative" href="../../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
<use class="fr-artwork-minor" href="../../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
<use class="fr-artwork-major" href="../../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
</svg>
</div>
</div>
</div>
</fieldset>
</div>


### Ensemble de boutons radio riches avec textes d'aide


Légende pour l'ensemble de champs
texte additionel


Libellé radio
Texte de description additionnel


Libellé radio
Texte de description additionnel


Libellé radio
Texte de description additionnel


###
Extrait de code


<div class="fr-form-group">
<fieldset class="fr-fieldset">
<legend class="fr-fieldset__legend fr-text--regular" id='radio-rich-hint-legend'>
Légende pour l'ensemble de champs
<span class="fr-hint-text">texte additionel</span>
</legend>
<div class="fr-fieldset__content">
<div class="fr-radio-group fr-radio-rich">
<input type="radio" id="radio-rich-hint-1" name="radio-rich-hint">
<label class="fr-label" for="radio-rich-hint-1">
Libellé radio
<span class="fr-hint-text">Texte de description additionnel</span>
</label>
<div class="fr-radio-rich__img">
<svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
<use class="fr-artwork-decorative" href="../../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
<use class="fr-artwork-minor" href="../../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
<use class="fr-artwork-major" href="../../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
</svg>
</div>
</div>
<div class="fr-radio-group fr-radio-rich">
<input type="radio" id="radio-rich-hint-2" name="radio-rich-hint">
<label class="fr-label" for="radio-rich-hint-2">
Libellé radio
<span class="fr-hint-text">Texte de description additionnel</span>
</label>
<div class="fr-radio-rich__img">
<svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
<use class="fr-artwork-decorative" href="../../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
<use class="fr-artwork-minor" href="../../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
<use class="fr-artwork-major" href="../../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
</svg>
</div>
</div>
<div class="fr-radio-group fr-radio-rich">
<input type="radio" id="radio-rich-hint-3" name="radio-rich-hint">
<label class="fr-label" for="radio-rich-hint-3">
Libellé radio
<span class="fr-hint-text">Texte de description additionnel</span>
</label>
<div class="fr-radio-rich__img">
<svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
<use class="fr-artwork-decorative" href="../../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
<use class="fr-artwork-minor" href="../../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
<use class="fr-artwork-major" href="../../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
</svg>
</div>
</div>
</div>
</fieldset>
</div>


### Ensemble de boutons radio riches avec textes d'aide, en ligne


Légende pour l'ensemble de champs
texte additionel


Libellé radio
Texte de description additionnel


Libellé radio
Texte de description additionnel


Libellé radio
Texte de description additionnel


###
Extrait de code


<div class="fr-form-group">
<fieldset class="fr-fieldset fr-fieldset--inline">
<legend class="fr-fieldset__legend fr-text--regular" id='radio-rich-hint-inline-legend'>
Légende pour l'ensemble de champs
<span class="fr-hint-text">texte additionel</span>
</legend>
<div class="fr-fieldset__content">
<div class="fr-radio-group fr-radio-rich">
<input type="radio" id="radio-rich-hint-inline-1" name="radio-rich-hint-inline">
<label class="fr-label" for="radio-rich-hint-inline-1">
Libellé radio
<span class="fr-hint-text">Texte de description additionnel</span>
</label>
<div class="fr-radio-rich__img">
<svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
<use class="fr-artwork-decorative" href="../../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
<use class="fr-artwork-minor" href="../../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
<use class="fr-artwork-major" href="../../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
</svg>
</div>
</div>
<div class="fr-radio-group fr-radio-rich">
<input type="radio" id="radio-rich-hint-inline-2" name="radio-rich-hint-inline">
<label class="fr-label" for="radio-rich-hint-inline-2">
Libellé radio
<span class="fr-hint-text">Texte de description additionnel</span>
</label>
<div class="fr-radio-rich__img">
<svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
<use class="fr-artwork-decorative" href="../../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
<use class="fr-artwork-minor" href="../../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
<use class="fr-artwork-major" href="../../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
</svg>
</div>
</div>
<div class="fr-radio-group fr-radio-rich">
<input type="radio" id="radio-rich-hint-inline-3" name="radio-rich-hint-inline">
<label class="fr-label" for="radio-rich-hint-inline-3">
Libellé radio
<span class="fr-hint-text">Texte de description additionnel</span>
</label>
<div class="fr-radio-rich__img">
<svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
<use class="fr-artwork-decorative" href="../../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
<use class="fr-artwork-minor" href="../../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
<use class="fr-artwork-major" href="../../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
</svg>
</div>
</div>
</div>
</fieldset>
</div>


### Ensemble de boutons radio riches avec erreur et textes d'aide


Légende pour l'ensemble de champs
texte additionel


Libellé radio
Texte de description additionnel


Libellé radio
Texte de description additionnel


Libellé radio
Texte de description additionnel


Texte d'erreur obligatoire


###
Extrait de code


<div class="fr-form-group">
<fieldset class="fr-fieldset fr-fieldset--error" aria-labelledby="radio-rich-error-legend radio-rich-error-desc-error" role="group">
<legend class="fr-fieldset__legend fr-text--regular" id='radio-rich-error-legend'>
Légende pour l'ensemble de champs
<span class="fr-hint-text">texte additionel</span>
</legend>
<div class="fr-fieldset__content">
<div class="fr-radio-group fr-radio-rich">
<input type="radio" id="radio-rich-error-1" name="radio-rich-error">
<label class="fr-label" for="radio-rich-error-1">
Libellé radio
<span class="fr-hint-text">Texte de description additionnel</span>
</label>
<div class="fr-radio-rich__img">
<svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
<use class="fr-artwork-decorative" href="../../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
<use class="fr-artwork-minor" href="../../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
<use class="fr-artwork-major" href="../../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
</svg>
</div>
</div>
<div class="fr-radio-group fr-radio-rich">
<input type="radio" id="radio-rich-error-2" name="radio-rich-error">
<label class="fr-label" for="radio-rich-error-2">
Libellé radio
<span class="fr-hint-text">Texte de description additionnel</span>
</label>
<div class="fr-radio-rich__img">
<svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
<use class="fr-artwork-decorative" href="../../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
<use class="fr-artwork-minor" href="../../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
<use class="fr-artwork-major" href="../../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
</svg>
</div>
</div>
<div class="fr-radio-group fr-radio-rich">
<input type="radio" id="radio-rich-error-3" name="radio-rich-error">
<label class="fr-label" for="radio-rich-error-3">
Libellé radio
<span class="fr-hint-text">Texte de description additionnel</span>
</label>
<div class="fr-radio-rich__img">
<svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
<use class="fr-artwork-decorative" href="../../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
<use class="fr-artwork-minor" href="../../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
<use class="fr-artwork-major" href="../../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
</svg>
</div>
</div>
</div>
<p id="radio-rich-error-desc-error" class="fr-error-text">
Texte d'erreur obligatoire
</p>
</fieldset>
</div>


### Ensemble de boutons radio riches avec erreur et textes d'aide, en ligne


Légende pour l'ensemble de champs
texte additionel


Libellé radio
Texte de description additionnel


Libellé radio
Texte de description additionnel


Libellé radio
Texte de description additionnel


Texte d'erreur obligatoire


###
Extrait de code


<div class="fr-form-group">
<fieldset class="fr-fieldset fr-fieldset--inline fr-fieldset--error" aria-labelledby="radio-rich-error-inline-legend radio-rich-error-inline-desc-error" role="group">
<legend class="fr-fieldset__legend fr-text--regular" id='radio-rich-error-inline-legend'>
Légende pour l'ensemble de champs
<span class="fr-hint-text">texte additionel</span>
</legend>
<div class="fr-fieldset__content">
<div class="fr-radio-group fr-radio-rich">
<input type="radio" id="radio-rich-error-inline-1" name="radio-rich-error-inline">
<label class="fr-label" for="radio-rich-error-inline-1">
Libellé radio
<span class="fr-hint-text">Texte de description additionnel</span>
</label>
<div class="fr-radio-rich__img">
<svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
<use class="fr-artwork-decorative" href="../../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
<use class="fr-artwork-minor" href="../../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
<use class="fr-artwork-major" href="../../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
</svg>
</div>
</div>
<div class="fr-radio-group fr-radio-rich">
<input type="radio" id="radio-rich-error-inline-2" name="radio-rich-error-inline">
<label class="fr-label" for="radio-rich-error-inline-2">
Libellé radio
<span class="fr-hint-text">Texte de description additionnel</span>
</label>
<div class="fr-radio-rich__img">
<svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
<use class="fr-artwork-decorative" href="../../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
<use class="fr-artwork-minor" href="../../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
<use class="fr-artwork-major" href="../../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
</svg>
</div>
</div>
<div class="fr-radio-group fr-radio-rich">
<input type="radio" id="radio-rich-error-inline-3" name="radio-rich-error-inline">
<label class="fr-label" for="radio-rich-error-inline-3">
Libellé radio
<span class="fr-hint-text">Texte de description additionnel</span>
</label>
<div class="fr-radio-rich__img">
<svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
<use class="fr-artwork-decorative" href="../../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
<use class="fr-artwork-minor" href="../../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
<use class="fr-artwork-major" href="../../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
</svg>
</div>
</div>
</div>
<p id="radio-rich-error-inline-desc-error" class="fr-error-text">
Texte d'erreur obligatoire
</p>
</fieldset>
</div>


### Ensemble de boutons radio riches désactivés


Légende pour l'ensemble de champs


Libellé radio
Texte de description additionnel


Libellé radio
Texte de description additionnel


Libellé radio
Texte de description additionnel


###
Extrait de code


<div class="fr-form-group">
<fieldset class="fr-fieldset">
<legend class="fr-fieldset__legend fr-text--regular" id='radio-rich-disabled-legend'>
Légende pour l'ensemble de champs
</legend>
<div class="fr-fieldset__content">
<div class="fr-radio-group fr-radio-rich">
<input disabled type="radio" id="radio-rich-disabled-1" name="radio-rich-disabled">
<label class="fr-label" for="radio-rich-disabled-1">
Libellé radio
<span class="fr-hint-text">Texte de description additionnel</span>
</label>
<div class="fr-radio-rich__img">
<svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
<use class="fr-artwork-decorative" href="../../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
<use class="fr-artwork-minor" href="../../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
<use class="fr-artwork-major" href="../../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
</svg>
</div>
</div>
<div class="fr-radio-group fr-radio-rich">
<input disabled checked type="radio" id="radio-rich-disabled-2" name="radio-rich-disabled">
<label class="fr-label" for="radio-rich-disabled-2">
Libellé radio
<span class="fr-hint-text">Texte de description additionnel</span>
</label>
<div class="fr-radio-rich__img">
<svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
<use class="fr-artwork-decorative" href="../../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
<use class="fr-artwork-minor" href="../../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
<use class="fr-artwork-major" href="../../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
</svg>
</div>
</div>
<div class="fr-radio-group fr-radio-rich">
<input disabled type="radio" id="radio-rich-disabled-3" name="radio-rich-disabled">
<label class="fr-label" for="radio-rich-disabled-3">
Libellé radio
<span class="fr-hint-text">Texte de description additionnel</span>
</label>
<div class="fr-radio-rich__img">
<svg aria-hidden="true" class="fr-artwork" viewBox="0 0 80 80" width="80px" height="80px">
<use class="fr-artwork-decorative" href="../../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-decorative"></use>
<use class="fr-artwork-minor" href="../../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-minor"></use>
<use class="fr-artwork-major" href="../../../../dist/artwork/pictograms/buildings/city-hall.svg#artwork-major"></use>
</svg>
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
