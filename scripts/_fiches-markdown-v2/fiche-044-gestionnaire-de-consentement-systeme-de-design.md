URL:
https://main--ds-gouv.netlify.app/example/component/consent

Title:
Gestionnaire de consentement - Système de design

Markdown:

Gestionnaire de consentement - Système de design


DSFR v1.14.0


[Retour](../)


# Gestionnaire de consentement (consent)


Le gestionnaire de consentement permet à l'utilisateur de définir ses préférences sur l'utilisation de ses données personnelles.
[Documentation](https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/gestionnaire-de-consentement)


### Gestionnaire de consentement


## À propos des cookies sur nomdusite.fr


Bienvenue ! Nous utilisons des cookies pour améliorer votre expérience et les services disponibles sur ce site. Pour en savoir plus, visitez la page . Vous pouvez, à tout moment, avoir le contrôle sur les cookies que vous souhaitez activer.


-
Tout accepter


-
Tout refuser


-
Personnaliser


###
Extrait de code


<div class="fr-consent-banner">
<h2 class="fr-h6">À propos des cookies sur nomdusite.fr</h2>
<div class="fr-consent-banner__content">
<p class="fr-text--sm">Bienvenue ! Nous utilisons des cookies pour améliorer votre expérience et les services disponibles sur ce site. Pour en savoir plus, visitez la page <a href="">Données personnelles et cookies</a>. Vous pouvez, à tout moment, avoir le contrôle sur les cookies que vous souhaitez activer.</p>
</div>
<ul class="fr-consent-banner__buttons fr-btns-group fr-btns-group--right fr-btns-group--inline-reverse fr-btns-group--inline-sm">
<li>
<button title="Autoriser tous les cookies" type="button" class="fr-btn">Tout accepter</button>
</li>
<li>
<button title="Refuser tous les cookies" type="button" class="fr-btn">Tout refuser</button>
</li>
<li>
<button data-fr-opened="false" aria-controls="fr-consent-modal" title="Personnaliser les cookies" type="button" class="fr-btn fr-btn--secondary">Personnaliser</button>
</li>
</ul>
</div>


### Panneau de gestion des cookies


Fermer


##
Panneau de gestion des cookies


Préférences pour tous les services.


Tout accepter


Tout refuser


Cookies obligatoires


Accepter


Refuser


Ce site utilise des cookies nécessaires à son bon fonctionnement qui ne peuvent pas être désactivés.


Nom de la finalité


Accepter


Refuser


Description optionnelle de la finalité, lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi in suscipit nulla, et pulvinar velit.


Voir plus de détails


Sous finalité 1


Accepter


Refuser


Sous finalité 2


Accepter


Refuser


Ce service utilise 3 cookies.


Sous finalité 3


Accepter


Refuser


Nom de la finalité


Accepter


Refuser


Description optionnelle de la finalité, lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi in suscipit nulla, et pulvinar velit.


Voir plus de détails


Sous finalité 1


Accepter


Refuser


Sous finalité 2


Accepter


Refuser


Ce service utilise 3 cookies.


Sous finalité 3


Accepter


Refuser


-
Confirmer mes choix


###
Extrait de code


