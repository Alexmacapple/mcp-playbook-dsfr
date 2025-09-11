URL:
https://main--ds-gouv.netlify.app/example/component/tooltip

Title:
Information contextuelle et Infobulle - Système de design

Markdown:

Information contextuelle et Infobulle - Système de design


DSFR v1.14.0


[Retour](../)


# Information contextuelle et Infobulle (tooltip)

[Documentation](https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/infobulle)


### Information contextuelle


Ouverture du tooltip au survol


Lorem ipsum dolor sit amet, consectetur adipiscing, incididunt, ut labore et dolore magna aliqua. Vitae sapien pellentesque habitant morbi tristique senectus et. Diam maecenas sed enim ut. Accumsan lacus vel facilisis volutpat est. Ut aliquam purus sit amet luctus. Lorem ipsum dolor sit amet consectetur adipiscing elit ut.


###
Extrait de code


<a aria-describedby="tooltip-3804" id="link-3805" href="#" class="fr-link">Exemple</a>
<span class="fr-tooltip fr-placement" id="tooltip-3804" role="tooltip">Lorem [...] elit ut.</span>


### Infobulle


L'ajout de la classe ' fr-btn--tooltip ' déclenche l'ouverture du tooltip au click.


Information contextuelle
Lorem ipsum dolor sit amet, consectetur adipiscing, incididunt, ut labore et dolore magna aliqua. Vitae sapien pellentesque habitant morbi tristique senectus et. Diam maecenas sed enim ut. Accumsan lacus vel facilisis volutpat est. Ut aliquam purus sit amet luctus. Lorem ipsum dolor sit amet consectetur adipiscing elit ut.


###
Extrait de code


<button aria-describedby="tooltip-3808" type="button" class="fr-btn--tooltip fr-btn">Information contextuelle</button>
<span class="fr-tooltip fr-placement" id="tooltip-3808" role="tooltip">Lorem [...] elit ut.</span>


### Information contextuelle dans une grille à gauche


Lorem ipsum dolor sit amet, consectetur adipiscing, incididunt, ut labore et dolore magna aliqua. Vitae sapien pellentesque habitant morbi tristique senectus et. Diam maecenas sed enim ut. Accumsan lacus vel facilisis volutpat est. Ut aliquam purus sit amet luctus. Lorem ipsum dolor sit amet consectetur adipiscing elit ut.


Lorem ipsum dolor sit amet, consectetur adipiscing, incididunt, ut labore et dolore magna aliqua. Vitae sapien pellentesque habitant morbi tristique senectus et. Diam maecenas sed enim ut. Accumsan lacus vel facilisis volutpat est. Ut aliquam purus sit amet luctus. Lorem ipsum dolor sit amet consectetur adipiscing elit ut.


###
Extrait de code


<div class="fr-grid-row fr-grid-row--gutters">
<div class="fr-col-4 fr-col-sm-2">
<a class="fr-link" href="#" aria-describedby="tooltip-3811">Exemple</a>
<span class="fr-tooltip fr-placement" id="tooltip-3811" role="tooltip">Lorem [...] elit ut.</span>
</div>
<div class="fr-col-8 fr-col-sm-10">
<p>Lorem [...] elit ut.</p>
</div>
</div>


### Information contextuelle dans une grille à droite


Lorem ipsum dolor sit amet, consectetur adipiscing, incididunt, ut labore et dolore magna aliqua. Vitae sapien pellentesque habitant morbi tristique senectus et. Diam maecenas sed enim ut. Accumsan lacus vel facilisis volutpat est. Ut aliquam purus sit amet luctus. Lorem ipsum dolor sit amet consectetur adipiscing elit ut.


Lorem ipsum dolor sit amet, consectetur adipiscing, incididunt, ut labore et dolore magna aliqua. Vitae sapien pellentesque habitant morbi tristique senectus et. Diam maecenas sed enim ut. Accumsan lacus vel facilisis volutpat est. Ut aliquam purus sit amet luctus. Lorem ipsum dolor sit amet consectetur adipiscing elit ut.


###
Extrait de code


<div class="fr-grid-row fr-grid-row--gutters">
<div class="fr-col-8 fr-col-sm-10">
<p>Lorem [...] elit ut.</p>
</div>
<div class="fr-col-4 fr-col-sm-2">
<a class="fr-link" href="#" aria-describedby="tooltip-3814">Exemple</a>
<span class="fr-tooltip fr-placement" id="tooltip-3814" role="tooltip">Lorem [...] elit ut.</span>
</div>
</div>


### Information contextuelle dans une liste


Partager la page

