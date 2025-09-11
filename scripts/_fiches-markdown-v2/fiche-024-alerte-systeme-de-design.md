URL:
https://main--ds-gouv.netlify.app/example/component/alert

Title:
Alerte - Système de design

Markdown:

Alerte - Système de design


DSFR v1.14.0


[Retour](../)


# Alerte (alert)


L'alerte permet d'attirer l'attention de l'utilisateur sur une information sans interrompre sa tâche.
[Documentation](https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/alerte)


## Alerte statique


Précisez le type d'alerte (Information/Succès/Erreur) dans le titre ou, à défaut, dans le contenu de l'alerte.

Le titre est défini par la classe "fr-alert__title", la balise <p> peut être remplacée par un niveau de titre hx suivant le contexte.


### Alerte par défaut


### Titre


Description


###
Extrait de code


<div id="alert-685" class="fr-alert">
<h3 class="fr-alert__title">Titre</h3>
<p>Description</p>
</div>


### Alerte succès


### Succès de l'envoi


Description


###
Extrait de code


<div id="alert-687" class="fr-alert fr-alert--success">
<h3 class="fr-alert__title">Succès de l'envoi</h3>
<p>Description</p>
</div>


### Alerte erreur


### Erreur détectée dans le formulaire


Description


###
Extrait de code


<div id="alert-689" class="fr-alert fr-alert--error">
<h3 class="fr-alert__title">Erreur détectée dans le formulaire</h3>
<p>Description</p>
</div>


### Alerte info


### Information Covid


Description


###
Extrait de code


<div id="alert-691" class="fr-alert fr-alert--info">
<h3 class="fr-alert__title">Information Covid</h3>
<p>Description</p>
</div>


### Alerte attention


### Attention


Description


###
Extrait de code


<div id="alert-693" class="fr-alert fr-alert--warning">
<h3 class="fr-alert__title">Attention</h3>
<p>Description</p>
</div>


### Alerte sans titre


Information : titre de l'information


###
Extrait de code


<div id="alert-695" class="fr-alert fr-alert--info">
<p>Information : titre de l'information</p>
</div>


### Alerte avec bouton fermer


### Information Covid


Cliquer sur la croix pour fermer l'alerte
Masquer le message


###
Extrait de code


<div id="alert-698" class="fr-alert fr-alert--info">
<h3 class="fr-alert__title">Information Covid</h3>
<p>Cliquer sur la croix pour fermer l'alerte</p>
<button title="Masquer le message" onclick="const alert = this.parentNode; alert.parentNode.removeChild(alert)" type="button" class="fr-btn--close fr-btn">Masquer le message</button>
</div>


### Alerte taille SM


### Titre


Description


###
Extrait de code


<div id="alert-700" class="fr-alert fr-alert--info fr-alert--sm">
<h3 class="fr-alert__title">Titre</h3>
<p>Description</p>
</div>


### Alerte taille SM sans titre


Information : titre de l'information


###
Extrait de code


<div id="alert-702" class="fr-alert fr-alert--info fr-alert--sm">
<p>Information : titre de l'information</p>
</div>


### Alerte taille SM refermable


Information : cliquer sur la croix pour fermer l'alerte
Masquer le message


###
Extrait de code


<div id="alert-705" class="fr-alert fr-alert--info fr-alert--sm">
<p>Information : cliquer sur la croix pour fermer l'alerte</p>
<button title="Masquer le message" onclick="const alert = this.parentNode; alert.parentNode.removeChild(alert)" type="button" class="fr-btn--close fr-btn">Masquer le message</button>
</div>


### Alerte icône personnalisée


### Titre


Description


###
Extrait de code


<div id="alert-707" class="fr-alert fr-icon-lock-fill">
<h3 class="fr-alert__title">Titre</h3>
<p>Description</p>
</div>


## Alerte dynamique


Ajouter l'attribut role="alert" lorsque les alertes sont ajoutées dynamiquement dans le DOM (en js après le chargement de la page)


#### Alerte ajoutée dynamiquement (type)


Bouton d'ajout


###
Extrait de code


<div id="alert-710" role="alert" class="fr-alert fr-alert--error">
<h3 class="fr-alert__title">Erreur détectée dans le formulaire</h3>
<p>Cliquer sur la croix pour fermer l'alerte</p>
<button title="Masquer le message" onclick="const alert = this.parentNode; alert.parentNode.removeChild(alert)" type="button" class="fr-btn--close fr-btn">Masquer le message</button>
</div>


## Dépréciation


Les exemples suivants sont dépréciés, ne pas utiliser comme référence

Pour support des versions précédentes


### Alerte avec bouton fermer


Information Covid


Cliquer sur la croix pour fermer l'alerte
Masquer le message


###
Extrait de code


<div class="fr-alert fr-alert--info">
<p class="fr-alert__title">Information Covid</p>
<p>Cliquer sur la croix pour fermer l'alerte</p>
<button title="Masquer le message" onclick="const alert = this.parentNode; alert.parentNode.removeChild(alert)" id="link-715" class="fr-link--close fr-link">Masquer le message</button>
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
