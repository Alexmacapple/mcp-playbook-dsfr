URL:
https://main--ds-gouv.netlify.app/example/component/toggle

Title:
Interrupteur - Système de design

Markdown:

Interrupteur - Système de design


DSFR v1.14.0


[Retour](../)


# Interrupteur (toggle)


Le composant "Interrupteur" permet à l'utilisateur de faire un choix entre deux états opposés (activé / désactivé).
[Documentation](https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/interrupteur)


#### Toggle simple avec bouton + libellé à droite


Libellé de l'interrupteur


###
Extrait de code


<div class="fr-toggle">
<input type="checkbox" class="fr-toggle__input" id="toggle-3838" aria-describedby="toggle-3838-messages">
<label class="fr-toggle__label" for="toggle-3838">Libellé de l'interrupteur</label>
<div class="fr-messages-group" id="toggle-3838-messages" aria-live="polite">
</div>
</div>


#### Toggle simple avec bouton + libellé à droite + texte d'aide


Libellé de l'interrupteur


Texte de description additionnel


###
Extrait de code


<div class="fr-toggle">
<input type="checkbox" class="fr-toggle__input" id="toggle-3842" aria-describedby="toggle-hint-3843 toggle-3842-messages">
<label class="fr-toggle__label" for="toggle-3842">Libellé de l'interrupteur</label>
<p class="fr-hint-text" id="toggle-hint-3843">Texte de description additionnel</p>
<div class="fr-messages-group" id="toggle-3842-messages" aria-live="polite">
</div>
</div>


#### Toggle simple avec bouton + libellé à droite + état


Libellé de l'interrupteur


###
Extrait de code


<div class="fr-toggle">
<input type="checkbox" class="fr-toggle__input" id="toggle-3846" aria-describedby="toggle-3846-messages">
<label class="fr-toggle__label" for="toggle-3846" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé de l'interrupteur</label>
<div class="fr-messages-group" id="toggle-3846-messages" aria-live="polite">
</div>
</div>


#### Toggle simple avec bouton + libellé à droite + état + texte d'aide


Libellé de l'interrupteur


Texte de description additionnel


###
Extrait de code


<div class="fr-toggle">
<input type="checkbox" class="fr-toggle__input" id="toggle-3850" aria-describedby="toggle-hint-3851 toggle-3850-messages">
<label class="fr-toggle__label" for="toggle-3850" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé de l'interrupteur</label>
<p class="fr-hint-text" id="toggle-hint-3851">Texte de description additionnel</p>
<div class="fr-messages-group" id="toggle-3850-messages" aria-live="polite">
</div>
</div>


#### Toggle simple avec bouton + libellé à droite + état + séparateur


Libellé de l'interrupteur


###
Extrait de code


<div class="fr-toggle fr-toggle--border-bottom">
<input type="checkbox" class="fr-toggle__input" id="toggle-3854" aria-describedby="toggle-3854-messages">
<label class="fr-toggle__label" for="toggle-3854" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé de l'interrupteur</label>
<div class="fr-messages-group" id="toggle-3854-messages" aria-live="polite">
</div>
</div>


#### Toggle simple avec bouton + libellé à droite + état + séparateur + texte d'aide


Libellé de l'interrupteur


Texte de description additionnel


###
Extrait de code


<div class="fr-toggle fr-toggle--border-bottom">
<input type="checkbox" class="fr-toggle__input" id="toggle-3858" aria-describedby="toggle-hint-3859 toggle-3858-messages">
<label class="fr-toggle__label" for="toggle-3858" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé de l'interrupteur</label>
<p class="fr-hint-text" id="toggle-hint-3859">Texte de description additionnel</p>
<div class="fr-messages-group" id="toggle-3858-messages" aria-live="polite">
</div>
</div>


#### Toggle simple disabled avec bouton + libellé à droite


Libellé de l'interrupteur


###
Extrait de code


<div class="fr-toggle">
<input type="checkbox" class="fr-toggle__input" id="toggle-3862" disabled aria-describedby="toggle-3862-messages">
<label class="fr-toggle__label" for="toggle-3862">Libellé de l'interrupteur</label>
<div class="fr-messages-group" id="toggle-3862-messages" aria-live="polite">
</div>
</div>


#### Toggle simple disabled avec bouton + libellé à droite + état


Libellé de l'interrupteur


###
Extrait de code


<div class="fr-toggle">
<input type="checkbox" class="fr-toggle__input" id="toggle-3865" disabled aria-describedby="toggle-3865-messages">
<label class="fr-toggle__label" for="toggle-3865" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé de l'interrupteur</label>
<div class="fr-messages-group" id="toggle-3865-messages" aria-live="polite">
</div>
</div>


#### Toggle simple disabled et pré-coché avec bouton + libellé à droite + état


Libellé de l'interrupteur


###
Extrait de code


<div class="fr-toggle">
<input type="checkbox" class="fr-toggle__input" id="toggle-3868" disabled checked aria-describedby="toggle-3868-messages">
<label class="fr-toggle__label" for="toggle-3868" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé de l'interrupteur</label>
<div class="fr-messages-group" id="toggle-3868-messages" aria-live="polite">
</div>
</div>


#### Toggle simple en erreur


Libellé de l'interrupteur


Texte d'erreur obligatoire


###
Extrait de code


<div class="fr-toggle fr-toggle--error">
<input type="checkbox" class="fr-toggle__input" id="toggle-3871" aria-describedby="toggle-3871-messages">
<label class="fr-toggle__label" for="toggle-3871">Libellé de l'interrupteur</label>
<div class="fr-messages-group" id="toggle-3871-messages" aria-live="polite">
<p class="fr-message fr-message--error" id="toggle-3871-message-error">Texte d'erreur obligatoire</p>
</div>
</div>