<dialog id="fr-consent-modal" class="fr-modal" aria-labelledby="fr-consent-modal-title">
<div class="fr-container fr-container--fluid fr-container-md">
<div class="fr-grid-row fr-grid-row--center">
<div class="fr-col-12 fr-col-md-10 fr-col-lg-8">
<div class="fr-modal__body">
<div class="fr-modal__header">
<button aria-controls="fr-consent-modal" title="Fermer" type="button" id="button-3783" class="fr-btn--close fr-btn">Fermer</button>
</div>
<div class="fr-modal__content">
<h2 id="fr-consent-modal-title" class="fr-modal__title">
Panneau de gestion des cookies
</h2>
<div class="fr-consent-manager">
<!-- Finalités -->
<div class="fr-consent-service fr-consent-manager__header">
<fieldset class="fr-fieldset">
<legend id="finality-legend" class="fr-consent-service__title">Préférences pour tous les services. <a href="">Données personnelles et cookies</a>
</legend>
<div class="fr-consent-service__radios">
<div class="fr-radio-group">
<input type="radio" id="consent-all-accept" name="consent-all">
<label class="fr-label" for="consent-all-accept">
Tout accepter
</label>
</div>
<div class="fr-radio-group">
<input type="radio" id="consent-all-refuse" name="consent-all">
<label class="fr-label" for="consent-all-refuse">
Tout refuser
</label>
</div>
</div>
</fieldset>
</div>
<div class="fr-consent-service">
<fieldset aria-labelledby="finality-0-legend finality-0-desc" role="group" class="fr-fieldset">
<legend id="finality-0-legend" class="fr-consent-service__title">Cookies obligatoires</legend>
<div class="fr-consent-service__radios">
<div class="fr-radio-group">
<input checked type="radio" id="consent-finality-0-accept" name="consent-finality-0">
<label class="fr-label" for="consent-finality-0-accept">
Accepter
</label>
</div>
<div class="fr-radio-group">
<input disabled type="radio" id="consent-finality-0-refuse" name="consent-finality-0">
<label class="fr-label" for="consent-finality-0-refuse">
Refuser
</label>
</div>
</div>
<p id="finality-0-desc" class="fr-consent-service__desc">Ce site utilise des cookies nécessaires à son bon fonctionnement qui ne peuvent pas être désactivés.</p>
</fieldset>
</div>
<div class="fr-consent-service">
<fieldset aria-labelledby="finality-1-legend finality-1-desc" role="group" class="fr-fieldset">
<legend id="finality-1-legend" class="fr-consent-service__title">Nom de la finalité</legend>
<div class="fr-consent-service__radios">
<div class="fr-radio-group">
<input type="radio" id="consent-finality-1-accept" name="consent-finality-1">
<label class="fr-label" for="consent-finality-1-accept">
Accepter
</label>
</div>
<div class="fr-radio-group">
<input type="radio" id="consent-finality-1-refuse" name="consent-finality-1">
<label class="fr-label" for="consent-finality-1-refuse">
Refuser
</label>
</div>
</div>
<p id="finality-1-desc" class="fr-consent-service__desc">Description optionnelle de la finalité, lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi in suscipit nulla, et pulvinar velit.</p>
<div class="fr-consent-service__collapse">
<button type="button" class="fr-consent-service__collapse-btn" aria-expanded="false" aria-describedby="finality-1-legend" aria-controls="finality-1-collapse"> Voir plus de détails</button>
</div>
<div class="fr-consent-services fr-collapse" id="finality-1-collapse">
<!-- Sous finalités -->
<div class="fr-consent-service">
<fieldset class="fr-fieldset fr-fieldset--inline">
<legend id="finality-1-service-1-legend" class="fr-consent-service__title">Sous finalité 1</legend>
<div class="fr-consent-service__radios fr-fieldset--inline">
<div class="fr-radio-group">
<input type="radio" id="consent-finality-1-service-1-accept" name="consent-finality-1-service-1">
<label class="fr-label" for="consent-finality-1-service-1-accept">
Accepter
</label>
</div>
<div class="fr-radio-group">
<input type="radio" id="consent-finality-1-service-1-refuse" name="consent-finality-1-service-1">
<label class="fr-label" for="consent-finality-1-service-1-refuse">
Refuser
</label>
</div>
</div>
</fieldset>
</div>
<div class="fr-consent-service">
<fieldset aria-labelledby="finality-1-service-2-legend finality-1-service-2-desc" role="group" class="fr-fieldset fr-fieldset--inline">
<legend id="finality-1-service-2-legend" class="fr-consent-service__title" aria-describedby="finality-1-service-2-desc">Sous finalité 2</legend>
<div class="fr-consent-service__radios fr-fieldset--inline">
<div class="fr-radio-group">
<input type="radio" id="consent-finality-1-service-2-accept" name="consent-finality-1-service-2">
<label class="fr-label" for="consent-finality-1-service-2-accept">
Accepter
</label>
</div>
<div class="fr-radio-group">
<input type="radio" id="consent-finality-1-service-2-refuse" name="consent-finality-1-service-2">
<label class="fr-label" for="consent-finality-1-service-2-refuse">
Refuser
</label>
</div>
</div>
<p id="finality-1-service-2-desc" class="fr-consent-service__desc">Ce service utilise 3 cookies.</p>
</fieldset>
</div>
<div class="fr-consent-service">
<fieldset class="fr-fieldset fr-fieldset--inline">
<legend id="finality-1-service-3-legend" class="fr-consent-service__title">Sous finalité 3</legend>
<div class="fr-consent-service__radios fr-fieldset--inline">
<div class="fr-radio-group">
<input type="radio" id="consent-finality-1-service-3-accept" name="consent-finality-1-service-3">
<label class="fr-label" for="consent-finality-1-service-3-accept">
Accepter
</label>
</div>
<div class="fr-radio-group">
<input type="radio" id="consent-finality-1-service-3-refuse" name="consent-finality-1-service-3">
<label class="fr-label" for="consent-finality-1-service-3-refuse">
Refuser
</label>
</div>
</div>
</fieldset>
</div>
</div>
</fieldset>
</div>
<div class="fr-consent-service">
<fieldset aria-labelledby="finality-2-legend finality-2-desc" role="group" class="fr-fieldset">
<legend id="finality-2-legend" class="fr-consent-service__title">Nom de la finalité</legend>
<div class="fr-consent-service__radios">
<div class="fr-radio-group">
<input type="radio" id="consent-finality-2-accept" name="consent-finality-2">
<label class="fr-label" for="consent-finality-2-accept">
Accepter
</label>
</div>
<div class="fr-radio-group">
<input type="radio" id="consent-finality-2-refuse" name="consent-finality-2">
<label class="fr-label" for="consent-finality-2-refuse">
Refuser
</label>
</div>
</div>
<p id="finality-2-desc" class="fr-consent-service__desc">Description optionnelle de la finalité, lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi in suscipit nulla, et pulvinar velit.</p>
<div class="fr-consent-service__collapse">
<button type="button" class="fr-consent-service__collapse-btn" aria-expanded="false" aria-describedby="finality-2-legend" aria-controls="finality-2-collapse"> Voir plus de détails</button>
</div>
<div class="fr-consent-services fr-collapse" id="finality-2-collapse">
<!-- Sous finalités -->
<div class="fr-consent-service">
<fieldset class="fr-fieldset fr-fieldset--inline">
<legend id="finality-2-service-1-legend" class="fr-consent-service__title">Sous finalité 1</legend>
<div class="fr-consent-service__radios fr-fieldset--inline">
<div class="fr-radio-group">
<input type="radio" id="consent-finality-2-service-1-accept" name="consent-finality-2-service-1">
<label class="fr-label" for="consent-finality-2-service-1-accept">
Accepter
</label>
</div>
<div class="fr-radio-group">
<input type="radio" id="consent-finality-2-service-1-refuse" name="consent-finality-2-service-1">
<label class="fr-label" for="consent-finality-2-service-1-refuse">
Refuser
</label>
</div>
</div>
</fieldset>
</div>
<div class="fr-consent-service">
<fieldset aria-labelledby="finality-2-service-2-legend finality-2-service-2-desc" role="group" class="fr-fieldset fr-fieldset--inline">
<legend id="finality-2-service-2-legend" class="fr-consent-service__title" aria-describedby="finality-2-service-2-desc">Sous finalité 2</legend>
<div class="fr-consent-service__radios fr-fieldset--inline">
<div class="fr-radio-group">
<input type="radio" id="consent-finality-2-service-2-accept" name="consent-finality-2-service-2">
<label class="fr-label" for="consent-finality-2-service-2-accept">
Accepter
</label>
</div>
<div class="fr-radio-group">
<input type="radio" id="consent-finality-2-service-2-refuse" name="consent-finality-2-service-2">
<label class="fr-label" for="consent-finality-2-service-2-refuse">
Refuser
</label>
</div>
</div>
<p id="finality-2-service-2-desc" class="fr-consent-service__desc">Ce service utilise 3 cookies.</p>
</fieldset>
</div>
<div class="fr-consent-service">
<fieldset class="fr-fieldset fr-fieldset--inline">
<legend id="finality-2-service-3-legend" class="fr-consent-service__title">Sous finalité 3</legend>
<div class="fr-consent-service__radios fr-fieldset--inline">
<div class="fr-radio-group">
<input type="radio" id="consent-finality-2-service-3-accept" name="consent-finality-2-service-3">
<label class="fr-label" for="consent-finality-2-service-3-accept">
Accepter
</label>
</div>
<div class="fr-radio-group">
<input type="radio" id="consent-finality-2-service-3-refuse" name="consent-finality-2-service-3">
<label class="fr-label" for="consent-finality-2-service-3-refuse">
Refuser
</label>
</div>
</div>
</fieldset>
</div>
</div>
</fieldset>
</div>
<!-- Bouton de confirmation/fermeture -->
<ul class="fr-consent-manager__buttons fr-btns-group fr-btns-group--right fr-btns-group--inline-sm">
<li>
<button type="button" class="fr-btn">Confirmer mes choix</button>
</li>
</ul>
</div>
</div>
</div>
</div>
</div>
</div>
</dialog>


