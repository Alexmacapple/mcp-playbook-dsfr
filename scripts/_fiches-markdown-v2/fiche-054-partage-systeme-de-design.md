URL:
https://main--ds-gouv.netlify.app/example/component/share

Title:
Partage - Système de design

Markdown:

Partage - Système de design


DSFR v1.14.0


[Retour](../)


# Partage (share)


Les boutons de partage permettent aux utilisateurs de partager facilement un contenu, via les réseaux sociaux, par envoi de mail ou en copiant l'URL du contenu dans le presse-papier.
[Documentation](https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/partage)


## Méta données


Données à insérer dans la partie

de la page, pour fournir un aperçu de la page aux applications tierces lors du partage.


###
Extrait de code


<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="[À MODIFIER - @usernameTwitter]">
<meta property="og:title" content="[À MODIFIER - Système de Design de l'État]">
<meta property="og:description" content="[À MODIFIER - Développer vos sites et applications en utilisant des composants prêts à l'emploi, accessibles et ergonomiques]">
<meta property="og:image" content="[À MODIFIER - https://systeme-de-design.gouv.fr/src/img/systeme-de-design.gouv.fr.jpg]">
<meta property="og:type" content="website">
<meta property="og:url" content="[À MODIFIER - https://systeme-de-design.gouv.fr/]">
<meta property="og:site_name" content="[À MODIFIER - Site officiel du Système de Design de l'État]">
<meta property="og:image:alt" content="[À MODIFIER - République Française - Système de Design de l'État]">
<meta name="twitter:image:alt" content="[À MODIFIER - République Française - Système de Design de l'État]">


## Boutons de partage par défaut


Les icones réseaux sociaux disponibles pour ce composant sont définies dans :


###
src/component/share/style/_setting.scss


////
/// Logo Setting
/// @group logo
////

$share-icons: (
bluesky: bluesky-line,
facebook: facebook-circle-line,
linkedin: linkedin-box-line,
mastodon: mastodon-line,
threads: threads-line,
twitter: twitter-line,
twitter-x: twitter-x-line
);


Il est aussi possible d'appliquer une classe utilitaire sur un bouton pour utiliser une icone du dsfr (ex: "fr-icon-rss-line")


Partager la page

