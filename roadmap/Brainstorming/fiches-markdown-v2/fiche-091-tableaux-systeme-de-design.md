URL:
https://main--ds-gouv.netlify.app/example/component/table/deprecated

Title:
Tableaux - Système de design

Markdown:

Tableaux - Système de design


DSFR v1.14.0


[Retour](../)


# Tableaux (table)


Les tableaux sont utilisés pour organiser et afficher les informations d'un jeu de données.
[Documentation](https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/tableau)


## Dépréciation


Les exemples suivants sont dépréciés, ne pas utiliser comme référence

Pour support des versions précédentes


### Tableau par défaut


Titre du tableau (caption)


th0
th1
th2
th3
th4
th5


Lorem ipsum dolor sit ame
Lorem ipsum dolor sit ame
Lorem ipsum dolor sit ame
Lorem ipsum dolor sit ame
Lorem ipsum dolor sit ame
Lorem ipsum dolor sit ame


Lorem ipsum dolor sit ame
Lorem ipsum dolor sit ame
Lorem ipsum dolor sit ame
Lorem ipsum dolor sit ame
Lorem ipsum dolor sit ame
Lorem ipsum dolor sit ame


###
Extrait de code


<div class="fr-table" id="table-7000">
<table>
<caption>Titre du tableau (caption)</caption>
<thead>
<tr>
<th scope="col">th0 </th>
<th scope="col">th1 </th>
<th scope="col">th2 </th>
<th scope="col">th3 </th>
<th scope="col">th4 </th>
<th scope="col">th5 </th>
</tr>
</thead>
<tbody>
<tr>
<td>Lorem [...] elit ut.</td>
<td>Lorem [...] elit ut.</td>
<td>Lorem [...] elit ut.</td>
<td>Lorem [...] elit ut.</td>
<td>Lorem [...] elit ut.</td>
<td>Lorem [...] elit ut.</td>
</tr>
<tr>
<td>Lorem [...] elit ut.</td>
<td>Lorem [...] elit ut.</td>
<td>Lorem [...] elit ut.</td>
<td>Lorem [...] elit ut.</td>
<td>Lorem [...] elit ut.</td>
<td>Lorem [...] elit ut.</td>
</tr>
</tbody>
</table>
</div>


### Tableau minimal


Titre du tableau (caption)


th0
th1


Lorem ipsum dolor sit ame
Lorem ipsum dolor sit ame


Lorem ipsum dolor sit ame
Lorem ipsum dolor sit ame


###
Extrait de code


<div class="fr-table" id="table-7003">
<table>
<caption>Titre du tableau (caption)</caption>
<thead>
<tr>
<th scope="col">th0 </th>
<th scope="col">th1 </th>
</tr>
</thead>
<tbody>
<tr>
<td>Lorem [...] elit ut.</td>
<td>Lorem [...] elit ut.</td>
</tr>
<tr>
<td>Lorem [...] elit ut.</td>
<td>Lorem [...] elit ut.</td>
</tr>
</tbody>
</table>
</div>


### Tableau avec bordure


Titre du tableau (caption)


th0
th1
th2
th3
th4
th5


Lorem ipsum dolor sit ame
Lorem ipsum dolor sit ame
Lorem ipsum dolor sit ame
Lorem ipsum dolor sit ame
Lorem ipsum dolor sit ame
Lorem ipsum dolor sit ame


Lorem ipsum dolor sit ame
Lorem ipsum dolor sit ame
Lorem ipsum dolor sit ame
Lorem ipsum dolor sit ame
Lorem ipsum dolor sit ame
Lorem ipsum dolor sit ame


###
Extrait de code


