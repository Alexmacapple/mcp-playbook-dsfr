URL:
https://main--ds-gouv.netlify.app/example/component/badge

Title:
Badge - Système de design

Markdown:

Badge - Système de design


DSFR v1.14.0


[Retour](../)


# Badge (badge)


Le composant badge permet de mettre en avant une information de type "statut" ou "état" sur un élément du site.
[Documentation](https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/badge)


### Badge seul


Libellé badge


###
Extrait de code


<p id="badge-719" class="fr-badge">Libellé badge</p>


Il est conseillé d'ajouter une balise span avec la classe fr-ellipsis à l'interieur du badge pour que celui ci reste sur une seule ligne, avec le texte coupé par des points de suspensions.

### Badge sur une seule ligne - ellipsis


Libellé badge très long, coupé par des points de suspensions lorsque le Libellé dépasse la largeur du conteneur


###
Extrait de code


<p class="fr-badge">
<span class="fr-ellipsis">Libellé badge très long, coupé par des points de suspensions lorsque le Libellé dépasse la largeur du conteneur</span>
</p>


### Badge - succès


Libellé badge


###
Extrait de code


<p id="badge-722" class="fr-badge fr-badge--success">Libellé badge</p>


### Badge - succès sans icone


Libellé badge


###
Extrait de code


<p id="badge-724" class="fr-badge fr-badge--success fr-badge--no-icon">Libellé badge</p>


### Badge - erreur


Libellé badge


###
Extrait de code


<p id="badge-726" class="fr-badge fr-badge--error">Libellé badge</p>


### Badge - erreur sans icone


Libellé badge


###
Extrait de code


<p id="badge-728" class="fr-badge fr-badge--error fr-badge--no-icon">Libellé badge</p>


### Badge - information


Libellé badge


###
Extrait de code


<p id="badge-730" class="fr-badge fr-badge--info">Libellé badge</p>


### Badge - information sans icone


Libellé badge


###
Extrait de code


<p id="badge-732" class="fr-badge fr-badge--info fr-badge--no-icon">Libellé badge</p>


### Badge - avertissement


Libellé badge


###
Extrait de code


<p id="badge-734" class="fr-badge fr-badge--warning">Libellé badge</p>


### Badge - avertissement sans icone


Libellé badge


###
Extrait de code


<p id="badge-736" class="fr-badge fr-badge--warning fr-badge--no-icon">Libellé badge</p>


### Badge - nouveauté


Libellé badge


###
Extrait de code


<p id="badge-738" class="fr-badge fr-badge--new">Libellé badge</p>


### Badge - nouveauté sans icone


Libellé badge


###
Extrait de code


<p id="badge-740" class="fr-badge fr-badge--new fr-badge--no-icon">Libellé badge</p>


### Badge - personnalisé green-menthe


Libellé badge


###
Extrait de code


<p id="badge-742" class="fr-badge fr-badge--green-menthe">Libellé badge</p>


### Badge - personnalisé orange-terre-battue


Libellé badge


###
Extrait de code


<p id="badge-744" class="fr-badge fr-badge--orange-terre-battue">Libellé badge</p>


### Badge - personnalisé purple-glycine


Libellé badge


###
Extrait de code


<p id="badge-746" class="fr-badge fr-badge--purple-glycine">Libellé badge</p>


### Badge taille SM


Libellé badge


###
Extrait de code


<p id="badge-749" class="fr-badge fr-badge--sm">Libellé badge</p>


### Badge SM - succès


Libellé badge


###
Extrait de code


<p id="badge-751" class="fr-badge fr-badge--sm fr-badge--success">Libellé badge</p>


### Badge SM - erreur


Libellé badge


###
Extrait de code


<p id="badge-753" class="fr-badge fr-badge--sm fr-badge--error">Libellé badge</p>


### Badge SM - information


Libellé badge


###
Extrait de code


<p id="badge-755" class="fr-badge fr-badge--sm fr-badge--info">Libellé badge</p>


### Badge SM - avertissement


Libellé badge


###
Extrait de code


<p id="badge-757" class="fr-badge fr-badge--sm fr-badge--warning">Libellé badge</p>


### Badge SM - nouveauté


Libellé badge


###
Extrait de code


<p id="badge-759" class="fr-badge fr-badge--sm fr-badge--new">Libellé badge</p>


### Badge SM - personnalisé purple-glycine


Libellé badge


###
Extrait de code


<p id="badge-761" class="fr-badge fr-badge--sm fr-badge--purple-glycine">Libellé badge</p>


## Groupe de badges


Lorsque que l'on a plus d'un badge, il convient d'utiliser un groupe de badges.

La taille de tous les badges peut être définie au niveau du groupe.


### Groupe de badges


-


Libellé badge 1


-


Libellé badge 2


-


Libellé badge 3


-


Libellé badge 4


-


Libellé badge 5


-


Libellé badge 6


-


Libellé badge 7


-


Libellé badge 8


-


Libellé badge 9


###
Extrait de code


<ul class="fr-badges-group">
<li>
<p id="badge-763" class="fr-badge">Libellé badge 1</p>
</li>
<li>
<p id="badge-764" class="fr-badge">Libellé badge 2</p>
</li>
<li>
<p id="badge-765" class="fr-badge">Libellé badge 3</p>
</li>
<li>
<p id="badge-766" class="fr-badge">Libellé badge 4</p>
</li>
<li>
<p id="badge-767" class="fr-badge">Libellé badge 5</p>
</li>
<li>
<p id="badge-768" class="fr-badge">Libellé badge 6</p>
</li>
<li>
<p id="badge-769" class="fr-badge">Libellé badge 7</p>
</li>
<li>
<p id="badge-770" class="fr-badge">Libellé badge 8</p>
</li>
<li>
<p id="badge-771" class="fr-badge">Libellé badge 9</p>
</li>
</ul>


### Groupe de badges SM


-


Libellé badge 1


-


Libellé badge 2


-


Libellé badge 3


-


Libellé badge 4


-


Libellé badge 5


-


Libellé badge 6


-


Libellé badge 7


-


Libellé badge 8


-


Libellé badge 9


###
Extrait de code


<ul class="fr-badges-group fr-badges-group--sm">
<li>
<p id="badge-773" class="fr-badge">Libellé badge 1</p>
</li>
<li>
<p id="badge-774" class="fr-badge">Libellé badge 2</p>
</li>
<li>
<p id="badge-775" class="fr-badge">Libellé badge 3</p>
</li>
<li>
<p id="badge-776" class="fr-badge">Libellé badge 4</p>
</li>
<li>
<p id="badge-777" class="fr-badge">Libellé badge 5</p>
</li>
<li>
<p id="badge-778" class="fr-badge">Libellé badge 6</p>
</li>
<li>
<p id="badge-779" class="fr-badge">Libellé badge 7</p>
</li>
<li>
<p id="badge-780" class="fr-badge">Libellé badge 8</p>
</li>
<li>
<p id="badge-781" class="fr-badge">Libellé badge 9</p>
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