#### Toggle avec état - en erreur


Libellé de l'interrupteur


Texte d'erreur obligatoire


###
Extrait de code


<div class="fr-toggle fr-toggle--error">
<input type="checkbox" class="fr-toggle__input" id="toggle-3874" aria-describedby="toggle-3874-messages">
<label class="fr-toggle__label" for="toggle-3874" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé de l'interrupteur</label>
<div class="fr-messages-group" id="toggle-3874-messages" aria-live="polite">
<p class="fr-message fr-message--error" id="toggle-3874-message-error">Texte d'erreur obligatoire</p>
</div>
</div>


#### Toggle simple valide


Libellé de l'interrupteur


Texte de validation


###
Extrait de code


<div class="fr-toggle fr-toggle--valid">
<input type="checkbox" class="fr-toggle__input" id="toggle-3877" aria-describedby="toggle-3877-messages">
<label class="fr-toggle__label" for="toggle-3877">Libellé de l'interrupteur</label>
<div class="fr-messages-group" id="toggle-3877-messages" aria-live="polite">
<p class="fr-message fr-message--valid" id="toggle-3877-message-valid">Texte de validation</p>
</div>
</div>


#### Toggle avec état - valide


Libellé de l'interrupteur


Texte de validation


###
Extrait de code


<div class="fr-toggle fr-toggle--valid">
<input type="checkbox" class="fr-toggle__input" id="toggle-3880" aria-describedby="toggle-3880-messages">
<label class="fr-toggle__label" for="toggle-3880" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé de l'interrupteur</label>
<div class="fr-messages-group" id="toggle-3880-messages" aria-live="polite">
<p class="fr-message fr-message--valid" id="toggle-3880-message-valid">Texte de validation</p>
</div>
</div>


#### Groupe de toggles simple avec bouton + libellé à droite


Légende pour l'ensemble des éléments


-


Libellé de l'interrupteur


-


Libellé de l'interrupteur


-


Libellé de l'interrupteur


-


Libellé de l'interrupteur


-


Libellé de l'interrupteur


###
Extrait de code


<fieldset class="fr-fieldset" id="toggle-group-3884" aria-labelledby="toggle-group-3884-legend toggle-group-3884-messages">
<legend class="fr-fieldset__legend" id="toggle-group-3884-legend">
Légende pour l'ensemble des éléments
</legend>
<div class="fr-fieldset__element">
<ul class="fr-toggle__list">
<li>
<div class="fr-toggle" id="group-1-toggle-38850">
<input type="checkbox" class="fr-toggle__input" id="toggle-38850" aria-describedby="toggle-38850-messages">
<label class="fr-toggle__label" for="toggle-38850">Libellé de l'interrupteur</label>
<div class="fr-messages-group" id="toggle-38850-messages" aria-live="polite">
</div>
</div>
</li>
<li>
<div class="fr-toggle" id="group-1-toggle-38851">
<input type="checkbox" class="fr-toggle__input" id="toggle-38851" aria-describedby="toggle-38851-messages">
<label class="fr-toggle__label" for="toggle-38851">Libellé de l'interrupteur</label>
<div class="fr-messages-group" id="toggle-38851-messages" aria-live="polite">
</div>
</div>
</li>
<li>
<div class="fr-toggle" id="group-1-toggle-38852">
<input type="checkbox" class="fr-toggle__input" id="toggle-38852" aria-describedby="toggle-38852-messages">
<label class="fr-toggle__label" for="toggle-38852">Libellé de l'interrupteur</label>
<div class="fr-messages-group" id="toggle-38852-messages" aria-live="polite">
</div>
</div>
</li>
<li>
<div class="fr-toggle" id="group-1-toggle-38853">
<input type="checkbox" class="fr-toggle__input" id="toggle-38853" aria-describedby="toggle-38853-messages">
<label class="fr-toggle__label" for="toggle-38853">Libellé de l'interrupteur</label>
<div class="fr-messages-group" id="toggle-38853-messages" aria-live="polite">
</div>
</div>
</li>
<li>
<div class="fr-toggle" id="group-1-toggle-38854">
<input type="checkbox" class="fr-toggle__input" id="toggle-38854" aria-describedby="toggle-38854-messages">
<label class="fr-toggle__label" for="toggle-38854">Libellé de l'interrupteur</label>
<div class="fr-messages-group" id="toggle-38854-messages" aria-live="polite">
</div>
</div>
</li>
</ul>
</div>
<div class="fr-messages-group" id="toggle-group-3884-messages" aria-live="polite">
</div>
</fieldset>


#### Groupe de toggles simple avec bouton + libellé à droite + séparateur


Légende pour l'ensemble des éléments


-


Libellé de l'interrupteur


-


Libellé de l'interrupteur


-


Libellé de l'interrupteur


-


Libellé de l'interrupteur


-


Libellé de l'interrupteur


###
Extrait de code