<div class="fr-table fr-table--bordered" id="table-7006">
<table>
<caption>Titre du tableau (caption)</caption>
<thead>
<tr>
<th scope="col">th0 </th>
<th scope="col">th1 </th>
<th scope="col">th2 </th>
<th scope="col">th3 </th>
<th scope="col">th4 </th>
<th scope="col">th5 </th>
</tr>
</thead>
<tbody>
<tr>
<td>Lorem [...] elit ut.</td>
<td>Lorem [...] elit ut.</td>
<td>Lorem [...] elit ut.</td>
<td>Lorem [...] elit ut.</td>
<td>Lorem [...] elit ut.</td>
<td>Lorem [...] elit ut.</td>
</tr>
<tr>
<td>Lorem [...] elit ut.</td>
<td>Lorem [...] elit ut.</td>
<td>Lorem [...] elit ut.</td>
<td>Lorem [...] elit ut.</td>
<td>Lorem [...] elit ut.</td>
<td>Lorem [...] elit ut.</td>
</tr>
</tbody>
</table>
</div>


### Tableau non scrollable


Titre du tableau (caption) non scrollable


th0
th1
th2
th3
th4
th5


Lorem ipsum dolor sit ame
Lorem ipsum dolor sit ame
Lorem ipsum dolor sit ame
Lorem ipsum dolor sit ame
Lorem ipsum dolor sit ame
Lorem ipsum dolor sit ame


###
Extrait de code


<div class="fr-table fr-table--no-scroll" id="table-7009">
<table>
<caption>Titre du tableau (caption) non scrollable</caption>
<thead>
<tr>
<th scope="col">th0 </th>
<th scope="col">th1 </th>
<th scope="col">th2 </th>
<th scope="col">th3 </th>
<th scope="col">th4 </th>
<th scope="col">th5 </th>
</tr>
</thead>
<tbody>
<tr>
<td>Lorem [...] elit ut.</td>
<td>Lorem [...] elit ut.</td>
<td>Lorem [...] elit ut.</td>
<td>Lorem [...] elit ut.</td>
<td>Lorem [...] elit ut.</td>
<td>Lorem [...] elit ut.</td>
</tr>
</tbody>
</table>
</div>


### Tableau colonnes fixées (layout-fixed)


Titre du tableau (caption) fixé


th0
th1
th2


Lorem ipsum dolor sit ame
Lorem ipsum dolor sit ame
Lorem ipsum dolor sit ame


###
Extrait de code


<div class="fr-table fr-table--layout-fixed" id="table-7012">
<table>
<caption>Titre du tableau (caption) fixé</caption>
<thead>
<tr>
<th scope="col">th0 </th>
<th scope="col">th1 </th>
<th scope="col">th2 </th>
</tr>
</thead>
<tbody>
<tr>
<td>Lorem [...] elit ut.</td>
<td>Lorem [...] elit ut.</td>
<td>Lorem [...] elit ut.</td>
</tr>
</tbody>
</table>
</div>


### Tableau avec titre invisible


Titre du tableau (caption) caché


th0
th1
th2
th3
th4
th5


Lorem ipsum dolor sit ame
Lorem ipsum dolor sit ame
Lorem ipsum dolor sit ame
Lorem ipsum dolor sit ame
Lorem ipsum dolor sit ame
Lorem ipsum dolor sit ame


###
Extrait de code


<div class="fr-table fr-table--no-caption" id="table-7015">
<table>
<caption>Titre du tableau (caption) caché</caption>
<thead>
<tr>
<th scope="col">th0 </th>
<th scope="col">th1 </th>
<th scope="col">th2 </th>
<th scope="col">th3 </th>
<th scope="col">th4 </th>
<th scope="col">th5 </th>
</tr>
</thead>
<tbody>
<tr>
<td>Lorem [...] elit ut.</td>
<td>Lorem [...] elit ut.</td>
<td>Lorem [...] elit ut.</td>
<td>Lorem [...] elit ut.</td>
<td>Lorem [...] elit ut.</td>
<td>Lorem [...] elit ut.</td>
</tr>
</tbody>
</table>
</div>


### Tableau avec titre en bas


Titre du tableau (caption) en bas


th0
th1
th2
th3
th4
th5


Lorem ipsum dolor sit ame
Lorem ipsum dolor sit ame
Lorem ipsum dolor sit ame
Lorem ipsum dolor sit ame
Lorem ipsum dolor sit ame
Lorem ipsum dolor sit ame


###
Extrait de code


