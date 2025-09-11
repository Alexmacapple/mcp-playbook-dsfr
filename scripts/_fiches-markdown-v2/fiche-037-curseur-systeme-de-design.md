URL:
https://main--ds-gouv.netlify.app/example/component/range

Title:
Curseur - Système de design

Markdown:

Curseur - Système de design


DSFR v1.14.0


[Retour](../)


# Curseur (range)


Les curseurs sont des entrées numériques qui permettent de voir graphiquement une sélection par rapport a une valeur minimale et maximale. Ils servent à montrer en temps réelle les options choisies et éclairer la prise de décision.
[Documentation](https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/curseur)


### Curseur simple


Libellé
Texte de description additionnel, valeur de 0 à 100.


50

0
100


###
Extrait de code


<div class="fr-range-group" id="range-1778-group">
<label class="fr-label">
Libellé
<span class="fr-hint-text">Texte de description additionnel, valeur de 0 à 100.</span>
</label>
<div class="fr-range">
<span class="fr-range__output">50</span>
<input id="range-1777" name="range-1777" type="range" aria-labelledby="range-1777-label" max="100" value="50" aria-describedby="range-1777-messages">
<span class="fr-range__min" aria-hidden="true">0</span>
<span class="fr-range__max" aria-hidden="true">100</span>
</div>
<div class="fr-messages-group" id="range-1777-messages" aria-live="polite">
</div>
</div>


### Curseur simple taille SM


Libellé
Texte de description additionnel, valeur de 0 à 100.


50

0
100


###
Extrait de code


<div class="fr-range-group" id="range-1783-group">
<label class="fr-label">
Libellé
<span class="fr-hint-text">Texte de description additionnel, valeur de 0 à 100.</span>
</label>
<div class="fr-range fr-range--sm">
<span class="fr-range__output">50</span>
<input id="range-1782" name="range-1782" type="range" aria-labelledby="range-1782-label" max="100" value="50" aria-describedby="range-1782-messages">
<span class="fr-range__min" aria-hidden="true">0</span>
<span class="fr-range__max" aria-hidden="true">100</span>
</div>
<div class="fr-messages-group" id="range-1782-messages" aria-live="polite">
</div>
</div>


### Curseur simple sans les indicateurs min/max


Libellé
Texte de description additionnel, valeur de 0 à 100.


50


###
Extrait de code


<div class="fr-range-group" id="range-1788-group">
<label class="fr-label">
Libellé
<span class="fr-hint-text">Texte de description additionnel, valeur de 0 à 100.</span>
</label>
<div class="fr-range">
<span class="fr-range__output">50</span>
<input id="range-1787" name="range-1787" type="range" aria-labelledby="range-1787-label" max="100" value="50" aria-describedby="range-1787-messages">
</div>
<div class="fr-messages-group" id="range-1787-messages" aria-live="polite">
</div>
</div>


### Curseur avec étapes


Libellé
Texte de description additionnel, valeur de 0 à 100.


50

0
100


###
Extrait de code


<div class="fr-range-group" id="range-1793-group">
<label class="fr-label">
Libellé
<span class="fr-hint-text">Texte de description additionnel, valeur de 0 à 100.</span>
</label>
<div class="fr-range fr-range--step">
<span class="fr-range__output">50</span>
<input id="range-1792" name="range-1792" type="range" aria-labelledby="range-1792-label" max="100" value="50" step="10" aria-describedby="range-1792-messages">
<span class="fr-range__min" aria-hidden="true">0</span>
<span class="fr-range__max" aria-hidden="true">100</span>
</div>
<div class="fr-messages-group" id="range-1792-messages" aria-live="polite">
</div>
</div>


### Curseur avec étapes taille SM


Libellé
Texte de description additionnel, valeur de 0 à 100.


50

0
100


###
Extrait de code


<div class="fr-range-group" id="range-1798-group">
<label class="fr-label">
Libellé
<span class="fr-hint-text">Texte de description additionnel, valeur de 0 à 100.</span>
</label>
<div class="fr-range fr-range--sm fr-range--step">
<span class="fr-range__output">50</span>
<input id="range-1797" name="range-1797" type="range" aria-labelledby="range-1797-label" max="100" value="50" step="10" aria-describedby="range-1797-messages">
<span class="fr-range__min" aria-hidden="true">0</span>
<span class="fr-range__max" aria-hidden="true">100</span>
</div>
<div class="fr-messages-group" id="range-1797-messages" aria-live="polite">
</div>
</div>


### Curseur double avec valeurs min et max


Libellé
Texte de description additionnel, valeur de 0 à 100.


25


0
100


###
Extrait de code


<div class="fr-range-group" id="range-1803-group">
<label class="fr-label">
Libellé
<span class="fr-hint-text">Texte de description additionnel, valeur de 0 à 100.</span>
</label>
<div class="fr-range fr-range--double">
<span class="fr-range__output">25</span>
<input id="range-1802" name="range-1802" type="range" aria-labelledby="range-1802-label" max="100" value="25" aria-describedby="range-1802-messages">
<input id="range-1802-2" name="range-1802-2" type="range" aria-labelledby="range-1802-label" max="100" value="75" aria-describedby="range-1802-messages">
<span class="fr-range__min" aria-hidden="true">0</span>
<span class="fr-range__max" aria-hidden="true">100</span>
</div>
<div class="fr-messages-group" id="range-1802-messages" aria-live="polite">
</div>
</div>