<fieldset class="fr-fieldset" id="toggle-group-3889" aria-labelledby="toggle-group-3889-legend toggle-group-3889-messages">
<legend class="fr-fieldset__legend" id="toggle-group-3889-legend">
Légende pour l'ensemble des éléments
</legend>
<div class="fr-fieldset__element">
<ul class="fr-toggle__list">
<li>
<div class="fr-toggle fr-toggle--border-bottom" id="group-2-toggle-38900">
<input type="checkbox" class="fr-toggle__input" id="toggle-38900" aria-describedby="toggle-38900-messages">
<label class="fr-toggle__label" for="toggle-38900">Libellé de l'interrupteur</label>
<div class="fr-messages-group" id="toggle-38900-messages" aria-live="polite">
</div>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom" id="group-2-toggle-38901">
<input type="checkbox" class="fr-toggle__input" id="toggle-38901" aria-describedby="toggle-38901-messages">
<label class="fr-toggle__label" for="toggle-38901">Libellé de l'interrupteur</label>
<div class="fr-messages-group" id="toggle-38901-messages" aria-live="polite">
</div>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom" id="group-2-toggle-38902">
<input type="checkbox" class="fr-toggle__input" id="toggle-38902" aria-describedby="toggle-38902-messages">
<label class="fr-toggle__label" for="toggle-38902">Libellé de l'interrupteur</label>
<div class="fr-messages-group" id="toggle-38902-messages" aria-live="polite">
</div>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom" id="group-2-toggle-38903">
<input type="checkbox" class="fr-toggle__input" id="toggle-38903" aria-describedby="toggle-38903-messages">
<label class="fr-toggle__label" for="toggle-38903">Libellé de l'interrupteur</label>
<div class="fr-messages-group" id="toggle-38903-messages" aria-live="polite">
</div>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom" id="group-2-toggle-38904">
<input type="checkbox" class="fr-toggle__input" id="toggle-38904" aria-describedby="toggle-38904-messages">
<label class="fr-toggle__label" for="toggle-38904">Libellé de l'interrupteur</label>
<div class="fr-messages-group" id="toggle-38904-messages" aria-live="polite">
</div>
</div>
</li>
</ul>
</div>
<div class="fr-messages-group" id="toggle-group-3889-messages" aria-live="polite">
</div>
</fieldset>


#### Groupe de toggles simple avec bouton + libellé à droite + séparateur + texte d'aide


Légende pour l'ensemble des éléments


-


Libellé de l'interrupteur


Texte de description additionnel


-


Libellé de l'interrupteur


Texte de description additionnel


-


Libellé de l'interrupteur


Texte de description additionnel


-


Libellé de l'interrupteur


Texte de description additionnel


-


Libellé de l'interrupteur


Texte de description additionnel


###
Extrait de code


<fieldset class="fr-fieldset" id="toggle-group-3899" aria-labelledby="toggle-group-3899-legend toggle-group-3899-messages">
<legend class="fr-fieldset__legend" id="toggle-group-3899-legend">
Légende pour l'ensemble des éléments
</legend>
<div class="fr-fieldset__element">
<ul class="fr-toggle__list">
<li>
<div class="fr-toggle fr-toggle--border-bottom" id="group-3-toggle-39000">
<input type="checkbox" class="fr-toggle__input" id="toggle-39000" aria-describedby="toggle-hint-3901 toggle-39000-messages">
<label class="fr-toggle__label" for="toggle-39000">Libellé de l'interrupteur</label>
<p class="fr-hint-text" id="toggle-hint-3901">Texte de description additionnel</p>
<div class="fr-messages-group" id="toggle-39000-messages" aria-live="polite">
</div>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom" id="group-3-toggle-39001">
<input type="checkbox" class="fr-toggle__input" id="toggle-39001" aria-describedby="toggle-hint-3902 toggle-39001-messages">
<label class="fr-toggle__label" for="toggle-39001">Libellé de l'interrupteur</label>
<p class="fr-hint-text" id="toggle-hint-3902">Texte de description additionnel</p>
<div class="fr-messages-group" id="toggle-39001-messages" aria-live="polite">
</div>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom" id="group-3-toggle-39002">
<input type="checkbox" class="fr-toggle__input" id="toggle-39002" aria-describedby="toggle-hint-3903 toggle-39002-messages">
<label class="fr-toggle__label" for="toggle-39002">Libellé de l'interrupteur</label>
<p class="fr-hint-text" id="toggle-hint-3903">Texte de description additionnel</p>
<div class="fr-messages-group" id="toggle-39002-messages" aria-live="polite">
</div>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom" id="group-3-toggle-39003">
<input type="checkbox" class="fr-toggle__input" id="toggle-39003" aria-describedby="toggle-hint-3904 toggle-39003-messages">
<label class="fr-toggle__label" for="toggle-39003">Libellé de l'interrupteur</label>
<p class="fr-hint-text" id="toggle-hint-3904">Texte de description additionnel</p>
<div class="fr-messages-group" id="toggle-39003-messages" aria-live="polite">
</div>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom" id="group-3-toggle-39004">
<input type="checkbox" class="fr-toggle__input" id="toggle-39004" aria-describedby="toggle-hint-3905 toggle-39004-messages">
<label class="fr-toggle__label" for="toggle-39004">Libellé de l'interrupteur</label>
<p class="fr-hint-text" id="toggle-hint-3905">Texte de description additionnel</p>
<div class="fr-messages-group" id="toggle-39004-messages" aria-live="polite">
</div>
</div>
</li>
</ul>
</div>
<div class="fr-messages-group" id="toggle-group-3899-messages" aria-live="polite">
</div>
</fieldset>


#### Groupe de toggles simple avec bouton + libellé à droite + état + séparateur


Légende pour l'ensemble des éléments


-


Libellé de l'interrupteur


-


Libellé de l'interrupteur


-


Libellé de l'interrupteur


-


Libellé de l'interrupteur


-


Libellé de l'interrupteur


###
Extrait de code


