URL:
https://main--ds-gouv.netlify.app/example/layout/pattern/date

Title:
Bloc fonctionnel de date unique - Système de design

Markdown:

Bloc fonctionnel de date unique - Système de design


DSFR v1.14.0


[Retour](../)


# Bloc fonctionnel de date unique (date)


Le champ de saisie de date fixe reprend trois champs de saisie de texte.
[Documentation](https://www.systeme-de-design.gouv.fr/elements-d-interface/blocs-fonctionnels/date-unique)


#### Défaut


Date de naissance
Indication : texte de description additionnel


Jour
Exemple : 14


Mois
Exemple : 12


Année
Exemple : 1984


###
Extrait de code


<fieldset class="fr-fieldset" id="date-7421" aria-labelledby="date-7421-legend date-7421-messages">
<legend class="fr-fieldset__legend--regular fr-fieldset__legend" id="date-7421-legend">
Date de naissance
<span class="fr-hint-text">Indication : texte de description additionnel</span>
</legend>
<div class="fr-fieldset__element fr-fieldset__element--inline fr-fieldset__element--number">
<div class="fr-input-group" id="input-group-7422">
<label class="fr-label" for="date-7421-bday-day">
Jour
<span class="fr-hint-text">Exemple : 14</span>
</label>
<input class="fr-input" name="day" autocomplete="bday-day" id="date-7421-bday-day" type="text">
</div>
</div>
<div class="fr-fieldset__element fr-fieldset__element--inline fr-fieldset__element--number">
<div class="fr-input-group" id="input-group-7423">
<label class="fr-label" for="date-7421-bday-month">
Mois
<span class="fr-hint-text">Exemple : 12</span>
</label>
<input class="fr-input" name="month" autocomplete="bday-month" id="date-7421-bday-month" type="text">
</div>
</div>
<div class="fr-fieldset__element fr-fieldset__element--inline fr-fieldset__element--inline-grow fr-fieldset__element--year">
<div class="fr-input-group" id="input-group-7424">
<label class="fr-label" for="date-7421-bday-year">
Année
<span class="fr-hint-text">Exemple : 1984</span>
</label>
<input class="fr-input" name="year" autocomplete="bday-year" id="date-7421-bday-year" type="text">
</div>
</div>
<div class="fr-messages-group" id="date-7421-messages" aria-live="polite">
</div>
</fieldset>


#### Erreur unitaire


Date de naissance
Indication : texte de description additionnel


Jour
Exemple : 14


Mois
Exemple : 12


Année
Exemple : 1984


Le jour est invalide


Le mois est invalide


L'année est invalide


###
Extrait de code


<fieldset class="fr-fieldset fr-fieldset--error" id="date-error-7430" role="group" aria-labelledby="date-error-7430-legend date-error-7430-messages">
<legend class="fr-fieldset__legend--regular fr-fieldset__legend" id="date-error-7430-legend">
Date de naissance
<span class="fr-hint-text">Indication : texte de description additionnel</span>
</legend>
<div class="fr-fieldset__element fr-fieldset__element--inline fr-fieldset__element--number">
<div class="fr-input-group" id="input-group-7431">
<label class="fr-label" for="date-error-7430-bday-day">
Jour
<span class="fr-hint-text">Exemple : 14</span>
</label>
<input class="fr-input" name="day" value="00" autocomplete="bday-day" id="date-error-7430-bday-day" type="text">
</div>
</div>
<div class="fr-fieldset__element fr-fieldset__element--inline fr-fieldset__element--number">
<div class="fr-input-group" id="input-group-7432">
<label class="fr-label" for="date-error-7430-bday-month">
Mois
<span class="fr-hint-text">Exemple : 12</span>
</label>
<input class="fr-input" name="month" value="13" autocomplete="bday-month" id="date-error-7430-bday-month" type="text">
</div>
</div>
<div class="fr-fieldset__element fr-fieldset__element--inline fr-fieldset__element--inline-grow fr-fieldset__element--year">
<div class="fr-input-group" id="input-group-7433">
<label class="fr-label" for="date-error-7430-bday-year">
Année
<span class="fr-hint-text">Exemple : 1984</span>
</label>
<input class="fr-input" name="year" value="1995e" autocomplete="bday-year" id="date-error-7430-bday-year" type="text">
</div>
</div>
<div class="fr-messages-group" id="date-error-7430-messages" aria-live="polite">
<p class="fr-message fr-message--error" id="date-error-7430-message-error-1">Le jour est invalide</p>
<p class="fr-message fr-message--error" id="date-error-7430-message-error-2">Le mois est invalide</p>
<p class="fr-message fr-message--error" id="date-error-7430-message-error-3">L'année est invalide</p>
</div>
</fieldset>


#### Erreur globale


Date de naissance
Indication : texte de description additionnel


Jour
Exemple : 14


Mois
Exemple : 12


Année
Exemple : 1984


La date est postérieure à aujourd'hui


###
Extrait de code


<fieldset class="fr-fieldset fr-fieldset--error" id="date-error-7439" role="group" aria-labelledby="date-error-7439-legend date-error-7439-messages">
<legend class="fr-fieldset__legend--regular fr-fieldset__legend" id="date-error-7439-legend">
Date de naissance
<span class="fr-hint-text">Indication : texte de description additionnel</span>
</legend>
<div class="fr-fieldset__element fr-fieldset__element--inline fr-fieldset__element--number">
<div class="fr-input-group" id="input-group-7440">
<label class="fr-label" for="date-error-7439-bday-day">
Jour
<span class="fr-hint-text">Exemple : 14</span>
</label>
<input class="fr-input" name="day" value="03" autocomplete="bday-day" id="date-error-7439-bday-day" type="text">
</div>
</div>
<div class="fr-fieldset__element fr-fieldset__element--inline fr-fieldset__element--number">
<div class="fr-input-group" id="input-group-7441">
<label class="fr-label" for="date-error-7439-bday-month">
Mois
<span class="fr-hint-text">Exemple : 12</span>
</label>
<input class="fr-input" name="month" value="03" autocomplete="bday-month" id="date-error-7439-bday-month" type="text">
</div>
</div>
<div class="fr-fieldset__element fr-fieldset__element--inline fr-fieldset__element--inline-grow fr-fieldset__element--year">
<div class="fr-input-group" id="input-group-7442">
<label class="fr-label" for="date-error-7439-bday-year">
Année
<span class="fr-hint-text">Exemple : 1984</span>
</label>
<input class="fr-input" name="year" value="2525" autocomplete="bday-year" id="date-error-7439-bday-year" type="text">
</div>
</div>
<div class="fr-messages-group" id="date-error-7439-messages" aria-live="polite">
<p class="fr-message fr-message--error" id="date-error-7439-message-error">La date est postérieure à aujourd'hui</p>
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
