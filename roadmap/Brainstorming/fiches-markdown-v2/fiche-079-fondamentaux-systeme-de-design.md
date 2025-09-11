URL:
https://main--ds-gouv.netlify.app/example/core/link/link-raw

Title:
Fondamentaux - Système de design

Markdown:

Fondamentaux - Système de design


DSFR v1.14.0


[Retour](../)


# Fondamentaux (core)


Le package core est utilisé comme fondation du Design System, il contient plusieurs éléments fondamentaux.


### Typographie


Les typographies Marianne(R) et Spectral sont les typographies officielles de la charte de l'État. Leur usage crée une cohérence entre les interfaces et offre une expérience positive à l'utilisateur. Leur respect renforce également la reconnaissance de la parole de l'État.


### Icônes


Les icônes fonctionnelles sont des symboles visuels qui accompagnent l'utilisateur dans ses actions et qui aident à sa compréhension de l'interface.


### Icônes de favoris - Favicon


L'icône de favoris est un petit icône associé à un site web. Il permet à l'utilisateur de repérer qu'il se trouve sur un site de l'état.


### Medias


Les médias désignent vos contenus photos et vidéos. Lorsqu'ils sont intégré à une page de contenu, il est recommandé de suivre les règles décrites ci-dessous.


### Grille


La grille proposée par le design system vous permet de structurer vos pages et vos contenus simplement.


##### Documentation


-
[Typographie](https://www.systeme-de-design.gouv.fr/elements-d-interface/fondamentaux-de-l-identite-de-l-etat/typographie/)


-
[Icônes](https://www.systeme-de-design.gouv.fr/elements-d-interface/fondamentaux-techniques/icones)


-
[Icônes de favoris - Favicon](https://www.systeme-de-design.gouv.fr/elements-d-interface/fondamentaux-techniques/icone-de-favoris)


-
[Médias fondamentaux](https://www.systeme-de-design.gouv.fr/elements-d-interface/fondamentaux-techniques/medias)


-
[Grille](https://www.systeme-de-design.gouv.fr/elements-d-interface/fondamentaux-techniques/grille-et-points-de-rupture)


## Liens bruts


### Lien brut


Utilisation de la classe fr-raw-link sur les balises de lien pour les afficher de manière brut.


Lorem ipsum dolor sit amet, consectetur adipiscing, [lien interne](../) incididunt, ut labore et dolore magna aliqua. Vitae sapien pellentesque habitant morbi tristique senectus et. Diam maecenas sed enim ut. Accumsan lacus vel facilisis volutpat est. Ut aliquam purus sit amet luctus. Lorem ipsum dolor sit amet consectetur adipiscing elit ut.


###
Extrait de code


<p>Lorem [...] adipiscing, <a class="fr-raw-link" title="titre lien" href="../">lien interne</a> incididunt, [...] elit ut.</p>


### Lien externe brut


Utilisation de la classe fr-raw-link sur les balises de lien pour les afficher de manière brut.


Lorem ipsum dolor sit amet, consectetur adipiscing, [lien externe - nouvelle fenêtre](https://www.systeme-de-design.gouv.fr/) incididunt, ut labore et dolore magna aliqua. Vitae sapien pellentesque habitant morbi tristique senectus et. Diam maecenas sed enim ut. Accumsan lacus vel facilisis volutpat est. Ut aliquam purus sit amet luctus. Lorem ipsum dolor sit amet consectetur adipiscing elit ut.


###
Extrait de code


<p>Lorem [...] adipiscing, <a class="fr-raw-link" href="https://www.systeme-de-design.gouv.fr/" rel="noopener external" target="_blank" title="lien externe - nouvelle fenêtre">lien externe - nouvelle fenêtre</a> incididunt, [...] elit ut.</p>


### Exemple sur plusieurs blocs de texte


Utilisation de la classe fr-raw-link sur un wrapper pour afficher les liens de manière brut.


Lorem ipsum dolor sit amet, consectetur adipiscing, [lien interne](../) incididunt, ut labore et dolore magna aliqua. Vitae sapien pellentesque habitant morbi tristique senectus et. Diam maecenas sed enim ut. Accumsan lacus vel facilisis volutpat est. Ut aliquam purus sit amet luctus. Lorem ipsum dolor sit amet consectetur adipiscing elit ut.


Lorem ipsum dolor sit amet, consectetur adipiscing, [lien externe - nouvelle fenêtre](https://www.systeme-de-design.gouv.fr/) incididunt, ut labore et dolore magna aliqua. Vitae sapien pellentesque habitant morbi tristique senectus et. Diam maecenas sed enim ut. Accumsan lacus vel facilisis volutpat est. Ut aliquam purus sit amet luctus. Lorem ipsum dolor sit amet consectetur adipiscing elit ut.


###
Extrait de code


<div class="fr-raw-link">
<p>Lorem [...] adipiscing, <a title="titre lien" href="../">lien interne</a> incididunt, [...] elit ut.</p>
<p>Lorem [...] adipiscing, <a href="https://www.systeme-de-design.gouv.fr/" rel="noopener external" target="_blank" title="lien externe - nouvelle fenêtre">lien externe - nouvelle fenêtre</a> incididunt, [...] elit ut.</p>
</div>


### Exemple d'utilisation avec une librairie externe


Utilisation de la classe fr-raw-link sur un wrapper pour afficher les liens de manière brut.


Interupteur de la classe
fr-raw-link sur le wrapper


###
Extrait de code


<!-- Based on Leaflet Quick Start Guide [https://leafletjs.com/examples/quick-start/] -->
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=" crossorigin="" />
<script
src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"
integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo="
crossorigin=""
></script>
<div class="fr-raw-link">
<div id="map" class="map"></div>
<div class="fr-toggle">
<input type="checkbox" class="fr-toggle__input" id="fr-raw-link" checked aria-describedby="fr-raw-link-messages">
<label class="fr-toggle__label" for="fr-raw-link" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Interupteur de la classe
<code class="fr-px-1w">fr-raw-link</code>sur le wrapper
</label>
<div class="fr-messages-group" id="fr-raw-link-messages" aria-live="polite">
</div>
</div>
</div>
<style>
.map {
height: 400px;
}

</style>
<script>
const map = L.map('map', {
center: [48.8588897, 2.320041],
zoom: 13,
});
const linkClass = 'fr-raw-link';

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
maxZoom: 19,
attribution:
'(C) <a href="http://www.openstreetmap.org/copyright" target="_blank">OpenStreetMap</a>',
}).addTo(map);

L.popup({ closeButton: false })
.setLatLng([48.8588897, 2.320041])
.setContent('20 avenue de Ségur 75007 Paris')
.openOn(map);

const toggle = document.getElementById(linkClass);
const wrapper = document.getElementById('map').parentNode;

toggle.addEventListener('change', function () {
if (this.checked) {
wrapper.classList.add(linkClass);
} else {
wrapper.classList.remove(linkClass);
}
});
</script>


Libellé bouton


Fermer


##
Paramètres d'affichage


Choisissez un thème pour personnaliser l'apparence du site.


Thème clair


Thème sombre


Système
Utilise les paramètres système
