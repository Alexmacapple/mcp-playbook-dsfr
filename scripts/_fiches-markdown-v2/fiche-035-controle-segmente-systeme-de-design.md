URL:
https://main--ds-gouv.netlify.app/example/component/segmented

Title:
Contrôle segmenté - Système de design

Markdown:

Contrôle segmenté - Système de design


DSFR v1.14.0


[Retour](../)


# Contrôle segmenté (segmented)


Le composant "contrôle segmenté" incite l'utilisateur à choisir entre plusieurs options d'affichage disponibles (vues), mutuellement exclusives avec une valeur sélectionnée par défaut.
[Documentation](https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/controle-segmente)


### Contrôle segmenté simple


Légende


Libellé


Libellé


Libellé


###
Extrait de code


<fieldset class="fr-segmented">
<legend class="fr-segmented__legend">
Légende
</legend>
<div class="fr-segmented__elements">
<div class="fr-segmented__element">
<input value="1" type="radio" id="segmented-1753-1" name="segmented-1753">
<label class="fr-label" for="segmented-1753-1">
Libellé
</label>
</div>
<div class="fr-segmented__element">
<input value="2" checked type="radio" id="segmented-1753-2" name="segmented-1753">
<label class="fr-label" for="segmented-1753-2">
Libellé
</label>
</div>
<div class="fr-segmented__element">
<input value="3" type="radio" id="segmented-1753-3" name="segmented-1753">
<label class="fr-label" for="segmented-1753-3">
Libellé
</label>
</div>
</div>
</fieldset>


### Contrôle segmenté taille SM


Légende


Libellé


Libellé


Libellé


###
Extrait de code


<fieldset class="fr-segmented fr-segmented--sm">
<legend class="fr-segmented__legend">
Légende
</legend>
<div class="fr-segmented__elements">
<div class="fr-segmented__element">
<input value="1" type="radio" id="segmented-1756-1" name="segmented-1756">
<label class="fr-label" for="segmented-1756-1">
Libellé
</label>
</div>
<div class="fr-segmented__element">
<input value="2" checked type="radio" id="segmented-1756-2" name="segmented-1756">
<label class="fr-label" for="segmented-1756-2">
Libellé
</label>
</div>
<div class="fr-segmented__element">
<input value="3" type="radio" id="segmented-1756-3" name="segmented-1756">
<label class="fr-label" for="segmented-1756-3">
Libellé
</label>
</div>
</div>
</fieldset>


### Contrôle segmenté avec légende en ligne


Légende


Libellé


Libellé


Libellé


###
Extrait de code


<fieldset class="fr-segmented">
<legend class="fr-segmented__legend fr-segmented__legend--inline">
Légende
</legend>
<div class="fr-segmented__elements">
<div class="fr-segmented__element">
<input value="1" type="radio" id="segmented-1759-1" name="segmented-1759">
<label class="fr-label" for="segmented-1759-1">
Libellé
</label>
</div>
<div class="fr-segmented__element">
<input value="2" checked type="radio" id="segmented-1759-2" name="segmented-1759">
<label class="fr-label" for="segmented-1759-2">
Libellé
</label>
</div>
<div class="fr-segmented__element">
<input value="3" type="radio" id="segmented-1759-3" name="segmented-1759">
<label class="fr-label" for="segmented-1759-3">
Libellé
</label>
</div>
</div>
</fieldset>


### Contrôle segmenté avec texte d'aide


Légende
texte additionel


Libellé


Libellé


Libellé


###
Extrait de code


<fieldset class="fr-segmented">
<legend class="fr-segmented__legend">
Légende
<span class="fr-hint-text">texte additionel</span>
</legend>
<div class="fr-segmented__elements">
<div class="fr-segmented__element">
<input value="1" type="radio" id="segmented-1762-1" name="segmented-1762">
<label class="fr-label" for="segmented-1762-1">
Libellé
</label>
</div>
<div class="fr-segmented__element">
<input value="2" checked type="radio" id="segmented-1762-2" name="segmented-1762">
<label class="fr-label" for="segmented-1762-2">
Libellé
</label>
</div>
<div class="fr-segmented__element">
<input value="3" type="radio" id="segmented-1762-3" name="segmented-1762">
<label class="fr-label" for="segmented-1762-3">
Libellé
</label>
</div>
</div>
</fieldset>


### Contrôle segmenté avec icônes


Légende


Libellé


Libellé


Libellé


###
Extrait de code


