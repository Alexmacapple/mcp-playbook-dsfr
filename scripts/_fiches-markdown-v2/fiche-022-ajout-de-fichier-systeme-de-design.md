URL:
https://main--ds-gouv.netlify.app/example/component/upload

Title:
Ajout de fichier - Système de design

Markdown:

Ajout de fichier - Système de design


DSFR v1.14.0


[Retour](../)


# Ajout de fichier (upload)


Ce composant permet aux utilisateurs de sélectionner et envoyer un ou plusieurs fichiers.
[Documentation](https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/ajout-de-fichier)


### Bouton upload 1 seul fichier


Ajouter un fichier
Indication : taille maximale : 500 Mo. Formats supportés : jpg, png, pdf. Plusieurs fichiers possibles. Lorem ipsum dolor sit amet, consectetur adipiscing.


###
Extrait de code


<div class="fr-upload-group">
<label class="fr-label" for="file-upload">
Ajouter un fichier
<span class="fr-hint-text">Indication : taille maximale : 500 Mo. Formats supportés : jpg, png, pdf. Plusieurs fichiers possibles. Lorem ipsum dolor sit amet, consectetur adipiscing.</span>
</label>
<input class="fr-upload" aria-describedby="file-upload-messages" type="file" id="file-upload" name="file-upload">
<div class="fr-messages-group" id="file-upload-messages" aria-live="polite">
</div>
</div>


### Bouton upload avec erreur


Ajouter un fichier
Indication : taille maximale : 500 Mo. Formats supportés : jpg, png, pdf. Plusieurs fichiers possibles. Lorem ipsum dolor sit amet, consectetur adipiscing.


Format de fichier non supporté


###
Extrait de code


<div class="fr-upload-group fr-upload-group--error">
<label class="fr-label" for="file-upload-with-error">
Ajouter un fichier
<span class="fr-hint-text">Indication : taille maximale : 500 Mo. Formats supportés : jpg, png, pdf. Plusieurs fichiers possibles. Lorem ipsum dolor sit amet, consectetur adipiscing.</span>
</label>
<input class="fr-upload" aria-describedby="file-upload-with-error-messages" type="file" id="file-upload-with-error" name="file-upload-with-error">
<div class="fr-messages-group" id="file-upload-with-error-messages" aria-live="polite">
<p class="fr-message fr-message--error" id="file-upload-with-error-message-error">Format de fichier non supporté</p>
</div>
</div>


### Bouton upload fichiers multiples


Ajouter des fichiers
Indication : taille maximale : 500 Mo. Formats supportés : jpg, png, pdf. Plusieurs fichiers possibles. Lorem ipsum dolor sit amet, consectetur adipiscing.


###
Extrait de code


<div class="fr-upload-group">
<label class="fr-label" for="file-upload-multiple">
Ajouter des fichiers
<span class="fr-hint-text">Indication : taille maximale : 500 Mo. Formats supportés : jpg, png, pdf. Plusieurs fichiers possibles. Lorem ipsum dolor sit amet, consectetur adipiscing.</span>
</label>
<input class="fr-upload" aria-describedby="file-upload-multiple-messages" multiple type="file" id="file-upload-multiple" name="file-upload-multiple">
<div class="fr-messages-group" id="file-upload-multiple-messages" aria-live="polite">
</div>
</div>


### Bouton upload désactivé


Ajouter un fichier
Indication : taille maximale : 500 Mo. Formats supportés : jpg, png, pdf. Plusieurs fichiers possibles. Lorem ipsum dolor sit amet, consectetur adipiscing.


###
Extrait de code


<div class="fr-upload-group fr-upload-group--disabled">
<label class="fr-label" for="file-upload-disabled">
Ajouter un fichier
<span class="fr-hint-text">Indication : taille maximale : 500 Mo. Formats supportés : jpg, png, pdf. Plusieurs fichiers possibles. Lorem ipsum dolor sit amet, consectetur adipiscing.</span>
</label>
<input class="fr-upload" disabled aria-describedby="file-upload-disabled-messages" type="file" id="file-upload-disabled" name="file-upload-disabled">
<div class="fr-messages-group" id="file-upload-disabled-messages" aria-live="polite">
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
