URL:
https://main--ds-gouv.netlify.app/example/component/form

Title:
Formulaire - Système de design

Markdown:

Formulaire - Système de design


DSFR v1.14.0


[Retour](../)


# Formulaire (form)


Ce package permet de mettre en forme les différents champs d'un formulaire, notamment en ce qui concerne les espacements et texte d'aide et d'erreur.


### Ensemble de champs de saisie


Légende pour l'ensemble des éléments


Libellé champ de saisie


Libellé champ de saisie


Libellé champ de saisie


###
Extrait de code


<fieldset class="fr-fieldset" id="text" aria-labelledby="text-legend text-messages">
<legend class="fr-fieldset__legend" id="text-legend">
Légende pour l'ensemble des éléments
</legend>
<div class="fr-fieldset__element">
<div class="fr-input-group" id="input-group-3733">
<label class="fr-label" for="text-1">
Libellé champ de saisie
</label>
<input class="fr-input" aria-describedby="text-1-messages" name="text-1" id="text-1" type="text">
<div class="fr-messages-group" id="text-1-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-fieldset__element">
<div class="fr-input-group" id="input-group-3734">
<label class="fr-label" for="text-2">
Libellé champ de saisie
</label>
<input class="fr-input" aria-describedby="text-2-messages" name="text-2" id="text-2" type="text">
<div class="fr-messages-group" id="text-2-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-fieldset__element">
<div class="fr-input-group" id="input-group-3735">
<label class="fr-label" for="text-3">
Libellé champ de saisie
</label>
<input class="fr-input" aria-describedby="text-3-messages" name="text-3" id="text-3" type="text">
<div class="fr-messages-group" id="text-3-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-messages-group" id="text-messages" aria-live="polite">
</div>
</fieldset>


### Ensemble de boutons radio


Légende pour l'ensemble des éléments


Libellé bouton radio


Libellé bouton radio


Libellé bouton radio


###
Extrait de code


<fieldset class="fr-fieldset" id="radio" aria-labelledby="radio-legend radio-messages">
<legend class="fr-fieldset__legend--regular fr-fieldset__legend" id="radio-legend">
Légende pour l'ensemble des éléments
</legend>
<div class="fr-fieldset__element">
<div class="fr-radio-group">
<input value="1" type="radio" id="radio-1" name="radio">
<label class="fr-label" for="radio-1">
Libellé bouton radio
</label>
</div>
</div>
<div class="fr-fieldset__element">
<div class="fr-radio-group">
<input value="2" type="radio" id="radio-2" name="radio">
<label class="fr-label" for="radio-2">
Libellé bouton radio
</label>
</div>
</div>
<div class="fr-fieldset__element">
<div class="fr-radio-group">
<input value="3" type="radio" id="radio-3" name="radio">
<label class="fr-label" for="radio-3">
Libellé bouton radio
</label>
</div>
</div>
<div class="fr-messages-group" id="radio-messages" aria-live="polite">
</div>
</fieldset>


### Ensemble de cases à cocher


Légende pour l'ensemble des éléments


Libellé case à cocher


Libellé case à cocher


Libellé case à cocher


###
Extrait de code


<fieldset class="fr-fieldset" id="checkbox" aria-labelledby="checkbox-legend checkbox-messages">
<legend class="fr-fieldset__legend--regular fr-fieldset__legend" id="checkbox-legend">
Légende pour l'ensemble des éléments
</legend>
<div class="fr-fieldset__element">
<div class="fr-checkbox-group">
<input name="checkbox-1" id="checkbox-1" type="checkbox" aria-describedby="checkbox-1-messages">
<label class="fr-label" for="checkbox-1">
Libellé case à cocher
</label>
<div class="fr-messages-group" id="checkbox-1-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-fieldset__element">
<div class="fr-checkbox-group">
<input name="checkbox-2" id="checkbox-2" type="checkbox" aria-describedby="checkbox-2-messages">
<label class="fr-label" for="checkbox-2">
Libellé case à cocher
</label>
<div class="fr-messages-group" id="checkbox-2-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-fieldset__element">
<div class="fr-checkbox-group">
<input name="checkbox-3" id="checkbox-3" type="checkbox" aria-describedby="checkbox-3-messages">
<label class="fr-label" for="checkbox-3">
Libellé case à cocher
</label>
<div class="fr-messages-group" id="checkbox-3-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-messages-group" id="checkbox-messages" aria-live="polite">
</div>
</fieldset>