<fieldset class="fr-fieldset" id="toggle-group-3909" aria-labelledby="toggle-group-3909-legend toggle-group-3909-messages">
<legend class="fr-fieldset__legend" id="toggle-group-3909-legend">
Légende pour l'ensemble des éléments
</legend>
<div class="fr-fieldset__element">
<ul class="fr-toggle__list">
<li>
<div class="fr-toggle fr-toggle--border-bottom" id="group-4-toggle-39100">
<input type="checkbox" class="fr-toggle__input" id="toggle-39100" aria-describedby="toggle-39100-messages">
<label class="fr-toggle__label" for="toggle-39100" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé de l'interrupteur</label>
<div class="fr-messages-group" id="toggle-39100-messages" aria-live="polite">
</div>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom" id="group-4-toggle-39101">
<input type="checkbox" class="fr-toggle__input" id="toggle-39101" aria-describedby="toggle-39101-messages">
<label class="fr-toggle__label" for="toggle-39101" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé de l'interrupteur</label>
<div class="fr-messages-group" id="toggle-39101-messages" aria-live="polite">
</div>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom" id="group-4-toggle-39102">
<input type="checkbox" class="fr-toggle__input" id="toggle-39102" aria-describedby="toggle-39102-messages">
<label class="fr-toggle__label" for="toggle-39102" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé de l'interrupteur</label>
<div class="fr-messages-group" id="toggle-39102-messages" aria-live="polite">
</div>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom" id="group-4-toggle-39103">
<input type="checkbox" class="fr-toggle__input" id="toggle-39103" aria-describedby="toggle-39103-messages">
<label class="fr-toggle__label" for="toggle-39103" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé de l'interrupteur</label>
<div class="fr-messages-group" id="toggle-39103-messages" aria-live="polite">
</div>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom" id="group-4-toggle-39104">
<input type="checkbox" class="fr-toggle__input" id="toggle-39104" aria-describedby="toggle-39104-messages">
<label class="fr-toggle__label" for="toggle-39104" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé de l'interrupteur</label>
<div class="fr-messages-group" id="toggle-39104-messages" aria-live="polite">
</div>
</div>
</li>
</ul>
</div>
<div class="fr-messages-group" id="toggle-group-3909-messages" aria-live="polite">
</div>
</fieldset>


#### Groupe de toggles simple avec bouton + libellé à droite + état + séparateur + texte d'aide


Légende pour l'ensemble des éléments


-


Libellé de l'interrupteur


Texte de description additionnel


-


Libellé de l'interrupteur


Texte de description additionnel


-


Libellé de l'interrupteur


Texte de description additionnel


-


Libellé de l'interrupteur


Texte de description additionnel


-


Libellé de l'interrupteur


Texte de description additionnel


###
Extrait de code


<fieldset class="fr-fieldset" id="toggle-group-3919" aria-labelledby="toggle-group-3919-legend toggle-group-3919-messages">
<legend class="fr-fieldset__legend" id="toggle-group-3919-legend">
Légende pour l'ensemble des éléments
</legend>
<div class="fr-fieldset__element">
<ul class="fr-toggle__list">
<li>
<div class="fr-toggle fr-toggle--border-bottom" id="group-5-toggle-39200">
<input type="checkbox" class="fr-toggle__input" id="toggle-39200" aria-describedby="toggle-hint-3921 toggle-39200-messages">
<label class="fr-toggle__label" for="toggle-39200" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé de l'interrupteur</label>
<p class="fr-hint-text" id="toggle-hint-3921">Texte de description additionnel</p>
<div class="fr-messages-group" id="toggle-39200-messages" aria-live="polite">
</div>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom" id="group-5-toggle-39201">
<input type="checkbox" class="fr-toggle__input" id="toggle-39201" aria-describedby="toggle-hint-3922 toggle-39201-messages">
<label class="fr-toggle__label" for="toggle-39201" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé de l'interrupteur</label>
<p class="fr-hint-text" id="toggle-hint-3922">Texte de description additionnel</p>
<div class="fr-messages-group" id="toggle-39201-messages" aria-live="polite">
</div>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom" id="group-5-toggle-39202">
<input type="checkbox" class="fr-toggle__input" id="toggle-39202" aria-describedby="toggle-hint-3923 toggle-39202-messages">
<label class="fr-toggle__label" for="toggle-39202" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé de l'interrupteur</label>
<p class="fr-hint-text" id="toggle-hint-3923">Texte de description additionnel</p>
<div class="fr-messages-group" id="toggle-39202-messages" aria-live="polite">
</div>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom" id="group-5-toggle-39203">
<input type="checkbox" class="fr-toggle__input" id="toggle-39203" aria-describedby="toggle-hint-3924 toggle-39203-messages">
<label class="fr-toggle__label" for="toggle-39203" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé de l'interrupteur</label>
<p class="fr-hint-text" id="toggle-hint-3924">Texte de description additionnel</p>
<div class="fr-messages-group" id="toggle-39203-messages" aria-live="polite">
</div>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom" id="group-5-toggle-39204">
<input type="checkbox" class="fr-toggle__input" id="toggle-39204" aria-describedby="toggle-hint-3925 toggle-39204-messages">
<label class="fr-toggle__label" for="toggle-39204" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé de l'interrupteur</label>
<p class="fr-hint-text" id="toggle-hint-3925">Texte de description additionnel</p>
<div class="fr-messages-group" id="toggle-39204-messages" aria-live="polite">
</div>
</div>
</li>
</ul>
</div>
<div class="fr-messages-group" id="toggle-group-3919-messages" aria-live="polite">
</div>
</fieldset>


#### Groupe de toggles simple avec bouton + libellé à droite + état + séparateur + texte d'aide + erreur


Légende pour l'ensemble des éléments


-


Libellé de l'interrupteur


Texte de description additionnel


-


Libellé de l'interrupteur


Texte de description additionnel


-


Libellé de l'interrupteur


Texte de description additionnel


-


Libellé de l'interrupteur


Texte de description additionnel


-


Libellé de l'interrupteur


Texte de description additionnel


Texte d'erreur obligatoire


###
Extrait de code