-
[Partager sur Facebook](https://www.facebook.com/sharer.php?u=%5B%C3%80%20MODIFIER%20-%20url%20de%20la%20page%5D)


-

[Partager sur X (anciennement Twitter)](https://twitter.com/intent/tweet?url=%5B%C3%80%20MODIFIER%20-%20url%20de%20la%20page%5D&text=%5B%C3%80%20MODIFIER%20-%20titre%20ou%20texte%20descriptif%20de%20la%20page%5D&via=%5B%C3%80%20MODIFIER%20-%20via%5D&hashtags=%5B%C3%80%20MODIFIER%20-%20hashtags%5D) (anciennement Twitter)


-

[Partager sur Bluesky](https://bsky.app/intent/compose?text=%5B%C3%80%20MODIFIER%20-%20titre%20ou%20texte%20descriptif%20de%20la%20page%5D+%5B%C3%80%20MODIFIER%20-%20url%20de%20la%20page%5D)


-
[Partager sur LinkedIn](https://www.linkedin.com/shareArticle?url=%5B%C3%80%20MODIFIER%20-%20url%20de%20la%20page%5D&title=%5B%C3%80%20MODIFIER%20-%20titre%20ou%20texte%20descriptif%20de%20la%20page%5D)


-
[Partager par email](mailto:?subject=%5B%C3%80%20MODIFIER%20-%20objet%20du%20mail%5D&body=%5B%C3%80%20MODIFIER%20-%20titre%20ou%20texte%20descriptif%20de%20la%20page%5D%20%5B%C3%80%20MODIFIER%20-%20url%20de%20la%20page%5D)


-
Copier dans le presse-papier


###
Extrait de code


<div class="fr-share" id="share-6625">
<p class="fr-share__title">Partager la page</p>
<ul class="fr-btns-group">
<li>
<a onclick="window.open(this.href,'Partager sur Facebook','toolbar=no,location=yes,status=no,menubar=no,scrollbars=yes,resizable=yes,width=600,height=450'); event.preventDefault();" id="share-6626" href="https://www.facebook.com/sharer.php?u=[À MODIFIER - url de la page]" target="_blank" rel="noopener external" class="fr-btn--facebook fr-btn">Partager sur Facebook</a>
</li>
<li>
<!-- Les paramètres de la reqûete doivent être URI-encodés (ex: encodeURIComponent() en js) -->
<a onclick="window.open(this.href,'Partager sur X (anciennement Twitter)','toolbar=no,location=yes,status=no,menubar=no,scrollbars=yes,resizable=yes,width=600,height=420'); event.preventDefault();" id="share-6627" href="https://twitter.com/intent/tweet?url=[À MODIFIER - url de la page]&text=[À MODIFIER - titre ou texte descriptif de la page]&via=[À MODIFIER - via]&hashtags=[À MODIFIER - hashtags]" target="_blank" rel="noopener external" class="fr-btn--twitter-x fr-btn">Partager sur X (anciennement Twitter)</a>
</li>
<li>
<!-- Les paramètres de la reqûete doivent être URI-encodés (ex: encodeURIComponent() en js) -->
<a onclick="window.open(this.href,'Partager sur Bluesky','toolbar=no,location=yes,status=no,menubar=no,scrollbars=yes,resizable=yes,width=600,height=430'); event.preventDefault();" id="share-6628" href="https://bsky.app/intent/compose?text=[À MODIFIER - titre ou texte descriptif de la page]+[À MODIFIER - url de la page]" target="_blank" rel="noopener external" class="fr-btn--bluesky fr-btn">Partager sur Bluesky</a>
</li>
<li>
<a onclick="window.open(this.href,'Partager sur LinkedIn','toolbar=no,location=yes,status=no,menubar=no,scrollbars=yes,resizable=yes,width=550,height=550'); event.preventDefault();" id="share-6629" href="https://www.linkedin.com/shareArticle?url=[À MODIFIER - url de la page]&title=[À MODIFIER - titre ou texte descriptif de la page]" target="_blank" rel="noopener external" class="fr-btn--linkedin fr-btn">Partager sur LinkedIn</a>
</li>
<li>
<a id="share-6630" href="mailto:?subject=[À MODIFIER - objet du mail]&body=[À MODIFIER - titre ou texte descriptif de la page] [À MODIFIER - url de la page]" target="_blank" rel="noopener external" class="fr-btn--mail fr-btn">Partager par email</a>
</li>
<li>
<button onclick="navigator.clipboard.writeText(window.location).then(function() {alert('Adresse copiée dans le presse papier.')});" type="button" id="share-6631" class="fr-btn--copy fr-btn">Copier dans le presse-papier</button>
</li>
</ul>
</div>


### Boutons de partage version inactive


Partager la page


Veuillez [autoriser le dépôt de cookies](%5B%C3%80%20MODIFIER%20-%20url%20page%20autorisation%20cookies%5D) pour partager sur Facebook, Twitter, Bluesky et LinkedIn.

-


-
(anciennement Twitter)


-


-


-
[Partager par email](mailto:?subject=%5B%C3%80%20MODIFIER%20-%20objet%20du%20mail%5D&body=%5B%C3%80%20MODIFIER%20-%20titre%20ou%20texte%20descriptif%20de%20la%20page%5D%20%5B%C3%80%20MODIFIER%20-%20url%20de%20la%20page%5D)


-
Copier dans le presse-papier


###
Extrait de code


<div class="fr-share" id="share-6640">
<p class="fr-share__title">Partager la page</p>
<p class="fr-share__text">Veuillez <a href="[À MODIFIER - url page autorisation cookies]">autoriser le dépôt de cookies</a> pour partager sur Facebook, Twitter, Bluesky et LinkedIn.</p>
<ul class="fr-btns-group">
<li>
<a id="share-6641" target="_blank" rel="noopener external" aria-disabled="true" role="link" class="fr-btn--facebook fr-btn">Partager sur Facebook</a>
</li>
<li>
<a id="share-6642" target="_blank" rel="noopener external" aria-disabled="true" role="link" class="fr-btn--twitter-x fr-btn">Partager sur X (anciennement Twitter)</a>
</li>
<li>
<a id="share-6643" target="_blank" rel="noopener external" aria-disabled="true" role="link" class="fr-btn--bluesky fr-btn">Partager sur Bluesky</a>
</li>
<li>
<a id="share-6644" target="_blank" rel="noopener external" aria-disabled="true" role="link" class="fr-btn--linkedin fr-btn">Partager sur LinkedIn</a>
</li>
<li>
<a id="share-6645" href="mailto:?subject=[À MODIFIER - objet du mail]&body=[À MODIFIER - titre ou texte descriptif de la page] [À MODIFIER - url de la page]" target="_blank" rel="noopener external" class="fr-btn--mail fr-btn">Partager par email</a>
</li>
<li>
<button onclick="navigator.clipboard.writeText(window.location).then(function() {alert('Adresse copiée dans le presse papier.')});" type="button" id="share-6646" class="fr-btn--copy fr-btn">Copier dans le presse-papier</button>
</li>
</ul>
</div>


## Dépréciation


Les exemples suivants sont dépréciés, ne pas utiliser comme référence

Pour support des versions précédentes


### Boutons de partage par défaut


Partager la page

-
[Partager sur Facebook](https://www.facebook.com/sharer.php?u=%5B%C3%80%20MODIFIER%20-%20url%20de%20la%20page%5D)


-

[Partager sur Twitter](https://twitter.com/intent/tweet?url=%5B%C3%80%20MODIFIER%20-%20url%20de%20la%20page%5D&text=%5B%C3%80%20MODIFIER%20-%20titre%20ou%20texte%20descriptif%20de%20la%20page%5D&via=%5B%C3%80%20MODIFIER%20-%20via%5D&hashtags=%5B%C3%80%20MODIFIER%20-%20hashtags%5D)


-
[Partager sur LinkedIn](https://www.linkedin.com/shareArticle?url=%5B%C3%80%20MODIFIER%20-%20url%20de%20la%20page%5D&title=%5B%C3%80%20MODIFIER%20-%20titre%20ou%20texte%20descriptif%20de%20la%20page%5D)


-
[Partager par email](mailto:?subject=%5B%C3%80%20MODIFIER%20-%20objet%20du%20mail%5D&body=%5B%C3%80%20MODIFIER%20-%20titre%20ou%20texte%20descriptif%20de%20la%20page%5D%20%5B%C3%80%20MODIFIER%20-%20url%20de%20la%20page%5D)


-
Copier dans le presse-papier


###
Extrait de code


<div class="fr-share">
<p class="fr-share__title">Partager la page</p>
<ul class="fr-share__group">
<li>
<a class="fr-share__link fr-share__link--facebook" title="Partager sur Facebook - nouvelle fenêtre" href="https://www.facebook.com/sharer.php?u=[À MODIFIER - url de la page]" target="_blank" rel="noopener" onclick="window.open(this.href,'Partager sur Facebook','toolbar=no,location=yes,status=no,menubar=no,scrollbars=yes,resizable=yes,width=600,height=450'); event.preventDefault();">Partager sur Facebook</a>
</li>
<li>
<!-- Les paramètres de la reqûete doivent être URI-encodés (ex: encodeURIComponent() en js) -->
<a class="fr-share__link fr-share__link--twitter" title="Partager sur Twitter - nouvelle fenêtre" href="https://twitter.com/intent/tweet?url=[À MODIFIER - url de la page]&text=[À MODIFIER - titre ou texte descriptif de la page]&via=[À MODIFIER - via]&hashtags=[À MODIFIER - hashtags]" target="_blank" rel="noopener" onclick="window.open(this.href,'Partager sur Twitter','toolbar=no,location=yes,status=no,menubar=no,scrollbars=yes,resizable=yes,width=600,height=420'); event.preventDefault();">Partager sur Twitter</a>
</li>
<li>
<a class="fr-share__link fr-share__link--linkedin" title="Partager sur LinkedIn - nouvelle fenêtre" href="https://www.linkedin.com/shareArticle?url=[À MODIFIER - url de la page]&title=[À MODIFIER - titre ou texte descriptif de la page]" target="_blank" rel="noopener" onclick="window.open(this.href,'Partager sur LinkedIn','toolbar=no,location=yes,status=no,menubar=no,scrollbars=yes,resizable=yes,width=550,height=550'); event.preventDefault();">Partager sur LinkedIn</a>
</li>
<li>
<a class="fr-share__link fr-share__link--mail" href="mailto:?subject=[À MODIFIER - objet du mail]&body=[À MODIFIER - titre ou texte descriptif de la page] [À MODIFIER - url de la page]" title="Partager par email" target="_blank">Partager par email</a>
</li>
<li>
<button class="fr-share__link fr-share__link--copy" title="Copier dans le presse-papier" onclick="navigator.clipboard.writeText(window.location);alert('Adresse copiée dans le presse papier.');">Copier dans le presse-papier</button>
</li>
</ul>
</div>


### Boutons de partage version inactive


Partager la page


Veuillez [autoriser le dépôt de cookies](%5B%C3%80) pour partager sur Facebook, Twitter et LinkedIn.

-


-


-


-
[Partager par email](mailto:?subject=%5B%C3%80%20MODIFIER%20-%20objet%20du%20mail%5D&body=%5B%C3%80%20MODIFIER%20-%20titre%20ou%20texte%20descriptif%20de%20la%20page%5D%20%5B%C3%80%20MODIFIER%20-%20url%20de%20la%20page%5D)


-
Copier dans le presse-papier


###
Extrait de code


<div class="fr-share">
<p class="fr-share__title">Partager la page</p>
<p class="fr-share__text">Veuillez <a href=[À MODIFIER - url page autorisation cookies]>autoriser le dépôt de cookies</a> pour partager sur Facebook, Twitter et LinkedIn.</p>
<ul class="fr-share__group">
<li>
<a class="fr-share__link fr-share__link--facebook" title="Partager sur Facebook - désactivé" aria-disabled="true" role="link">Partager sur Facebook</a>
</li>
<li>
<a class="fr-share__link fr-share__link--twitter" title="Partager sur Twitter - désactivé" aria-disabled="true" role="link">Partager sur Twitter</a>
</li>
<li>
<a class="fr-share__link fr-share__link--linkedin" title="Partager sur LinkedIn - désactivé" aria-disabled="true" role="link">Partager sur LinkedIn</a>
</li>
<li>
<a class="fr-share__link fr-share__link--mail" href="mailto:?subject=[À MODIFIER - objet du mail]&body=[À MODIFIER - titre ou texte descriptif de la page] [À MODIFIER - url de la page]" title="Partager par email" target="_blank">Partager par email</a>
</li>
<li>
<button class="fr-share__link fr-share__link--copy" title="Copier dans le presse-papier" onclick="navigator.clipboard.writeText(window.location);alert('Adresse copiée dans le presse papier.');">Copier dans le presse-papier</button>
</li>
</ul>
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