### Ensemble de boutons radio, en ligne


Légende pour l'ensemble des éléments


Libellé bouton radio


Libellé bouton radio


Libellé bouton radio


###
Extrait de code


<fieldset class="fr-fieldset" id="radio-inline" aria-labelledby="radio-inline-legend radio-inline-messages">
<legend class="fr-fieldset__legend--regular fr-fieldset__legend" id="radio-inline-legend">
Légende pour l'ensemble des éléments
</legend>
<div class="fr-fieldset__element fr-fieldset__element--inline">
<div class="fr-radio-group">
<input value="1" type="radio" id="radio-inline-1" name="radio-inline">
<label class="fr-label" for="radio-inline-1">
Libellé bouton radio
</label>
</div>
</div>
<div class="fr-fieldset__element fr-fieldset__element--inline">
<div class="fr-radio-group">
<input value="2" type="radio" id="radio-inline-2" name="radio-inline">
<label class="fr-label" for="radio-inline-2">
Libellé bouton radio
</label>
</div>
</div>
<div class="fr-fieldset__element fr-fieldset__element--inline">
<div class="fr-radio-group">
<input value="3" type="radio" id="radio-inline-3" name="radio-inline">
<label class="fr-label" for="radio-inline-3">
Libellé bouton radio
</label>
</div>
</div>
<div class="fr-messages-group" id="radio-inline-messages" aria-live="polite">
</div>
</fieldset>


### Ensemble de cases à cocher, en ligne


Légende pour l'ensemble des éléments


Libellé case à cocher


Libellé case à cocher


Libellé case à cocher


###
Extrait de code


<fieldset class="fr-fieldset" id="checkbox-inline" aria-labelledby="checkbox-inline-legend checkbox-inline-messages">
<legend class="fr-fieldset__legend--regular fr-fieldset__legend" id="checkbox-inline-legend">
Légende pour l'ensemble des éléments
</legend>
<div class="fr-fieldset__element fr-fieldset__element--inline">
<div class="fr-checkbox-group">
<input name="checkbox-inline-1" id="checkbox-inline-1" type="checkbox" aria-describedby="checkbox-inline-1-messages">
<label class="fr-label" for="checkbox-inline-1">
Libellé case à cocher
</label>
<div class="fr-messages-group" id="checkbox-inline-1-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-fieldset__element fr-fieldset__element--inline">
<div class="fr-checkbox-group">
<input name="checkbox-inline-2" id="checkbox-inline-2" type="checkbox" aria-describedby="checkbox-inline-2-messages">
<label class="fr-label" for="checkbox-inline-2">
Libellé case à cocher
</label>
<div class="fr-messages-group" id="checkbox-inline-2-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-fieldset__element fr-fieldset__element--inline">
<div class="fr-checkbox-group">
<input name="checkbox-inline-3" id="checkbox-inline-3" type="checkbox" aria-describedby="checkbox-inline-3-messages">
<label class="fr-label" for="checkbox-inline-3">
Libellé case à cocher
</label>
<div class="fr-messages-group" id="checkbox-inline-3-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-messages-group" id="checkbox-inline-messages" aria-live="polite">
</div>
</fieldset>


### Ensemble de boutons radio avec erreur


Légende pour l'ensemble des éléments
Texte de description additionnel


Libellé bouton radio


Libellé bouton radio


Libellé bouton radio


Texte d'erreur obligatoire


