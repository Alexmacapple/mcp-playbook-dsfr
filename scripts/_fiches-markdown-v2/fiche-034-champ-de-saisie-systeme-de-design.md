URL:
https://main--ds-gouv.netlify.app/example/component/input

Title:
Champ de saisie - Système de design

Markdown:

Champ de saisie - Système de design


DSFR v1.14.0


[Retour](../)


# Champ de saisie (input)


Les champs permettent à un utilisateur d'entrer du contenu et données.
[Documentation](https://www.systeme-de-design.gouv.fr/elements-d-interface/blocs-fonctionnels/adresse-electronique)


### Champ de type "text"


Libellé champ de saisie


###
Extrait de code


<div class="fr-input-group" id="input-group-1503">
<label class="fr-label" for="text-input-text">
Libellé champ de saisie
</label>
<input class="fr-input" aria-describedby="text-input-text-messages" id="text-input-text" type="text">
<div class="fr-messages-group" id="text-input-text-messages" aria-live="polite">
</div>
</div>


### Champ de type "number"


Libellé champ de saisie


###
Extrait de code


<div class="fr-input-group" id="input-group-1506">
<label class="fr-label" for="text-input-number">
Libellé champ de saisie
</label>
<input class="fr-input" pattern="[0-9]*" inputmode="numeric" aria-describedby="text-input-number-messages" id="text-input-number" type="number">
<div class="fr-messages-group" id="text-input-number-messages" aria-live="polite">
</div>
</div>


### Champ de type "search"


Libellé champ de saisie


###
Extrait de code


<div class="fr-input-group" id="input-group-1509">
<label class="fr-label" for="text-input-search">
Libellé champ de saisie
</label>
<input class="fr-input" aria-describedby="text-input-search-messages" id="text-input-search" type="search">
<div class="fr-messages-group" id="text-input-search-messages" aria-live="polite">
</div>
</div>


### Champ de type "date"


Préférez l'utilisation du modèle de bloc de [Date unique](../../../pattern/date/)


Libellé champ de saisie


###
Extrait de code


<div class="fr-input-group" id="input-group-1512">
<label class="fr-label" for="text-input-date">
Libellé champ de saisie
</label>
<input class="fr-input" aria-describedby="text-input-date-messages" id="text-input-date" type="date">
<div class="fr-messages-group" id="text-input-date-messages" aria-live="polite">
</div>
</div>


### Champ de type "textarea"


Libellé champ de saisie


###
Extrait de code


<div class="fr-input-group" id="input-group-1515">
<label class="fr-label" for="textarea">
Libellé champ de saisie
</label>
<textarea class="fr-input" aria-describedby="textarea-messages" id="textarea"></textarea>
<div class="fr-messages-group" id="textarea-messages" aria-live="polite">
</div>
</div>


### Champ de type "password"


Préférez l'utilisation du composant [Mot de passe](../../password/)


Libellé champ de saisie


###
Extrait de code


<div class="fr-input-group" id="input-group-1518">
<label class="fr-label" for="text-input-password">
Libellé champ de saisie
</label>
<input class="fr-input" aria-describedby="text-input-password-messages" id="text-input-password" type="password">
<div class="fr-messages-group" id="text-input-password-messages" aria-live="polite">
</div>
</div>


### Combo champ + bouton d'envoi


Libellé champ de saisie


Envoyer


###
Extrait de code


<div class="fr-input-group" id="input-group-1521">
<label class="fr-label" for="text-input-button">
Libellé champ de saisie
</label>
<div class="fr-input-wrap fr-input-wrap--addon">
<input class="fr-input" aria-describedby="text-input-button-messages" id="text-input-button" type="text">
<button type="submit" class="fr-btn">Envoyer</button>
</div>
<div class="fr-messages-group" id="text-input-button-messages" aria-live="polite">
</div>
</div>


### Combo champ + bouton d'action


Libellé champ de saisie


Supprimer le champ


###
Extrait de code


<div class="fr-input-group" id="input-group-1524">
<label class="fr-label" for="text-input-action">
Libellé champ de saisie
</label>
<div class="fr-input-wrap fr-input-wrap--action">
<input class="fr-input" aria-describedby="text-input-action-messages" id="text-input-action" type="text">
<button type="button" class="fr-btn fr-icon-delete-line fr-btn--secondary">Supprimer le champ</button>
</div>
<div class="fr-messages-group" id="text-input-action-messages" aria-live="polite">
</div>
</div>


### Champ avec placeholder


Libellé champ de saisie


###
Extrait de code


<div class="fr-input-group" id="input-group-1527">
<label class="fr-label" for="text-input-placeholder">
Libellé champ de saisie
</label>
<input class="fr-input" aria-describedby="text-input-placeholder-messages" placeholder="placeholder" id="text-input-placeholder" type="text">
<div class="fr-messages-group" id="text-input-placeholder-messages" aria-live="polite">
</div>
</div>


### Champ avec valeur initiale


Libellé champ de saisie


###
Extrait de code


<div class="fr-input-group" id="input-group-1530">
<label class="fr-label" for="text-input-value">
Libellé champ de saisie
</label>
<input class="fr-input" value="value" aria-describedby="text-input-value-messages" id="text-input-value" type="text">
<div class="fr-messages-group" id="text-input-value-messages" aria-live="polite">
</div>
</div>


### Champ avec icône personalisée


Libellé champ de saisie
Texte de description additionnel


###
Extrait de code


<div class="fr-input-group" id="input-group-1533">
<label class="fr-label" for="text-input-icon">
Libellé champ de saisie
<span class="fr-hint-text">Texte de description additionnel</span>
</label>
<div class="fr-input-wrap fr-icon-alert-line">
<input class="fr-input" aria-describedby="text-input-icon-messages" id="text-input-icon" type="text">
</div>
<div class="fr-messages-group" id="text-input-icon-messages" aria-live="polite">
</div>
</div>


### Champ désactivé


Libellé champ de saisie


###
Extrait de code


<div class="fr-input-group fr-input-group--disabled" id="input-group-1536">
<label class="fr-label" for="text-input-disabled">
Libellé champ de saisie
</label>
<input class="fr-input" aria-describedby="text-input-disabled-messages" disabled id="text-input-disabled" type="text">
<div class="fr-messages-group" id="text-input-disabled-messages" aria-live="polite">
</div>
</div>


### Champ avec texte additionnel


Libellé champ de saisie
Texte de description additionnel


###
Extrait de code


<div class="fr-input-group" id="input-group-1539">
<label class="fr-label" for="text-input-hint">
Libellé champ de saisie
<span class="fr-hint-text">Texte de description additionnel</span>
</label>
<input class="fr-input" aria-describedby="text-input-hint-messages" id="text-input-hint" type="text">
<div class="fr-messages-group" id="text-input-hint-messages" aria-live="polite">
</div>
</div>


### Champ valide avec texte de succès


Libellé champ de saisie


Texte de validation


###
Extrait de code


<div class="fr-input-group fr-input-group--valid" id="input-group-1542">
<label class="fr-label" for="text-input-valid">
Libellé champ de saisie
</label>
<input class="fr-input" aria-describedby="text-input-valid-messages" id="text-input-valid" type="text">
<div class="fr-messages-group" id="text-input-valid-messages" aria-live="polite">
<p class="fr-message fr-message--valid" id="text-input-valid-message-valid">Texte de validation</p>
</div>
</div>


### Champ en erreur avec texte d'erreur


Libellé champ de saisie


Texte d'erreur obligatoire


###
Extrait de code


<div class="fr-input-group fr-input-group--error" id="input-group-1545">
<label class="fr-label" for="text-input-error">
Libellé champ de saisie
</label>
<input class="fr-input" aria-describedby="text-input-error-messages" id="text-input-error" type="text">
<div class="fr-messages-group" id="text-input-error-messages" aria-live="polite">
<p class="fr-message fr-message--error" id="text-input-error-message-error">Texte d'erreur obligatoire</p>
</div>
</div>


### Autres versions


-
[version dépréciée](deprecated)


Libellé bouton


Fermer


##
Paramètres d'affichage


Choisissez un thème pour personnaliser l'apparence du site.


Thème clair


Thème sombre


Système
Utilise les paramètres système
