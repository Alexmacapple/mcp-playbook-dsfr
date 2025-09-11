URL:
https://main--ds-gouv.netlify.app/example/layout/pattern/civility

Title:
Bloc fonctionnel de civilité - Système de design

Markdown:

Bloc fonctionnel de civilité - Système de design


DSFR v1.14.0


[Retour](../)


# Bloc fonctionnel de civilité (civility)


La demande de civilité permet à un utilisateur de donner sa civilité (sexe, situation familière, titre d'appel).
[Documentation](https://www.systeme-de-design.gouv.fr/elements-d-interface/blocs-fonctionnels/civilite)


#### Demande du sexe


Sexe


Feminin


Masculin


###
Extrait de code


<fieldset class="fr-fieldset" id="sex-7393" aria-labelledby="sex-7393-legend sex-7393-messages">
<legend class="fr-fieldset__legend--regular fr-fieldset__legend" id="sex-7393-legend">
Sexe
</legend>
<div class="fr-fieldset__element">
<div class="fr-radio-group fr-radio-group--sm">
<input type="radio" id="female-7394" name="sex">
<label class="fr-label" for="female-7394">
Feminin
</label>
</div>
</div>
<div class="fr-fieldset__element">
<div class="fr-radio-group fr-radio-group--sm">
<input type="radio" id="male-7395" name="sex">
<label class="fr-label" for="male-7395">
Masculin
</label>
</div>
</div>
<div class="fr-messages-group" id="sex-7393-messages" aria-live="polite">
</div>
</fieldset>


#### Demande de situation familiale


Demande de situation familiale


Situation familiale


Sélectionner une option
Célibataire
Concubinage
Pacsé
Marié
Veuf
Divorcé
Sans réponse


###
Extrait de code


<fieldset class="fr-fieldset" id="family-7399" aria-labelledby="family-7399-legend family-7399-messages">
<legend class="fr-sr-only" id="family-7399-legend">
Demande de situation familiale
</legend>
<div class="fr-fieldset__element">
<div class="fr-select-group">
<label class="fr-label" for="family-7400">
Situation familiale
</label>
<select class="fr-select" aria-describedby="family-7400-messages" id="family-7400" name="family">
<option value="" selected disabled>Sélectionner une option</option>
<option value="1">Célibataire</option>
<option value="2">Concubinage</option>
<option value="3">Pacsé</option>
<option value="4">Marié</option>
<option value="5">Veuf</option>
<option value="6">Divorcé</option>
<option value="7">Sans réponse</option>
</select>
<div class="fr-messages-group" id="family-7400-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-messages-group" id="family-7399-messages" aria-live="polite">
</div>
</fieldset>


Les boutons radios sont recommandés lorsque l'utilisateur doit choisir un élément parmi 2 à 5 choix possibles.


#### Demande du titre d'appel


Titre d'appel


Docteur


Inspecteur


Sans réponse


###
Extrait de code


<fieldset class="fr-fieldset" id="honorific-7406" aria-labelledby="honorific-7406-legend honorific-7406-messages">
<legend class="fr-fieldset__legend--regular fr-fieldset__legend" id="honorific-7406-legend">
Titre d'appel
</legend>
<div class="fr-fieldset__element">
<div class="fr-radio-group fr-radio-group--sm">
<input type="radio" id="honorific-7407" name="honorific">
<label class="fr-label" for="honorific-7407">
Docteur
</label>
</div>
</div>
<div class="fr-fieldset__element">
<div class="fr-radio-group fr-radio-group--sm">
<input type="radio" id="honorific-7408" name="honorific">
<label class="fr-label" for="honorific-7408">
Inspecteur
</label>
</div>
</div>
<div class="fr-fieldset__element">
<div class="fr-radio-group fr-radio-group--sm">
<input type="radio" id="honorific-7409" name="honorific">
<label class="fr-label" for="honorific-7409">
Sans réponse
</label>
</div>
</div>
<div class="fr-messages-group" id="honorific-7406-messages" aria-live="polite">
</div>
</fieldset>


Au delà de 5 choix ou lorsque l'espace n'est pas suffisant, il est préférable d'utiliser une liste déroulante.


#### Demande du titre d'appel


Demande du titre d'appel


Titre d'appel


Sélectionner une option
Recteur
Inspecteur
Proviseur
Professeur
Docteur
Principal
Sans réponse


###
Extrait de code


<fieldset class="fr-fieldset" id="honorific-7413" aria-labelledby="honorific-7413-legend honorific-7413-messages">
<legend class="fr-sr-only" id="honorific-7413-legend">
Demande du titre d'appel
</legend>
<div class="fr-fieldset__element">
<div class="fr-select-group">
<label class="fr-label" for="honorific-7414">
Titre d'appel
</label>
<select class="fr-select" aria-describedby="honorific-7414-messages" id="honorific-7414" name="honorific">
<option value="" selected disabled>Sélectionner une option</option>
<option value="1">Recteur</option>
<option value="2">Inspecteur</option>
<option value="3">Proviseur</option>
<option value="4">Professeur</option>
<option value="5">Docteur</option>
<option value="6">Principal</option>
<option value="7">Sans réponse</option>
</select>
<div class="fr-messages-group" id="honorific-7414-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-messages-group" id="honorific-7413-messages" aria-live="polite">
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