###
Extrait de code


<fieldset class="fr-fieldset fr-fieldset--error" id="radio-error" role="group" aria-labelledby="radio-error-legend radio-error-messages">
<legend class="fr-fieldset__legend--regular fr-fieldset__legend" id="radio-error-legend">
Légende pour l'ensemble des éléments
<span class="fr-hint-text">Texte de description additionnel</span>
</legend>
<div class="fr-fieldset__element">
<div class="fr-radio-group">
<input value="1" type="radio" id="radio-error-1" name="radio-error">
<label class="fr-label" for="radio-error-1">
Libellé bouton radio
</label>
</div>
</div>
<div class="fr-fieldset__element">
<div class="fr-radio-group">
<input value="2" type="radio" id="radio-error-2" name="radio-error">
<label class="fr-label" for="radio-error-2">
Libellé bouton radio
</label>
</div>
</div>
<div class="fr-fieldset__element">
<div class="fr-radio-group">
<input value="3" type="radio" id="radio-error-3" name="radio-error">
<label class="fr-label" for="radio-error-3">
Libellé bouton radio
</label>
</div>
</div>
<div class="fr-messages-group" id="radio-error-messages" aria-live="polite">
<p class="fr-message fr-message--error" id="radio-error-message-error">Texte d'erreur obligatoire</p>
</div>
</fieldset>


### Ensemble de boutons radio riches


Légende pour l'ensemble des éléments
Texte de description additionnel


Libellé bouton radio
Texte de description additionnel


Libellé bouton radio
Texte de description additionnel


Libellé bouton radio
Texte de description additionnel


###
Extrait de code


<fieldset class="fr-fieldset" id="radio-rich" aria-labelledby="radio-rich-legend radio-rich-messages">
<legend class="fr-fieldset__legend--regular fr-fieldset__legend" id="radio-rich-legend">
Légende pour l'ensemble des éléments
<span class="fr-hint-text">Texte de description additionnel</span>
</legend>
<div class="fr-fieldset__element">
<div class="fr-radio-group fr-radio-rich">
<input value="1" type="radio" id="radio-rich-1" name="radio-rich">
<label class="fr-label" for="radio-rich-1">
Libellé bouton radio
<span class="fr-hint-text">Texte de description additionnel</span>
</label>
</div>
</div>
<div class="fr-fieldset__element">
<div class="fr-radio-group fr-radio-rich">
<input value="2" type="radio" id="radio-rich-2" name="radio-rich">
<label class="fr-label" for="radio-rich-2">
Libellé bouton radio
<span class="fr-hint-text">Texte de description additionnel</span>
</label>
</div>
</div>
<div class="fr-fieldset__element">
<div class="fr-radio-group fr-radio-rich">
<input value="3" type="radio" id="radio-rich-3" name="radio-rich">
<label class="fr-label" for="radio-rich-3">
Libellé bouton radio
<span class="fr-hint-text">Texte de description additionnel</span>
</label>
</div>
</div>
<div class="fr-messages-group" id="radio-rich-messages" aria-live="polite">
</div>
</fieldset>


### Ensemble de cases à cocher, avec erreur


Légende pour l'ensemble des éléments
Texte de description additionnel


Libellé case à cocher


Libellé case à cocher


Libellé case à cocher


Texte d'erreur obligatoire


###
Extrait de code


