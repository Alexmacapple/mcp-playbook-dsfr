URL:
https://main--ds-gouv.netlify.app/example/component/tab

Title:
Onglets - Système de design

Markdown:

Onglets - Système de design


DSFR v1.14.0


[Retour](../)


# Onglets (tab)


Le composant onglet permet aux utilisateurs de naviguer dans différentes sections de contenu au sein d'une même page.
[Documentation](https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/onglet)


### Onglets 4 éléments


-
Libellé onglet 1


-
Libellé onglet 2


-
Libellé onglet 3


-
Libellé onglet 4


#### Contenu 1


- list item
- list item niveau 2

- list item niveau 2


- list item


#### Contenu 2

![no alt text](../../../example/img/placeholder.16x9.png)


- list item

- list item


#### Contenu 3

![no alt text](../../../example/img/placeholder.16x9.png)


- list item
- list item niveau 2


- list item


#### Contenu 4


Lorem ipsum dolor sit amet, consectetur adipiscing, [link test](https://www.systeme-de-design.gouv.fr/) incididunt, ut labore et dolore magna aliqua. Vitae sapien pellentesque habitant morbi tristique senectus et. Diam maecenas sed enim ut. Accumsan lacus vel facilisis volutpat est. Ut aliquam purus sit amet luctus. Lorem ipsum dolor sit amet consectetur adipiscing elit ut.

- list item


###
Extrait de code


<div class="fr-tabs">
<ul class="fr-tabs__list" role="tablist" aria-label="[A modifier | nom du système d'onglet]">
<li role="presentation">
<button type="button" id="tab-6123" class="fr-tabs__tab fr-icon-checkbox-circle-line fr-tabs__tab--icon-left" tabindex="0" role="tab" aria-selected="true" aria-controls="tab-6123-panel">Libellé onglet 1</button>
</li>
<li role="presentation">
<button type="button" id="tab-6124" class="fr-tabs__tab fr-icon-checkbox-circle-line fr-tabs__tab--icon-left" tabindex="-1" role="tab" aria-selected="false" aria-controls="tab-6124-panel">Libellé onglet 2</button>
</li>
<li role="presentation">
<button type="button" id="tab-6125" class="fr-tabs__tab fr-icon-checkbox-circle-line fr-tabs__tab--icon-left" tabindex="-1" role="tab" aria-selected="false" aria-controls="tab-6125-panel">Libellé onglet 3</button>
</li>
<li role="presentation">
<button type="button" id="tab-6126" class="fr-tabs__tab fr-icon-checkbox-circle-line fr-tabs__tab--icon-left" tabindex="-1" role="tab" aria-selected="false" aria-controls="tab-6126-panel">Libellé onglet 4</button>
</li>
</ul>
<div id="tab-6123-panel" class="fr-tabs__panel fr-tabs__panel--selected" role="tabpanel" aria-labelledby="tab-6123" tabindex="0">
<!-- données de test -->
</div>
<div id="tab-6124-panel" class="fr-tabs__panel" role="tabpanel" aria-labelledby="tab-6124" tabindex="0">
<!-- données de test -->
</div>
<div id="tab-6125-panel" class="fr-tabs__panel" role="tabpanel" aria-labelledby="tab-6125" tabindex="0">
<!-- données de test -->
</div>
<div id="tab-6126-panel" class="fr-tabs__panel" role="tabpanel" aria-labelledby="tab-6126" tabindex="0">
<!-- données de test -->
</div>
</div>


### Onglets 2 éléments


-
Libellé onglet 1


-
Libellé onglet 2


#### Contenu 1


- list item
- list item niveau 2

- list item niveau 2


- list item


#### Contenu 2


Lorem ipsum dolor sit amet, consectetur adipiscing, [link test](https://www.systeme-de-design.gouv.fr/) incididunt, ut labore et dolore magna aliqua. Vitae sapien pellentesque habitant morbi tristique senectus et. Diam maecenas sed enim ut. Accumsan lacus vel facilisis volutpat est. Ut aliquam purus sit amet luctus. Lorem ipsum dolor sit amet consectetur adipiscing elit ut.

- list item

- list item
- list item niveau 2

- list item niveau 2


###
Extrait de code


<div class="fr-tabs">
<ul class="fr-tabs__list" role="tablist" aria-label="[A modifier | nom du système d'onglet]">
<li role="presentation">
<button type="button" id="tab-6130" class="fr-tabs__tab" tabindex="0" role="tab" aria-selected="true" aria-controls="tab-6130-panel">Libellé onglet 1</button>
</li>
<li role="presentation">
<button type="button" id="tab-6131" class="fr-tabs__tab" tabindex="-1" role="tab" aria-selected="false" aria-controls="tab-6131-panel">Libellé onglet 2</button>
</li>
</ul>
<div id="tab-6130-panel" class="fr-tabs__panel fr-tabs__panel--selected" role="tabpanel" aria-labelledby="tab-6130" tabindex="0">
<!-- données de test -->
</div>
<div id="tab-6131-panel" class="fr-tabs__panel" role="tabpanel" aria-labelledby="tab-6131" tabindex="0">
<!-- données de test -->
</div>
</div>


### Onglets dans onglets


-
Onglet principal 0


-
Onglet principal 1


-
Onglet imbriqué 0


-
Onglet imbriqué 1


-
Onglet imbriqué 2


-
Libellé onglet 1


-
Libellé onglet 2


#### Contenu 1

![no alt text](../../../example/img/placeholder.16x9.png)


Lorem ipsum dolor sit amet, consectetur adipiscing, [link test](https://www.systeme-de-design.gouv.fr/) incididunt, ut labore et dolore magna aliqua. Vitae sapien pellentesque habitant morbi tristique senectus et. Diam maecenas sed enim ut. Accumsan lacus vel facilisis volutpat est. Ut aliquam purus sit amet luctus. Lorem ipsum dolor sit amet consectetur adipiscing elit ut.

- list item


#### Contenu 2


- list item
- list item niveau 2

- list item niveau 2


- list item


-
Libellé onglet 1


-
Libellé onglet 2


-
Libellé onglet 3


#### Contenu 1


Lorem ipsum dolor sit amet, consectetur adipiscing, [link test](https://www.systeme-de-design.gouv.fr/) incididunt, ut labore et dolore magna aliqua. Vitae sapien pellentesque habitant morbi tristique senectus et. Diam maecenas sed enim ut. Accumsan lacus vel facilisis volutpat est. Ut aliquam purus sit amet luctus. Lorem ipsum dolor sit amet consectetur adipiscing elit ut.

- list item
- list item niveau 2


#### Contenu 2

![no alt text](../../../example/img/placeholder.16x9.png)


- list item
- list item niveau 2


#### Contenu 3


Lorem ipsum dolor sit amet, consectetur adipiscing, [link test](https://www.systeme-de-design.gouv.fr/) incididunt, ut labore et dolore magna aliqua. Vitae sapien pellentesque habitant morbi tristique senectus et. Diam maecenas sed enim ut. Accumsan lacus vel facilisis volutpat est. Ut aliquam purus sit amet luctus. Lorem ipsum dolor sit amet consectetur adipiscing elit ut.

- list item

- list item


-
Libellé onglet 1


-
Libellé onglet 2


-
Libellé onglet 3


-
Libellé onglet 4


#### Contenu 1

![no alt text](../../../example/img/placeholder.16x9.png)


- list item
- list item niveau 2

- list item niveau 2


#### Contenu 2


Lorem ipsum dolor sit amet, consectetur adipiscing, [link test](https://www.systeme-de-design.gouv.fr/) incididunt, ut labore et dolore magna aliqua. Vitae sapien pellentesque habitant morbi tristique senectus et. Diam maecenas sed enim ut. Accumsan lacus vel facilisis volutpat est. Ut aliquam purus sit amet luctus. Lorem ipsum dolor sit amet consectetur adipiscing elit ut.

- list item

- list item


#### Contenu 3


Lorem ipsum dolor sit amet, consectetur adipiscing, [link test](https://www.systeme-de-design.gouv.fr/) incididunt, ut labore et dolore magna aliqua. Vitae sapien pellentesque habitant morbi tristique senectus et. Diam maecenas sed enim ut. Accumsan lacus vel facilisis volutpat est. Ut aliquam purus sit amet luctus. Lorem ipsum dolor sit amet consectetur adipiscing elit ut.

- list item
- list item niveau 2


- list item
- list item niveau 2

- list item niveau 2


#### Contenu 4


Lorem ipsum dolor sit amet, consectetur adipiscing, [link test](https://www.systeme-de-design.gouv.fr/) incididunt, ut labore et dolore magna aliqua. Vitae sapien pellentesque habitant morbi tristique senectus et. Diam maecenas sed enim ut. Accumsan lacus vel facilisis volutpat est. Ut aliquam purus sit amet luctus. Lorem ipsum dolor sit amet consectetur adipiscing elit ut.

- list item

- list item


-
Onglet imbriqué 0


-
Onglet imbriqué 1


-
Libellé onglet 1


-
Libellé onglet 2


#### Contenu 1


Lorem ipsum dolor sit amet, consectetur adipiscing, [link test](https://www.systeme-de-design.gouv.fr/) incididunt, ut labore et dolore magna aliqua. Vitae sapien pellentesque habitant morbi tristique senectus et. Diam maecenas sed enim ut. Accumsan lacus vel facilisis volutpat est. Ut aliquam purus sit amet luctus. Lorem ipsum dolor sit amet consectetur adipiscing elit ut.

- list item
- list item niveau 2

- list item niveau 2


- list item


#### Contenu 2

![no alt text](../../../example/img/placeholder.16x9.png)


- list item


-
Libellé onglet 1


-
Libellé onglet 2


-
Libellé onglet 3


#### Contenu 1


- list item

- list item


#### Contenu 2

![no alt text](../../../example/img/placeholder.16x9.png)


- list item
- list item niveau 2

- list item niveau 2


- list item
- list item niveau 2

- list item niveau 2


#### Contenu 3


- list item


###
Extrait de code


<div class="fr-tabs">
<ul class="fr-tabs__list" role="tablist" aria-label="[A modifier | nom du système d'onglet]">
<li role="presentation">
<button type="button" id="tabs-in-tabs-6171" class="fr-tabs__tab" tabindex="0" role="tab" aria-selected="true" aria-controls="tabs-in-tabs-6171-panel">Onglet principal 0</button>
</li>
<li role="presentation">
<button type="button" id="tabs-in-tabs-6182" class="fr-tabs__tab" tabindex="-1" role="tab" aria-selected="false" aria-controls="tabs-in-tabs-6182-panel">Onglet principal 1</button>
</li>
</ul>
<div id="tabs-in-tabs-6171-panel" class="fr-tabs__panel fr-tabs__panel--selected" role="tabpanel" aria-labelledby="tabs-in-tabs-6171" tabindex="0">
<div class="fr-tabs">
<ul class="fr-tabs__list" role="tablist" aria-label="[A modifier | nom du système d'onglet]">
<li role="presentation">
<button type="button" id="tab-6172" class="fr-tabs__tab" tabindex="0" role="tab" aria-selected="true" aria-controls="tab-6172-panel">Onglet imbriqué 0</button>
</li>
<li role="presentation">
<button type="button" id="tab-6173" class="fr-tabs__tab" tabindex="-1" role="tab" aria-selected="false" aria-controls="tab-6173-panel">Onglet imbriqué 1</button>
</li>
<li role="presentation">
<button type="button" id="tab-6174" class="fr-tabs__tab" tabindex="-1" role="tab" aria-selected="false" aria-controls="tab-6174-panel">Onglet imbriqué 2</button>
</li>
</ul>
<div id="tab-6172-panel" class="fr-tabs__panel fr-tabs__panel--selected" role="tabpanel" aria-labelledby="tab-6172" tabindex="0">
<div class="fr-tabs">
<ul class="fr-tabs__list" role="tablist" aria-label="[A modifier | nom du système d'onglet]">
<li role="presentation">
<button type="button" id="tab-6160" class="fr-tabs__tab" tabindex="0" role="tab" aria-selected="true" aria-controls="tab-6160-panel">Libellé onglet 1</button>
</li>
<li role="presentation">
<button type="button" id="tab-6161" class="fr-tabs__tab" tabindex="-1" role="tab" aria-selected="false" aria-controls="tab-6161-panel">Libellé onglet 2</button>
</li>
</ul>
<div id="tab-6160-panel" class="fr-tabs__panel fr-tabs__panel--selected" role="tabpanel" aria-labelledby="tab-6160" tabindex="0">
<!-- données de test -->
</div>
<div id="tab-6161-panel" class="fr-tabs__panel" role="tabpanel" aria-labelledby="tab-6161" tabindex="0">
<!-- données de test -->
</div>
</div>
</div>
<div id="tab-6173-panel" class="fr-tabs__panel" role="tabpanel" aria-labelledby="tab-6173" tabindex="0">
<div class="fr-tabs">
<ul class="fr-tabs__list" role="tablist" aria-label="[A modifier | nom du système d'onglet]">
<li role="presentation">
<button type="button" id="tab-6163" class="fr-tabs__tab" tabindex="0" role="tab" aria-selected="true" aria-controls="tab-6163-panel">Libellé onglet 1</button>
</li>
<li role="presentation">
<button type="button" id="tab-6164" class="fr-tabs__tab" tabindex="-1" role="tab" aria-selected="false" aria-controls="tab-6164-panel">Libellé onglet 2</button>
</li>
<li role="presentation">
<button type="button" id="tab-6165" class="fr-tabs__tab" tabindex="-1" role="tab" aria-selected="false" aria-controls="tab-6165-panel">Libellé onglet 3</button>
</li>
</ul>
<div id="tab-6163-panel" class="fr-tabs__panel fr-tabs__panel--selected" role="tabpanel" aria-labelledby="tab-6163" tabindex="0">
<!-- données de test -->
</div>
<div id="tab-6164-panel" class="fr-tabs__panel" role="tabpanel" aria-labelledby="tab-6164" tabindex="0">
<!-- données de test -->
</div>
<div id="tab-6165-panel" class="fr-tabs__panel" role="tabpanel" aria-labelledby="tab-6165" tabindex="0">
<!-- données de test -->
</div>
</div>
</div>
<div id="tab-6174-panel" class="fr-tabs__panel" role="tabpanel" aria-labelledby="tab-6174" tabindex="0">
<div class="fr-tabs">
<ul class="fr-tabs__list" role="tablist" aria-label="[A modifier | nom du système d'onglet]">
<li role="presentation">
<button type="button" id="tab-6167" class="fr-tabs__tab" tabindex="0" role="tab" aria-selected="true" aria-controls="tab-6167-panel">Libellé onglet 1</button>
</li>
<li role="presentation">
<button type="button" id="tab-6168" class="fr-tabs__tab" tabindex="-1" role="tab" aria-selected="false" aria-controls="tab-6168-panel">Libellé onglet 2</button>
</li>
<li role="presentation">
<button type="button" id="tab-6169" class="fr-tabs__tab" tabindex="-1" role="tab" aria-selected="false" aria-controls="tab-6169-panel">Libellé onglet 3</button>
</li>
<li role="presentation">
<button type="button" id="tab-6170" class="fr-tabs__tab" tabindex="-1" role="tab" aria-selected="false" aria-controls="tab-6170-panel">Libellé onglet 4</button>
</li>
</ul>
<div id="tab-6167-panel" class="fr-tabs__panel fr-tabs__panel--selected" role="tabpanel" aria-labelledby="tab-6167" tabindex="0">
<!-- données de test -->
</div>
<div id="tab-6168-panel" class="fr-tabs__panel" role="tabpanel" aria-labelledby="tab-6168" tabindex="0">
<!-- données de test -->
</div>
<div id="tab-6169-panel" class="fr-tabs__panel" role="tabpanel" aria-labelledby="tab-6169" tabindex="0">
<!-- données de test -->
</div>
<div id="tab-6170-panel" class="fr-tabs__panel" role="tabpanel" aria-labelledby="tab-6170" tabindex="0">
<!-- données de test -->
</div>
</div>
</div>
</div>
</div>
<div id="tabs-in-tabs-6182-panel" class="fr-tabs__panel" role="tabpanel" aria-labelledby="tabs-in-tabs-6182" tabindex="0">
<div class="fr-tabs">
<ul class="fr-tabs__list" role="tablist" aria-label="[A modifier | nom du système d'onglet]">
<li role="presentation">
<button type="button" id="tab-6183" class="fr-tabs__tab" tabindex="0" role="tab" aria-selected="true" aria-controls="tab-6183-panel">Onglet imbriqué 0</button>
</li>
<li role="presentation">
<button type="button" id="tab-6184" class="fr-tabs__tab" tabindex="-1" role="tab" aria-selected="false" aria-controls="tab-6184-panel">Onglet imbriqué 1</button>
</li>
</ul>
<div id="tab-6183-panel" class="fr-tabs__panel fr-tabs__panel--selected" role="tabpanel" aria-labelledby="tab-6183" tabindex="0">
<div class="fr-tabs">
<ul class="fr-tabs__list" role="tablist" aria-label="[A modifier | nom du système d'onglet]">
<li role="presentation">
<button type="button" id="tab-6176" class="fr-tabs__tab" tabindex="0" role="tab" aria-selected="true" aria-controls="tab-6176-panel">Libellé onglet 1</button>
</li>
<li role="presentation">
<button type="button" id="tab-6177" class="fr-tabs__tab" tabindex="-1" role="tab" aria-selected="false" aria-controls="tab-6177-panel">Libellé onglet 2</button>
</li>
</ul>
<div id="tab-6176-panel" class="fr-tabs__panel fr-tabs__panel--selected" role="tabpanel" aria-labelledby="tab-6176" tabindex="0">
<!-- données de test -->
</div>
<div id="tab-6177-panel" class="fr-tabs__panel" role="tabpanel" aria-labelledby="tab-6177" tabindex="0">
<!-- données de test -->
</div>
</div>
</div>
<div id="tab-6184-panel" class="fr-tabs__panel" role="tabpanel" aria-labelledby="tab-6184" tabindex="0">
<div class="fr-tabs">
<ul class="fr-tabs__list" role="tablist" aria-label="[A modifier | nom du système d'onglet]">
<li role="presentation">
<button type="button" id="tab-6179" class="fr-tabs__tab" tabindex="0" role="tab" aria-selected="true" aria-controls="tab-6179-panel">Libellé onglet 1</button>
</li>
<li role="presentation">
<button type="button" id="tab-6180" class="fr-tabs__tab" tabindex="-1" role="tab" aria-selected="false" aria-controls="tab-6180-panel">Libellé onglet 2</button>
</li>
<li role="presentation">
<button type="button" id="tab-6181" class="fr-tabs__tab" tabindex="-1" role="tab" aria-selected="false" aria-controls="tab-6181-panel">Libellé onglet 3</button>
</li>
</ul>
<div id="tab-6179-panel" class="fr-tabs__panel fr-tabs__panel--selected" role="tabpanel" aria-labelledby="tab-6179" tabindex="0">
<!-- données de test -->
</div>
<div id="tab-6180-panel" class="fr-tabs__panel" role="tabpanel" aria-labelledby="tab-6180" tabindex="0">
<!-- données de test -->
</div>
<div id="tab-6181-panel" class="fr-tabs__panel" role="tabpanel" aria-labelledby="tab-6181" tabindex="0">
<!-- données de test -->
</div>
</div>
</div>
</div>
</div>
</div>


### Accordéon dans onglets


-
Libellé onglet 1


-
Libellé onglet 2


###
Libellé accordéon


#### Contenu

![no alt text](../../../example/img/placeholder.16x9.png)


Lorem ipsum dolor sit amet, consectetur adipiscing, [link test](https://www.systeme-de-design.gouv.fr/) incididunt, ut labore et dolore magna aliqua. Vitae sapien pellentesque habitant morbi tristique senectus et. Diam maecenas sed enim ut. Accumsan lacus vel facilisis volutpat est. Ut aliquam purus sit amet luctus. Lorem ipsum dolor sit amet consectetur adipiscing elit ut.

- list item


###
Libellé accordéon


#### Contenu


Lorem ipsum dolor sit amet, consectetur adipiscing, [link test](https://www.systeme-de-design.gouv.fr/) incididunt, ut labore et dolore magna aliqua. Vitae sapien pellentesque habitant morbi tristique senectus et. Diam maecenas sed enim ut. Accumsan lacus vel facilisis volutpat est. Ut aliquam purus sit amet luctus. Lorem ipsum dolor sit amet consectetur adipiscing elit ut.

- list item

- list item


###
Extrait de code


<div class="fr-tabs">
<ul class="fr-tabs__list" role="tablist" aria-label="[A modifier | nom du système d'onglet]">
<li role="presentation">
<button type="button" id="tab-accordion-6190" class="fr-tabs__tab" tabindex="0" role="tab" aria-selected="true" aria-controls="tab-accordion-6190-panel">Libellé onglet 1</button>
</li>
<li role="presentation">
<button type="button" id="tab-accordion-6192" class="fr-tabs__tab" tabindex="-1" role="tab" aria-selected="false" aria-controls="tab-accordion-6192-panel">Libellé onglet 2</button>
</li>
</ul>
<div id="tab-accordion-6190-panel" class="fr-tabs__panel fr-tabs__panel--selected" role="tabpanel" aria-labelledby="tab-accordion-6190" tabindex="0">
<section class="fr-accordion">
<h3 class="fr-accordion__title">
<button type="button" class="fr-accordion__btn" aria-expanded="false" aria-controls="accordion-6191">Libellé accordéon</button>
</h3>
<div class="fr-collapse" id="accordion-6191">
<!-- données de test -->
</div>
</section>
</div>
<div id="tab-accordion-6192-panel" class="fr-tabs__panel" role="tabpanel" aria-labelledby="tab-accordion-6192" tabindex="0">
<section class="fr-accordion">
<h3 class="fr-accordion__title">
<button type="button" class="fr-accordion__btn" aria-expanded="false" aria-controls="accordion-6193">Libellé accordéon</button>
</h3>
<div class="fr-collapse" id="accordion-6193">
<!-- données de test -->
</div>
</section>
</div>
</div>


### Onglets 100% largeur du viewport en mobile


-
Libellé onglet 1


-
Libellé onglet 2


#### Contenu 1

![no alt text](../../../example/img/placeholder.16x9.png)


- list item

- list item


#### Contenu 2


Lorem ipsum dolor sit amet, consectetur adipiscing, [link test](https://www.systeme-de-design.gouv.fr/) incididunt, ut labore et dolore magna aliqua. Vitae sapien pellentesque habitant morbi tristique senectus et. Diam maecenas sed enim ut. Accumsan lacus vel facilisis volutpat est. Ut aliquam purus sit amet luctus. Lorem ipsum dolor sit amet consectetur adipiscing elit ut.

- list item


###
Extrait de code


<div class="fr-tabs fr-tabs--viewport-width">
<ul class="fr-tabs__list" role="tablist" aria-label="[A modifier | nom du système d'onglet]">
<li role="presentation">
<button type="button" id="tab-6197" class="fr-tabs__tab" tabindex="0" role="tab" aria-selected="true" aria-controls="tab-6197-panel">Libellé onglet 1</button>
</li>
<li role="presentation">
<button type="button" id="tab-6198" class="fr-tabs__tab" tabindex="-1" role="tab" aria-selected="false" aria-controls="tab-6198-panel">Libellé onglet 2</button>
</li>
</ul>
<div id="tab-6197-panel" class="fr-tabs__panel fr-tabs__panel--selected" role="tabpanel" aria-labelledby="tab-6197" tabindex="0">
<!-- données de test -->
</div>
<div id="tab-6198-panel" class="fr-tabs__panel" role="tabpanel" aria-labelledby="tab-6198" tabindex="0">
<!-- données de test -->
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