<fieldset class="fr-fieldset fr-fieldset--error" id="toggle-group-3934" role="group" aria-labelledby="toggle-group-3934-legend toggle-group-3934-messages">
<legend class="fr-fieldset__legend" id="toggle-group-3934-legend">
Légende pour l'ensemble des éléments
</legend>
<div class="fr-fieldset__element">
<ul class="fr-toggle__list">
<li>
<div class="fr-toggle fr-toggle--border-bottom" id="group-6-toggle-39350">
<input type="checkbox" class="fr-toggle__input" id="toggle-39350" aria-describedby="toggle-hint-3936 toggle-39350-messages">
<label class="fr-toggle__label" for="toggle-39350" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé de l'interrupteur</label>
<p class="fr-hint-text" id="toggle-hint-3936">Texte de description additionnel</p>
<div class="fr-messages-group" id="toggle-39350-messages" aria-live="polite">
</div>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom" id="group-6-toggle-39351">
<input type="checkbox" class="fr-toggle__input" id="toggle-39351" aria-describedby="toggle-hint-3937 toggle-39351-messages">
<label class="fr-toggle__label" for="toggle-39351" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé de l'interrupteur</label>
<p class="fr-hint-text" id="toggle-hint-3937">Texte de description additionnel</p>
<div class="fr-messages-group" id="toggle-39351-messages" aria-live="polite">
</div>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom" id="group-6-toggle-39352">
<input type="checkbox" class="fr-toggle__input" id="toggle-39352" aria-describedby="toggle-hint-3938 toggle-39352-messages">
<label class="fr-toggle__label" for="toggle-39352" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé de l'interrupteur</label>
<p class="fr-hint-text" id="toggle-hint-3938">Texte de description additionnel</p>
<div class="fr-messages-group" id="toggle-39352-messages" aria-live="polite">
</div>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom" id="group-6-toggle-39353">
<input type="checkbox" class="fr-toggle__input" id="toggle-39353" aria-describedby="toggle-hint-3939 toggle-39353-messages">
<label class="fr-toggle__label" for="toggle-39353" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé de l'interrupteur</label>
<p class="fr-hint-text" id="toggle-hint-3939">Texte de description additionnel</p>
<div class="fr-messages-group" id="toggle-39353-messages" aria-live="polite">
</div>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom" id="group-6-toggle-39354">
<input type="checkbox" class="fr-toggle__input" id="toggle-39354" aria-describedby="toggle-hint-3940 toggle-39354-messages">
<label class="fr-toggle__label" for="toggle-39354" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé de l'interrupteur</label>
<p class="fr-hint-text" id="toggle-hint-3940">Texte de description additionnel</p>
<div class="fr-messages-group" id="toggle-39354-messages" aria-live="polite">
</div>
</div>
</li>
</ul>
</div>
<div class="fr-messages-group" id="toggle-group-3934-messages" aria-live="polite">
<p class="fr-message fr-message--error" id="toggle-group-3934-message-error">Texte d'erreur obligatoire</p>
</div>
</fieldset>


#### Groupe de toggles simple avec bouton + libellé à droite + état + séparateur + texte d'aide + valide


Légende pour l'ensemble des éléments


-


Libellé de l'interrupteur


Texte de description additionnel


-


Libellé de l'interrupteur


Texte de description additionnel


-


Libellé de l'interrupteur


Texte de description additionnel


-


Libellé de l'interrupteur


Texte de description additionnel


-


Libellé de l'interrupteur


Texte de description additionnel


Texte de validation


###
Extrait de code


<fieldset class="fr-fieldset fr-fieldset--valid" id="toggle-group-3949" role="group" aria-labelledby="toggle-group-3949-legend toggle-group-3949-messages">
<legend class="fr-fieldset__legend" id="toggle-group-3949-legend">
Légende pour l'ensemble des éléments
</legend>
<div class="fr-fieldset__element">
<ul class="fr-toggle__list">
<li>
<div class="fr-toggle fr-toggle--border-bottom" id="group-7-toggle-39500">
<input type="checkbox" class="fr-toggle__input" id="toggle-39500" aria-describedby="toggle-hint-3951 toggle-39500-messages">
<label class="fr-toggle__label" for="toggle-39500" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé de l'interrupteur</label>
<p class="fr-hint-text" id="toggle-hint-3951">Texte de description additionnel</p>
<div class="fr-messages-group" id="toggle-39500-messages" aria-live="polite">
</div>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom" id="group-7-toggle-39501">
<input type="checkbox" class="fr-toggle__input" id="toggle-39501" aria-describedby="toggle-hint-3952 toggle-39501-messages">
<label class="fr-toggle__label" for="toggle-39501" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé de l'interrupteur</label>
<p class="fr-hint-text" id="toggle-hint-3952">Texte de description additionnel</p>
<div class="fr-messages-group" id="toggle-39501-messages" aria-live="polite">
</div>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom" id="group-7-toggle-39502">
<input type="checkbox" class="fr-toggle__input" id="toggle-39502" aria-describedby="toggle-hint-3953 toggle-39502-messages">
<label class="fr-toggle__label" for="toggle-39502" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé de l'interrupteur</label>
<p class="fr-hint-text" id="toggle-hint-3953">Texte de description additionnel</p>
<div class="fr-messages-group" id="toggle-39502-messages" aria-live="polite">
</div>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom" id="group-7-toggle-39503">
<input type="checkbox" class="fr-toggle__input" id="toggle-39503" aria-describedby="toggle-hint-3954 toggle-39503-messages">
<label class="fr-toggle__label" for="toggle-39503" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé de l'interrupteur</label>
<p class="fr-hint-text" id="toggle-hint-3954">Texte de description additionnel</p>
<div class="fr-messages-group" id="toggle-39503-messages" aria-live="polite">
</div>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom" id="group-7-toggle-39504">
<input type="checkbox" class="fr-toggle__input" id="toggle-39504" aria-describedby="toggle-hint-3955 toggle-39504-messages">
<label class="fr-toggle__label" for="toggle-39504" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé de l'interrupteur</label>
<p class="fr-hint-text" id="toggle-hint-3955">Texte de description additionnel</p>
<div class="fr-messages-group" id="toggle-39504-messages" aria-live="polite">
</div>
</div>
</li>
</ul>
</div>
<div class="fr-messages-group" id="toggle-group-3949-messages" aria-live="polite">
<p class="fr-message fr-message--valid" id="toggle-group-3949-message-valid">Texte de validation</p>
</div>
</fieldset>


