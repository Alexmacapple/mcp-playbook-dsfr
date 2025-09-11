URL:
https://main--ds-gouv.netlify.app/example/component/toggle/deprecated

Title:
Interrupteur - Système de design

Markdown:

Interrupteur - Système de design


DSFR v1.14.0


[Retour](../)


# Interrupteur (toggle)


Le composant "Interrupteur" permet à l'utilisateur de faire un choix entre deux états opposés (activé / désactivé).
[Documentation](https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/interrupteur)


## Dépréciation


Les exemples suivants sont dépréciés, ne pas utiliser comme référence

Pour support des versions précédentes


#### Toggle simple avec bouton + libellé à droite


Libellé action interrupteur


###
Extrait de code


<div class="fr-toggle">
<input type="checkbox" class="fr-toggle__input" id="toggle-4029">
<label class="fr-toggle__label" for="toggle-4029">Libellé action interrupteur</label>
</div>


#### Toggle simple avec bouton + libellé à droite + texte d'aide


Libellé action interrupteur


Texte d'aide pour clarifier l'action


###
Extrait de code


<div class="fr-toggle">
<input type="checkbox" class="fr-toggle__input" aria-describedby="toggle-4032-hint-text" id="toggle-4032">
<label class="fr-toggle__label" for="toggle-4032">Libellé action interrupteur</label>
<p class="fr-hint-text" id="toggle-4032-hint-text">Texte d'aide pour clarifier l'action</p>
</div>


#### Toggle simple avec bouton + libellé à droite + état


Libellé action interrupteur


###
Extrait de code


<div class="fr-toggle">
<input type="checkbox" class="fr-toggle__input" id="toggle-4035">
<label class="fr-toggle__label" for="toggle-4035" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé action interrupteur</label>
</div>


#### Toggle simple avec bouton + libellé à droite + état + texte d'aide


Libellé action interrupteur


Texte d'aide pour clarifier l'action


###
Extrait de code


<div class="fr-toggle">
<input type="checkbox" class="fr-toggle__input" aria-describedby="toggle-4038-hint-text" id="toggle-4038">
<label class="fr-toggle__label" for="toggle-4038" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé action interrupteur</label>
<p class="fr-hint-text" id="toggle-4038-hint-text">Texte d'aide pour clarifier l'action</p>
</div>


#### Toggle simple avec bouton + libellé à droite + état + séparateur


Libellé action interrupteur


###
Extrait de code


<div class="fr-toggle fr-toggle--border-bottom">
<input type="checkbox" class="fr-toggle__input" id="toggle-4041">
<label class="fr-toggle__label" for="toggle-4041" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé action interrupteur</label>
</div>


#### Toggle simple avec bouton + libellé à droite + état + séparateur + texte d'aide


Libellé action interrupteur


Texte d'aide pour clarifier l'action


###
Extrait de code


<div class="fr-toggle fr-toggle--border-bottom">
<input type="checkbox" class="fr-toggle__input" aria-describedby="toggle-4044-hint-text" id="toggle-4044">
<label class="fr-toggle__label" for="toggle-4044" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé action interrupteur</label>
<p class="fr-hint-text" id="toggle-4044-hint-text">Texte d'aide pour clarifier l'action</p>
</div>


#### Toggle simple disabled avec bouton + libellé à droite


Libellé action interrupteur


###
Extrait de code


<div class="fr-toggle">
<input type="checkbox" class="fr-toggle__input" disabled id="toggle-4047">
<label class="fr-toggle__label" for="toggle-4047">Libellé action interrupteur</label>
</div>


#### Toggle simple disabled avec bouton + libellé à droite + état


Libellé action interrupteur


###
Extrait de code


<div class="fr-toggle">
<input type="checkbox" class="fr-toggle__input" disabled id="toggle-4050">
<label class="fr-toggle__label" for="toggle-4050" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé action interrupteur</label>
</div>


#### Toggle simple disabled et pré-coché avec bouton + libellé à droite + état


Libellé action interrupteur


###
Extrait de code