### Curseur double taille SM


Libellé
Texte de description additionnel, valeur de 0 à 100.


25


0
100


###
Extrait de code


<div class="fr-range-group" id="range-1808-group">
<label class="fr-label">
Libellé
<span class="fr-hint-text">Texte de description additionnel, valeur de 0 à 100.</span>
</label>
<div class="fr-range fr-range--sm fr-range--double">
<span class="fr-range__output">25</span>
<input id="range-1807" name="range-1807" type="range" aria-labelledby="range-1807-label" max="100" value="25" aria-describedby="range-1807-messages">
<input id="range-1807-2" name="range-1807-2" type="range" aria-labelledby="range-1807-label" max="100" value="75" aria-describedby="range-1807-messages">
<span class="fr-range__min" aria-hidden="true">0</span>
<span class="fr-range__max" aria-hidden="true">100</span>
</div>
<div class="fr-messages-group" id="range-1807-messages" aria-live="polite">
</div>
</div>


### Curseur avec préfixe et suffixe


Libellé
Texte de description additionnel, valeur de 0 à 100.


~50%

~0%
~100%


###
Extrait de code


<div class="fr-range-group" id="range-1813-group">
<label class="fr-label">
Libellé
<span class="fr-hint-text">Texte de description additionnel, valeur de 0 à 100.</span>
</label>
<div class="fr-range" data-fr-prefix="~" data-fr-suffix="%">
<span class="fr-range__output">~50%</span>
<input id="range-1812" name="range-1812" type="range" aria-labelledby="range-1812-label" max="100" value="50" aria-describedby="range-1812-messages">
<span class="fr-range__min" aria-hidden="true">~0%</span>
<span class="fr-range__max" aria-hidden="true">~100%</span>
</div>
<div class="fr-messages-group" id="range-1812-messages" aria-live="polite">
</div>
</div>


### Curseur désactivé


Libellé
Texte de description additionnel, valeur de 0 à 100.


50

0
100


###
Extrait de code


<div class="fr-range-group fr-range-group--disabled" id="range-1818-group">
<label class="fr-label">
Libellé
<span class="fr-hint-text">Texte de description additionnel, valeur de 0 à 100.</span>
</label>
<div class="fr-range">
<span class="fr-range__output">50</span>
<input id="range-1817" name="range-1817" type="range" aria-labelledby="range-1817-label" max="100" value="50" disabled aria-describedby="range-1817-messages">
<span class="fr-range__min" aria-hidden="true">0</span>
<span class="fr-range__max" aria-hidden="true">100</span>
</div>
<div class="fr-messages-group" id="range-1817-messages" aria-live="polite">
</div>
</div>


### Curseur avec étape désactivé


Libellé
Texte de description additionnel, valeur de 0 à 100.


50

0
100


###
Extrait de code


<div class="fr-range-group fr-range-group--disabled" id="range-1823-group">
<label class="fr-label">
Libellé
<span class="fr-hint-text">Texte de description additionnel, valeur de 0 à 100.</span>
</label>
<div class="fr-range fr-range--step">
<span class="fr-range__output">50</span>
<input id="range-1822" name="range-1822" type="range" aria-labelledby="range-1822-label" max="100" value="50" step="10" disabled aria-describedby="range-1822-messages">
<span class="fr-range__min" aria-hidden="true">0</span>
<span class="fr-range__max" aria-hidden="true">100</span>
</div>
<div class="fr-messages-group" id="range-1822-messages" aria-live="polite">
</div>
</div>


### Curseur double désactivé


Libellé
Texte de description additionnel, valeur de 0 à 100.


20


0
100


###
Extrait de code


<div class="fr-range-group fr-range-group--disabled" id="range-1828-group">
<label class="fr-label">
Libellé
<span class="fr-hint-text">Texte de description additionnel, valeur de 0 à 100.</span>
</label>
<div class="fr-range fr-range--double">
<span class="fr-range__output">20</span>
<input id="range-1827" name="range-1827" type="range" aria-labelledby="range-1827-label" max="100" value="20" disabled aria-describedby="range-1827-messages">
<input id="range-1827-2" name="range-1827-2" type="range" aria-labelledby="range-1827-label" max="100" value="80" disabled aria-describedby="range-1827-messages">
<span class="fr-range__min" aria-hidden="true">0</span>
<span class="fr-range__max" aria-hidden="true">100</span>
</div>
<div class="fr-messages-group" id="range-1827-messages" aria-live="polite">
</div>
</div>


### Curseur avec erreur


Libellé
Texte de description additionnel, valeur de 0 à 100.


50

0
100


Valeur sélectionnée impossible


###
Extrait de code


<div class="fr-range-group fr-range-group--error" id="range-1833-group">
<label class="fr-label">
Libellé
<span class="fr-hint-text">Texte de description additionnel, valeur de 0 à 100.</span>
</label>
<div class="fr-range">
<span class="fr-range__output">50</span>
<input id="range-1832" name="range-1832" type="range" aria-labelledby="range-1832-label" max="100" value="50" aria-describedby="range-1832-messages">
<span class="fr-range__min" aria-hidden="true">0</span>
<span class="fr-range__max" aria-hidden="true">100</span>
</div>
<div class="fr-messages-group" id="range-1832-messages" aria-live="polite">
<p class="fr-message fr-message--error" id="range-1832-message-error">Valeur sélectionnée impossible</p>
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
