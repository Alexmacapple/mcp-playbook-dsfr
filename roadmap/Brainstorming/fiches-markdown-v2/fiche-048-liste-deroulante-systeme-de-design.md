URL:
https://main--ds-gouv.netlify.app/example/component/select

Title:
Liste déroulante - Système de design

Markdown:

Liste déroulante - Système de design


DSFR v1.14.0


[Retour](../)


# Liste déroulante (select)


La liste déroulante permet à un utilisateur de choisir un élément dans une liste donnée.
[Documentation](https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/liste-deroulante)


### Liste déroulante par défaut


Libellé pour liste déroulante


Sélectionner une option
Option 1
Option 2
Option 3
Option 4


###
Extrait de code


<div class="fr-select-group">
<label class="fr-label" for="select">
Libellé pour liste déroulante
</label>
<select class="fr-select" aria-describedby="select-messages" id="select" name="select">
<option value="" selected disabled>Sélectionner une option</option>
<option value="1">Option 1</option>
<option value="2">Option 2</option>
<option value="3">Option 3</option>
<option value="4">Option 4</option>
</select>
<div class="fr-messages-group" id="select-messages" aria-live="polite">
</div>
</div>


### Liste déroulante désactivée


Libellé pour liste déroulante


Sélectionner une option
Option 1
Option 2
Option 3
Option 4


###
Extrait de code


<div class="fr-select-group fr-select-group--disabled">
<label class="fr-label" for="select-disabled">
Libellé pour liste déroulante
</label>
<select class="fr-select" aria-describedby="select-disabled-messages" disabled id="select-disabled" name="select-disabled">
<option value="" selected disabled>Sélectionner une option</option>
<option value="1">Option 1</option>
<option value="2">Option 2</option>
<option value="3">Option 3</option>
<option value="4">Option 4</option>
</select>
<div class="fr-messages-group" id="select-disabled-messages" aria-live="polite">
</div>
</div>


### Liste déroulante avec texte de description


Libellé pour liste déroulante
Texte de description additionnel


Sélectionner une option
Option 1
Option 2
Option 3
Option 4


###
Extrait de code


<div class="fr-select-group">
<label class="fr-label" for="select-hint">
Libellé pour liste déroulante
<span class="fr-hint-text">Texte de description additionnel</span>
</label>
<select class="fr-select" aria-describedby="select-hint-messages" id="select-hint" name="select-hint">
<option value="" selected disabled>Sélectionner une option</option>
<option value="1">Option 1</option>
<option value="2">Option 2</option>
<option value="3">Option 3</option>
<option value="4">Option 4</option>
</select>
<div class="fr-messages-group" id="select-hint-messages" aria-live="polite">
</div>
</div>


### Liste déroulante valide


Libellé pour liste déroulante


Sélectionner une option
Option 1
Option 2
Option 3
Option 4


Texte de validation


###
Extrait de code


<div class="fr-select-group fr-select-group--valid">
<label class="fr-label" for="select-valid">
Libellé pour liste déroulante
</label>
<select class="fr-select" aria-describedby="select-valid-messages" id="select-valid" name="select-valid">
<option value="" selected disabled>Sélectionner une option</option>
<option value="1">Option 1</option>
<option value="2">Option 2</option>
<option value="3">Option 3</option>
<option value="4">Option 4</option>
</select>
<div class="fr-messages-group" id="select-valid-messages" aria-live="polite">
<p class="fr-message fr-message--valid" id="select-valid-message-valid">Texte de validation</p>
</div>
</div>


### Liste déroulante erreur


Libellé pour liste déroulante


Sélectionner une option
Option 1
Option 2
Option 3
Option 4


Texte d'erreur obligatoire


###
Extrait de code


<div class="fr-select-group fr-select-group--error">
<label class="fr-label" for="select-error">
Libellé pour liste déroulante
</label>
<select class="fr-select" aria-describedby="select-error-messages" id="select-error" name="select-error">
<option value="" selected disabled>Sélectionner une option</option>
<option value="1">Option 1</option>
<option value="2">Option 2</option>
<option value="3">Option 3</option>
<option value="4">Option 4</option>
</select>
<div class="fr-messages-group" id="select-error-messages" aria-live="polite">
<p class="fr-message fr-message--error" id="select-error-message-error">Texte d'erreur obligatoire</p>
</div>
</div>


### Liste déroulante avec groupe d'options


Libellé pour liste déroulante


Selectionnez une option

Option 1
Option 2
Option 3
Option 4


Option 5
Option 6
Option 7


###
Extrait de code


<div class="fr-select-group">
<label class="fr-label" for="select-group">
Libellé pour liste déroulante
</label>
<select class="fr-select" aria-describedby="select-group-messages" id="select-group" name="select-group">
<option value="" selected disabled>Selectionnez une option</option>
<optgroup label="Groupe 1">
<option value="1">Option 1</option>
<option value="2">Option 2</option>
<option value="3">Option 3</option>
<option value="4">Option 4</option>
</optgroup>
<optgroup label="Groupe 2">
<option value="5">Option 5</option>
<option value="6">Option 6</option>
<option value="7">Option 7</option>
</optgroup>
</select>
<div class="fr-messages-group" id="select-group-messages" aria-live="polite">
</div>
</div>


### Autres versions


-
[version dépréciée](deprecated)


Libellé bouton


Fermer


##
Paramètres d'affichage


Choisissez un thème pour personnaliser l'apparence du site.


Thème clair


Thème sombre


Système
Utilise les paramètres système