### Placeholder cookies désactivés standard


#### **Nom du service** est désactivé


Autorisez le dépôt de cookies pour accéder à cette fonctionnalité.
Autoriser


###
Extrait de code


<div class="fr-consent-placeholder">
<h4 class="fr-h6">**Nom du service** est désactivé</h4>
<p>Autorisez le dépôt de cookies pour accéder à cette fonctionnalité.</p>
<button title="Autorisez le dépôt de cookies pour accéder au service **Nom du service**" type="button" class="fr-btn">Autoriser</button>
</div>


### Placeholder dans un bloc vidéo responsive grande taille


#### **Nom du service** est désactivé


Autorisez le dépôt de cookies pour accèder à cette fonctionnalité.
Autoriser


Description / Source


Transcription


Agrandir


Fermer


##
Titre de la transcription


- list item


###
Extrait de code


<figure role="group" class="fr-content-media fr-content-media--lg" id="media-3792">
<div class="fr-responsive-vid">
<div class="fr-consent-placeholder">
<h4 class="fr-h6">**Nom du service** est désactivé</h4>
<p>Autorisez le dépôt de cookies pour accèder à cette fonctionnalité.</p>
<button type="button" class="fr-btn">Autoriser</button>
</div>
</div>
<figcaption class="fr-content-media__caption">
Description / Source
<a id="link-3794" href="#" class="fr-link">Libellé lien</a>
</figcaption>
</figure>
<div class="fr-transcription" id="transcription-3793">
<button type="button" class="fr-transcription__btn" aria-expanded="false" aria-controls="fr-transcription-collapse-transcription-3793">Transcription</button>
<div class="fr-collapse" id="fr-transcription-collapse-transcription-3793">
<div class="fr-transcription__footer">
<div class="fr-transcription__actions-group">
<button aria-controls="fr-transcription-modal-transcription-3793" aria-label="Agrandir la transcription" data-fr-opened="false" type="button" class="fr-btn--fullscreen fr-btn">Agrandir</button>
</div>
</div>
<dialog id="fr-transcription-modal-transcription-3793" class="fr-modal" aria-labelledby="fr-transcription-modal-transcription-3793-title">
<div class="fr-container fr-container--fluid fr-container-md">
<div class="fr-grid-row fr-grid-row--center">
<div class="fr-col-12 fr-col-md-10 fr-col-lg-8">
<div class="fr-modal__body">
<div class="fr-modal__header">
<button aria-controls="fr-transcription-modal-transcription-3793" title="Fermer" type="button" id="button-3796" class="fr-btn--close fr-btn">Fermer</button>
</div>
<div class="fr-modal__content">
<h2 id="fr-transcription-modal-transcription-3793-title" class="fr-modal__title">
Titre de la transcription
</h2>
<!-- données de test -->
<div>
<ul>
<li>list item</li>
</ul>
</div>
</div>
</div>
</div>
</div>
</div>
</dialog>
</div>
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