<div class="fr-toggle">
<input type="checkbox" class="fr-toggle__input" disabled checked id="toggle-4053">
<label class="fr-toggle__label" for="toggle-4053" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé action interrupteur</label>
</div>


#### Groupe de toggles simple avec bouton + libellé à droite + séparateur


-


Libellé action interrupteur


-


Libellé action interrupteur


-


Libellé action interrupteur


-


Libellé action interrupteur


-


Libellé action interrupteur


###
Extrait de code


<ul class="fr-toggle__list">
<li>
<div class="fr-toggle fr-toggle--border-bottom">
<input type="checkbox" class="fr-toggle__input" id="group-1-toggle-0">
<label class="fr-toggle__label" for="group-1-toggle-0">Libellé action interrupteur</label>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom">
<input type="checkbox" class="fr-toggle__input" id="group-1-toggle-1">
<label class="fr-toggle__label" for="group-1-toggle-1">Libellé action interrupteur</label>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom">
<input type="checkbox" class="fr-toggle__input" id="group-1-toggle-2">
<label class="fr-toggle__label" for="group-1-toggle-2">Libellé action interrupteur</label>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom">
<input type="checkbox" class="fr-toggle__input" id="group-1-toggle-3">
<label class="fr-toggle__label" for="group-1-toggle-3">Libellé action interrupteur</label>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom">
<input type="checkbox" class="fr-toggle__input" id="group-1-toggle-4">
<label class="fr-toggle__label" for="group-1-toggle-4">Libellé action interrupteur</label>
</div>
</li>
</ul>


#### Groupe de toggles simple avec bouton + libellé à droite + séparateur + texte d'aide


-


Libellé action interrupteur


Texte d'aide pour clarifier l'action


-


Libellé action interrupteur


Texte d'aide pour clarifier l'action


-


Libellé action interrupteur


Texte d'aide pour clarifier l'action


-


Libellé action interrupteur


Texte d'aide pour clarifier l'action


-


Libellé action interrupteur


Texte d'aide pour clarifier l'action


###
Extrait de code


<ul class="fr-toggle__list">
<li>
<div class="fr-toggle fr-toggle--border-bottom">
<input type="checkbox" class="fr-toggle__input" aria-describedby="group-1-toggle-hint-0-hint-text" id="group-1-toggle-hint-0">
<label class="fr-toggle__label" for="group-1-toggle-hint-0">Libellé action interrupteur</label>
<p class="fr-hint-text" id="group-1-toggle-hint-0-hint-text">Texte d'aide pour clarifier l'action</p>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom">
<input type="checkbox" class="fr-toggle__input" aria-describedby="group-1-toggle-hint-1-hint-text" id="group-1-toggle-hint-1">
<label class="fr-toggle__label" for="group-1-toggle-hint-1">Libellé action interrupteur</label>
<p class="fr-hint-text" id="group-1-toggle-hint-1-hint-text">Texte d'aide pour clarifier l'action</p>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom">
<input type="checkbox" class="fr-toggle__input" aria-describedby="group-1-toggle-hint-2-hint-text" id="group-1-toggle-hint-2">
<label class="fr-toggle__label" for="group-1-toggle-hint-2">Libellé action interrupteur</label>
<p class="fr-hint-text" id="group-1-toggle-hint-2-hint-text">Texte d'aide pour clarifier l'action</p>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom">
<input type="checkbox" class="fr-toggle__input" aria-describedby="group-1-toggle-hint-3-hint-text" id="group-1-toggle-hint-3">
<label class="fr-toggle__label" for="group-1-toggle-hint-3">Libellé action interrupteur</label>
<p class="fr-hint-text" id="group-1-toggle-hint-3-hint-text">Texte d'aide pour clarifier l'action</p>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom">
<input type="checkbox" class="fr-toggle__input" aria-describedby="group-1-toggle-hint-4-hint-text" id="group-1-toggle-hint-4">
<label class="fr-toggle__label" for="group-1-toggle-hint-4">Libellé action interrupteur</label>
<p class="fr-hint-text" id="group-1-toggle-hint-4-hint-text">Texte d'aide pour clarifier l'action</p>
</div>
</li>
</ul>