#### Toggle simple avec bouton + libellé à gauche


Libellé de l'interrupteur


###
Extrait de code


<div class="fr-toggle fr-toggle--label-left">
<input type="checkbox" class="fr-toggle__input" id="toggle-3958" aria-describedby="toggle-3958-messages">
<label class="fr-toggle__label" for="toggle-3958">Libellé de l'interrupteur</label>
<div class="fr-messages-group" id="toggle-3958-messages" aria-live="polite">
</div>
</div>


#### Toggle simple avec bouton + libellé à gauche + texte d'aide


Libellé de l'interrupteur


Texte de description additionnel


###
Extrait de code


<div class="fr-toggle fr-toggle--label-left">
<input type="checkbox" class="fr-toggle__input" id="toggle-3962" aria-describedby="toggle-hint-3963 toggle-3962-messages">
<label class="fr-toggle__label" for="toggle-3962">Libellé de l'interrupteur</label>
<p class="fr-hint-text" id="toggle-hint-3963">Texte de description additionnel</p>
<div class="fr-messages-group" id="toggle-3962-messages" aria-live="polite">
</div>
</div>


#### Toggle simple avec bouton + libellé à gauche + état


Libellé de l'interrupteur


###
Extrait de code


<div class="fr-toggle fr-toggle--label-left">
<input type="checkbox" class="fr-toggle__input" id="toggle-3966" aria-describedby="toggle-3966-messages">
<label class="fr-toggle__label" for="toggle-3966" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé de l'interrupteur</label>
<div class="fr-messages-group" id="toggle-3966-messages" aria-live="polite">
</div>
</div>


#### Toggle simple avec bouton + libellé à gauche + état + texte d'aide


Libellé de l'interrupteur


Texte de description additionnel


###
Extrait de code


<div class="fr-toggle fr-toggle--label-left">
<input type="checkbox" class="fr-toggle__input" id="toggle-3970" aria-describedby="toggle-hint-3971 toggle-3970-messages">
<label class="fr-toggle__label" for="toggle-3970" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé de l'interrupteur</label>
<p class="fr-hint-text" id="toggle-hint-3971">Texte de description additionnel</p>
<div class="fr-messages-group" id="toggle-3970-messages" aria-live="polite">
</div>
</div>


#### Toggle simple avec bouton + libellé à gauche + état + séparateur


Libellé de l'interrupteur


###
Extrait de code


<div class="fr-toggle fr-toggle--border-bottom fr-toggle--label-left">
<input type="checkbox" class="fr-toggle__input" id="toggle-3974" aria-describedby="toggle-3974-messages">
<label class="fr-toggle__label" for="toggle-3974" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé de l'interrupteur</label>
<div class="fr-messages-group" id="toggle-3974-messages" aria-live="polite">
</div>
</div>


#### Toggle simple avec bouton + libellé à gauche + état + séparateur + texte d'aide


Libellé de l'interrupteur


Texte de description additionnel


###
Extrait de code


<div class="fr-toggle fr-toggle--border-bottom fr-toggle--label-left">
<input type="checkbox" class="fr-toggle__input" id="toggle-3978" aria-describedby="toggle-hint-3979 toggle-3978-messages">
<label class="fr-toggle__label" for="toggle-3978" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé de l'interrupteur</label>
<p class="fr-hint-text" id="toggle-hint-3979">Texte de description additionnel</p>
<div class="fr-messages-group" id="toggle-3978-messages" aria-live="polite">
</div>
</div>


#### Toggle simple disabled avec bouton + libellé à gauche


Libellé de l'interrupteur


###
Extrait de code


<div class="fr-toggle fr-toggle--label-left">
<input type="checkbox" class="fr-toggle__input" id="toggle-3982" disabled aria-describedby="toggle-3982-messages">
<label class="fr-toggle__label" for="toggle-3982">Libellé de l'interrupteur</label>
<div class="fr-messages-group" id="toggle-3982-messages" aria-live="polite">
</div>
</div>


#### Toggle simple disabled avec bouton + libellé à gauche + état


Libellé de l'interrupteur


###
Extrait de code


<div class="fr-toggle fr-toggle--label-left">
<input type="checkbox" class="fr-toggle__input" id="toggle-3985" disabled aria-describedby="toggle-3985-messages">
<label class="fr-toggle__label" for="toggle-3985" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé de l'interrupteur</label>
<div class="fr-messages-group" id="toggle-3985-messages" aria-live="polite">
</div>
</div>


#### Groupe de toggles simple avec bouton + libellé à gauche + séparateur


Légende pour l'ensemble des éléments


-


Libellé de l'interrupteur


-


Libellé de l'interrupteur


-


Libellé de l'interrupteur


-


Libellé de l'interrupteur


-


Libellé de l'interrupteur


###
Extrait de code


