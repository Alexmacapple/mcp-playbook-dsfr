URL:
https://main--ds-gouv.netlify.app/example/layout/pattern/address

Title:
Bloc fonctionnel d'adresse postale - Système de design

Markdown:

Bloc fonctionnel d'adresse postale - Système de design


DSFR v1.14.0


[Retour](../)


# Bloc fonctionnel d'adresse postale (address)


La demande d'adresse postale permet d'aider un utilisateur à saisir son adresse.


#### Demande d'une adresse postale nationale


Adresse postale


Adresse
Indication : numéro et voie


Complément d'adresse (optionnel)
Indication : bâtiment, immeuble, escalier et numéro d'appartement


Code postal
Format attendu : 5 chiffres


Ville ou commune
Exemple : Montpellier


###
Extrait de code


<fieldset class="fr-fieldset" id="address-7329" aria-labelledby="address-7329-legend address-7329-messages">
<legend class="fr-sr-only" id="address-7329-legend">
Adresse postale
</legend>
<div class="fr-fieldset__element">
<div class="fr-input-group" id="input-group-7330">
<label class="fr-label" for="address-7324">
Adresse
<span class="fr-hint-text">Indication : numéro et voie</span>
</label>
<input class="fr-input" aria-describedby="address-7324-messages" name="address-line1" autocomplete="address-line1" id="address-7324" type="text">
<div class="fr-messages-group" id="address-7324-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-fieldset__element">
<div class="fr-input-group" id="input-group-7331">
<label class="fr-label" for="complement-7325">
Complément d'adresse (optionnel)
<span class="fr-hint-text">Indication : bâtiment, immeuble, escalier et numéro d'appartement</span>
</label>
<input class="fr-input" aria-describedby="complement-7325-messages" name="address-line2" autocomplete="address-line2" id="complement-7325" type="text">
<div class="fr-messages-group" id="complement-7325-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-fieldset__element fr-fieldset__element--inline fr-fieldset__element--postal">
<div class="fr-input-group" id="input-group-7332">
<label class="fr-label" for="postal-7326">
Code postal
<span class="fr-hint-text">Format attendu : 5 chiffres</span>
</label>
<input class="fr-input" aria-describedby="postal-7326-messages" name="postal-code" autocomplete="postal-code" id="postal-7326" type="text">
<div class="fr-messages-group" id="postal-7326-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-fieldset__element fr-fieldset__element--inline@md fr-fieldset__element--inline-grow">
<div class="fr-input-group" id="input-group-7333">
<label class="fr-label" for="city-7327">
Ville ou commune
<span class="fr-hint-text">Exemple : Montpellier</span>
</label>
<input class="fr-input" aria-describedby="city-7327-messages" name="address-level2" autocomplete="address-level2" id="city-7327" type="text">
<div class="fr-messages-group" id="city-7327-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-messages-group" id="address-7329-messages" aria-live="polite">
</div>
</fieldset>


#### Demande d'une adresse postale nationale + Lieu-dit, commune déléguée ou boîte postale


Adresse postale


Adresse
Indication : numéro et voie


Complément d'adresse (optionnel)
Indication : bâtiment, immeuble, escalier et numéro d'appartement


Lieu-dit, commune déléguée ou boîte postale


Code postal
Format attendu : 5 chiffres


Ville ou commune
Exemple : Montpellier


###
Extrait de code