#### Groupe de toggles simple avec bouton + libellé à droite + état + séparateur


-


Libellé action interrupteur


-


Libellé action interrupteur


-


Libellé action interrupteur


-


Libellé action interrupteur


-


Libellé action interrupteur


###
Extrait de code


<ul class="fr-toggle__list">
<li>
<div class="fr-toggle fr-toggle--border-bottom">
<input type="checkbox" class="fr-toggle__input" id="group-2-toggle-0">
<label class="fr-toggle__label" for="group-2-toggle-0" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé action interrupteur</label>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom">
<input type="checkbox" class="fr-toggle__input" id="group-2-toggle-1">
<label class="fr-toggle__label" for="group-2-toggle-1" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé action interrupteur</label>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom">
<input type="checkbox" class="fr-toggle__input" id="group-2-toggle-2">
<label class="fr-toggle__label" for="group-2-toggle-2" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé action interrupteur</label>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom">
<input type="checkbox" class="fr-toggle__input" id="group-2-toggle-3">
<label class="fr-toggle__label" for="group-2-toggle-3" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé action interrupteur</label>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom">
<input type="checkbox" class="fr-toggle__input" id="group-2-toggle-4">
<label class="fr-toggle__label" for="group-2-toggle-4" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé action interrupteur</label>
</div>
</li>
</ul>


#### Groupe de toggles simple avec bouton + libellé à droite + état + séparateur + texte d'aide


-


Libellé action interrupteur


Texte d'aide pour clarifier l'action


-


Libellé action interrupteur


Texte d'aide pour clarifier l'action


-


Libellé action interrupteur


Texte d'aide pour clarifier l'action


-


Libellé action interrupteur


Texte d'aide pour clarifier l'action


-


Libellé action interrupteur


Texte d'aide pour clarifier l'action


###
Extrait de code


<ul class="fr-toggle__list">
<li>
<div class="fr-toggle fr-toggle--border-bottom">
<input type="checkbox" class="fr-toggle__input" aria-describedby="group-2-toggle-hint-0-hint-text" id="group-2-toggle-hint-0">
<label class="fr-toggle__label" for="group-2-toggle-hint-0" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé action interrupteur</label>
<p class="fr-hint-text" id="group-2-toggle-hint-0-hint-text">Texte d'aide pour clarifier l'action</p>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom">
<input type="checkbox" class="fr-toggle__input" aria-describedby="group-2-toggle-hint-1-hint-text" id="group-2-toggle-hint-1">
<label class="fr-toggle__label" for="group-2-toggle-hint-1" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé action interrupteur</label>
<p class="fr-hint-text" id="group-2-toggle-hint-1-hint-text">Texte d'aide pour clarifier l'action</p>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom">
<input type="checkbox" class="fr-toggle__input" aria-describedby="group-2-toggle-hint-2-hint-text" id="group-2-toggle-hint-2">
<label class="fr-toggle__label" for="group-2-toggle-hint-2" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé action interrupteur</label>
<p class="fr-hint-text" id="group-2-toggle-hint-2-hint-text">Texte d'aide pour clarifier l'action</p>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom">
<input type="checkbox" class="fr-toggle__input" aria-describedby="group-2-toggle-hint-3-hint-text" id="group-2-toggle-hint-3">
<label class="fr-toggle__label" for="group-2-toggle-hint-3" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé action interrupteur</label>
<p class="fr-hint-text" id="group-2-toggle-hint-3-hint-text">Texte d'aide pour clarifier l'action</p>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom">
<input type="checkbox" class="fr-toggle__input" aria-describedby="group-2-toggle-hint-4-hint-text" id="group-2-toggle-hint-4">
<label class="fr-toggle__label" for="group-2-toggle-hint-4" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé action interrupteur</label>
<p class="fr-hint-text" id="group-2-toggle-hint-4-hint-text">Texte d'aide pour clarifier l'action</p>
</div>
</li>
</ul>