<fieldset class="fr-fieldset" id="toggle-group-3989" aria-labelledby="toggle-group-3989-legend toggle-group-3989-messages">
<legend class="fr-fieldset__legend" id="toggle-group-3989-legend">
Légende pour l'ensemble des éléments
</legend>
<div class="fr-fieldset__element">
<ul class="fr-toggle__list">
<li>
<div class="fr-toggle fr-toggle--border-bottom fr-toggle--label-left" id="group-8-toggle-39900">
<input type="checkbox" class="fr-toggle__input" id="toggle-39900" aria-describedby="toggle-39900-messages">
<label class="fr-toggle__label" for="toggle-39900">Libellé de l'interrupteur</label>
<div class="fr-messages-group" id="toggle-39900-messages" aria-live="polite">
</div>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom fr-toggle--label-left" id="group-8-toggle-39901">
<input type="checkbox" class="fr-toggle__input" id="toggle-39901" aria-describedby="toggle-39901-messages">
<label class="fr-toggle__label" for="toggle-39901">Libellé de l'interrupteur</label>
<div class="fr-messages-group" id="toggle-39901-messages" aria-live="polite">
</div>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom fr-toggle--label-left" id="group-8-toggle-39902">
<input type="checkbox" class="fr-toggle__input" id="toggle-39902" aria-describedby="toggle-39902-messages">
<label class="fr-toggle__label" for="toggle-39902">Libellé de l'interrupteur</label>
<div class="fr-messages-group" id="toggle-39902-messages" aria-live="polite">
</div>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom fr-toggle--label-left" id="group-8-toggle-39903">
<input type="checkbox" class="fr-toggle__input" id="toggle-39903" aria-describedby="toggle-39903-messages">
<label class="fr-toggle__label" for="toggle-39903">Libellé de l'interrupteur</label>
<div class="fr-messages-group" id="toggle-39903-messages" aria-live="polite">
</div>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom fr-toggle--label-left" id="group-8-toggle-39904">
<input type="checkbox" class="fr-toggle__input" id="toggle-39904" aria-describedby="toggle-39904-messages">
<label class="fr-toggle__label" for="toggle-39904">Libellé de l'interrupteur</label>
<div class="fr-messages-group" id="toggle-39904-messages" aria-live="polite">
</div>
</div>
</li>
</ul>
</div>
<div class="fr-messages-group" id="toggle-group-3989-messages" aria-live="polite">
</div>
</fieldset>


#### Groupe de toggles simple avec bouton + libellé à gauche + séparateur + texte d'aide


Légende pour l'ensemble des éléments


-


Libellé de l'interrupteur


Texte de description additionnel


-


Libellé de l'interrupteur


Texte de description additionnel


-


Libellé de l'interrupteur


Texte de description additionnel


-


Libellé de l'interrupteur


Texte de description additionnel


-


Libellé de l'interrupteur


Texte de description additionnel


###
Extrait de code


<fieldset class="fr-fieldset" id="toggle-group-3999" aria-labelledby="toggle-group-3999-legend toggle-group-3999-messages">
<legend class="fr-fieldset__legend" id="toggle-group-3999-legend">
Légende pour l'ensemble des éléments
</legend>
<div class="fr-fieldset__element">
<ul class="fr-toggle__list">
<li>
<div class="fr-toggle fr-toggle--border-bottom fr-toggle--label-left" id="group-9-toggle-40000">
<input type="checkbox" class="fr-toggle__input" id="toggle-40000" aria-describedby="toggle-hint-4001 toggle-40000-messages">
<label class="fr-toggle__label" for="toggle-40000">Libellé de l'interrupteur</label>
<p class="fr-hint-text" id="toggle-hint-4001">Texte de description additionnel</p>
<div class="fr-messages-group" id="toggle-40000-messages" aria-live="polite">
</div>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom fr-toggle--label-left" id="group-9-toggle-40001">
<input type="checkbox" class="fr-toggle__input" id="toggle-40001" aria-describedby="toggle-hint-4002 toggle-40001-messages">
<label class="fr-toggle__label" for="toggle-40001">Libellé de l'interrupteur</label>
<p class="fr-hint-text" id="toggle-hint-4002">Texte de description additionnel</p>
<div class="fr-messages-group" id="toggle-40001-messages" aria-live="polite">
</div>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom fr-toggle--label-left" id="group-9-toggle-40002">
<input type="checkbox" class="fr-toggle__input" id="toggle-40002" aria-describedby="toggle-hint-4003 toggle-40002-messages">
<label class="fr-toggle__label" for="toggle-40002">Libellé de l'interrupteur</label>
<p class="fr-hint-text" id="toggle-hint-4003">Texte de description additionnel</p>
<div class="fr-messages-group" id="toggle-40002-messages" aria-live="polite">
</div>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom fr-toggle--label-left" id="group-9-toggle-40003">
<input type="checkbox" class="fr-toggle__input" id="toggle-40003" aria-describedby="toggle-hint-4004 toggle-40003-messages">
<label class="fr-toggle__label" for="toggle-40003">Libellé de l'interrupteur</label>
<p class="fr-hint-text" id="toggle-hint-4004">Texte de description additionnel</p>
<div class="fr-messages-group" id="toggle-40003-messages" aria-live="polite">
</div>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom fr-toggle--label-left" id="group-9-toggle-40004">
<input type="checkbox" class="fr-toggle__input" id="toggle-40004" aria-describedby="toggle-hint-4005 toggle-40004-messages">
<label class="fr-toggle__label" for="toggle-40004">Libellé de l'interrupteur</label>
<p class="fr-hint-text" id="toggle-hint-4005">Texte de description additionnel</p>
<div class="fr-messages-group" id="toggle-40004-messages" aria-live="polite">
</div>
</div>
</li>
</ul>
</div>
<div class="fr-messages-group" id="toggle-group-3999-messages" aria-live="polite">
</div>
</fieldset>


#### Groupe de toggles simple avec bouton + libellé à gauche + état + séparateur


Légende pour l'ensemble des éléments


-


Libellé de l'interrupteur


-


Libellé de l'interrupteur


-


Libellé de l'interrupteur


-


Libellé de l'interrupteur


-


Libellé de l'interrupteur


###
Extrait de code


