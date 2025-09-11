URL:
https://main--ds-gouv.netlify.app/example/component/download/deprecated

Title:
Téléchargement de fichier - Système de design

Markdown:

Téléchargement de fichier - Système de design


DSFR v1.14.0


[Retour](../)


# Téléchargement de fichier (download)


Ce composant est déprécié. La fonctionnalité "téléchargement de fichier" est maintenant disponible directement sur le composant carte et le composant lien.
[Documentation](https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/telechargement-de-fichier)


## Dépréciation


Les exemples suivants sont dépréciés, ne pas utiliser comme référence

Pour support des versions précédentes


## Téléchargement de fichier


Il existe 2 variantes possible pour ce composant. La forme de lien, et la forme de carte.

L'intitulé du lien doit commencer par 'Télécharger'.

Le détail est obligatoire et doit conntenir le type (extension du fichier), le poids, la langue (si différente)). Laisser le détail vide si utilisation de l'utilitaire js de remplissage automatique


###
Lien de téléchargement


## Lien de téléchargment


L'attribut "download" permettant de télécharger directement le document, sans l'ouvrir, est optionnel. Ajouter un nom de fichier en valeur de cet attribut pour renommer le fichier avant de le télécharger. Mettre un attribut target="_blank" pour ouvrir le document dans une nouvelle fenêtre.


### Lien de téléchargement seul


###
[Télécharger le document lorem ipsum sit dolores amet

JPG - 61,88 ko](%5B%C3%80%20MODIFIER%20-%20../../../../example/img/image.jpg%5D)


###
Extrait de code


<div class="fr-download">
<h3>
<a href="[À MODIFIER - ../../../../example/img/image.jpg]" id="fr-download-link-7056" download class="fr-download__link">Télécharger le document lorem ipsum sit dolores amet
<span class="fr-download__detail">
JPG - 61,88 ko
</span>
</a>
</h3>
</div>


###
Groupe de liens


### Groupe de liens de téléchargement


-


###
[Télécharger le document lorem ipsum sit dolores amet

PDF - 61,88 Ko](%5B%C3%80%20MODIFIER%20-%20../../../../example/img/image.jpg%5D)


-


###
[Télécharger le document lorem ipsum sit dolores amet

PDF - 61,88 Ko](%5B%C3%80%20MODIFIER%20-%20../../../../example/img/image.jpg%5D)


-


###
[Télécharger le document lorem ipsum sit dolores amet

PDF - 61,88 Ko](%5B%C3%80%20MODIFIER%20-%20../../../../example/img/image.jpg%5D)


###
Extrait de code


<div class="fr-downloads-group">
<ul>
<li>
<div class="fr-download">
<h3>
<a href="[À MODIFIER - ../../../../example/img/image.jpg]" id="fr-download-link-7062" download class="fr-download__link">Télécharger le document lorem ipsum sit dolores amet
<span class="fr-download__detail">
PDF - 61,88 Ko
</span>
</a>
</h3>
</div>
</li>
<li>
<div class="fr-download">
<h3>
<a href="[À MODIFIER - ../../../../example/img/image.jpg]" id="fr-download-link-7063" download class="fr-download__link">Télécharger le document lorem ipsum sit dolores amet
<span class="fr-download__detail">
PDF - 61,88 Ko
</span>
</a>
</h3>
</div>
</li>
<li>
<div class="fr-download">
<h3>
<a href="[À MODIFIER - ../../../../example/img/image.jpg]" id="fr-download-link-7064" download class="fr-download__link">Télécharger le document lorem ipsum sit dolores amet
<span class="fr-download__detail">
PDF - 61,88 Ko
</span>
</a>
</h3>
</div>
</li>
</ul>
</div>


#### Groupe de liens de téléchargement avec bordure


dans une grille, sur 3 à 8 colonnes en version desktop


Titre facultatif

-


###
[Télécharger le document lorem ipsum sit dolores amet

PDF - 61,88 Ko](%5B%C3%80%20MODIFIER%20-%20../../../../example/img/image.jpg%5D)


-


###
[Télécharger le document lorem ipsum sit dolores amet

PDF - 61,88 Ko](%5B%C3%80%20MODIFIER%20-%20../../../../example/img/image.jpg%5D)


-


###
[Télécharger le document lorem ipsum sit dolores amet

PDF - 61,88 Ko](%5B%C3%80%20MODIFIER%20-%20../../../../example/img/image.jpg%5D)


###
Extrait de code


