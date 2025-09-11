URL:
https://main--ds-gouv.netlify.app/example/layout/pattern/email

Title:
Bloc fonctionnel de demande d'email - Système de design

Markdown:

Bloc fonctionnel de demande d'email - Système de design


DSFR v1.14.0


[Retour](../)


# Bloc fonctionnel de demande d'email (email)


La demande d'email est un bloc fonctionnel qui permet de saisir un email.
[Documentation](https://www.systeme-de-design.gouv.fr/elements-d-interface/blocs-fonctionnels/email)


### Demande d'une adresse électronique


Adresse électronique
Format attendu : nom@domaine.fr


###
Extrait de code


<div class="fr-input-group" id="input-group-7448">
<label class="fr-label" for="email-7447">
Adresse électronique
<span class="fr-hint-text">Format attendu : nom@domaine.fr</span>
</label>
<input class="fr-input" spellcheck="false" autocomplete="email" aria-describedby="email-7447-messages" id="email-7447" type="email">
<div class="fr-messages-group" id="email-7447-messages" aria-live="polite">
</div>
</div>


### Demande d'une adresse électronique - Erreur


Adresse électronique
Format attendu : nom@domaine.fr


Le format de l'adresse electronique saisie n'est pas valide. Le format attendu est : nom@domaine.fr


###
Extrait de code


<div class="fr-input-group fr-input-group--error" id="input-group-7453">
<label class="fr-label" for="email-7452">
Adresse électronique
<span class="fr-hint-text">Format attendu : nom@domaine.fr</span>
</label>
<input class="fr-input" spellcheck="false" autocomplete="email" aria-describedby="email-7452-messages" id="email-7452" type="email">
<div class="fr-messages-group" id="email-7452-messages" aria-live="polite">
<p class="fr-message fr-message--error" id="email-7452-message-error">Le format de l'adresse electronique saisie n'est pas valide. Le format attendu est : nom@domaine.fr</p>
</div>
</div>


### Demande et indication de traitement d'une adresse électronique


Adresse électronique
Indication : cette adresse est utilisée uniquement pour la connexion au service.
Format attendu : nom@domaine.fr


###
Extrait de code


<div class="fr-input-group" id="input-group-7458">
<label class="fr-label" for="email-7457">
Adresse électronique
<span class="fr-hint-text">Indication : cette adresse est utilisée uniquement pour la connexion au service.</span>
<span class="fr-hint-text">Format attendu : nom@domaine.fr</span>
</label>
<input class="fr-input" spellcheck="false" autocomplete="email" aria-describedby="email-7457-messages" id="email-7457" type="email">
<div class="fr-messages-group" id="email-7457-messages" aria-live="polite">
</div>
</div>


### Demande et indication de traitement d'une adresse électronique - Erreur


Adresse électronique
Indication : cette adresse est utilisée uniquement pour la connexion au service.
Format attendu : nom@domaine.fr


Le format de l'adresse electronique saisie n'est pas valide. Le format attendu est : nom@domaine.fr


###
Extrait de code


<div class="fr-input-group fr-input-group--error" id="input-group-7463">
<label class="fr-label" for="email-7462">
Adresse électronique
<span class="fr-hint-text">Indication : cette adresse est utilisée uniquement pour la connexion au service.</span>
<span class="fr-hint-text">Format attendu : nom@domaine.fr</span>
</label>
<input class="fr-input" spellcheck="false" autocomplete="email" aria-describedby="email-7462-messages" id="email-7462" type="email">
<div class="fr-messages-group" id="email-7462-messages" aria-live="polite">
<p class="fr-message fr-message--error" id="email-7462-message-error">Le format de l'adresse electronique saisie n'est pas valide. Le format attendu est : nom@domaine.fr</p>
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
