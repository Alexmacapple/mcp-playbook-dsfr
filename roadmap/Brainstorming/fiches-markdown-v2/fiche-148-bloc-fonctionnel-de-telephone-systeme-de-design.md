URL:
https://main--ds-gouv.netlify.app/example/layout/pattern/tel

Title:
Bloc fonctionnel de téléphone - Système de design

Markdown:

Bloc fonctionnel de téléphone - Système de design


DSFR v1.14.0


[Retour](../)


# Bloc fonctionnel de téléphone (tel)


La demande de numéro de téléphone est un bloc fonctionnel qui permet de saisir un numéro de téléphone.
[Documentation](https://www.systeme-de-design.gouv.fr/elements-d-interface/blocs-fonctionnels/tel)


### Demande d'un numéro de téléphone


Numéro de téléphone
Format attendu : (+33) 1 22 33 44 55


###
Extrait de code


<div class="fr-input-group" id="input-group-7747">
<label class="fr-label" for="tel-7746">
Numéro de téléphone
<span class="fr-hint-text">Format attendu : (+33) 1 22 33 44 55</span>
</label>
<input class="fr-input" autocomplete="tel" aria-describedby="tel-7746-messages" id="tel-7746" type="tel">
<div class="fr-messages-group" id="tel-7746-messages" aria-live="polite">
</div>
</div>


### Demande d'un numéro de téléphone - Erreur


Numéro de téléphone
Format attendu : (+33) 1 22 33 44 55


Le format de numéro de téléphone saisie n'est pas valide. Le format attendu est : (+33) 1 22 33 44 55


###
Extrait de code


<div class="fr-input-group fr-input-group--error" id="input-group-7752">
<label class="fr-label" for="tel-7751">
Numéro de téléphone
<span class="fr-hint-text">Format attendu : (+33) 1 22 33 44 55</span>
</label>
<input class="fr-input" autocomplete="tel" aria-describedby="tel-7751-messages" id="tel-7751" type="tel">
<div class="fr-messages-group" id="tel-7751-messages" aria-live="polite">
<p class="fr-message fr-message--error" id="tel-7751-message-error">Le format de numéro de téléphone saisie n'est pas valide. Le format attendu est : (+33) 1 22 33 44 55</p>
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