<fieldset class="fr-fieldset" id="toggle-group-4009" aria-labelledby="toggle-group-4009-legend toggle-group-4009-messages">
<legend class="fr-fieldset__legend" id="toggle-group-4009-legend">
Légende pour l'ensemble des éléments
</legend>
<div class="fr-fieldset__element">
<ul class="fr-toggle__list">
<li>
<div class="fr-toggle fr-toggle--border-bottom fr-toggle--label-left" id="group-10-toggle-40100">
<input type="checkbox" class="fr-toggle__input" id="toggle-40100" aria-describedby="toggle-40100-messages">
<label class="fr-toggle__label" for="toggle-40100" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé de l'interrupteur</label>
<div class="fr-messages-group" id="toggle-40100-messages" aria-live="polite">
</div>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom fr-toggle--label-left" id="group-10-toggle-40101">
<input type="checkbox" class="fr-toggle__input" id="toggle-40101" aria-describedby="toggle-40101-messages">
<label class="fr-toggle__label" for="toggle-40101" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé de l'interrupteur</label>
<div class="fr-messages-group" id="toggle-40101-messages" aria-live="polite">
</div>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom fr-toggle--label-left" id="group-10-toggle-40102">
<input type="checkbox" class="fr-toggle__input" id="toggle-40102" aria-describedby="toggle-40102-messages">
<label class="fr-toggle__label" for="toggle-40102" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé de l'interrupteur</label>
<div class="fr-messages-group" id="toggle-40102-messages" aria-live="polite">
</div>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom fr-toggle--label-left" id="group-10-toggle-40103">
<input type="checkbox" class="fr-toggle__input" id="toggle-40103" aria-describedby="toggle-40103-messages">
<label class="fr-toggle__label" for="toggle-40103" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé de l'interrupteur</label>
<div class="fr-messages-group" id="toggle-40103-messages" aria-live="polite">
</div>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom fr-toggle--label-left" id="group-10-toggle-40104">
<input type="checkbox" class="fr-toggle__input" id="toggle-40104" aria-describedby="toggle-40104-messages">
<label class="fr-toggle__label" for="toggle-40104" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé de l'interrupteur</label>
<div class="fr-messages-group" id="toggle-40104-messages" aria-live="polite">
</div>
</div>
</li>
</ul>
</div>
<div class="fr-messages-group" id="toggle-group-4009-messages" aria-live="polite">
</div>
</fieldset>


#### Groupe de toggles simple avec bouton + libellé à gauche + état + séparateur + texte d'aide


Légende pour l'ensemble des éléments


-


Libellé de l'interrupteur


Texte de description additionnel


-


Libellé de l'interrupteur


Texte de description additionnel


-


Libellé de l'interrupteur


Texte de description additionnel


-


Libellé de l'interrupteur


Texte de description additionnel


-


Libellé de l'interrupteur


Texte de description additionnel


###
Extrait de code


<fieldset class="fr-fieldset" id="toggle-group-4019" aria-labelledby="toggle-group-4019-legend toggle-group-4019-messages">
<legend class="fr-fieldset__legend" id="toggle-group-4019-legend">
Légende pour l'ensemble des éléments
</legend>
<div class="fr-fieldset__element">
<ul class="fr-toggle__list">
<li>
<div class="fr-toggle fr-toggle--border-bottom fr-toggle--label-left" id="group-11-toggle-40200">
<input type="checkbox" class="fr-toggle__input" id="toggle-40200" aria-describedby="toggle-hint-4021 toggle-40200-messages">
<label class="fr-toggle__label" for="toggle-40200" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé de l'interrupteur</label>
<p class="fr-hint-text" id="toggle-hint-4021">Texte de description additionnel</p>
<div class="fr-messages-group" id="toggle-40200-messages" aria-live="polite">
</div>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom fr-toggle--label-left" id="group-11-toggle-40201">
<input type="checkbox" class="fr-toggle__input" id="toggle-40201" aria-describedby="toggle-hint-4022 toggle-40201-messages">
<label class="fr-toggle__label" for="toggle-40201" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé de l'interrupteur</label>
<p class="fr-hint-text" id="toggle-hint-4022">Texte de description additionnel</p>
<div class="fr-messages-group" id="toggle-40201-messages" aria-live="polite">
</div>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom fr-toggle--label-left" id="group-11-toggle-40202">
<input type="checkbox" class="fr-toggle__input" id="toggle-40202" aria-describedby="toggle-hint-4023 toggle-40202-messages">
<label class="fr-toggle__label" for="toggle-40202" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé de l'interrupteur</label>
<p class="fr-hint-text" id="toggle-hint-4023">Texte de description additionnel</p>
<div class="fr-messages-group" id="toggle-40202-messages" aria-live="polite">
</div>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom fr-toggle--label-left" id="group-11-toggle-40203">
<input type="checkbox" class="fr-toggle__input" id="toggle-40203" aria-describedby="toggle-hint-4024 toggle-40203-messages">
<label class="fr-toggle__label" for="toggle-40203" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé de l'interrupteur</label>
<p class="fr-hint-text" id="toggle-hint-4024">Texte de description additionnel</p>
<div class="fr-messages-group" id="toggle-40203-messages" aria-live="polite">
</div>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom fr-toggle--label-left" id="group-11-toggle-40204">
<input type="checkbox" class="fr-toggle__input" id="toggle-40204" aria-describedby="toggle-hint-4025 toggle-40204-messages">
<label class="fr-toggle__label" for="toggle-40204" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé de l'interrupteur</label>
<p class="fr-hint-text" id="toggle-hint-4025">Texte de description additionnel</p>
<div class="fr-messages-group" id="toggle-40204-messages" aria-live="polite">
</div>
</div>
</li>
</ul>
</div>
<div class="fr-messages-group" id="toggle-group-4019-messages" aria-live="polite">
</div>
</fieldset>


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
