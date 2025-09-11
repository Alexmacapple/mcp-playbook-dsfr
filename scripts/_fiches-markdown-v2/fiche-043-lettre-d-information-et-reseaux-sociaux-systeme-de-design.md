URL:
https://main--ds-gouv.netlify.app/example/component/follow

Title:
Lettre d'information et Réseaux Sociaux - Système de design

Markdown:

Lettre d'information et Réseaux Sociaux - Système de design


DSFR v1.14.0


[Retour](../)


# Lettre d'information et Réseaux Sociaux (follow)


Le bloc "Lettre d'information et Réseaux Sociaux" est composé d'un bloc permettant à l'utilisateur de s'inscrire à la newsletter de l'organisation et/ou d'un bloc de liens permettant d'accéder aux réseaux sociaux de l'organisation depuis le pied de page.
[Documentation](https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/lettre-d-information-et-reseaux-sociaux)


## Réseaux sociaux seuls


Les icones réseaux sociaux disponibles pour ce composant sont définies dans :


###
src/component/follow/style/_setting.scss


////
/// Logo Setting
/// @group logo
////

$follow-icons: (
bluesky: bluesky-fill,
dailymotion: dailymotion-fill,
facebook: facebook-circle-fill,
github: github-fill,
instagram: instagram-fill,
linkedin: linkedin-box-fill,
mastodon: mastodon-fill,
snapchat: snapchat-fill,
telegram: telegram-fill,
threads: threads-fill,
tiktok: tiktok-fill,
twitch: twitch-fill,
twitter: twitter-fill,
twitter-x: twitter-x-fill,
vimeo: vimeo-fill,
youtube: youtube-fill,
);


Il est aussi possible d'appliquer une classe utilitaire sur un bouton pour utiliser une icone du dsfr (ex: "fr-icon-rss-line")


## Suivez-nous

sur les réseaux sociaux