#### Toggle simple avec bouton + libellé à gauche


Libellé action interrupteur


###
Extrait de code


<div class="fr-toggle fr-toggle--label-left">
<input type="checkbox" class="fr-toggle__input" id="toggle-4060">
<label class="fr-toggle__label" for="toggle-4060">Libellé action interrupteur</label>
</div>


#### Toggle simple avec bouton + libellé à gauche + texte d'aide


Libellé action interrupteur


Texte d'aide pour clarifier l'action


###
Extrait de code


<div class="fr-toggle fr-toggle--label-left">
<input type="checkbox" class="fr-toggle__input" aria-describedby="toggle-4063-hint-text" id="toggle-4063">
<label class="fr-toggle__label" for="toggle-4063">Libellé action interrupteur</label>
<p class="fr-hint-text" id="toggle-4063-hint-text">Texte d'aide pour clarifier l'action</p>
</div>


#### Toggle simple avec bouton + libellé à gauche + état


Libellé action interrupteur


###
Extrait de code


<div class="fr-toggle fr-toggle--label-left">
<input type="checkbox" class="fr-toggle__input" id="toggle-4066">
<label class="fr-toggle__label" for="toggle-4066" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé action interrupteur</label>
</div>


#### Toggle simple avec bouton + libellé à gauche + état + texte d'aide


Libellé action interrupteur


Texte d'aide pour clarifier l'action


###
Extrait de code


<div class="fr-toggle fr-toggle--label-left">
<input type="checkbox" class="fr-toggle__input" aria-describedby="toggle-4069-hint-text" id="toggle-4069">
<label class="fr-toggle__label" for="toggle-4069" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé action interrupteur</label>
<p class="fr-hint-text" id="toggle-4069-hint-text">Texte d'aide pour clarifier l'action</p>
</div>


#### Toggle simple avec bouton + libellé à gauche + état + séparateur


Libellé action interrupteur


###
Extrait de code


<div class="fr-toggle fr-toggle--border-bottom fr-toggle--label-left">
<input type="checkbox" class="fr-toggle__input" id="toggle-4072">
<label class="fr-toggle__label" for="toggle-4072" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé action interrupteur</label>
</div>


#### Toggle simple avec bouton + libellé à gauche + état + séparateur + texte d'aide


Libellé action interrupteur


Texte d'aide pour clarifier l'action


###
Extrait de code


<div class="fr-toggle fr-toggle--border-bottom fr-toggle--label-left">
<input type="checkbox" class="fr-toggle__input" aria-describedby="toggle-4075-hint-text" id="toggle-4075">
<label class="fr-toggle__label" for="toggle-4075" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé action interrupteur</label>
<p class="fr-hint-text" id="toggle-4075-hint-text">Texte d'aide pour clarifier l'action</p>
</div>


#### Toggle simple disabled avec bouton + libellé à gauche


Libellé action interrupteur


###
Extrait de code


<div class="fr-toggle fr-toggle--label-left">
<input type="checkbox" class="fr-toggle__input" disabled id="toggle-4078">
<label class="fr-toggle__label" for="toggle-4078">Libellé action interrupteur</label>
</div>


#### Toggle simple disabled avec bouton + libellé à gauche + état


Libellé action interrupteur


###
Extrait de code


<div class="fr-toggle fr-toggle--label-left">
<input type="checkbox" class="fr-toggle__input" disabled id="toggle-4081">
<label class="fr-toggle__label" for="toggle-4081" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé action interrupteur</label>
</div>


#### Groupe de toggles simple avec bouton + libellé à gauche + séparateur


-


Libellé action interrupteur


-


Libellé action interrupteur


-


Libellé action interrupteur


-


Libellé action interrupteur


-


Libellé action interrupteur


###
Extrait de code


