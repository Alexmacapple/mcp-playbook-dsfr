URL:
https://main--ds-gouv.netlify.app/example/component/breadcrumb/alternative

Title:
Fil d'Ariane - Système de design

Markdown:

Fil d'Ariane - Système de design


DSFR v1.14.0


[Retour](../)


# Fil d'Ariane (breadcrumb)


Le fil d'Ariane est un système de navigation secondaire qui permet à l'utilisateur de se situer sur le site qu'il consulte.
[Documentation](https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/fil-d-ariane)


### Fil d'Ariane avec boutons


Voir le fil d'Ariane


1.
Accueil


2.
Segment 1: lorem ipsum


3.
Segment 2: lorem ipsum


4.
Segment 3: lorem ipsum


5.
Segment 4: lorem ipsum


6.
Segment 5: lorem ipsum


7.
Segment 6: lorem ipsum


8.
Segment 7: lorem ipsum


9.


###
Extrait de code


<nav role="navigation" class="fr-breadcrumb" aria-label="vous êtes ici :">
<button type="button" class="fr-breadcrumb__button" aria-expanded="false" aria-controls="breadcrumb-3727">Voir le fil d'Ariane</button>
<div class="fr-collapse" id="breadcrumb-3727">
<ol class="fr-breadcrumb__list">
<li>
<button class="fr-breadcrumb__link" type="button" id="breadcrumb-3719">Accueil</button>
</li>
<li>
<button class="fr-breadcrumb__link" type="button" id="breadcrumb-3720">Segment 1: lorem ipsum</button>
</li>
<li>
<button class="fr-breadcrumb__link" type="button" id="breadcrumb-3721">Segment 2: lorem ipsum</button>
</li>
<li>
<button class="fr-breadcrumb__link" type="button" id="breadcrumb-3722">Segment 3: lorem ipsum</button>
</li>
<li>
<button class="fr-breadcrumb__link" type="button" id="breadcrumb-3723">Segment 4: lorem ipsum</button>
</li>
<li>
<button class="fr-breadcrumb__link" type="button" id="breadcrumb-3724">Segment 5: lorem ipsum</button>
</li>
<li>
<button class="fr-breadcrumb__link" type="button" id="breadcrumb-3725">Segment 6: lorem ipsum</button>
</li>
<li>
<button class="fr-breadcrumb__link" type="button" id="breadcrumb-3726">Segment 7: lorem ipsum</button>
</li>
<li>
<a class="fr-breadcrumb__link" aria-current="page">Page Actuelle</a>
</li>
</ol>
</div>
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
