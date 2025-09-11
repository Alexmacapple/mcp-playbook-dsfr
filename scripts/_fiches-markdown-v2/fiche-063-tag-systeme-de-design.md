URL:
https://main--ds-gouv.netlify.app/example/component/tag

Title:
Tag - Système de design

Markdown:

Tag - Système de design


DSFR v1.14.0


[Retour](../)


# Tag (tag)


Le tag catégorise/classe/organise les contenus à l'aide de mots-clés. Il aide les utilisateurs à rechercher et à trouver facilement une information.
[Documentation](https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/tag)


## Tag non cliquable


Tag simple sans interaction


### Tag non cliquable sans icône


Libellé tag


###
Extrait de code


<p class="fr-tag">Libellé tag</p>


### Tag non cliquable icône à gauche


Libellé tag


###
Extrait de code


<p class="fr-tag fr-icon-arrow-left-line fr-tag--icon-left">Libellé tag</p>


### Tag non cliquable taille SM


Libellé tag


###
Extrait de code


<p class="fr-tag fr-tag--sm">Libellé tag</p>


## Tag cliquable


La balise utilisée pour le tag cliquable est un "a" s'il s'agit d'un lien (href), si pas de href utiliser "button".


### Tag cliquable


###
Extrait de code


<a class="fr-tag" href="#">Libellé tag</a>


### Tag cliquable avec icône


###
Extrait de code


<a class="fr-tag fr-icon-arrow-left-line fr-tag--icon-left" href="#">Libellé tag</a>


### Tag cliquable SM


###
Extrait de code


<a class="fr-tag fr-tag--sm" href="#">Libellé tag</a>


### Tag cliquable accentué


###
Extrait de code


<a class="fr-tag fr-tag--green-emeraude" href="#">Libellé tag</a>


### Tag cliquable désactivé


###
Extrait de code


<a class="fr-tag" aria-disabled="true" role="link">Libellé tag</a>


### Tag bouton cliquable désactivé


###
Extrait de code


<a class="fr-tag" aria-disabled="true" role="link">Libellé tag</a>


### Tag cliquable désactivé SM


###
Extrait de code


<a class="fr-tag fr-tag--sm" aria-disabled="true" role="link">Libellé tag</a>


## Tag sélectionnable


Le tag sélectionnable n'autorise pas l'accentuation.


### Tag sélectionnable


Libellé tag


###
Extrait de code


<button class="fr-tag" aria-pressed="false" type="button">Libellé tag</button>


### Tag sélectionnable avec icone


Libellé tag


###
Extrait de code


<button class="fr-tag fr-icon-information-line fr-tag--icon-left" aria-pressed="false" type="button">Libellé tag</button>


### Tag sélectionnable taille sm


Libellé tag


###
Extrait de code


<button class="fr-tag fr-tag--sm" aria-pressed="false" type="button">Libellé tag</button>


### Tag sélectionnable désactivé


Libellé tag


###
Extrait de code


<button class="fr-tag" aria-pressed="false" type="button" disabled>Libellé tag</button>


## Tag supprimable


Le tag supprimable n'autorise ni accentuation ni icône personnalisée.

Le javascript présent dans l'attribut onclick est donné à titre d'exemple, à vous de l'implémenter dans votre contexte technique.


### Tag supprimable


Libellé tag


###
Extrait de code


<button class="fr-tag fr-tag--dismiss" type="button" aria-label="Retirer [À MODIFIER - le filtre Libellé tag]">Libellé tag</button>


### Tag supprimable taille sm


Libellé tag


###
Extrait de code


<button class="fr-tag fr-tag--sm fr-tag--dismiss" type="button" aria-label="Retirer [À MODIFIER - le filtre Libellé tag]">Libellé tag</button>


### Tag supprimable désactivé


Libellé tag


###
Extrait de code


<button class="fr-tag fr-tag--dismiss" type="button" aria-label="Retirer [À MODIFIER - le filtre Libellé tag]" disabled>Libellé tag</button>


## Groupe de tags


Lorsque que l'on a plus d'un tag, il convient d'utiliser un groupe de tags.

La taille de tous les tags peut être définie au niveau du groupe.


### Groupe de tags non cliquables


-


Libellé tag 1


-


Libellé tag 2


-


Libellé tag 3


-


Libellé tag 4


-


Libellé tag 5


-