-
[Facebook](%5B%C3%80%20MODIFIER%20-%20Lien%20vers%20le%20facebook%20de%20l'organisation%5D)


-
[X (anciennement Twitter)](%5B%C3%80%20MODIFIER%20-%20Lien%20vers%20le%20twitter%20de%20l'organisation%5D) (anciennement Twitter)


-
[Bluesky](%5B%C3%80%20MODIFIER%20-%20Lien%20vers%20le%20bluesky%20de%20l'organisation%5D)


-
[Linkedin](%5B%C3%80%20MODIFIER%20-%20Lien%20vers%20le%20linkedin%20de%20l'organisation%5D)


-
[Instagram](%5B%C3%80%20MODIFIER%20-%20Lien%20vers%20l'instagram%20de%20l'organisation%5D)


-
[Youtube](%5B%C3%80%20MODIFIER%20-%20Lien%20vers%20le%20youtube%20de%20l'organisation%5D)


###
Extrait de code


<div class="fr-follow" id="follow-4096">
<div class="fr-container">
<div class="fr-grid-row">
<div class="fr-col-12">
<div class="fr-follow__social">
<h2 class="fr-h5">Suivez-nous
<br> sur les réseaux sociaux
</h2>
<ul class="fr-btns-group">
<li>
<a title="[À MODIFIER - Intitulé du lien] - nouvelle fenêtre" id="social-button-4097" href="[À MODIFIER - Lien vers le facebook de l'organisation]" target="_blank" rel="noopener external" class="fr-btn--facebook fr-btn">Facebook</a>
</li>
<li>
<a title="[À MODIFIER - Intitulé du lien] - nouvelle fenêtre" id="social-button-4098" href="[À MODIFIER - Lien vers le twitter de l'organisation]" target="_blank" rel="noopener external" class="fr-btn--twitter-x fr-btn">X (anciennement Twitter)</a>
</li>
<li>
<a title="[À MODIFIER - Intitulé du lien] - nouvelle fenêtre" id="social-button-4099" href="[À MODIFIER - Lien vers le bluesky de l'organisation]" target="_blank" rel="noopener external" class="fr-btn--bluesky fr-btn">Bluesky</a>
</li>
<li>
<a title="[À MODIFIER - Intitulé du lien] - nouvelle fenêtre" id="social-button-4100" href="[À MODIFIER - Lien vers le linkedin de l'organisation]" target="_blank" rel="noopener external" class="fr-btn--linkedin fr-btn">Linkedin</a>
</li>
<li>
<a title="[À MODIFIER - Intitulé du lien] - nouvelle fenêtre" id="social-button-4101" href="[À MODIFIER - Lien vers l'instagram de l'organisation]" target="_blank" rel="noopener external" class="fr-btn--instagram fr-btn">Instagram</a>
</li>
<li>
<a title="[À MODIFIER - Intitulé du lien] - nouvelle fenêtre" id="social-button-4102" href="[À MODIFIER - Lien vers le youtube de l'organisation]" target="_blank" rel="noopener external" class="fr-btn--youtube fr-btn">Youtube</a>
</li>
</ul>
</div>
</div>
</div>
</div>
</div>


### Lettre d'info seule


## Abonnez-vous à notre lettre d'information


Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas varius tortor nibh, sit amet tempor nibh finibus et.


-
S'abonner


###
Extrait de code


<div class="fr-follow" id="follow-4107">
<div class="fr-container">
<div class="fr-grid-row">
<div class="fr-col-12">
<div class="fr-follow__newsletter">
<div>
<h2 class="fr-h5">Abonnez-vous à notre lettre d'information</h2>
<p class="fr-text--sm">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas varius tortor nibh, sit amet tempor nibh finibus et.</p>
</div>
<div>
<ul class="fr-btns-group fr-btns-group--inline-md">
<li>
<button title="S'abonner à notre lettre d'information" type="button" id="newsletter-button-4106" class="fr-btn">S'abonner</button>
</li>
</ul>
</div>
</div>
</div>
</div>
</div>
</div>


### Lettre d'info seule avec formulaire


## Abonnez-vous à notre lettre d'information


Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas varius tortor nibh, sit amet tempor nibh finibus et.


Votre adresse électronique (ex. : nom@domaine.fr)


S'abonner


En renseignant votre adresse électronique, vous acceptez de recevoir nos actualités par courriel. Vous pouvez vous désinscrire à tout moment à l'aide des liens de désinscription ou en nous contactant.


###
Extrait de code


<div class="fr-follow" id="follow-4115">
<div class="fr-container">
<div class="fr-grid-row">
<div class="fr-col-12">
<div class="fr-follow__newsletter">
<div>
<h2 class="fr-h5">Abonnez-vous à notre lettre d'information</h2>
<p class="fr-text--sm">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas varius tortor nibh, sit amet tempor nibh finibus et.</p>
</div>
<div>
<form action="">
<div class="fr-input-group" id="input-group-4116">
<label class="fr-label" for="newsletter-email-4113">
Votre adresse électronique (ex. : nom@domaine.fr)
</label>
<div class="fr-input-wrap fr-input-wrap--addon">
<input class="fr-input" title="Votre adresse électronique (ex. : nom@domaine.fr)" autocomplete="email" attributes="[object Object]" aria-describedby="newsletter-email-4113-hint-text newsletter-email-4113-messages" placeholder="Votre adresse électronique (ex. : nom@domaine.fr)" id="newsletter-email-4113" type="email">
<button title="S'abonner à notre lettre d'information" type="submit" id="newsletter-button-4114" class="fr-btn">S'abonner</button>
</div>
<div class="fr-messages-group" id="newsletter-email-4113-messages" aria-live="polite">
</div>
</div>
<p id="newsletter-email-4113-hint-text" class="fr-hint-text">En renseignant votre adresse électronique, vous acceptez de recevoir nos actualités par courriel. Vous pouvez vous désinscrire à tout moment à l'aide des liens de désinscription ou en nous contactant.</p>
</form>
</div>
</div>
</div>
</div>
</div>
</div>


### Réseaux sociaux et Lettre d'info mise en avant


## Abonnez-vous à notre lettre d'information


Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas varius tortor nibh, sit amet tempor nibh finibus et.


-
S'abonner


## Suivez-nous

sur les réseaux sociaux


-
[Facebook](%5B%C3%80%20MODIFIER%20-%20Lien%20vers%20le%20facebook%20de%20l'organisation%5D)


-
[X (anciennement Twitter)](%5B%C3%80%20MODIFIER%20-%20Lien%20vers%20le%20twitter%20de%20l'organisation%5D) (anciennement Twitter)


-
[Bluesky](%5B%C3%80%20MODIFIER%20-%20Lien%20vers%20le%20bluesky%20de%20l'organisation%5D)


-
[Linkedin](%5B%C3%80%20MODIFIER%20-%20Lien%20vers%20le%20linkedin%20de%20l'organisation%5D)


-
[Instagram](%5B%C3%80%20MODIFIER%20-%20Lien%20vers%20l'instagram%20de%20l'organisation%5D)


-
[Youtube](%5B%C3%80%20MODIFIER%20-%20Lien%20vers%20le%20youtube%20de%20l'organisation%5D)


###
Extrait de code


<div class="fr-follow" id="follow-4127">
<div class="fr-container">
<div class="fr-grid-row">
<div class="fr-col-12 fr-col-md-8">
<div class="fr-follow__newsletter">
<div>
<h2 class="fr-h5">Abonnez-vous à notre lettre d'information</h2>
<p class="fr-text--sm">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas varius tortor nibh, sit amet tempor nibh finibus et.</p>
</div>
<div>
<ul class="fr-btns-group fr-btns-group--inline-md">
<li>
<button title="S'abonner à notre lettre d'information" type="button" id="newsletter-button-4126" class="fr-btn">S'abonner</button>
</li>
</ul>
</div>
</div>
</div>
<div class="fr-col-12 fr-col-md-4">
<div class="fr-follow__social">
<h2 class="fr-h5">Suivez-nous
<br> sur les réseaux sociaux
</h2>
<ul class="fr-btns-group">
<li>
<a title="[À MODIFIER - Intitulé du lien] - nouvelle fenêtre" id="social-button-4128" href="[À MODIFIER - Lien vers le facebook de l'organisation]" target="_blank" rel="noopener external" class="fr-btn--facebook fr-btn">Facebook</a>
</li>
<li>
<a title="[À MODIFIER - Intitulé du lien] - nouvelle fenêtre" id="social-button-4129" href="[À MODIFIER - Lien vers le twitter de l'organisation]" target="_blank" rel="noopener external" class="fr-btn--twitter-x fr-btn">X (anciennement Twitter)</a>
</li>
<li>
<a title="[À MODIFIER - Intitulé du lien] - nouvelle fenêtre" id="social-button-4130" href="[À MODIFIER - Lien vers le bluesky de l'organisation]" target="_blank" rel="noopener external" class="fr-btn--bluesky fr-btn">Bluesky</a>
</li>
<li>
<a title="[À MODIFIER - Intitulé du lien] - nouvelle fenêtre" id="social-button-4131" href="[À MODIFIER - Lien vers le linkedin de l'organisation]" target="_blank" rel="noopener external" class="fr-btn--linkedin fr-btn">Linkedin</a>
</li>
<li>
<a title="[À MODIFIER - Intitulé du lien] - nouvelle fenêtre" id="social-button-4132" href="[À MODIFIER - Lien vers l'instagram de l'organisation]" target="_blank" rel="noopener external" class="fr-btn--instagram fr-btn">Instagram</a>
</li>
<li>
<a title="[À MODIFIER - Intitulé du lien] - nouvelle fenêtre" id="social-button-4133" href="[À MODIFIER - Lien vers le youtube de l'organisation]" target="_blank" rel="noopener external" class="fr-btn--youtube fr-btn">Youtube</a>
</li>
</ul>
</div>
</div>
</div>
</div>
</div>


### Réseaux sociaux et Lettre d'info avec formulaire


## Abonnez-vous à notre lettre d'information


Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas varius tortor nibh, sit amet tempor nibh finibus et.


Votre adresse électronique (ex. : nom@domaine.fr)


S'abonner


En renseignant votre adresse électronique, vous acceptez de recevoir nos actualités par courriel. Vous pouvez vous désinscrire à tout moment à l'aide des liens de désinscription ou en nous contactant.


## Suivez-nous

sur les réseaux sociaux


-
[Facebook](%5B%C3%80%20MODIFIER%20-%20Lien%20vers%20le%20facebook%20de%20l'organisation%5D)


-
[X (anciennement Twitter)](%5B%C3%80%20MODIFIER%20-%20Lien%20vers%20le%20twitter%20de%20l'organisation%5D) (anciennement Twitter)


-
[Bluesky](%5B%C3%80%20MODIFIER%20-%20Lien%20vers%20le%20bluesky%20de%20l'organisation%5D)


-
[Linkedin](%5B%C3%80%20MODIFIER%20-%20Lien%20vers%20le%20linkedin%20de%20l'organisation%5D)


-
[Instagram](%5B%C3%80%20MODIFIER%20-%20Lien%20vers%20l'instagram%20de%20l'organisation%5D)


-
[Youtube](%5B%C3%80%20MODIFIER%20-%20Lien%20vers%20le%20youtube%20de%20l'organisation%5D)


###
Extrait de code


<div class="fr-follow" id="follow-4147">
<div class="fr-container">
<div class="fr-grid-row">
<div class="fr-col-12 fr-col-md-8">
<div class="fr-follow__newsletter">
<div>
<h2 class="fr-h5">Abonnez-vous à notre lettre d'information</h2>
<p class="fr-text--sm">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas varius tortor nibh, sit amet tempor nibh finibus et.</p>
</div>
<div>
<form action="">
<div class="fr-input-group" id="input-group-4148">
<label class="fr-label" for="newsletter-email-4145">
Votre adresse électronique (ex. : nom@domaine.fr)
</label>
<div class="fr-input-wrap fr-input-wrap--addon">
<input class="fr-input" title="Votre adresse électronique (ex. : nom@domaine.fr)" autocomplete="email" aria-describedby="newsletter-email-4145-hint-text newsletter-email-4145-messages" placeholder="Votre adresse électronique (ex. : nom@domaine.fr)" id="newsletter-email-4145" type="email">
<button title="S'abonner à notre lettre d'information" type="submit" id="newsletter-button-4146" class="fr-btn">S'abonner</button>
</div>
<div class="fr-messages-group" id="newsletter-email-4145-messages" aria-live="polite">
</div>
</div>
<p id="newsletter-email-4145-hint-text" class="fr-hint-text">En renseignant votre adresse électronique, vous acceptez de recevoir nos actualités par courriel. Vous pouvez vous désinscrire à tout moment à l'aide des liens de désinscription ou en nous contactant.</p>
</form>
</div>
</div>
</div>
<div class="fr-col-12 fr-col-md-4">
<div class="fr-follow__social">
<h2 class="fr-h5">Suivez-nous
<br> sur les réseaux sociaux
</h2>
<ul class="fr-btns-group">
<li>
<a title="[À MODIFIER - Intitulé du lien] - nouvelle fenêtre" id="social-button-4149" href="[À MODIFIER - Lien vers le facebook de l'organisation]" target="_blank" rel="noopener external" class="fr-btn--facebook fr-btn">Facebook</a>
</li>
<li>
<a title="[À MODIFIER - Intitulé du lien] - nouvelle fenêtre" id="social-button-4150" href="[À MODIFIER - Lien vers le twitter de l'organisation]" target="_blank" rel="noopener external" class="fr-btn--twitter-x fr-btn">X (anciennement Twitter)</a>
</li>
<li>
<a title="[À MODIFIER - Intitulé du lien] - nouvelle fenêtre" id="social-button-4151" href="[À MODIFIER - Lien vers le bluesky de l'organisation]" target="_blank" rel="noopener external" class="fr-btn--bluesky fr-btn">Bluesky</a>
</li>
<li>
<a title="[À MODIFIER - Intitulé du lien] - nouvelle fenêtre" id="social-button-4152" href="[À MODIFIER - Lien vers le linkedin de l'organisation]" target="_blank" rel="noopener external" class="fr-btn--linkedin fr-btn">Linkedin</a>
</li>
<li>
<a title="[À MODIFIER - Intitulé du lien] - nouvelle fenêtre" id="social-button-4153" href="[À MODIFIER - Lien vers l'instagram de l'organisation]" target="_blank" rel="noopener external" class="fr-btn--instagram fr-btn">Instagram</a>
</li>
<li>
<a title="[À MODIFIER - Intitulé du lien] - nouvelle fenêtre" id="social-button-4154" href="[À MODIFIER - Lien vers le youtube de l'organisation]" target="_blank" rel="noopener external" class="fr-btn--youtube fr-btn">Youtube</a>
</li>
</ul>
</div>
</div>
</div>
</div>
</div>


### Réseaux sociaux et Lettre d'info avec formulaire - succès


## Abonnez-vous à notre lettre d'information


Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas varius tortor nibh, sit amet tempor nibh finibus et.


Votre inscription a bien été prise en compte.


## Suivez-nous

sur les réseaux sociaux


-
[Facebook](%5B%C3%80%20MODIFIER%20-%20Lien%20vers%20le%20facebook%20de%20l'organisation%5D)


-
[X (anciennement Twitter)](%5B%C3%80%20MODIFIER%20-%20Lien%20vers%20le%20twitter%20de%20l'organisation%5D) (anciennement Twitter)


-
[Bluesky](%5B%C3%80%20MODIFIER%20-%20Lien%20vers%20le%20bluesky%20de%20l'organisation%5D)


-
[Linkedin](%5B%C3%80%20MODIFIER%20-%20Lien%20vers%20le%20linkedin%20de%20l'organisation%5D)


-
[Instagram](%5B%C3%80%20MODIFIER%20-%20Lien%20vers%20l'instagram%20de%20l'organisation%5D)


-
[Youtube](%5B%C3%80%20MODIFIER%20-%20Lien%20vers%20le%20youtube%20de%20l'organisation%5D)


###
Extrait de code


<div class="fr-follow" id="follow-4165">
<div class="fr-container">
<div class="fr-grid-row">
<div class="fr-col-12 fr-col-md-8">
<div class="fr-follow__newsletter">
<div>
<h2 class="fr-h5">Abonnez-vous à notre lettre d'information</h2>
<p class="fr-text--sm">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas varius tortor nibh, sit amet tempor nibh finibus et.</p>
</div>
<div>
<div id="newsletter-alert-4164" class="fr-alert fr-alert--success">
<p>Votre inscription a bien été prise en compte.</p>
</div>
</div>
</div>
</div>
<div class="fr-col-12 fr-col-md-4">
<div class="fr-follow__social">
<h2 class="fr-h5">Suivez-nous
<br> sur les réseaux sociaux
</h2>
<ul class="fr-btns-group">
<li>
<a title="[À MODIFIER - Intitulé du lien] - nouvelle fenêtre" id="social-button-4166" href="[À MODIFIER - Lien vers le facebook de l'organisation]" target="_blank" rel="noopener external" class="fr-btn--facebook fr-btn">Facebook</a>
</li>
<li>
<a title="[À MODIFIER - Intitulé du lien] - nouvelle fenêtre" id="social-button-4167" href="[À MODIFIER - Lien vers le twitter de l'organisation]" target="_blank" rel="noopener external" class="fr-btn--twitter-x fr-btn">X (anciennement Twitter)</a>
</li>
<li>
<a title="[À MODIFIER - Intitulé du lien] - nouvelle fenêtre" id="social-button-4168" href="[À MODIFIER - Lien vers le bluesky de l'organisation]" target="_blank" rel="noopener external" class="fr-btn--bluesky fr-btn">Bluesky</a>
</li>
<li>
<a title="[À MODIFIER - Intitulé du lien] - nouvelle fenêtre" id="social-button-4169" href="[À MODIFIER - Lien vers le linkedin de l'organisation]" target="_blank" rel="noopener external" class="fr-btn--linkedin fr-btn">Linkedin</a>
</li>
<li>
<a title="[À MODIFIER - Intitulé du lien] - nouvelle fenêtre" id="social-button-4170" href="[À MODIFIER - Lien vers l'instagram de l'organisation]" target="_blank" rel="noopener external" class="fr-btn--instagram fr-btn">Instagram</a>
</li>
<li>
<a title="[À MODIFIER - Intitulé du lien] - nouvelle fenêtre" id="social-button-4171" href="[À MODIFIER - Lien vers le youtube de l'organisation]" target="_blank" rel="noopener external" class="fr-btn--youtube fr-btn">Youtube</a>
</li>
</ul>
</div>
</div>
</div>
</div>
</div>


### Réseaux sociaux et Lettre d'info avec formulaire - erreur


## Abonnez-vous à notre lettre d'information


Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas varius tortor nibh, sit amet tempor nibh finibus et.


Votre adresse électronique (ex. : nom@domaine.fr)


S'abonner


Le format de l'adresse electronique saisie n'est pas valide. Le format attendu est : nom@domaine.fr


En renseignant votre adresse électronique, vous acceptez de recevoir nos actualités par courriel. Vous pouvez vous désinscrire à tout moment à l'aide des liens de désinscription ou en nous contactant.


## Suivez-nous

sur les réseaux sociaux


-
[Facebook](%5B%C3%80%20MODIFIER%20-%20Lien%20vers%20le%20facebook%20de%20l'organisation%5D)


-
[X (anciennement Twitter)](%5B%C3%80%20MODIFIER%20-%20Lien%20vers%20le%20twitter%20de%20l'organisation%5D) (anciennement Twitter)


-
[Bluesky](%5B%C3%80%20MODIFIER%20-%20Lien%20vers%20le%20bluesky%20de%20l'organisation%5D)


-
[Linkedin](%5B%C3%80%20MODIFIER%20-%20Lien%20vers%20le%20linkedin%20de%20l'organisation%5D)


-
[Instagram](%5B%C3%80%20MODIFIER%20-%20Lien%20vers%20l'instagram%20de%20l'organisation%5D)


-
[Youtube](%5B%C3%80%20MODIFIER%20-%20Lien%20vers%20le%20youtube%20de%20l'organisation%5D)


###
Extrait de code


<div class="fr-follow" id="follow-4185">
<div class="fr-container">
<div class="fr-grid-row">
<div class="fr-col-12 fr-col-md-8">
<div class="fr-follow__newsletter">
<div>
<h2 class="fr-h5">Abonnez-vous à notre lettre d'information</h2>
<p class="fr-text--sm">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas varius tortor nibh, sit amet tempor nibh finibus et.</p>
</div>
<div>
<form action="">
<div class="fr-input-group fr-input-group--error" id="input-group-4186">
<label class="fr-label" for="newsletter-email-4183">
Votre adresse électronique (ex. : nom@domaine.fr)
</label>
<div class="fr-input-wrap fr-input-wrap--addon">
<input class="fr-input" title="Votre adresse électronique (ex. : nom@domaine.fr)" autocomplete="email" aria-describedby="newsletter-email-4183-hint-text newsletter-email-4183-messages" placeholder="Votre adresse électronique (ex. : nom@domaine.fr)" id="newsletter-email-4183" type="email">
<button title="S'abonner à notre lettre d'information" type="submit" id="newsletter-button-4184" class="fr-btn">S'abonner</button>
</div>
<div class="fr-messages-group" id="newsletter-email-4183-messages" aria-live="polite">
<p class="fr-message fr-message--error" id="newsletter-email-4183-message-error">Le format de l'adresse electronique saisie n'est pas valide. Le format attendu est : nom@domaine.fr</p>
</div>
</div>
<p id="newsletter-email-4183-hint-text" class="fr-hint-text">En renseignant votre adresse électronique, vous acceptez de recevoir nos actualités par courriel. Vous pouvez vous désinscrire à tout moment à l'aide des liens de désinscription ou en nous contactant.</p>
</form>
</div>
</div>
</div>
<div class="fr-col-12 fr-col-md-4">
<div class="fr-follow__social">
<h2 class="fr-h5">Suivez-nous
<br> sur les réseaux sociaux
</h2>
<ul class="fr-btns-group">
<li>
<a title="[À MODIFIER - Intitulé du lien] - nouvelle fenêtre" id="social-button-4187" href="[À MODIFIER - Lien vers le facebook de l'organisation]" target="_blank" rel="noopener external" class="fr-btn--facebook fr-btn">Facebook</a>
</li>
<li>
<a title="[À MODIFIER - Intitulé du lien] - nouvelle fenêtre" id="social-button-4188" href="[À MODIFIER - Lien vers le twitter de l'organisation]" target="_blank" rel="noopener external" class="fr-btn--twitter-x fr-btn">X (anciennement Twitter)</a>
</li>
<li>
<a title="[À MODIFIER - Intitulé du lien] - nouvelle fenêtre" id="social-button-4189" href="[À MODIFIER - Lien vers le bluesky de l'organisation]" target="_blank" rel="noopener external" class="fr-btn--bluesky fr-btn">Bluesky</a>
</li>
<li>
<a title="[À MODIFIER - Intitulé du lien] - nouvelle fenêtre" id="social-button-4190" href="[À MODIFIER - Lien vers le linkedin de l'organisation]" target="_blank" rel="noopener external" class="fr-btn--linkedin fr-btn">Linkedin</a>
</li>
<li>
<a title="[À MODIFIER - Intitulé du lien] - nouvelle fenêtre" id="social-button-4191" href="[À MODIFIER - Lien vers l'instagram de l'organisation]" target="_blank" rel="noopener external" class="fr-btn--instagram fr-btn">Instagram</a>
</li>
<li>
<a title="[À MODIFIER - Intitulé du lien] - nouvelle fenêtre" id="social-button-4192" href="[À MODIFIER - Lien vers le youtube de l'organisation]" target="_blank" rel="noopener external" class="fr-btn--youtube fr-btn">Youtube</a>
</li>
</ul>
</div>
</div>
</div>
</div>
</div>


## Dépréciation


Les exemples suivants sont dépréciés, ne pas utiliser comme référence

Pour support des versions précédentes


### Réseaux sociaux seuls


Suivez-nous

sur les réseaux sociaux


-
[facebook](%5B%C3%80%20MODIFIER%20-%20Lien%20vers%20le%20facebook%20de%20l'organisation%5D)


-
[twitter-x](%5B%C3%80%20MODIFIER%20-%20Lien%20vers%20le%20twitter%20de%20l'organisation%5D)


-
[instagram](%5B%C3%80%20MODIFIER%20-%20Lien%20vers%20l'instagram%20de%20l'organisation%5D)


-
[linkedin](%5B%C3%80%20MODIFIER%20-%20Lien%20vers%20le%20linkedin%20de%20l'organisation%5D)


-
[youtube](%5B%C3%80%20MODIFIER%20-%20Lien%20vers%20le%20youtube%20de%20l'organisation%5D)


###
Extrait de code


<div class="fr-follow">
<div class="fr-container">
<div class="fr-grid-row">
<div class="fr-col-12">
<div class="fr-follow__social">
<p class="fr-h5">Suivez-nous
<br> sur les réseaux sociaux
</p>
<ul class="fr-links-group">
<li>
<a title="[À MODIFIER - Intitulé du lien] - nouvelle fenêtre" id="link-4199" href="[À MODIFIER - Lien vers le facebook de l'organisation]" target="_blank" rel="noopener external" class="fr-link--facebook fr-link">facebook</a>
</li>
<li>
<a title="[À MODIFIER - Intitulé du lien] - nouvelle fenêtre" id="link-4200" href="[À MODIFIER - Lien vers le twitter de l'organisation]" target="_blank" rel="noopener external" class="fr-link--twitter-x fr-link">twitter-x</a>
</li>
<li>
<a title="[À MODIFIER - Intitulé du lien] - nouvelle fenêtre" id="link-4201" href="[À MODIFIER - Lien vers l'instagram de l'organisation]" target="_blank" rel="noopener external" class="fr-link--instagram fr-link">instagram</a>
</li>
<li>
<a title="[À MODIFIER - Intitulé du lien] - nouvelle fenêtre" id="link-4202" href="[À MODIFIER - Lien vers le linkedin de l'organisation]" target="_blank" rel="noopener external" class="fr-link--linkedin fr-link">linkedin</a>
</li>
<li>
<a title="[À MODIFIER - Intitulé du lien] - nouvelle fenêtre" id="link-4203" href="[À MODIFIER - Lien vers le youtube de l'organisation]" target="_blank" rel="noopener external" class="fr-link--youtube fr-link">youtube</a>
</li>
</ul>
</div>
</div>
</div>
</div>
</div>


### Réseaux sociaux et Lettre d'info mise en avant


Abonnez-vous à notre lettre d'information


Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas varius tortor nibh, sit amet tempor nibh finibus et.


S'abonner


Suivez-nous

sur les réseaux sociaux


-
[facebook](%5B%C3%80%20MODIFIER%20-%20Lien%20vers%20le%20facebook%20de%20l'organisation%5D)


-
[twitter-x](%5B%C3%80%20MODIFIER%20-%20Lien%20vers%20le%20twitter%20de%20l'organisation%5D)


-
[instagram](%5B%C3%80%20MODIFIER%20-%20Lien%20vers%20l'instagram%20de%20l'organisation%5D)


-
[linkedin](%5B%C3%80%20MODIFIER%20-%20Lien%20vers%20le%20linkedin%20de%20l'organisation%5D)


-
[youtube](%5B%C3%80%20MODIFIER%20-%20Lien%20vers%20le%20youtube%20de%20l'organisation%5D)


###
Extrait de code


<div class="fr-follow">
<div class="fr-container">
<div class="fr-grid-row">
<div class="fr-col-12 fr-col-md-8">
<div class="fr-follow__newsletter">
<div>
<p class="fr-h5">Abonnez-vous à notre lettre d'information</p>
<p class="fr-text--sm">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas varius tortor nibh, sit amet tempor nibh finibus et.</p>
</div>
<div>
<button title="S'abonner à notre lettre d'information" type="button" class="fr-btn">S'abonner</button>
</div>
</div>
</div>
<div class="fr-col-12 fr-col-md-4">
<div class="fr-follow__social">
<p class="fr-h5">Suivez-nous
<br> sur les réseaux sociaux
</p>
<ul class="fr-links-group">
<li>
<a title="[À MODIFIER - Intitulé du lien] - nouvelle fenêtre" id="link-4210" href="[À MODIFIER - Lien vers le facebook de l'organisation]" target="_blank" rel="noopener external" class="fr-link--facebook fr-link">facebook</a>
</li>
<li>
<a title="[À MODIFIER - Intitulé du lien] - nouvelle fenêtre" id="link-4211" href="[À MODIFIER - Lien vers le twitter de l'organisation]" target="_blank" rel="noopener external" class="fr-link--twitter-x fr-link">twitter-x</a>
</li>
<li>
<a title="[À MODIFIER - Intitulé du lien] - nouvelle fenêtre" id="link-4212" href="[À MODIFIER - Lien vers l'instagram de l'organisation]" target="_blank" rel="noopener external" class="fr-link--instagram fr-link">instagram</a>
</li>
<li>
<a title="[À MODIFIER - Intitulé du lien] - nouvelle fenêtre" id="link-4213" href="[À MODIFIER - Lien vers le linkedin de l'organisation]" target="_blank" rel="noopener external" class="fr-link--linkedin fr-link">linkedin</a>
</li>
<li>
<a title="[À MODIFIER - Intitulé du lien] - nouvelle fenêtre" id="link-4214" href="[À MODIFIER - Lien vers le youtube de l'organisation]" target="_blank" rel="noopener external" class="fr-link--youtube fr-link">youtube</a>
</li>
</ul>
</div>
</div>
</div>
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