-
[Partager sur Facebook](https://www.facebook.com/sharer.php?u=%5B%C3%80%20MODIFIER%20-%20url%20de%20la%20page%5D)
Lorem ipsum dolor sit amet, consectetur adipiscing, incididunt, ut labore et dolore magna aliqua. Vitae sapien pellentesque habitant morbi tristique senectus et. Diam maecenas sed enim ut. Accumsan lacus vel facilisis volutpat est. Ut aliquam purus sit amet luctus. Lorem ipsum dolor sit amet consectetur adipiscing elit ut.


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


<div class="fr-share" id="share-3825">
<p class="fr-share__title">Partager la page</p>
<ul class="fr-btns-group">
<li>
<a onclick="window.open(this.href,'Partager sur Facebook','toolbar=no,location=yes,status=no,menubar=no,scrollbars=yes,resizable=yes,width=600,height=450'); event.preventDefault();" aria-describedby="tooltip-3824" id="share-3826" href="https://www.facebook.com/sharer.php?u=[À MODIFIER - url de la page]" target="_blank" rel="noopener external" class="fr-btn--facebook fr-btn">Partager sur Facebook</a>
<span class="fr-tooltip fr-placement" id="tooltip-3824" role="tooltip">Lorem [...] elit ut.</span>
</li>
<li>
<!-- Les paramètres de la reqûete doivent être URI-encodés (ex: encodeURIComponent() en js) -->
<a onclick="window.open(this.href,'Partager sur X (anciennement Twitter)','toolbar=no,location=yes,status=no,menubar=no,scrollbars=yes,resizable=yes,width=600,height=420'); event.preventDefault();" id="share-3827" href="https://twitter.com/intent/tweet?url=[À MODIFIER - url de la page]&text=[À MODIFIER - titre ou texte descriptif de la page]&via=[À MODIFIER - via]&hashtags=[À MODIFIER - hashtags]" target="_blank" rel="noopener external" class="fr-btn--twitter-x fr-btn">Partager sur X (anciennement Twitter)</a>
</li>
<li>
<!-- Les paramètres de la reqûete doivent être URI-encodés (ex: encodeURIComponent() en js) -->
<a onclick="window.open(this.href,'Partager sur Bluesky','toolbar=no,location=yes,status=no,menubar=no,scrollbars=yes,resizable=yes,width=600,height=430'); event.preventDefault();" id="share-3828" href="https://bsky.app/intent/compose?text=[À MODIFIER - titre ou texte descriptif de la page]+[À MODIFIER - url de la page]" target="_blank" rel="noopener external" class="fr-btn--bluesky fr-btn">Partager sur Bluesky</a>
</li>
<li>
<a onclick="window.open(this.href,'Partager sur LinkedIn','toolbar=no,location=yes,status=no,menubar=no,scrollbars=yes,resizable=yes,width=550,height=550'); event.preventDefault();" id="share-3829" href="https://www.linkedin.com/shareArticle?url=[À MODIFIER - url de la page]&title=[À MODIFIER - titre ou texte descriptif de la page]" target="_blank" rel="noopener external" class="fr-btn--linkedin fr-btn">Partager sur LinkedIn</a>
</li>
<li>
<a id="share-3830" href="mailto:?subject=[À MODIFIER - objet du mail]&body=[À MODIFIER - titre ou texte descriptif de la page] [À MODIFIER - url de la page]" target="_blank" rel="noopener external" class="fr-btn--mail fr-btn">Partager par email</a>
</li>
<li>
<button onclick="navigator.clipboard.writeText(window.location).then(function() {alert('Adresse copiée dans le presse papier.')});" type="button" id="share-3831" class="fr-btn--copy fr-btn">Copier dans le presse-papier</button>
</li>
</ul>
</div>


### Infobulle dans un tableau


th0


th1


th2


th3


Lorem ipsum dolor sit ame


Lorem ipsum dolor sit ame


Lorem ipsum dolor sit ame


Lorem ipsum dolor sit ame


Lorem ipsum dolor sit ame


Lorem ipsum dolor sit ame


Information contextuelle
Lorem ipsum dolor sit amet, consectetur adipiscing, incididunt, ut labore et dolore magna aliqua. Vitae sapien pellentesque habitant morbi tristique senectus et. Diam maecenas sed enim ut. Accumsan lacus vel facilisis volutpat est. Ut aliquam purus sit amet luctus. Lorem ipsum dolor sit amet consectetur adipiscing elit ut.


Lorem ipsum dolor sit ame


Lorem ipsum dolor sit ame


Lorem ipsum dolor sit ame


Lorem ipsum dolor sit ame


Lorem ipsum dolor sit ame


Lorem ipsum dolor sit ame


Lorem ipsum dolor sit ame


Lorem ipsum dolor sit ame


Lorem ipsum dolor sit ame


###
Extrait de code


<div class="fr-table" id="tootltip-table-component">
<div class="fr-table__wrapper">
<div class="fr-table__container">
<div class="fr-table__content">
<table id="tootltip-table">
<thead>
<tr>
<th scope="col">
th0
</th>
<th scope="col">
th1
</th>
<th scope="col">
th2
</th>
<th scope="col">
th3
</th>
</tr>
</thead>
<tbody>
<tr id="tootltip-table-row-key-1" data-row-key="1">
<td>
Lorem [...] elit ut.
</td>
<td>
Lorem [...] elit ut.
</td>
<td>
Lorem [...] elit ut.
</td>
<td>
Lorem [...] elit ut.
</td>
</tr>
<tr id="tootltip-table-row-key-2" data-row-key="2">
<td>
Lorem [...] elit ut.
</td>
<td>
Lorem [...] elit ut.
</td>
<td>
<button aria-describedby="tooltip-3834" type="button" class="fr-btn--tooltip fr-btn">Information contextuelle</button>
<span class="fr-tooltip fr-placement" id="tooltip-3834" role="tooltip">Lorem [...] elit ut.</span>
</td>
<td>
Lorem [...] elit ut.
</td>
</tr>
<tr id="tootltip-table-row-key-3" data-row-key="3">
<td>
Lorem [...] elit ut.
</td>
<td>
Lorem [...] elit ut.
</td>
<td>
Lorem [...] elit ut.
</td>
<td>
Lorem [...] elit ut.
</td>
</tr>
<tr id="tootltip-table-row-key-4" data-row-key="4">
<td>
Lorem [...] elit ut.
</td>
<td>
Lorem [...] elit ut.
</td>
<td>
Lorem [...] elit ut.
</td>
<td>
Lorem [...] elit ut.
</td>
</tr>
</tbody>
</table>
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