Libellé tag 6


-


Libellé tag 7


-


Libellé tag 8


-


Libellé tag 9


###
Extrait de code


<ul class="fr-tags-group">
<li>
<p class="fr-tag">Libellé tag 1</p>
</li>
<li>
<p class="fr-tag">Libellé tag 2</p>
</li>
<li>
<p class="fr-tag">Libellé tag 3</p>
</li>
<li>
<p class="fr-tag">Libellé tag 4</p>
</li>
<li>
<p class="fr-tag">Libellé tag 5</p>
</li>
<li>
<p class="fr-tag">Libellé tag 6</p>
</li>
<li>
<p class="fr-tag">Libellé tag 7</p>
</li>
<li>
<p class="fr-tag">Libellé tag 8</p>
</li>
<li>
<p class="fr-tag">Libellé tag 9</p>
</li>
</ul>


### Groupe de tags non cliquables SM


-


Libellé tag 1


-


Libellé tag 2


-


Libellé tag 3


-


Libellé tag 4


-


Libellé tag 5


-


Libellé tag 6


-


Libellé tag 7


-


Libellé tag 8


-


Libellé tag 9


###
Extrait de code


<ul class="fr-tags-group fr-tags-group--sm">
<li>
<p class="fr-tag">Libellé tag 1</p>
</li>
<li>
<p class="fr-tag">Libellé tag 2</p>
</li>
<li>
<p class="fr-tag">Libellé tag 3</p>
</li>
<li>
<p class="fr-tag">Libellé tag 4</p>
</li>
<li>
<p class="fr-tag">Libellé tag 5</p>
</li>
<li>
<p class="fr-tag">Libellé tag 6</p>
</li>
<li>
<p class="fr-tag">Libellé tag 7</p>
</li>
<li>
<p class="fr-tag">Libellé tag 8</p>
</li>
<li>
<p class="fr-tag">Libellé tag 9</p>
</li>
</ul>


### Groupe de tags cliquables


-
[Libellé tag 1](%5B%C3%80%20MODIFIER%20-%20url%5D)


-
[Libellé tag 2](%5B%C3%80%20MODIFIER%20-%20url%5D)


-
[Libellé tag 3](%5B%C3%80%20MODIFIER%20-%20url%5D)


-
[Libellé tag 4](%5B%C3%80%20MODIFIER%20-%20url%5D)


-
[Libellé tag 5](%5B%C3%80%20MODIFIER%20-%20url%5D)


-
[Libellé tag 6](%5B%C3%80%20MODIFIER%20-%20url%5D)


-
[Libellé tag 7](%5B%C3%80%20MODIFIER%20-%20url%5D)


-
[Libellé tag 8](%5B%C3%80%20MODIFIER%20-%20url%5D)


-
[Libellé tag 9](%5B%C3%80%20MODIFIER%20-%20url%5D)


###
Extrait de code


<ul class="fr-tags-group">
<li>
<a class="fr-tag" href="[À MODIFIER - url]">Libellé tag 1</a>
</li>
<li>
<a class="fr-tag" href="[À MODIFIER - url]">Libellé tag 2</a>
</li>
<li>
<a class="fr-tag" href="[À MODIFIER - url]">Libellé tag 3</a>
</li>
<li>
<a class="fr-tag" href="[À MODIFIER - url]">Libellé tag 4</a>
</li>
<li>
<a class="fr-tag" href="[À MODIFIER - url]">Libellé tag 5</a>
</li>
<li>
<a class="fr-tag" href="[À MODIFIER - url]">Libellé tag 6</a>
</li>
<li>
<a class="fr-tag" href="[À MODIFIER - url]">Libellé tag 7</a>
</li>
<li>
<a class="fr-tag" href="[À MODIFIER - url]">Libellé tag 8</a>
</li>
<li>
<a class="fr-tag" href="[À MODIFIER - url]">Libellé tag 9</a>
</li>
</ul>


### Groupe de tags cliquables SM


-
[Libellé tag 1](%5B%C3%80%20MODIFIER%20-%20url%5D)


-
[Libellé tag 2](%5B%C3%80%20MODIFIER%20-%20url%5D)


-
[Libellé tag 3](%5B%C3%80%20MODIFIER%20-%20url%5D)


-
[Libellé tag 4](%5B%C3%80%20MODIFIER%20-%20url%5D)


