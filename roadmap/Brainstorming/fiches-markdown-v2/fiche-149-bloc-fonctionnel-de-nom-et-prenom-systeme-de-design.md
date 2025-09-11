URL:
https://main--ds-gouv.netlify.app/example/layout/pattern/name

Title:
Bloc fonctionnel de nom et prénom - Système de design

Markdown:

Bloc fonctionnel de nom et prénom - Système de design


DSFR v1.14.0


[Retour](../)


# Bloc fonctionnel de nom et prénom (name)


La demande de nom et prénom permet d'aider un utilisateur à saisir son nom et son prénom.
[Documentation](https://www.systeme-de-design.gouv.fr/elements-d-interface/blocs-fonctionnels/nom-et-prenom)


## Demande d'un nom et d'un prénom en France


#### Défaut


Nom


Nom


Prénom


###
Extrait de code


<fieldset class="fr-fieldset" id="firstname-disabled-7482" aria-labelledby="firstname-disabled-7482-legend firstname-disabled-7482-messages">
<legend class="fr-sr-only" id="firstname-disabled-7482-legend">
Nom
</legend>
<div class="fr-fieldset__element">
<div class="fr-input-group" id="input-group-7490">
<label class="fr-label" for="family-name-7484">
Nom
</label>
<input class="fr-input" aria-describedby="family-name-7484-messages" name="family-name" autocomplete="family-name" id="family-name-7484" spellcheck="false" type="text">
<div class="fr-messages-group" id="family-name-7484-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-fieldset__element">
<div class="fr-input-group" id="input-group-7491">
<label class="fr-label" for="given-7489">
Prénom
</label>
<input class="fr-input" aria-describedby="given-7489-messages" name="given-name" autocomplete="given-name" id="given-7489" spellcheck="false" type="text">
<div class="fr-messages-group" id="given-7489-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-messages-group" id="firstname-disabled-7482-messages" aria-live="polite">
</div>
</fieldset>


#### Avec prénom désactivé


Nom


Nom


Prénom


Prénom


Je n'ai pas de prénom


###
Extrait de code


<fieldset class="fr-fieldset" id="firstname-disabled-7505" aria-labelledby="firstname-disabled-7505-legend firstname-disabled-7505-messages">
<legend class="fr-sr-only" id="firstname-disabled-7505-legend">
Nom
</legend>
<div class="fr-fieldset__element">
<div class="fr-input-group" id="input-group-7515">
<label class="fr-label" for="family-name-7507">
Nom
</label>
<input class="fr-input" aria-describedby="family-name-7507-messages" name="family-name" autocomplete="family-name" id="family-name-7507" spellcheck="false" type="text">
<div class="fr-messages-group" id="family-name-7507-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-fieldset__element">
<fieldset class="fr-mb-n4v fr-fieldset" id="firstname-fieldset-7513" disabled aria-labelledby="firstname-fieldset-7513-legend firstname-fieldset-7513-messages">
<legend class="fr-sr-only" id="firstname-fieldset-7513-legend">
Prénom
</legend>
<div class="fr-fieldset__element">
<div class="fr-input-group" id="input-group-7516">
<label class="fr-label" for="given-7512">
Prénom
</label>
<input class="fr-input" aria-describedby="given-7512-messages" name="given-name" autocomplete="given-name" id="given-7512" spellcheck="false" type="text">
<div class="fr-messages-group" id="given-7512-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-messages-group" id="firstname-fieldset-7513-messages" aria-live="polite">
</div>
</fieldset>
</div>
<div class="fr-fieldset__element">
<div class="fr-checkbox-group fr-checkbox-group--sm">
<input onclick="toggleDisabled(this, 'firstname-fieldset-7513')" checked name="firstname-disabled" id="disabler-7514" type="checkbox" aria-describedby="disabler-7514-messages">
<label class="fr-label" for="disabler-7514">
Je n'ai pas de prénom
</label>
<div class="fr-messages-group" id="disabler-7514-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-messages-group" id="firstname-disabled-7505-messages" aria-live="polite">
</div>
</fieldset>


#### Avec nom d'usage


Nom


Nom


Nom d'usage
Indication : ancien nom...


Prénom


###
Extrait de code


<fieldset class="fr-fieldset" id="married-name-7529" aria-labelledby="married-name-7529-legend married-name-7529-messages">
<legend class="fr-sr-only" id="married-name-7529-legend">
Nom
</legend>
<div class="fr-fieldset__element">
<div class="fr-input-group" id="input-group-7537">
<label class="fr-label" for="family-name-7531">
Nom
</label>
<input class="fr-input" aria-describedby="family-name-7531-messages" name="family-name" autocomplete="family-name" id="family-name-7531" spellcheck="false" type="text">
<div class="fr-messages-group" id="family-name-7531-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-fieldset__element">
<div class="fr-input-group" id="input-group-7538">
<label class="fr-label" for="married-7534">
Nom d'usage
<span class="fr-hint-text">Indication : ancien nom...</span>
</label>
<input class="fr-input" aria-describedby="married-7534-messages" name="married-name" autocomplete="family-name" id="married-7534" spellcheck="false" type="text">
<div class="fr-messages-group" id="married-7534-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-fieldset__element">
<div class="fr-input-group" id="input-group-7539">
<label class="fr-label" for="given-7536">
Prénom
</label>
<input class="fr-input" aria-describedby="given-7536-messages" name="given-name" autocomplete="given-name" id="given-7536" spellcheck="false" type="text">
<div class="fr-messages-group" id="given-7536-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-messages-group" id="married-name-7529-messages" aria-live="polite">
</div>
</fieldset>


#### Avec nom d'usage + prénom désactivé


Nom


Nom


Nom d'usage
Indication : ancien nom...


Prénom


Prénom


Je n'ai pas de prénom


###
Extrait de code


<fieldset class="fr-fieldset" id="married-and-firstname-disabled-7554" aria-labelledby="married-and-firstname-disabled-7554-legend married-and-firstname-disabled-7554-messages">
<legend class="fr-sr-only" id="married-and-firstname-disabled-7554-legend">
Nom
</legend>
<div class="fr-fieldset__element">
<div class="fr-input-group" id="input-group-7564">
<label class="fr-label" for="family-name-7556">
Nom
</label>
<input class="fr-input" aria-describedby="family-name-7556-messages" name="family-name" autocomplete="family-name" id="family-name-7556" spellcheck="false" type="text">
<div class="fr-messages-group" id="family-name-7556-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-fieldset__element">
<div class="fr-input-group" id="input-group-7565">
<label class="fr-label" for="married-7559">
Nom d'usage
<span class="fr-hint-text">Indication : ancien nom...</span>
</label>
<input class="fr-input" aria-describedby="married-7559-messages" name="married-name" autocomplete="family-name" id="married-7559" spellcheck="false" type="text">
<div class="fr-messages-group" id="married-7559-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-fieldset__element">
<fieldset class="fr-mb-n4v fr-fieldset" id="firstname-fieldset-7562" disabled aria-labelledby="firstname-fieldset-7562-legend firstname-fieldset-7562-messages">
<legend class="fr-sr-only" id="firstname-fieldset-7562-legend">
Prénom
</legend>
<div class="fr-fieldset__element">
<div class="fr-input-group" id="input-group-7566">
<label class="fr-label" for="given-7561">
Prénom
</label>
<input class="fr-input" aria-describedby="given-7561-messages" name="given-name" autocomplete="given-name" id="given-7561" spellcheck="false" type="text">
<div class="fr-messages-group" id="given-7561-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-messages-group" id="firstname-fieldset-7562-messages" aria-live="polite">
</div>
</fieldset>
</div>
<div class="fr-fieldset__element">
<div class="fr-checkbox-group fr-checkbox-group--sm">
<input onclick="toggleDisabled(this, 'firstname-fieldset-7562')" checked name="firstname-disabled" id="disabler-7563" type="checkbox" aria-describedby="disabler-7563-messages">
<label class="fr-label" for="disabler-7563">
Je n'ai pas de prénom
</label>
<div class="fr-messages-group" id="disabler-7563-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-messages-group" id="married-and-firstname-disabled-7554-messages" aria-live="polite">
</div>
</fieldset>


#### Avec bouton


Nom


Nom


Prénom


Prénom


Ajouter un prénom


Je n'ai pas de prénom


###
Extrait de code


<fieldset class="fr-fieldset" id="button-7580" aria-labelledby="button-7580-legend button-7580-messages">
<legend class="fr-sr-only" id="button-7580-legend">
Nom
</legend>
<div class="fr-fieldset__element">
<div class="fr-input-group" id="input-group-7590">
<label class="fr-label" for="family-name-7582">
Nom
</label>
<input class="fr-input" aria-describedby="family-name-7582-messages" name="family-name" autocomplete="family-name" id="family-name-7582" spellcheck="false" type="text">
<div class="fr-messages-group" id="family-name-7582-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-fieldset__element">
<fieldset class="fr-mb-n4v fr-fieldset" id="firstname-fieldset-7588" aria-labelledby="firstname-fieldset-7588-legend firstname-fieldset-7588-messages">
<legend class="fr-sr-only" id="firstname-fieldset-7588-legend">
Prénom
</legend>
<div class="fr-fieldset__element">
<div class="fr-input-group" id="input-group-7591">
<label class="fr-label" for="given-7587">
Prénom
</label>
<input class="fr-input" aria-describedby="given-7587-messages" name="given-name" autocomplete="given-name" id="given-7587" spellcheck="false" type="text">
<div class="fr-messages-group" id="given-7587-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-fieldset__element">
<button onclick="addFirstname(this, 'given-7587')" type="button" class="fr-btn fr-btn--sm fr-icon-add-line fr-btn--icon-left fr-btn--secondary">Ajouter un prénom</button>
</div>
<div class="fr-messages-group" id="firstname-fieldset-7588-messages" aria-live="polite">
</div>
</fieldset>
</div>
<div class="fr-fieldset__element">
<div class="fr-checkbox-group fr-checkbox-group--sm">
<input onclick="toggleDisabled(this, 'firstname-fieldset-7588')" name="firstname-disabled" id="disabler-7589" type="checkbox" aria-describedby="disabler-7589-messages">
<label class="fr-label" for="disabler-7589">
Je n'ai pas de prénom
</label>
<div class="fr-messages-group" id="disabler-7589-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-messages-group" id="button-7580-messages" aria-live="polite">
</div>
</fieldset>


#### Avec bouton + prénom désactivé


Nom


Nom


Prénom


Prénom


Ajouter un prénom


Je n'ai pas de prénom


###
Extrait de code


<fieldset class="fr-fieldset" id="button-and-firstname-disabled-7605" aria-labelledby="button-and-firstname-disabled-7605-legend button-and-firstname-disabled-7605-messages">
<legend class="fr-sr-only" id="button-and-firstname-disabled-7605-legend">
Nom
</legend>
<div class="fr-fieldset__element">
<div class="fr-input-group" id="input-group-7615">
<label class="fr-label" for="family-name-7607">
Nom
</label>
<input class="fr-input" aria-describedby="family-name-7607-messages" name="family-name" autocomplete="family-name" id="family-name-7607" spellcheck="false" type="text">
<div class="fr-messages-group" id="family-name-7607-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-fieldset__element">
<fieldset class="fr-mb-n4v fr-fieldset" id="firstname-fieldset-7613" disabled aria-labelledby="firstname-fieldset-7613-legend firstname-fieldset-7613-messages">
<legend class="fr-sr-only" id="firstname-fieldset-7613-legend">
Prénom
</legend>
<div class="fr-fieldset__element">
<div class="fr-input-group" id="input-group-7616">
<label class="fr-label" for="given-7612">
Prénom
</label>
<input class="fr-input" aria-describedby="given-7612-messages" name="given-name" autocomplete="given-name" id="given-7612" spellcheck="false" type="text">
<div class="fr-messages-group" id="given-7612-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-fieldset__element">
<button onclick="addFirstname(this, 'given-7612')" type="button" class="fr-btn fr-btn--sm fr-icon-add-line fr-btn--icon-left fr-btn--secondary">Ajouter un prénom</button>
</div>
<div class="fr-messages-group" id="firstname-fieldset-7613-messages" aria-live="polite">
</div>
</fieldset>
</div>
<div class="fr-fieldset__element">
<div class="fr-checkbox-group fr-checkbox-group--sm">
<input onclick="toggleDisabled(this, 'firstname-fieldset-7613')" checked name="firstname-disabled" id="disabler-7614" type="checkbox" aria-describedby="disabler-7614-messages">
<label class="fr-label" for="disabler-7614">
Je n'ai pas de prénom
</label>
<div class="fr-messages-group" id="disabler-7614-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-messages-group" id="button-and-firstname-disabled-7605-messages" aria-live="polite">
</div>
</fieldset>


## Demande d'un nom et d'un prénom à l'international


#### Défaut


Nom


Pays


Sélectionner une option
France
Allemagne
Italie
Espagne
Royaume-Uni


Nom


Prénom


Prénom


Je n'ai pas de prénom


###
Extrait de code


<fieldset class="fr-fieldset" id="name-international-7630" aria-labelledby="name-international-7630-legend name-international-7630-messages">
<legend class="fr-sr-only" id="name-international-7630-legend">
Nom
</legend>
<div class="fr-fieldset__element">
<div class="fr-select-group">
<label class="fr-label" for="country-7631">
Pays
</label>
<select class="fr-select" aria-describedby="country-7631-messages" id="country-7631" name="country">
<option value="" selected disabled>Sélectionner une option</option>
<option value="FR">France</option>
<option value="DE">Allemagne</option>
<option value="IT">Italie</option>
<option value="ES">Espagne</option>
<option value="GB">Royaume-Uni</option>
</select>
<div class="fr-messages-group" id="country-7631-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-fieldset__element">
<div class="fr-input-group" id="input-group-7640">
<label class="fr-label" for="family-name-7632">
Nom
</label>
<input class="fr-input" aria-describedby="family-name-7632-messages" name="family-name" autocomplete="family-name" id="family-name-7632" spellcheck="false" type="text">
<div class="fr-messages-group" id="family-name-7632-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-fieldset__element">
<fieldset class="fr-mb-n4v fr-fieldset" id="firstname-fieldset-7638" aria-labelledby="firstname-fieldset-7638-legend firstname-fieldset-7638-messages">
<legend class="fr-sr-only" id="firstname-fieldset-7638-legend">
Prénom
</legend>
<div class="fr-fieldset__element">
<div class="fr-input-group" id="input-group-7641">
<label class="fr-label" for="given-7637">
Prénom
</label>
<input class="fr-input" aria-describedby="given-7637-messages" name="given-name" autocomplete="given-name" id="given-7637" spellcheck="false" type="text">
<div class="fr-messages-group" id="given-7637-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-messages-group" id="firstname-fieldset-7638-messages" aria-live="polite">
</div>
</fieldset>
</div>
<div class="fr-fieldset__element">
<div class="fr-checkbox-group fr-checkbox-group--sm">
<input onclick="toggleDisabled(this, 'firstname-fieldset-7638')" name="firstname-disabled" id="disabler-7639" type="checkbox" aria-describedby="disabler-7639-messages">
<label class="fr-label" for="disabler-7639">
Je n'ai pas de prénom
</label>
<div class="fr-messages-group" id="disabler-7639-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-messages-group" id="name-international-7630-messages" aria-live="polite">
</div>
</fieldset>


#### Avec prénom désactivé


Nom


Pays


Sélectionner une option
France
Allemagne
Italie
Espagne
Royaume-Uni


Nom


Prénom


Prénom


Je n'ai pas de prénom


###
Extrait de code


<fieldset class="fr-fieldset" id="name-international-7655" aria-labelledby="name-international-7655-legend name-international-7655-messages">
<legend class="fr-sr-only" id="name-international-7655-legend">
Nom
</legend>
<div class="fr-fieldset__element">
<div class="fr-select-group">
<label class="fr-label" for="country-7656">
Pays
</label>
<select class="fr-select" aria-describedby="country-7656-messages" id="country-7656" name="country">
<option value="" selected disabled>Sélectionner une option</option>
<option value="FR">France</option>
<option value="DE">Allemagne</option>
<option value="IT">Italie</option>
<option value="ES">Espagne</option>
<option value="GB">Royaume-Uni</option>
</select>
<div class="fr-messages-group" id="country-7656-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-fieldset__element">
<div class="fr-input-group" id="input-group-7665">
<label class="fr-label" for="family-name-7657">
Nom
</label>
<input class="fr-input" aria-describedby="family-name-7657-messages" name="family-name" autocomplete="family-name" id="family-name-7657" spellcheck="false" type="text">
<div class="fr-messages-group" id="family-name-7657-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-fieldset__element">
<fieldset class="fr-mb-n4v fr-fieldset" id="firstname-fieldset-7663" disabled aria-labelledby="firstname-fieldset-7663-legend firstname-fieldset-7663-messages">
<legend class="fr-sr-only" id="firstname-fieldset-7663-legend">
Prénom
</legend>
<div class="fr-fieldset__element">
<div class="fr-input-group" id="input-group-7666">
<label class="fr-label" for="given-7662">
Prénom
</label>
<input class="fr-input" aria-describedby="given-7662-messages" name="given-name" autocomplete="given-name" id="given-7662" spellcheck="false" type="text">
<div class="fr-messages-group" id="given-7662-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-messages-group" id="firstname-fieldset-7663-messages" aria-live="polite">
</div>
</fieldset>
</div>
<div class="fr-fieldset__element">
<div class="fr-checkbox-group fr-checkbox-group--sm">
<input onclick="toggleDisabled(this, 'firstname-fieldset-7663')" checked name="firstname-disabled" id="disabler-7664" type="checkbox" aria-describedby="disabler-7664-messages">
<label class="fr-label" for="disabler-7664">
Je n'ai pas de prénom
</label>
<div class="fr-messages-group" id="disabler-7664-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-messages-group" id="name-international-7655-messages" aria-live="polite">
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