<fieldset class="fr-fieldset" id="address-7353" aria-labelledby="address-7353-legend address-7353-messages">
<legend class="fr-sr-only" id="address-7353-legend">
Adresse postale
</legend>
<div class="fr-fieldset__element">
<div class="fr-input-group" id="input-group-7354">
<label class="fr-label" for="address-7347">
Adresse
<span class="fr-hint-text">Indication : numéro et voie</span>
</label>
<input class="fr-input" aria-describedby="address-7347-messages" name="address-line1" autocomplete="address-line1" id="address-7347" type="text">
<div class="fr-messages-group" id="address-7347-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-fieldset__element">
<div class="fr-input-group" id="input-group-7355">
<label class="fr-label" for="complement-7348">
Complément d'adresse (optionnel)
<span class="fr-hint-text">Indication : bâtiment, immeuble, escalier et numéro d'appartement</span>
</label>
<input class="fr-input" aria-describedby="complement-7348-messages" name="address-line2" autocomplete="address-line2" id="complement-7348" type="text">
<div class="fr-messages-group" id="complement-7348-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-fieldset__element">
<div class="fr-input-group" id="input-group-7356">
<label class="fr-label" for="locality-7349">
Lieu-dit, commune déléguée ou boîte postale
</label>
<input class="fr-input" aria-describedby="locality-7349-messages" name="address-level3" autocomplete="address-line3" id="locality-7349" type="text">
<div class="fr-messages-group" id="locality-7349-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-fieldset__element fr-fieldset__element--inline fr-fieldset__element--postal">
<div class="fr-input-group" id="input-group-7357">
<label class="fr-label" for="postal-7350">
Code postal
<span class="fr-hint-text">Format attendu : 5 chiffres</span>
</label>
<input class="fr-input" aria-describedby="postal-7350-messages" name="postal-code" autocomplete="postal-code" id="postal-7350" type="text">
<div class="fr-messages-group" id="postal-7350-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-fieldset__element fr-fieldset__element--inline@md fr-fieldset__element--inline-grow">
<div class="fr-input-group" id="input-group-7358">
<label class="fr-label" for="city-7351">
Ville ou commune
<span class="fr-hint-text">Exemple : Montpellier</span>
</label>
<input class="fr-input" aria-describedby="city-7351-messages" name="address-level2" autocomplete="address-level2" id="city-7351" type="text">
<div class="fr-messages-group" id="city-7351-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-messages-group" id="address-7353-messages" aria-live="polite">
</div>
</fieldset>


#### Complément d'adresse


Complément d'adresse postale


Numéro


Voie


Bâtiment


Immeuble


Escalier


Numéro d'appartement


###
Extrait de code


<fieldset class="fr-fieldset" id="address-7381" aria-labelledby="address-7381-legend address-7381-messages">
<legend class="fr-sr-only" id="address-7381-legend">
Complément d'adresse postale
</legend>
<div class="fr-fieldset__element fr-fieldset__element--inline fr-fieldset__element--inline-grow fr-fieldset__element--number">
<div class="fr-input-group" id="input-group-7382">
<label class="fr-label" for="number-7375">
Numéro
</label>
<input class="fr-input" aria-describedby="number-7375-messages" name="number" id="number-7375" type="text">
<div class="fr-messages-group" id="number-7375-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-fieldset__element fr-fieldset__element--inline fr-fieldset__element--inline-grow">
<div class="fr-input-group" id="input-group-7383">
<label class="fr-label" for="street-7376">
Voie
</label>
<input class="fr-input" aria-describedby="street-7376-messages" name="street" id="street-7376" type="text">
<div class="fr-messages-group" id="street-7376-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-fieldset__element">
<div class="fr-input-group" id="input-group-7384">
<label class="fr-label" for="building-7377">
Bâtiment
</label>
<input class="fr-input" aria-describedby="building-7377-messages" name="building" id="building-7377" type="text">
<div class="fr-messages-group" id="building-7377-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-fieldset__element">
<div class="fr-input-group" id="input-group-7385">
<label class="fr-label" for="block-7378">
Immeuble
</label>
<input class="fr-input" aria-describedby="block-7378-messages" name="block" id="block-7378" type="text">
<div class="fr-messages-group" id="block-7378-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-fieldset__element">
<div class="fr-input-group" id="input-group-7386">
<label class="fr-label" for="stare-7379">
Escalier
</label>
<input class="fr-input" aria-describedby="stare-7379-messages" name="stare" id="stare-7379" type="text">
<div class="fr-messages-group" id="stare-7379-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-fieldset__element">
<div class="fr-input-group" id="input-group-7387">
<label class="fr-label" for="apartment-7380">
Numéro d'appartement
</label>
<input class="fr-input" aria-describedby="apartment-7380-messages" name="apartment" id="apartment-7380" type="text">
<div class="fr-messages-group" id="apartment-7380-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-messages-group" id="address-7381-messages" aria-live="polite">
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