<div class="fr-table fr-table--caption-bottom" id="table-7018">
<table>
<caption>Titre du tableau (caption) en bas</caption>
<thead>
<tr>
<th scope="col">th0 </th>
<th scope="col">th1 </th>
<th scope="col">th2 </th>
<th scope="col">th3 </th>
<th scope="col">th4 </th>
<th scope="col">th5 </th>
</tr>
</thead>
<tbody>
<tr>
<td>Lorem [...] elit ut.</td>
<td>Lorem [...] elit ut.</td>
<td>Lorem [...] elit ut.</td>
<td>Lorem [...] elit ut.</td>
<td>Lorem [...] elit ut.</td>
<td>Lorem [...] elit ut.</td>
</tr>
</tbody>
</table>
</div>


### Tableau accentué


Titre du tableau (caption)


th0
th1
th2
th3
th4
th5


Lorem ipsum dolor sit ame
Lorem ipsum dolor sit ame
Lorem ipsum dolor sit ame
Lorem ipsum dolor sit ame
Lorem ipsum dolor sit ame
Lorem ipsum dolor sit ame


Lorem ipsum dolor sit ame
Lorem ipsum dolor sit ame
Lorem ipsum dolor sit ame
Lorem ipsum dolor sit ame
Lorem ipsum dolor sit ame
Lorem ipsum dolor sit ame


###
Extrait de code


<div class="fr-table fr-table--green-emeraude" id="table-7021">
<table>
<caption>Titre du tableau (caption)</caption>
<thead>
<tr>
<th scope="col">th0 </th>
<th scope="col">th1 </th>
<th scope="col">th2 </th>
<th scope="col">th3 </th>
<th scope="col">th4 </th>
<th scope="col">th5 </th>
</tr>
</thead>
<tbody>
<tr>
<td>Lorem [...] elit ut.</td>
<td>Lorem [...] elit ut.</td>
<td>Lorem [...] elit ut.</td>
<td>Lorem [...] elit ut.</td>
<td>Lorem [...] elit ut.</td>
<td>Lorem [...] elit ut.</td>
</tr>
<tr>
<td>Lorem [...] elit ut.</td>
<td>Lorem [...] elit ut.</td>
<td>Lorem [...] elit ut.</td>
<td>Lorem [...] elit ut.</td>
<td>Lorem [...] elit ut.</td>
<td>Lorem [...] elit ut.</td>
</tr>
</tbody>
</table>
</div>


### Tableau accentué avec bordure


Titre du tableau (caption)


th0
th1
th2
th3
th4
th5


Lorem ipsum dolor sit ame
Lorem ipsum dolor sit ame
Lorem ipsum dolor sit ame
Lorem ipsum dolor sit ame
Lorem ipsum dolor sit ame
Lorem ipsum dolor sit ame


Lorem ipsum dolor sit ame
Lorem ipsum dolor sit ame
Lorem ipsum dolor sit ame
Lorem ipsum dolor sit ame
Lorem ipsum dolor sit ame
Lorem ipsum dolor sit ame


###
Extrait de code


<div class="fr-table fr-table--green-emeraude fr-table--bordered" id="table-7024">
<table>
<caption>Titre du tableau (caption)</caption>
<thead>
<tr>
<th scope="col">th0 </th>
<th scope="col">th1 </th>
<th scope="col">th2 </th>
<th scope="col">th3 </th>
<th scope="col">th4 </th>
<th scope="col">th5 </th>
</tr>
</thead>
<tbody>
<tr>
<td>Lorem [...] elit ut.</td>
<td>Lorem [...] elit ut.</td>
<td>Lorem [...] elit ut.</td>
<td>Lorem [...] elit ut.</td>
<td>Lorem [...] elit ut.</td>
<td>Lorem [...] elit ut.</td>
</tr>
<tr>
<td>Lorem [...] elit ut.</td>
<td>Lorem [...] elit ut.</td>
<td>Lorem [...] elit ut.</td>
<td>Lorem [...] elit ut.</td>
<td>Lorem [...] elit ut.</td>
<td>Lorem [...] elit ut.</td>
</tr>
</tbody>
</table>
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