-
[Libellé tag 5](%5B%C3%80%20MODIFIER%20-%20url%5D)


-
[Libellé tag 6](%5B%C3%80%20MODIFIER%20-%20url%5D)


-
[Libellé tag 7](%5B%C3%80%20MODIFIER%20-%20url%5D)


-
[Libellé tag 8](%5B%C3%80%20MODIFIER%20-%20url%5D)


-
[Libellé tag 9](%5B%C3%80%20MODIFIER%20-%20url%5D)


###
Extrait de code


<ul class="fr-tags-group fr-tags-group--sm">
<li>
<a class="fr-tag" href="[À MODIFIER - url]">Libellé tag 1</a>
</li>
<li>
<a class="fr-tag" href="[À MODIFIER - url]">Libellé tag 2</a>
</li>
<li>
<a class="fr-tag" href="[À MODIFIER - url]">Libellé tag 3</a>
</li>
<li>
<a class="fr-tag" href="[À MODIFIER - url]">Libellé tag 4</a>
</li>
<li>
<a class="fr-tag" href="[À MODIFIER - url]">Libellé tag 5</a>
</li>
<li>
<a class="fr-tag" href="[À MODIFIER - url]">Libellé tag 6</a>
</li>
<li>
<a class="fr-tag" href="[À MODIFIER - url]">Libellé tag 7</a>
</li>
<li>
<a class="fr-tag" href="[À MODIFIER - url]">Libellé tag 8</a>
</li>
<li>
<a class="fr-tag" href="[À MODIFIER - url]">Libellé tag 9</a>
</li>
</ul>


### Groupe de tags sélectionnables


-
Libellé tag 1


-
Libellé tag 2


-
Libellé tag 3


-
Libellé tag 4


-
Libellé tag 5


-
Libellé tag 6


-
Libellé tag 7


-
Libellé tag 8


-
Libellé tag 9


###
Extrait de code


<ul class="fr-tags-group">
<li>
<button class="fr-tag" type="button" aria-pressed="false">Libellé tag 1</button>
</li>
<li>
<button class="fr-tag" type="button" aria-pressed="false">Libellé tag 2</button>
</li>
<li>
<button class="fr-tag" type="button" aria-pressed="false">Libellé tag 3</button>
</li>
<li>
<button class="fr-tag" type="button" aria-pressed="false">Libellé tag 4</button>
</li>
<li>
<button class="fr-tag" type="button" aria-pressed="false">Libellé tag 5</button>
</li>
<li>
<button class="fr-tag" type="button" aria-pressed="false">Libellé tag 6</button>
</li>
<li>
<button class="fr-tag" type="button" aria-pressed="false">Libellé tag 7</button>
</li>
<li>
<button class="fr-tag" type="button" aria-pressed="false">Libellé tag 8</button>
</li>
<li>
<button class="fr-tag" type="button" aria-pressed="false">Libellé tag 9</button>
</li>
</ul>


### Groupe de tags sélectionnables SM


-
Libellé tag 1


-
Libellé tag 2


-
Libellé tag 3


-
Libellé tag 4


-
Libellé tag 5


-
Libellé tag 6


-
Libellé tag 7


-
Libellé tag 8


-
Libellé tag 9


###
Extrait de code


<ul class="fr-tags-group fr-tags-group--sm">
<li>
<button class="fr-tag" type="button" aria-pressed="false">Libellé tag 1</button>
</li>
<li>
<button class="fr-tag" type="button" aria-pressed="false">Libellé tag 2</button>
</li>
<li>
<button class="fr-tag" type="button" aria-pressed="false">Libellé tag 3</button>
</li>
<li>
<button class="fr-tag" type="button" aria-pressed="false">Libellé tag 4</button>
</li>
<li>
<button class="fr-tag" type="button" aria-pressed="false">Libellé tag 5</button>
</li>
<li>
<button class="fr-tag" type="button" aria-pressed="false">Libellé tag 6</button>
</li>
<li>
<button class="fr-tag" type="button" aria-pressed="false">Libellé tag 7</button>
</li>
<li>
<button class="fr-tag" type="button" aria-pressed="false">Libellé tag 8</button>
</li>
<li>
<button class="fr-tag" type="button" aria-pressed="false">Libellé tag 9</button>
</li>
</ul>


### Groupe de tags supprimables


