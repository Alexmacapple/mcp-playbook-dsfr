URL:
https://main--ds-gouv.netlify.app/example/component/link/download

Title:
Lien - Système de design

Markdown:

Lien - Système de design


DSFR v1.14.0


[Retour](../)


# Lien (link)


Le lien permet la navigation entre une page et un autre contenu au sein de la même page, du même site ou externe. Pour les actions d'un autre type - comme la soumission d'un formulaire - il faut utiliser le composant bouton.
[Documentation](https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/lien)


### Lien de téléchargement


[Télécharger le document lorem ipsum sit dolores amet JPG - 61,88 ko](/example/img/image.jpg)


###
Extrait de code


<a id="link-4320" download="true" href="/example/img/image.jpg" class="fr-link fr-link--download">Télécharger le document lorem ipsum sit dolores amet <span class="fr-link__detail">JPG - 61,88 ko</span>
</a>


### Lien de téléchargement avec bouton


Télécharger le document lorem ipsum sit dolores amet JPG - 61,88 ko


###
Extrait de code


<button id="link-4323" download="true" class="fr-link fr-link--download">Télécharger le document lorem ipsum sit dolores amet <span class="fr-link__detail">JPG - 61,88 ko</span>
</button>


### Groupe de lien de téléchargement


-
[Télécharger le document lorem ipsum sit dolores amet JPG - 61,88 ko](%5B%C3%80%20MODIFIER%20-%20../../../../example/img/image.jpg%5D)


-
[Télécharger le document lorem ipsum sit dolores amet JPG - 61,88 ko](%5B%C3%80%20MODIFIER%20-%20../../../../example/img/image.jpg%5D)


-
[Télécharger le document lorem ipsum sit dolores amet JPG - 61,88 ko](%5B%C3%80%20MODIFIER%20-%20../../../../example/img/image.jpg%5D)


###
Extrait de code


<ul class="fr-links-group">
<li>
<a id="link-4328" download="true" href="[À MODIFIER - ../../../../example/img/image.jpg]" class="fr-link fr-link--download">Télécharger le document lorem ipsum sit dolores amet <span class="fr-link__detail">JPG - 61,88 ko</span>
</a>
</li>
<li>
<a id="link-4329" download="true" href="[À MODIFIER - ../../../../example/img/image.jpg]" class="fr-link fr-link--download">Télécharger le document lorem ipsum sit dolores amet <span class="fr-link__detail">JPG - 61,88 ko</span>
</a>
</li>
<li>
<a id="link-4330" download="true" href="[À MODIFIER - ../../../../example/img/image.jpg]" class="fr-link fr-link--download">Télécharger le document lorem ipsum sit dolores amet <span class="fr-link__detail">JPG - 61,88 ko</span>
</a>
</li>
</ul>


### Fichier en langue étrangère


Indiquer le code langue (ISO 639‑1) du fichier dans l'attribut "hreflang" et la langue en toute lettre dans le détail


[Télécharger le document lorem ipsum sit dolores amet PDF - 1,81 Mo - Anglais](lang=%22en%22)


###
Extrait de code


<a id="link-4333" hreflang="en" download="true" href="exemple.pdf" class="fr-link fr-link--download">Télécharger le document lorem ipsum sit dolores amet <span class="fr-link__detail">PDF - 1,81 Mo - Anglais</span>
</a>


### Remplissage automatique des détails


L'attribut data-fr-assess-file permet de remplir automatiquement le détail avec le type, le poids, et la langue (hreflang) du fichier.


[Télécharger le document lorem ipsum sit dolores amet](/example/img/image.jpg)


###
Extrait de code


<a id="link-4336" data-fr-assess-file download="true" href="/example/img/image.jpg" class="fr-link fr-link--download">Télécharger le document lorem ipsum sit dolores amet <span class="fr-link__detail"> </span>
</a>


### Remplissage automatique des détails en Bytes


Sur une page en anglais, ou toute autre langue utilisant l'unité "Bytes" plutot que "Octet", ajouter la valeur "bytes" sur l'attribut : data-fr-assess-file="bytes".


[Download the french document lorem ipsum](lang=%22fr%22)


###
Extrait de code


<a id="link-4339" hreflang="fr" data-fr-assess-file="bytes" download="true" href="/example/img/image.jpg" class="fr-link fr-link--download">Download the french document lorem ipsum <span class="fr-link__detail"> </span>
</a>


Libellé bouton


Fermer


##
Paramètres d'affichage


Choisissez un thème pour personnaliser l'apparence du site.


Thème clair


Thème sombre


Système
Utilise les paramètres système
