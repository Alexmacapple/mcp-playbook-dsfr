URL:
https://main--ds-gouv.netlify.app/example/component/pagination

Title:
Pagination - Système de design

Markdown:

Pagination - Système de design


DSFR v1.14.0


[Retour](../)


# Pagination (pagination)


La pagination permet à l'utilisateur de naviguer entre les différentes pages d'une liste d'éléments.
[Documentation](https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/pagination)


### Élément de navigation icône seule (par défaut)


-


###
Extrait de code


<nav role="navigation" class="fr-pagination" aria-label="Pagination">
<ul class="fr-pagination__list">
<li>
<a class="fr-pagination__link fr-pagination__link--prev" href="#">
Page précédente
</a>
</li>
</ul>
</nav>


### Élément de navigation avec libellés


-


###
Extrait de code


<nav role="navigation" class="fr-pagination" aria-label="Pagination">
<ul class="fr-pagination__list">
<li>
<a class="fr-pagination__link fr-pagination__link--prev fr-pagination__link--label" href="#">
Page précédente
</a>
</li>
</ul>
</nav>


### Élément de navigation avec libellés à partir du breakpoint LG


-


###
Extrait de code


<nav role="navigation" class="fr-pagination" aria-label="Pagination">
<ul class="fr-pagination__list">
<li>
<a class="fr-pagination__link fr-pagination__link--prev fr-pagination__link--lg-label" href="#">
Page précédente
</a>
</li>
</ul>
</nav>


### Pagination première page


-


-


-


-


-


-

...


-


-


-


-


-


###
Extrait de code


<nav role="navigation" class="fr-pagination" aria-label="Pagination" data-fr-analytics-page-total="132">
<ul class="fr-pagination__list">
<li>
<a class="fr-pagination__link fr-pagination__link--first" id="pagination-6222" title="Première page" aria-disabled="true" role="link">
Première page
</a>
</li>
<li>
<a class="fr-pagination__link fr-pagination__link--prev fr-pagination__link--lg-label" id="pagination-6223" title="Page précédente" aria-disabled="true" role="link">
Page précédente
</a>
</li>
<li>
<a class="fr-pagination__link" id="pagination-6215" aria-current="page" title="Page 1">
1
</a>
</li>
<li>
<a class="fr-pagination__link" id="pagination-6216" href="#" title="Page 2">
2
</a>
</li>
<li>
<a class="fr-pagination__link fr-hidden fr-unhidden-lg" id="pagination-6217" href="#" title="Page 3">
3
</a>
</li>
<li>
<span class="fr-pagination__link fr-hidden fr-unhidden-lg" id="pagination-6218">
...
</span>
</li>
<li>
<a class="fr-pagination__link fr-hidden fr-unhidden-lg" id="pagination-6219" href="#" title="Page 130">
130
</a>
</li>
<li>
<a class="fr-pagination__link fr-hidden fr-unhidden-lg" id="pagination-6220" href="#" title="Page 131">
131
</a>
</li>
<li>
<a class="fr-pagination__link" id="pagination-6221" href="#" title="Page 132">
132
</a>
</li>
<li>
<a class="fr-pagination__link fr-pagination__link--next fr-pagination__link--lg-label" id="pagination-6224" href="#" title="Page suivante">
Page suivante
</a>
</li>
<li>
<a class="fr-pagination__link fr-pagination__link--last" id="pagination-6225" href="#" title="Dernière page">
Dernière page
</a>
</li>
</ul>
</nav>


### Pagination deuxième page


-


-


-


-


-


-

...


-


-


-


-


-


###
Extrait de code


<nav role="navigation" class="fr-pagination" aria-label="Pagination" data-fr-analytics-page-total="132">
<ul class="fr-pagination__list">
<li>
<a class="fr-pagination__link fr-pagination__link--first" id="pagination-6245" href="#" title="Première page">
Première page
</a>
</li>
<li>
<a class="fr-pagination__link fr-pagination__link--prev fr-pagination__link--lg-label" id="pagination-6246" href="#" title="Page précédente">
Page précédente
</a>
</li>
<li>
<a class="fr-pagination__link" id="pagination-6238" href="#" title="Page 1">
1
</a>
</li>
<li>
<a class="fr-pagination__link" id="pagination-6239" aria-current="page" title="Page 2">
2
</a>
</li>
<li>
<a class="fr-pagination__link fr-hidden fr-unhidden-lg" id="pagination-6240" href="#" title="Page 3">
3
</a>
</li>
<li>
<span class="fr-pagination__link fr-hidden fr-unhidden-lg" id="pagination-6241">
...
</span>
</li>
<li>
<a class="fr-pagination__link fr-hidden fr-unhidden-lg" id="pagination-6242" href="#" title="Page 130">
130
</a>
</li>
<li>
<a class="fr-pagination__link fr-hidden fr-unhidden-lg" id="pagination-6243" href="#" title="Page 131">
131
</a>
</li>
<li>
<a class="fr-pagination__link" id="pagination-6244" href="#" title="Page 132">
132
</a>
</li>
<li>
<a class="fr-pagination__link fr-pagination__link--next fr-pagination__link--lg-label" id="pagination-6247" href="#" title="Page suivante">
Page suivante
</a>
</li>
<li>
<a class="fr-pagination__link fr-pagination__link--last" id="pagination-6248" href="#" title="Dernière page">
Dernière page
</a>
</li>
</ul>
</nav>


### Pagination dernière page


-


-


-


-


-


-

...


-


-


-


-


-


###
Extrait de code


<nav role="navigation" class="fr-pagination" aria-label="Pagination" data-fr-analytics-page-total="132">
<ul class="fr-pagination__list">
<li>
<a class="fr-pagination__link fr-pagination__link--first" id="pagination-6268" href="#" title="Première page">
Première page
</a>
</li>
<li>
<a class="fr-pagination__link fr-pagination__link--prev fr-pagination__link--lg-label" id="pagination-6269" href="#" title="Page précédente">
Page précédente
</a>
</li>
<li>
<a class="fr-pagination__link" id="pagination-6261" href="#" title="Page 1">
1
</a>
</li>
<li>
<a class="fr-pagination__link" id="pagination-6262" href="#" title="Page 2">
2
</a>
</li>
<li>
<a class="fr-pagination__link fr-hidden fr-unhidden-lg" id="pagination-6263" href="#" title="Page 3">
3
</a>
</li>
<li>
<span class="fr-pagination__link fr-hidden fr-unhidden-lg" id="pagination-6264">
...
</span>
</li>
<li>
<a class="fr-pagination__link fr-hidden fr-unhidden-lg" id="pagination-6265" href="#" title="Page 130">
130
</a>
</li>
<li>
<a class="fr-pagination__link fr-hidden fr-unhidden-lg" id="pagination-6266" href="#" title="Page 131">
131
</a>
</li>
<li>
<a class="fr-pagination__link" id="pagination-6267" aria-current="page" title="Page 132">
132
</a>
</li>
<li>
<a class="fr-pagination__link fr-pagination__link--next fr-pagination__link--lg-label" id="pagination-6270" title="Page suivante" aria-disabled="true" role="link">
Page suivante
</a>
</li>
<li>
<a class="fr-pagination__link fr-pagination__link--last" id="pagination-6271" title="Dernière page" aria-disabled="true" role="link">
Dernière page
</a>
</li>
</ul>
</nav>


Libellé bouton


Fermer


##
Paramètres d'affichage


Choisissez un thème pour personnaliser l'apparence du site.


Thème clair


Thème sombre


Système
Utilise les paramètres système