<div class="fr-downloads-group fr-downloads-group--bordered">
<p class="fr-downloads-group__title">Titre facultatif</p>
<ul>
<li>
<div class="fr-download">
<h3>
<a href="[À MODIFIER - ../../../../example/img/image.jpg]" id="fr-download-link-7069" download class="fr-download__link">Télécharger le document lorem ipsum sit dolores amet
<span class="fr-download__detail">
PDF - 61,88 Ko
</span>
</a>
</h3>
</div>
</li>
<li>
<div class="fr-download">
<h3>
<a href="[À MODIFIER - ../../../../example/img/image.jpg]" id="fr-download-link-7070" download class="fr-download__link">Télécharger le document lorem ipsum sit dolores amet
<span class="fr-download__detail">
PDF - 61,88 Ko
</span>
</a>
</h3>
</div>
</li>
<li>
<div class="fr-download">
<h3>
<a href="[À MODIFIER - ../../../../example/img/image.jpg]" id="fr-download-link-7071" download class="fr-download__link">Télécharger le document lorem ipsum sit dolores amet
<span class="fr-download__detail">
PDF - 61,88 Ko
</span>
</a>
</h3>
</div>
</li>
</ul>
</div>


###
Carte de téléchargement


## Carte de téléchargement


Le modificateur "--card" sur un download ou un groupe de download permet d'appliquer le style des carte. Il permet aussi d'ajouter un texte de description (facultatif).


#### Carte de téléchargement


dans une grille de 6 colonnes en version desktop


###
[Télécharger le document lorem ipsum sit dolores amet

JPG - 61,88 ko](%5B%C3%80%20MODIFIER%20-%20../../../../example/img/image.jpg%5D)


Description texte body small regular consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore...


###
Extrait de code


<div class="fr-download fr-enlarge-link fr-download--card">
<h3>
<a href="[À MODIFIER - ../../../../example/img/image.jpg]" id="fr-download-link-7075" download class="fr-download__link">Télécharger le document lorem ipsum sit dolores amet
<span class="fr-download__detail">
JPG - 61,88 ko
</span>
</a>
</h3>
<p class="fr-download__desc">Description texte body small regular consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore...</p>
</div>


###
Groupe de cartes


### Cartes de téléchargement en grille


###
[Télécharger le document lorem ipsum sit dolores amet

JPG - 61,88 ko](%5B%C3%80%20MODIFIER%20-%20../../../../example/img/image.jpg%5D)


Description texte body small regular consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore...


###
[Télécharger le document lorem ipsum sit dolores amet

JPG - 61,88 ko](%5B%C3%80%20MODIFIER%20-%20../../../../example/img/image.jpg%5D)


Description texte body small regular consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore...


###
[Télécharger le document lorem ipsum sit dolores amet

JPG - 61,88 ko](%5B%C3%80%20MODIFIER%20-%20../../../../example/img/image.jpg%5D)


Description texte body small regular consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore...


###
[Télécharger le document lorem ipsum sit dolores amet

JPG - 61,88 ko](%5B%C3%80%20MODIFIER%20-%20../../../../example/img/image.jpg%5D)


Description texte body small regular consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore...


###
Extrait de code


<div class="fr-grid-row fr-grid-row--gutters">
<div class="fr-col-12 fr-col-md-4">
<div class="fr-download fr-enlarge-link fr-download--card">
<h3>
<a href="[À MODIFIER - ../../../../example/img/image.jpg]" id="fr-download-link-7082" download class="fr-download__link">Télécharger le document lorem ipsum sit dolores amet
<span class="fr-download__detail">
JPG - 61,88 ko
</span>
</a>
</h3>
<p class="fr-download__desc">Description texte body small regular consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore...</p>
</div>
</div>
<div class="fr-col-12 fr-col-md-4">
<div class="fr-download fr-enlarge-link fr-download--card">
<h3>
<a href="[À MODIFIER - ../../../../example/img/image.jpg]" id="fr-download-link-7083" download class="fr-download__link">Télécharger le document lorem ipsum sit dolores amet
<span class="fr-download__detail">
JPG - 61,88 ko
</span>
</a>
</h3>
<p class="fr-download__desc">Description texte body small regular consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore...</p>
</div>
</div>
<div class="fr-col-12 fr-col-md-4">
<div class="fr-download fr-enlarge-link fr-download--card">
<h3>
<a href="[À MODIFIER - ../../../../example/img/image.jpg]" id="fr-download-link-7084" download class="fr-download__link">Télécharger le document lorem ipsum sit dolores amet
<span class="fr-download__detail">
JPG - 61,88 ko
</span>
</a>
</h3>
<p class="fr-download__desc">Description texte body small regular consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore...</p>
</div>
</div>
<div class="fr-col-12 fr-col-md-4">
<div class="fr-download fr-enlarge-link fr-download--card">
<h3>
<a href="[À MODIFIER - ../../../../example/img/image.jpg]" id="fr-download-link-7085" download class="fr-download__link">Télécharger le document lorem ipsum sit dolores amet
<span class="fr-download__detail">
JPG - 61,88 ko
</span>
</a>
</h3>
<p class="fr-download__desc">Description texte body small regular consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore...</p>
</div>
</div>
</div>