<fieldset class="fr-fieldset fr-fieldset--error" id="checkbox-error" role="group" aria-labelledby="checkbox-error-legend checkbox-error-messages">
<legend class="fr-fieldset__legend--regular fr-fieldset__legend" id="checkbox-error-legend">
Légende pour l'ensemble des éléments
<span class="fr-hint-text">Texte de description additionnel</span>
</legend>
<div class="fr-fieldset__element">
<div class="fr-checkbox-group">
<input name="checkbox-error-1" id="checkbox-error-1" type="checkbox" aria-describedby="checkbox-error-1-messages">
<label class="fr-label" for="checkbox-error-1">
Libellé case à cocher
</label>
<div class="fr-messages-group" id="checkbox-error-1-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-fieldset__element">
<div class="fr-checkbox-group">
<input name="checkbox-error-2" id="checkbox-error-2" type="checkbox" aria-describedby="checkbox-error-2-messages">
<label class="fr-label" for="checkbox-error-2">
Libellé case à cocher
</label>
<div class="fr-messages-group" id="checkbox-error-2-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-fieldset__element">
<div class="fr-checkbox-group">
<input name="checkbox-error-3" id="checkbox-error-3" type="checkbox" aria-describedby="checkbox-error-3-messages">
<label class="fr-label" for="checkbox-error-3">
Libellé case à cocher
</label>
<div class="fr-messages-group" id="checkbox-error-3-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-messages-group" id="checkbox-error-messages" aria-live="polite">
<p class="fr-message fr-message--error" id="checkbox-error-message-error">Texte d'erreur obligatoire</p>
</div>
</fieldset>


### Ensemble de champs de saisie désactivés


Légende pour l'ensemble des éléments
Texte de description additionnel


Libellé champ de saisie
Texte de description additionnel


Libellé champ de saisie
Texte de description additionnel


Libellé champ de saisie
Texte de description additionnel


###
Extrait de code


<fieldset class="fr-fieldset" id="text-disabled" disabled aria-labelledby="text-disabled-legend text-disabled-messages">
<legend class="fr-fieldset__legend" id="text-disabled-legend">
Légende pour l'ensemble des éléments
<span class="fr-hint-text">Texte de description additionnel</span>
</legend>
<div class="fr-fieldset__element">
<div class="fr-input-group" id="input-group-3747">
<label class="fr-label" for="text-disabled-1">
Libellé champ de saisie
<span class="fr-hint-text">Texte de description additionnel</span>
</label>
<input class="fr-input" aria-describedby="text-disabled-1-messages" name="text-disabled-1" id="text-disabled-1" type="text">
<div class="fr-messages-group" id="text-disabled-1-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-fieldset__element">
<div class="fr-input-group" id="input-group-3748">
<label class="fr-label" for="text-disabled-2">
Libellé champ de saisie
<span class="fr-hint-text">Texte de description additionnel</span>
</label>
<input class="fr-input" aria-describedby="text-disabled-2-messages" name="text-disabled-2" id="text-disabled-2" type="text">
<div class="fr-messages-group" id="text-disabled-2-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-fieldset__element">
<div class="fr-input-group" id="input-group-3749">
<label class="fr-label" for="text-disabled-3">
Libellé champ de saisie
<span class="fr-hint-text">Texte de description additionnel</span>
</label>
<input class="fr-input" aria-describedby="text-disabled-3-messages" name="text-disabled-3" id="text-disabled-3" type="text">
<div class="fr-messages-group" id="text-disabled-3-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-messages-group" id="text-disabled-messages" aria-live="polite">
</div>
</fieldset>


### Ensemble de boutons radio désactivés


Légende pour l'ensemble des éléments
Texte de description additionnel


Libellé bouton radio
Texte de description additionnel


Libellé bouton radio
Texte de description additionnel


Libellé bouton radio
Texte de description additionnel


###
Extrait de code


