URL:
https://main--ds-gouv.netlify.app/example/component/password

Title:
Mot de passe - Système de design

Markdown:

Mot de passe - Système de design


DSFR v1.14.0


[Retour](../)


# Mot de passe (password)


La demande de mot de passe permet d'aider un utilisateur à créer ou saisir un mot de passe.
[Documentation](https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/mot-de-passe)


### Mot de passe


Mot de passe


Votre mot de passe doit contenir :


12 caractères minimum


1 caractère spécial minimum


1 chiffre minimum


Afficher


###
Extrait de code


<div class="fr-password" id="password-5803">
<label class="fr-password__label fr-label" for="password-5803-input">
Mot de passe
</label>
<div class="fr-input-wrap">
<input class="fr-password__input fr-input" autocapitalize="off" autocorrect="off" aria-describedby="password-5803-input-messages" aria-required="true" name="password" autocomplete="new-password" id="password-5803-input" type="password">
</div>
<div class="fr-messages-group" id="password-5803-input-messages" aria-live="polite">
<p class="fr-message" id="password-5803-input-message">Votre mot de passe doit contenir :</p>
<p class="fr-message fr-message--info" data-fr-valid="validé" data-fr-error="en erreur" id="password-5803-input-message-info">12 caractères minimum</p>
<p class="fr-message fr-message--info" data-fr-valid="validé" data-fr-error="en erreur" id="password-5803-input-message-info-1">1 caractère spécial minimum</p>
<p class="fr-message fr-message--info" data-fr-valid="validé" data-fr-error="en erreur" id="password-5803-input-message-info-2">1 chiffre minimum</p>
</div>
<div class="fr-password__checkbox fr-checkbox-group fr-checkbox-group--sm">
<input aria-label="Afficher le mot de passe" id="password-5803-show" type="checkbox">
<label class="fr--password__checkbox fr-label" for="password-5803-show">
Afficher
</label>
</div>
</div>


### Mot de passe avec description


Mot de passe
Texte de description additionnel


Votre mot de passe doit contenir :


12 caractères minimum


1 caractère spécial minimum


1 chiffre minimum


Afficher


###
Extrait de code


<div class="fr-password" id="password-5806">
<label class="fr-password__label fr-label" for="password-5806-input">
Mot de passe
<span class="fr-hint-text">Texte de description additionnel</span>
</label>
<div class="fr-input-wrap">
<input class="fr-password__input fr-input" autocapitalize="off" autocorrect="off" aria-describedby="password-5806-input-messages" aria-required="true" name="password" autocomplete="new-password" id="password-5806-input" type="password">
</div>
<div class="fr-messages-group" id="password-5806-input-messages" aria-live="polite">
<p class="fr-message" id="password-5806-input-message">Votre mot de passe doit contenir :</p>
<p class="fr-message fr-message--info" data-fr-valid="validé" data-fr-error="en erreur" id="password-5806-input-message-info">12 caractères minimum</p>
<p class="fr-message fr-message--info" data-fr-valid="validé" data-fr-error="en erreur" id="password-5806-input-message-info-1">1 caractère spécial minimum</p>
<p class="fr-message fr-message--info" data-fr-valid="validé" data-fr-error="en erreur" id="password-5806-input-message-info-2">1 chiffre minimum</p>
</div>
<div class="fr-password__checkbox fr-checkbox-group fr-checkbox-group--sm">
<input aria-label="Afficher le mot de passe" id="password-5806-show" type="checkbox">
<label class="fr--password__checkbox fr-label" for="password-5806-show">
Afficher
</label>
</div>
</div>


### Mot de passe après validation


Mot de passe


Votre mot de passe doit contenir :


12 caractères minimum


1 caractère spécial minimum


1 chiffre minimum


Afficher


###
Extrait de code


<div class="fr-password" id="password-5809">
<label class="fr-password__label fr-label" for="password-5809-input">
Mot de passe
</label>
<div class="fr-input-wrap">
<input class="fr-password__input fr-input" autocapitalize="off" autocorrect="off" aria-describedby="password-5809-input-messages" aria-required="true" name="password" value="x8A@" autocomplete="new-password" id="password-5809-input" type="password">
</div>
<div class="fr-messages-group" id="password-5809-input-messages" aria-live="polite">
<p class="fr-message" id="password-5809-input-message">Votre mot de passe doit contenir :</p>
<p class="fr-message fr-message--error" data-fr-valid="validé" data-fr-error="en erreur" id="password-5809-input-message-error">12 caractères minimum</p>
<p class="fr-message fr-message--valid" data-fr-valid="validé" data-fr-error="en erreur" id="password-5809-input-message-valid">1 caractère spécial minimum</p>
<p class="fr-message fr-message--valid" data-fr-valid="validé" data-fr-error="en erreur" id="password-5809-input-message-valid-1">1 chiffre minimum</p>
</div>
<div class="fr-password__checkbox fr-checkbox-group fr-checkbox-group--sm">
<input aria-label="Afficher le mot de passe" id="password-5809-show" type="checkbox">
<label class="fr--password__checkbox fr-label" for="password-5809-show">
Afficher
</label>
</div>
</div>


### Mot de passe de connexion


Mot de passe


Afficher


[Mot de passe oublié ?](%5B%C3%80%20MODIFIER%20-%20url%20de%20la%20page%20de%20r%C3%A9cup%C3%A9ration%5D)


###
Extrait de code


<div class="fr-password" id="password-5812">
<label class="fr-password__label fr-label" for="password-5812-input">
Mot de passe
</label>
<div class="fr-input-wrap">
<input class="fr-password__input fr-input" autocapitalize="off" autocorrect="off" aria-describedby="password-5812-input-messages" aria-required="true" name="password" autocomplete="current-password" id="password-5812-input" type="password">
</div>
<div class="fr-messages-group" id="password-5812-input-messages" aria-live="polite">
</div>
<div class="fr-password__checkbox fr-checkbox-group fr-checkbox-group--sm">
<input aria-label="Afficher le mot de passe" id="password-5812-show" type="checkbox">
<label class="fr--password__checkbox fr-label" for="password-5812-show">
Afficher
</label>
</div>
<p>
<a href="[À MODIFIER - url de la page de récupération]" class="fr-link">Mot de passe oublié ?</a>
</p>
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