###
Fichier en langue étrangère


## Fichier d'une autre langue


Si la langue du fichier à télécharger est différente de celle de la page courante, il est nécéssaire d'ajouter l'attribut hreflang avec comme valeur le code langue (ex: hreflang="en") sur le lien. L'attribut prend pour valeur le code langue selon la norme ISO 639-1 ( [Liste des codes ISO 639-1](https://fr.wikipedia.org/wiki/Liste_des_codes_ISO_639-1) ). Il faut aussi ajouter le nom de la langue dans les détails (sauf remplissage automatique en js)


### Lien de téléchargement - langue étrangère


###
[Télécharger le document lorem ipsum sit dolores amet

JPG - 61,88 ko - Anglais](%5B%C3%80%20MODIFIER%20-%20../../../../example/img/image.jpg%5D)


###
Extrait de code


<div class="fr-download">
<h3>
<a href="[À MODIFIER - ../../../../example/img/image.jpg]" id="fr-download-link-7089" download hreflang="en" class="fr-download__link">Télécharger le document lorem ipsum sit dolores amet
<span class="fr-download__detail">
JPG - 61,88 ko - Anglais
</span>
</a>
</h3>
</div>


### Carte de téléchargement - langue étrangère


###
[Télécharger le document lorem ipsum sit dolores amet

JPG - 61,88 ko - Anglais](%5B%C3%80%20MODIFIER%20-%20../../../../example/img/image.jpg%5D)


Description texte body small regular consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore...


###
Extrait de code


<div class="fr-download fr-enlarge-link fr-download--card">
<h3>
<a href="[À MODIFIER - ../../../../example/img/image.jpg]" id="fr-download-link-7092" download hreflang="en" class="fr-download__link">Télécharger le document lorem ipsum sit dolores amet
<span class="fr-download__detail">
JPG - 61,88 ko - Anglais
</span>
</a>
</h3>
<p class="fr-download__desc">Description texte body small regular consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore...</p>
</div>


###
Utilitaire js


## Remplissage automatique des informations du fichier


Un utilitaire JS est disponible via l'attribut "data-fr-assess-file" pour remplacer le contenu du détails (type, poids, langue).

Le type du fichier est déterminé par son extension depuis l'attribut href.

Pour récupérer le poids, il est nécessaire que le fichier soit sur le même domaine ou que celui-ci autorise les requêtes cross-domain. Par défaut, l'unité de poids est l'octet. Il est possible d'opter pour l'unité bytes en ajoutant l'option dans l'attribut data-fr-assess-file="bytes"

La langue du fichier (si différente) doit être définie par son code langue dans l'attribut hreflang


### Lien de téléchargement remplissage automatique des détails


###
[Télécharger le document lorem ipsum sit dolores amet](../../../../dist/favicon/favicon.ico)


###
Extrait de code


<div class="fr-download">
<h3>
<a href="../../../../dist/favicon/favicon.ico" data-fr-assess-file id="fr-download-link-7096" download class="fr-download__link">Télécharger le document lorem ipsum sit dolores amet
<span class="fr-download__detail">
</span>
</a>
</h3>
</div>


### Carte de téléchargement remplissage automatique des détails


###
[Télécharger le document lorem ipsum sit dolores amet](../../../../dist/favicon/favicon.ico)


Description texte body small regular consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore...


###
Extrait de code


<div class="fr-download fr-enlarge-link fr-download--card">
<h3>
<a href="../../../../dist/favicon/favicon.ico" data-fr-assess-file id="fr-download-link-7099" download class="fr-download__link">Télécharger le document lorem ipsum sit dolores amet
<span class="fr-download__detail">
</span>
</a>
</h3>
<p class="fr-download__desc">Description texte body small regular consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore...</p>
</div>


### Remplissage automatique des détails + langue différente


###
[Télécharger le document lorem ipsum sit dolores amet](../../../../dist/favicon/favicon.ico)


###
Extrait de code


<div class="fr-download">
<h3>
<a href="../../../../dist/favicon/favicon.ico" data-fr-assess-file id="fr-download-link-7102" download hreflang="en" class="fr-download__link">Télécharger le document lorem ipsum sit dolores amet
<span class="fr-download__detail">
</span>
</a>
</h3>
</div>


### Poids du fichier en Bytes


###
[Download file lorem ipsum](../../../../dist/favicon/favicon.ico)


###
Extrait de code


<div class="fr-download" lang="en">
<h3>
<a href="../../../../dist/favicon/favicon.ico" data-fr-assess-file="bytes" id="fr-download-link-7105" download hreflang="en" class="fr-download__link">Download file lorem ipsum
<span class="fr-download__detail">
</span>
</a>
</h3>
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