<ul class="fr-toggle__list">
<li>
<div class="fr-toggle fr-toggle--border-bottom fr-toggle--label-left">
<input type="checkbox" class="fr-toggle__input" id="group-3-toggle-0">
<label class="fr-toggle__label" for="group-3-toggle-0">Libellé action interrupteur</label>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom fr-toggle--label-left">
<input type="checkbox" class="fr-toggle__input" id="group-3-toggle-1">
<label class="fr-toggle__label" for="group-3-toggle-1">Libellé action interrupteur</label>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom fr-toggle--label-left">
<input type="checkbox" class="fr-toggle__input" id="group-3-toggle-2">
<label class="fr-toggle__label" for="group-3-toggle-2">Libellé action interrupteur</label>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom fr-toggle--label-left">
<input type="checkbox" class="fr-toggle__input" id="group-3-toggle-3">
<label class="fr-toggle__label" for="group-3-toggle-3">Libellé action interrupteur</label>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom fr-toggle--label-left">
<input type="checkbox" class="fr-toggle__input" id="group-3-toggle-4">
<label class="fr-toggle__label" for="group-3-toggle-4">Libellé action interrupteur</label>
</div>
</li>
</ul>


#### Groupe de toggles simple avec bouton + libellé à gauche + séparateur + texte d'aide


-


Libellé action interrupteur


Texte d'aide pour clarifier l'action


-


Libellé action interrupteur


Texte d'aide pour clarifier l'action


-


Libellé action interrupteur


Texte d'aide pour clarifier l'action


-


Libellé action interrupteur


Texte d'aide pour clarifier l'action


-


Libellé action interrupteur


Texte d'aide pour clarifier l'action


###
Extrait de code


<ul class="fr-toggle__list">
<li>
<div class="fr-toggle fr-toggle--border-bottom fr-toggle--label-left">
<input type="checkbox" class="fr-toggle__input" aria-describedby="group-3-toggle-hint-0-hint-text" id="group-3-toggle-hint-0">
<label class="fr-toggle__label" for="group-3-toggle-hint-0">Libellé action interrupteur</label>
<p class="fr-hint-text" id="group-3-toggle-hint-0-hint-text">Texte d'aide pour clarifier l'action</p>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom fr-toggle--label-left">
<input type="checkbox" class="fr-toggle__input" aria-describedby="group-3-toggle-hint-1-hint-text" id="group-3-toggle-hint-1">
<label class="fr-toggle__label" for="group-3-toggle-hint-1">Libellé action interrupteur</label>
<p class="fr-hint-text" id="group-3-toggle-hint-1-hint-text">Texte d'aide pour clarifier l'action</p>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom fr-toggle--label-left">
<input type="checkbox" class="fr-toggle__input" aria-describedby="group-3-toggle-hint-2-hint-text" id="group-3-toggle-hint-2">
<label class="fr-toggle__label" for="group-3-toggle-hint-2">Libellé action interrupteur</label>
<p class="fr-hint-text" id="group-3-toggle-hint-2-hint-text">Texte d'aide pour clarifier l'action</p>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom fr-toggle--label-left">
<input type="checkbox" class="fr-toggle__input" aria-describedby="group-3-toggle-hint-3-hint-text" id="group-3-toggle-hint-3">
<label class="fr-toggle__label" for="group-3-toggle-hint-3">Libellé action interrupteur</label>
<p class="fr-hint-text" id="group-3-toggle-hint-3-hint-text">Texte d'aide pour clarifier l'action</p>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom fr-toggle--label-left">
<input type="checkbox" class="fr-toggle__input" aria-describedby="group-3-toggle-hint-4-hint-text" id="group-3-toggle-hint-4">
<label class="fr-toggle__label" for="group-3-toggle-hint-4">Libellé action interrupteur</label>
<p class="fr-hint-text" id="group-3-toggle-hint-4-hint-text">Texte d'aide pour clarifier l'action</p>
</div>
</li>
</ul>


#### Groupe de toggles simple avec bouton + libellé à gauche + état + séparateur


-


Libellé action interrupteur


-


Libellé action interrupteur


-


Libellé action interrupteur


-


Libellé action interrupteur


-