<fieldset class="fr-fieldset" id="radio-disabled" disabled aria-labelledby="radio-disabled-legend radio-disabled-messages">
<legend class="fr-fieldset__legend--regular fr-fieldset__legend" id="radio-disabled-legend">
Légende pour l'ensemble des éléments
<span class="fr-hint-text">Texte de description additionnel</span>
</legend>
<div class="fr-fieldset__element">
<div class="fr-radio-group">
<input value="1" type="radio" id="radio-disabled-1" name="radio-disabled">
<label class="fr-label" for="radio-disabled-1">
Libellé bouton radio
<span class="fr-hint-text">Texte de description additionnel</span>
</label>
</div>
</div>
<div class="fr-fieldset__element">
<div class="fr-radio-group">
<input value="2" type="radio" id="radio-disabled-2" name="radio-disabled">
<label class="fr-label" for="radio-disabled-2">
Libellé bouton radio
<span class="fr-hint-text">Texte de description additionnel</span>
</label>
</div>
</div>
<div class="fr-fieldset__element">
<div class="fr-radio-group">
<input value="3" type="radio" id="radio-disabled-3" name="radio-disabled">
<label class="fr-label" for="radio-disabled-3">
Libellé bouton radio
<span class="fr-hint-text">Texte de description additionnel</span>
</label>
</div>
</div>
<div class="fr-messages-group" id="radio-disabled-messages" aria-live="polite">
</div>
</fieldset>


### Ensemble de cases à cocher désactivés


Légende pour l'ensemble des éléments
Texte de description additionnel


Libellé case à cocher
Texte de description additionnel


Libellé case à cocher
Texte de description additionnel


Libellé case à cocher
Texte de description additionnel


###
Extrait de code


<fieldset class="fr-fieldset" id="checkbox-disabled" disabled aria-labelledby="checkbox-disabled-legend checkbox-disabled-messages">
<legend class="fr-fieldset__legend--regular fr-fieldset__legend" id="checkbox-disabled-legend">
Légende pour l'ensemble des éléments
<span class="fr-hint-text">Texte de description additionnel</span>
</legend>
<div class="fr-fieldset__element">
<div class="fr-checkbox-group">
<input name="checkbox-disabled-1" id="checkbox-disabled-1" type="checkbox" aria-describedby="checkbox-disabled-1-messages">
<label class="fr-label" for="checkbox-disabled-1">
Libellé case à cocher
<span class="fr-hint-text">Texte de description additionnel</span>
</label>
<div class="fr-messages-group" id="checkbox-disabled-1-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-fieldset__element">
<div class="fr-checkbox-group">
<input name="checkbox-disabled-2" id="checkbox-disabled-2" type="checkbox" aria-describedby="checkbox-disabled-2-messages">
<label class="fr-label" for="checkbox-disabled-2">
Libellé case à cocher
<span class="fr-hint-text">Texte de description additionnel</span>
</label>
<div class="fr-messages-group" id="checkbox-disabled-2-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-fieldset__element">
<div class="fr-checkbox-group">
<input name="checkbox-disabled-3" id="checkbox-disabled-3" type="checkbox" aria-describedby="checkbox-disabled-3-messages">
<label class="fr-label" for="checkbox-disabled-3">
Libellé case à cocher
<span class="fr-hint-text">Texte de description additionnel</span>
</label>
<div class="fr-messages-group" id="checkbox-disabled-3-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-messages-group" id="checkbox-disabled-messages" aria-live="polite">
</div>
</fieldset>


### Bouton type submit


Envoyer


###
Extrait de code


<button title="Envoyer le formulaire" type="submit" class="fr-btn">Envoyer</button>


### Input type submit


###
Extrait de code


<input title="Envoyer le formulaire" type="submit" value="Envoyer" class="fr-btn">


### Messages de formulaire


L'id des messages, ou du groupe de message, doit être associé à l'attribut * aria-describedby * ou * aria-labelledby * de l'élément de formulaire auquel il fait référence (le fieldset, ou le champ).


Message neutre


Message d'information


Message de succès


Message d'avertissement


Message d'erreur


###
Extrait de code


<div class="fr-messages-group" id="message-group" aria-live="polite">
<p class="fr-message" id="message-neutral">Message neutre</p>
<p class="fr-message fr-message--info" id="message-info">Message d'information</p>
<p class="fr-message fr-message--valid" id="message-valid">Message de succès</p>
<p class="fr-message fr-message--warning" id="message-warning">Message d'avertissement</p>
<p class="fr-message fr-message--error" id="message-error">Message d'erreur</p>
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
