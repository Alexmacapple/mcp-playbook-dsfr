URL:
https://main--ds-gouv.netlify.app/example/component/stepper

Title:
Indicateur d'étapes - Système de design

Markdown:

Indicateur d'étapes - Système de design


DSFR v1.14.0


[Retour](../)


# Indicateur d'étapes (stepper)


L'indicateur d'étape permet d'indiquer à l'utilisateur où il se trouve dans un formulaire ou dans une démarche.
[Documentation](https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/indicateur-d-etapes)


## Informations générales


L'indicateur d'étape peut contenir de 2 à 8 étapes.

Il doit être placé dans un conteneur de 6 à 8 colonnes de large en desktop, et 100% (12 colonnes) en mobile.

Le niveau de titre h2 peut être modifié suivant le contexte


### Exemple d'indicateur d'étape 1 sur 3


##
Titre de l'étape en cours
Étape 1 sur 3


Étape suivante : Titre de la prochaine étape


###
Extrait de code


<div class="fr-stepper">
<h2 class="fr-stepper__title">
Titre de l'étape en cours
<span class="fr-stepper__state">Étape 1 sur 3</span>
</h2>
<div class="fr-stepper__steps" data-fr-current-step="1" data-fr-steps="3"></div>
<p class="fr-stepper__details">
<span class="fr-text--bold">Étape suivante :</span> Titre de la prochaine étape
</p>
</div>


### Exemple d'indicateur d'étape 2 sur 8


##
Titre de l'étape en cours
Étape 2 sur 8


Étape suivante : Titre de la prochaine étape


###
Extrait de code


<div class="fr-stepper">
<h2 class="fr-stepper__title">
Titre de l'étape en cours
<span class="fr-stepper__state">Étape 2 sur 8</span>
</h2>
<div class="fr-stepper__steps" data-fr-current-step="2" data-fr-steps="8"></div>
<p class="fr-stepper__details">
<span class="fr-text--bold">Étape suivante :</span> Titre de la prochaine étape
</p>
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