Libellé action interrupteur


###
Extrait de code


<ul class="fr-toggle__list">
<li>
<div class="fr-toggle fr-toggle--border-bottom fr-toggle--label-left">
<input type="checkbox" class="fr-toggle__input" id="group-4-toggle-0">
<label class="fr-toggle__label" for="group-4-toggle-0" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé action interrupteur</label>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom fr-toggle--label-left">
<input type="checkbox" class="fr-toggle__input" id="group-4-toggle-1">
<label class="fr-toggle__label" for="group-4-toggle-1" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé action interrupteur</label>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom fr-toggle--label-left">
<input type="checkbox" class="fr-toggle__input" id="group-4-toggle-2">
<label class="fr-toggle__label" for="group-4-toggle-2" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé action interrupteur</label>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom fr-toggle--label-left">
<input type="checkbox" class="fr-toggle__input" id="group-4-toggle-3">
<label class="fr-toggle__label" for="group-4-toggle-3" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé action interrupteur</label>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom fr-toggle--label-left">
<input type="checkbox" class="fr-toggle__input" id="group-4-toggle-4">
<label class="fr-toggle__label" for="group-4-toggle-4" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé action interrupteur</label>
</div>
</li>
</ul>


#### Groupe de toggles simple avec bouton + libellé à gauche + état + séparateur + texte d'aide


-


Libellé action interrupteur


Texte d'aide pour clarifier l'action


-


Libellé action interrupteur


Texte d'aide pour clarifier l'action


-


Libellé action interrupteur


Texte d'aide pour clarifier l'action


-


Libellé action interrupteur


Texte d'aide pour clarifier l'action


-


Libellé action interrupteur


Texte d'aide pour clarifier l'action


###
Extrait de code


<ul class="fr-toggle__list">
<li>
<div class="fr-toggle fr-toggle--border-bottom fr-toggle--label-left">
<input type="checkbox" class="fr-toggle__input" aria-describedby="group-4-toggle-hint-0-hint-text" id="group-4-toggle-hint-0">
<label class="fr-toggle__label" for="group-4-toggle-hint-0" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé action interrupteur</label>
<p class="fr-hint-text" id="group-4-toggle-hint-0-hint-text">Texte d'aide pour clarifier l'action</p>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom fr-toggle--label-left">
<input type="checkbox" class="fr-toggle__input" aria-describedby="group-4-toggle-hint-1-hint-text" id="group-4-toggle-hint-1">
<label class="fr-toggle__label" for="group-4-toggle-hint-1" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé action interrupteur</label>
<p class="fr-hint-text" id="group-4-toggle-hint-1-hint-text">Texte d'aide pour clarifier l'action</p>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom fr-toggle--label-left">
<input type="checkbox" class="fr-toggle__input" aria-describedby="group-4-toggle-hint-2-hint-text" id="group-4-toggle-hint-2">
<label class="fr-toggle__label" for="group-4-toggle-hint-2" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé action interrupteur</label>
<p class="fr-hint-text" id="group-4-toggle-hint-2-hint-text">Texte d'aide pour clarifier l'action</p>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom fr-toggle--label-left">
<input type="checkbox" class="fr-toggle__input" aria-describedby="group-4-toggle-hint-3-hint-text" id="group-4-toggle-hint-3">
<label class="fr-toggle__label" for="group-4-toggle-hint-3" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé action interrupteur</label>
<p class="fr-hint-text" id="group-4-toggle-hint-3-hint-text">Texte d'aide pour clarifier l'action</p>
</div>
</li>
<li>
<div class="fr-toggle fr-toggle--border-bottom fr-toggle--label-left">
<input type="checkbox" class="fr-toggle__input" aria-describedby="group-4-toggle-hint-4-hint-text" id="group-4-toggle-hint-4">
<label class="fr-toggle__label" for="group-4-toggle-hint-4" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé action interrupteur</label>
<p class="fr-hint-text" id="group-4-toggle-hint-4-hint-text">Texte d'aide pour clarifier l'action</p>
</div>
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
