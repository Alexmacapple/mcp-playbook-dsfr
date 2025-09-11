URL:
https://main--ds-gouv.netlify.app/example/component/input/deprecated

Title:
Champ de saisie - Système de design

Markdown:

Champ de saisie - Système de design


DSFR v1.14.0


[Retour](../)


# Champ de saisie (input)


Les champs permettent à un utilisateur d'entrer du contenu et données.
[Documentation](https://www.systeme-de-design.gouv.fr/elements-d-interface/blocs-fonctionnels/adresse-electronique)


## Dépréciation


Les exemples suivants sont dépréciés, ne pas utiliser comme référence

Pour support des versions précédentes


### Champ de type "text"


Libellé champ de saisie


###
Extrait de code


<div class="fr-input-group">
<label class="fr-label" for="text-input-text">
Libellé champ de saisie
</label>
<input class="fr-input" id="text-input-text" type="text">
</div>


### Champ de type "number"


Libellé champ de saisie


###
Extrait de code


<div class="fr-input-group">
<label class="fr-label" for="text-input-number">
Libellé champ de saisie
</label>
<input class="fr-input" pattern="[0-9]*" inputmode="numeric" id="text-input-number" type="number">
</div>


### Champ de type "search"


Libellé champ de saisie


###
Extrait de code


<div class="fr-input-group">
<label class="fr-label" for="text-input-search">
Libellé champ de saisie
</label>
<input class="fr-input" id="text-input-search" type="search">
</div>


### Champ de type "date"


Libellé champ de saisie


###
Extrait de code


<div class="fr-input-group">
<label class="fr-label" for="text-input-date">
Libellé champ de saisie
</label>
<input class="fr-input" id="text-input-date" type="date">
</div>


### Champ de type "textarea"


Libellé champ de saisie


###
Extrait de code


<div class="fr-input-group">
<label class="fr-label" for="textarea">
Libellé champ de saisie
</label>
<textarea class="fr-input" id="textarea"></textarea>
</div>


### Champ de type "password"


Libellé champ de saisie


###
Extrait de code


<div class="fr-input-group">
<label class="fr-label" for="text-input-password">
Libellé champ de saisie
</label>
<input class="fr-input" id="text-input-password" type="password">
</div>


### Combo champ + bouton d'envoi


Libellé champ de saisie


Envoyer


###
Extrait de code


<div class="fr-input-group">
<label class="fr-label" for="text-input-button">
Libellé champ de saisie
</label>
<div class="fr-input-wrap fr-input-wrap--addon">
<input class="fr-input" id="text-input-button" type="text">
<button type="submit" class="fr-btn">Envoyer</button>
</div>
</div>


### Champ avec placeholder


Libellé champ de saisie


###
Extrait de code


<div class="fr-input-group">
<label class="fr-label" for="text-input-placeholder">
Libellé champ de saisie
</label>
<input class="fr-input" placeholder="placeholder" id="text-input-placeholder" type="text">
</div>


### Champ avec valeur initiale


Libellé champ de saisie


###
Extrait de code


<div class="fr-input-group">
<label class="fr-label" for="text-input-value">
Libellé champ de saisie
</label>
<input class="fr-input" value="value" id="text-input-value" type="text">
</div>


### Champ avec icône personalisée


Libellé champ de saisie
Texte de description additionnel


###
Extrait de code


<div class="fr-input-group">
<label class="fr-label" for="text-input-icon">
Libellé champ de saisie
<span class="fr-hint-text">Texte de description additionnel</span>
</label>
<div class="fr-input-wrap fr-icon-alert-line">
<input class="fr-input" id="text-input-icon" type="text">
</div>
</div>


### Champ désactivé


Libellé champ de saisie


###
Extrait de code


<div class="fr-input-group fr-input-group--disabled">
<label class="fr-label" for="text-input-disabled">
Libellé champ de saisie
</label>
<input class="fr-input" disabled id="text-input-disabled" type="text">
</div>


### Champ avec texte additionnel


Libellé champ de saisie
Texte de description additionnel


###
Extrait de code


<div class="fr-input-group">
<label class="fr-label" for="text-input-hint">
Libellé champ de saisie
<span class="fr-hint-text">Texte de description additionnel</span>
</label>
<input class="fr-input" id="text-input-hint" type="text">
</div>


### Champ valide avec texte de succès


Libellé champ de saisie


Texte de validation


###
Extrait de code


<div class="fr-input-group fr-input-group--valid">
<label class="fr-label" for="text-input-valid">
Libellé champ de saisie
</label>
<input class="fr-input fr-input--valid" aria-describedby="text-input-valid-desc-valid" id="text-input-valid" type="text">
<p id="text-input-valid-desc-valid" class="fr-valid-text">
Texte de validation
</p>
</div>


### Champ en erreur avec texte d'erreur


Libellé champ de saisie


Texte d'erreur obligatoire


###
Extrait de code


<div class="fr-input-group fr-input-group--error">
<label class="fr-label" for="text-input-error">
Libellé champ de saisie
</label>
<input class="fr-input fr-input--error" aria-describedby="text-input-error-desc-error" id="text-input-error" type="text">
<p id="text-input-error-desc-error" class="fr-error-text">
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