<fieldset class="fr-segmented">
<legend class="fr-segmented__legend">
Légende
</legend>
<div class="fr-segmented__elements">
<div class="fr-segmented__element">
<input value="1" type="radio" id="segmented-1765-1" name="segmented-1765">
<label class="fr-icon-road-map-line fr-label" for="segmented-1765-1">
Libellé
</label>
</div>
<div class="fr-segmented__element">
<input value="2" checked type="radio" id="segmented-1765-2" name="segmented-1765">
<label class="fr-icon-road-map-line fr-label" for="segmented-1765-2">
Libellé
</label>
</div>
<div class="fr-segmented__element">
<input value="3" type="radio" id="segmented-1765-3" name="segmented-1765">
<label class="fr-icon-road-map-line fr-label" for="segmented-1765-3">
Libellé
</label>
</div>
</div>
</fieldset>


### Contrôle segmenté sans légende


Légende


Libellé


Libellé


Libellé


###
Extrait de code


<fieldset class="fr-segmented fr-segmented--no-legend">
<legend class="fr-segmented__legend">
Légende
</legend>
<div class="fr-segmented__elements">
<div class="fr-segmented__element">
<input value="1" type="radio" id="segmented-1768-1" name="segmented-1768">
<label class="fr-label" for="segmented-1768-1">
Libellé
</label>
</div>
<div class="fr-segmented__element">
<input value="2" checked type="radio" id="segmented-1768-2" name="segmented-1768">
<label class="fr-label" for="segmented-1768-2">
Libellé
</label>
</div>
<div class="fr-segmented__element">
<input value="3" type="radio" id="segmented-1768-3" name="segmented-1768">
<label class="fr-label" for="segmented-1768-3">
Libellé
</label>
</div>
</div>
</fieldset>


### Contrôle segmenté désactivé


Légende


Libellé


Libellé


Libellé


###
Extrait de code


<fieldset class="fr-segmented">
<legend class="fr-segmented__legend">
Légende
</legend>
<div class="fr-segmented__elements">
<div class="fr-segmented__element">
<input value="1" type="radio" id="segmented-1771-1" name="segmented-1771">
<label class="fr-label" for="segmented-1771-1">
Libellé
</label>
</div>
<div class="fr-segmented__element">
<input value="2" checked type="radio" id="segmented-1771-2" name="segmented-1771">
<label class="fr-label" for="segmented-1771-2">
Libellé
</label>
</div>
<div class="fr-segmented__element">
<input value="3" disabled type="radio" id="segmented-1771-3" name="segmented-1771">
<label class="fr-label" for="segmented-1771-3">
Libellé
</label>
</div>
</div>
</fieldset>


## Contrôle segmenté cas maximum (non recommandé)


Lorsque la largeur du contrôle segmenté dépasse celle de son conteneur, la légende ne reste pas sur la même ligne. Si cela ne rentre toujours pas, les boutons passent en vertical. Réduisez la fenêtre pour voir le comportement de ce script.


Légende


Libellé long


Libellé trop long


Libellé


Libellé


Libellé


###
Extrait de code


<fieldset class="fr-segmented" id="segmented-max">
<legend class="fr-segmented__legend fr-segmented__legend--inline">
Légende
</legend>
<div class="fr-segmented__elements">
<div class="fr-segmented__element">
<input value="1" type="radio" id="segmented-max-1" name="segmented-max">
<label class="fr-icon-star-line fr-label" for="segmented-max-1">
Libellé long
</label>
</div>
<div class="fr-segmented__element">
<input value="2" checked type="radio" id="segmented-max-2" name="segmented-max">
<label class="fr-icon-time-line fr-label" for="segmented-max-2">
Libellé trop long
</label>
</div>
<div class="fr-segmented__element">
<input value="3" type="radio" id="segmented-max-3" name="segmented-max">
<label class="fr-icon-road-map-line fr-label" for="segmented-max-3">
Libellé
</label>
</div>
<div class="fr-segmented__element">
<input value="4" type="radio" id="segmented-max-4" name="segmented-max">
<label class="fr-icon-road-map-line fr-label" for="segmented-max-4">
Libellé
</label>
</div>
<div class="fr-segmented__element">
<input value="5" type="radio" id="segmented-max-5" name="segmented-max">
<label class="fr-icon-road-map-line fr-label" for="segmented-max-5">
Libellé
</label>
</div>
<div class="fr-segmented__element">
<input value="6" type="radio" id="segmented-max-6" name="segmented-max">
<label class="fr-icon-road-map-line fr-label" for="segmented-max-6">
Libellé
</label>
</div>
<div class="fr-segmented__element">
<input value="7" type="radio" id="segmented-max-7" name="segmented-max">
<label class="fr-icon-road-map-line fr-label" for="segmented-max-7">
Libellé
</label>
</div>
<div class="fr-segmented__element">
<input value="8" type="radio" id="segmented-max-8" name="segmented-max">
<label class="fr-icon-road-map-line fr-label" for="segmented-max-8">
Libellé
</label>
</div>
</div>
</fieldset>


Libellé bouton


Fermer


##
Paramètres d'affichage


Choisissez un thème pour personnaliser l'apparence du site.


Thème clair


Thème sombre


Système
Utilise les paramètres système
