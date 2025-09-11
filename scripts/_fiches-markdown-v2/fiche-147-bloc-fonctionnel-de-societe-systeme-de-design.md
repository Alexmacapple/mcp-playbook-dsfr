URL:
https://main--ds-gouv.netlify.app/example/layout/pattern/company

Title:
Bloc fonctionnel de société - Système de design

Markdown:

Bloc fonctionnel de société - Système de design


DSFR v1.14.0


[Retour](../)


# Bloc fonctionnel de société (company)


La demande de renseignement sur la société permet d'aider un utilisateur à saisir les renseignements concernant sa société.
[Documentation](https://www.systeme-de-design.gouv.fr/elements-d-interface/blocs-fonctionnels/societe)


#### Demande d'un numéro de SIRET


SIRET de l'entreprise


Numéro de SIRET


[Annuaire des entreprises](https://annuaire-entreprises.data.gouv.fr/)


###
Extrait de code


<fieldset class="fr-fieldset" id="siret-7673" aria-labelledby="siret-7673-legend siret-7673-messages">
<legend class="fr-sr-only" id="siret-7673-legend">
SIRET de l'entreprise
</legend>
<div class="fr-fieldset__element">
<div class="fr-input-group" id="input-group-7675">
<label class="fr-label" for="siret-7674">
Numéro de SIRET
</label>
<input class="fr-input" aria-describedby="siret-7674-messages" name="siret" id="siret-7674" type="text">
<div class="fr-messages-group" id="siret-7674-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-mt-n1v fr-fieldset__element">
<a title="Annuaire des entreprises - nouvelle fenêtre" target="_blank" rel="noopener" id="link-7676" href="https://annuaire-entreprises.data.gouv.fr/" class="fr-link">Annuaire des entreprises</a>
</div>
<div class="fr-messages-group" id="siret-7673-messages" aria-live="polite">
</div>
</fieldset>


#### Demande d'une adresse de siège social


Adresse postale


Dénomination


Adresse
Indication : numéro et voie


Complément d'adresse (optionnel)
Indication : bâtiment, immeuble, escalier et numéro d'appartement


Lieu-dit, commune déléguée ou boîte postale


Code postal
Format attendu : 5 chiffres


Ville ou commune
Exemple : Montpellier


Cedex


Pays


Sélectionner une option
France
Allemagne
Italie
Espagne
Royaume-Uni


###
Extrait de code


<fieldset class="fr-fieldset" id="address-7702" aria-labelledby="address-7702-legend address-7702-messages">
<legend class="fr-sr-only" id="address-7702-legend">
Adresse postale
</legend>
<div class="fr-fieldset__element">
<div class="fr-input-group" id="input-group-7703">
<label class="fr-label" for="name-7694">
Dénomination
</label>
<input class="fr-input" aria-describedby="name-7694-messages" name="organization-name" autocomplete="organization" id="name-7694" type="text">
<div class="fr-messages-group" id="name-7694-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-fieldset__element">
<div class="fr-input-group" id="input-group-7704">
<label class="fr-label" for="address-7695">
Adresse
<span class="fr-hint-text">Indication : numéro et voie</span>
</label>
<input class="fr-input" aria-describedby="address-7695-messages" name="address-line1" autocomplete="address-line1" id="address-7695" type="text">
<div class="fr-messages-group" id="address-7695-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-fieldset__element">
<div class="fr-input-group" id="input-group-7705">
<label class="fr-label" for="complement-7696">
Complément d'adresse (optionnel)
<span class="fr-hint-text">Indication : bâtiment, immeuble, escalier et numéro d'appartement</span>
</label>
<input class="fr-input" aria-describedby="complement-7696-messages" name="address-line2" autocomplete="address-line2" id="complement-7696" type="text">
<div class="fr-messages-group" id="complement-7696-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-fieldset__element">
<div class="fr-input-group" id="input-group-7706">
<label class="fr-label" for="locality-7697">
Lieu-dit, commune déléguée ou boîte postale
</label>
<input class="fr-input" aria-describedby="locality-7697-messages" name="address-level3" autocomplete="address-line3" id="locality-7697" type="text">
<div class="fr-messages-group" id="locality-7697-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-fieldset__element fr-fieldset__element--inline fr-fieldset__element--postal">
<div class="fr-input-group" id="input-group-7707">
<label class="fr-label" for="postal-7698">
Code postal
<span class="fr-hint-text">Format attendu : 5 chiffres</span>
</label>
<input class="fr-input" aria-describedby="postal-7698-messages" name="postal-code" autocomplete="postal-code" id="postal-7698" type="text">
<div class="fr-messages-group" id="postal-7698-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-fieldset__element fr-fieldset__element--inline@md fr-fieldset__element--inline-grow">
<div class="fr-input-group" id="input-group-7708">
<label class="fr-label" for="city-7699">
Ville ou commune
<span class="fr-hint-text">Exemple : Montpellier</span>
</label>
<input class="fr-input" aria-describedby="city-7699-messages" name="address-level2" autocomplete="address-level2" id="city-7699" type="text">
<div class="fr-messages-group" id="city-7699-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-fieldset__element">
<div class="fr-input-group" id="input-group-7709">
<label class="fr-label" for="cedex-7700">
Cedex
</label>
<input class="fr-input" aria-describedby="cedex-7700-messages" name="business-postal-code" autocomplete="cedex" id="cedex-7700" type="text">
<div class="fr-messages-group" id="cedex-7700-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-fieldset__element">
<div class="fr-select-group">
<label class="fr-label" for="country-7701">
Pays
</label>
<select class="fr-select" autocomplete="country" aria-describedby="country-7701-messages" id="country-7701" name="country">
<option value="" selected disabled>Sélectionner une option</option>
<option value="FR">France</option>
<option value="DE">Allemagne</option>
<option value="IT">Italie</option>
<option value="ES">Espagne</option>
<option value="GB">Royaume-Uni</option>
</select>
<div class="fr-messages-group" id="country-7701-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-messages-group" id="address-7702-messages" aria-live="polite">
</div>
</fieldset>


#### Demande d'un type de société


Type de société


Type de société


Sélectionner une option
Entrepreneur individuel (EI)
Entreprise unipersonnelle à responsabilité limitée (EURL)
Société à responsabilité limitée (SARL)
Société par actions simplifiée unipersonnelle (SASU)
Société par actions simplifiée (SAS)
Société anonyme (SA)
Société en nom collectif (SNC)
Société en commandite simple (SCS)
Société en commandite par actions (SCA)


###
Extrait de code


<fieldset class="fr-fieldset" id="structure-7713" aria-labelledby="structure-7713-legend structure-7713-messages">
<legend class="fr-sr-only" id="structure-7713-legend">
Type de société
</legend>
<div class="fr-fieldset__element">
<div class="fr-select-group">
<label class="fr-label" for="structure-7714">
Type de société
</label>
<select class="fr-select" aria-describedby="structure-7714-messages" id="structure-7714" name="structure">
<option value="" selected disabled>Sélectionner une option</option>
<option value="EI">Entrepreneur individuel (EI)</option>
<option value="EURL">Entreprise unipersonnelle à responsabilité limitée (EURL)</option>
<option value="SARL">Société à responsabilité limitée (SARL)</option>
<option value="SASU">Société par actions simplifiée unipersonnelle (SASU)</option>
<option value="SAS">Société par actions simplifiée (SAS)</option>
<option value="SA">Société anonyme (SA)</option>
<option value="SNC">Société en nom collectif (SNC)</option>
<option value="SCS">Société en commandite simple (SCS)</option>
<option value="SCA">Société en commandite par actions (SCA)</option>
</select>
<div class="fr-messages-group" id="structure-7714-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-messages-group" id="structure-7713-messages" aria-live="polite">
</div>
</fieldset>


#### Demande d'un représentant moral


Représentant moral de l'entreprise


Nom d'usage


Nom de naissance
Indication : nom de famille non rectifié après décision du tribunal.


Prénom


Fonction dans la société


###
Extrait de code


<fieldset class="fr-fieldset" id="representative-7729" aria-labelledby="representative-7729-legend representative-7729-messages">
<legend class="fr-sr-only" id="representative-7729-legend">
Représentant moral de l'entreprise
</legend>
<div class="fr-fieldset__element">
<div class="fr-input-group" id="input-group-7738">
<label class="fr-label" for="usual-7732">
Nom d'usage
</label>
<input class="fr-input" aria-describedby="usual-7732-messages" name="usual-name" autocomplete="family-name" id="usual-7732" spellcheck="false" type="text">
<div class="fr-messages-group" id="usual-7732-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-fieldset__element">
<div class="fr-input-group" id="input-group-7739">
<label class="fr-label" for="birth-7733">
Nom de naissance
<span class="fr-hint-text">Indication : nom de famille non rectifié après décision du tribunal.</span>
</label>
<input class="fr-input" aria-describedby="birth-7733-messages" name="birth-name" autocomplete="family-name" id="birth-7733" spellcheck="false" type="text">
<div class="fr-messages-group" id="birth-7733-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-fieldset__element">
<div class="fr-input-group" id="input-group-7740">
<label class="fr-label" for="givens-7735">
Prénom
</label>
<input class="fr-input" aria-describedby="givens-7735-messages" name="given-names" autocomplete="given-name" id="givens-7735" spellcheck="false" type="text">
<div class="fr-messages-group" id="givens-7735-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-fieldset__element">
<div class="fr-input-group" id="input-group-7741">
<label class="fr-label" for="representative-7737">
Fonction dans la société
</label>
<input class="fr-input" aria-describedby="representative-7737-messages" name="position" autocomplete="organization-title" id="representative-7737" type="text">
<div class="fr-messages-group" id="representative-7737-messages" aria-live="polite">
</div>
</div>
</div>
<div class="fr-messages-group" id="representative-7729-messages" aria-live="polite">
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
