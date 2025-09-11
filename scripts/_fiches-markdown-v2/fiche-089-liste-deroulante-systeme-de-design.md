URL:
https://main--ds-gouv.netlify.app/example/component/select/deprecated

Title:
Liste déroulante - Système de design

Markdown:

Liste déroulante - Système de design


DSFR v1.14.0


[Retour](../)


# Liste déroulante (select)


La liste déroulante permet à un utilisateur de choisir un élément dans une liste donnée.
[Documentation](https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/liste-deroulante)


## Dépréciation


Les exemples suivants sont dépréciés, ne pas utiliser comme référence

Pour support des versions précédentes


### Liste déroulante valide


Libellé pour liste déroulante


Sélectionner une option
Option 1
Option 2
Option 3
Option 4


Texte de validation


###
Extrait de code


<div class="fr-select-group fr-select-group--valid">
<label class="fr-label" for="select-valid">
Libellé pour liste déroulante
</label>
<select class="fr-select fr-select--valid" aria-describedby="select-valid-desc-valid" id="select-valid" name="select-valid">
<option value="" selected disabled hidden>Sélectionner une option</option>
<option value="1">Option 1</option>
<option value="2">Option 2</option>
<option value="3">Option 3</option>
<option value="4">Option 4</option>
</select>
<p id="select-valid-desc-valid" class="fr-valid-text">
Texte de validation
</p>
</div>


### Liste déroulante erreur


Libellé pour liste déroulante


Sélectionner une option
Option 1
Option 2
Option 3
Option 4


Texte d'erreur obligatoire


###
Extrait de code


<div class="fr-select-group fr-select-group--error">
<label class="fr-label" for="select-error">
Libellé pour liste déroulante
</label>
<select class="fr-select fr-select--error" aria-describedby="select-error-desc-error" id="select-error" name="select-error">
<option value="" selected disabled hidden>Sélectionner une option</option>
<option value="1">Option 1</option>
<option value="2">Option 2</option>
<option value="3">Option 3</option>
<option value="4">Option 4</option>
</select>
<p id="select-error-desc-error" class="fr-error-text">
Texte d'erreur obligatoire
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