-
Libellé tag 1


-
Libellé tag 2


-
Libellé tag 3


-
Libellé tag 4


-
Libellé tag 5


-
Libellé tag 6


-
Libellé tag 7


-
Libellé tag 8


-
Libellé tag 9


###
Extrait de code


<ul class="fr-tags-group">
<li>
<button class="fr-tag fr-tag--dismiss" type="button" aria-label="Retirer [À MODIFIER - le filtre Libellé tag 1]">Libellé tag 1</button>
</li>
<li>
<button class="fr-tag fr-tag--dismiss" type="button" aria-label="Retirer [À MODIFIER - le filtre Libellé tag 2]">Libellé tag 2</button>
</li>
<li>
<button class="fr-tag fr-tag--dismiss" type="button" aria-label="Retirer [À MODIFIER - le filtre Libellé tag 3]">Libellé tag 3</button>
</li>
<li>
<button class="fr-tag fr-tag--dismiss" type="button" aria-label="Retirer [À MODIFIER - le filtre Libellé tag 4]">Libellé tag 4</button>
</li>
<li>
<button class="fr-tag fr-tag--dismiss" type="button" aria-label="Retirer [À MODIFIER - le filtre Libellé tag 5]">Libellé tag 5</button>
</li>
<li>
<button class="fr-tag fr-tag--dismiss" type="button" aria-label="Retirer [À MODIFIER - le filtre Libellé tag 6]">Libellé tag 6</button>
</li>
<li>
<button class="fr-tag fr-tag--dismiss" type="button" aria-label="Retirer [À MODIFIER - le filtre Libellé tag 7]">Libellé tag 7</button>
</li>
<li>
<button class="fr-tag fr-tag--dismiss" type="button" aria-label="Retirer [À MODIFIER - le filtre Libellé tag 8]">Libellé tag 8</button>
</li>
<li>
<button class="fr-tag fr-tag--dismiss" type="button" aria-label="Retirer [À MODIFIER - le filtre Libellé tag 9]">Libellé tag 9</button>
</li>
</ul>


### Groupe de tags supprimables SM


-
Libellé tag 1


-
Libellé tag 2


-
Libellé tag 3


-
Libellé tag 4


-
Libellé tag 5


-
Libellé tag 6


-
Libellé tag 7


-
Libellé tag 8


-
Libellé tag 9


###
Extrait de code


<ul class="fr-tags-group fr-tags-group--sm">
<li>
<button class="fr-tag fr-tag--dismiss" type="button" aria-label="Retirer [À MODIFIER - le filtre Libellé tag 1]">Libellé tag 1</button>
</li>
<li>
<button class="fr-tag fr-tag--dismiss" type="button" aria-label="Retirer [À MODIFIER - le filtre Libellé tag 2]">Libellé tag 2</button>
</li>
<li>
<button class="fr-tag fr-tag--dismiss" type="button" aria-label="Retirer [À MODIFIER - le filtre Libellé tag 3]">Libellé tag 3</button>
</li>
<li>
<button class="fr-tag fr-tag--dismiss" type="button" aria-label="Retirer [À MODIFIER - le filtre Libellé tag 4]">Libellé tag 4</button>
</li>
<li>
<button class="fr-tag fr-tag--dismiss" type="button" aria-label="Retirer [À MODIFIER - le filtre Libellé tag 5]">Libellé tag 5</button>
</li>
<li>
<button class="fr-tag fr-tag--dismiss" type="button" aria-label="Retirer [À MODIFIER - le filtre Libellé tag 6]">Libellé tag 6</button>
</li>
<li>
<button class="fr-tag fr-tag--dismiss" type="button" aria-label="Retirer [À MODIFIER - le filtre Libellé tag 7]">Libellé tag 7</button>
</li>
<li>
<button class="fr-tag fr-tag--dismiss" type="button" aria-label="Retirer [À MODIFIER - le filtre Libellé tag 8]">Libellé tag 8</button>
</li>
<li>
<button class="fr-tag fr-tag--dismiss" type="button" aria-label="Retirer [À MODIFIER - le filtre Libellé tag 9]">Libellé tag 9</button>
</li>
</ul>


Libellé bouton


Fermer


##
Paramètres d'affichage


Choisissez un thème pour personnaliser l'apparence du site.


Thème clair


Thème sombre


Système
Utilise les paramètres système
