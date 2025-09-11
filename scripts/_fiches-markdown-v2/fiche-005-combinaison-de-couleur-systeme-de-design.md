URL:
https://main--ds-gouv.netlify.app/example/scheme

Title:
Combinaison de couleur - Système de design

Markdown:

Combinaison de couleur - Système de design


DSFR v1.14.0


[Retour](../)


# Combinaison de couleur (scheme)


scheme permet la définition de couleurs principales et du darkmode pour le Design System de l'Etat.


### Snippet à inclure en premier dans <body></body>


###
Extrait de code


<script type="module">
const e="system",t="dark",c="dark",o="data-fr-theme",a="data-fr-scheme",r=`:root[${o}], :root[${a}]`,m=()=>{document.documentElement.setAttribute(o,c),document.documentElement.style.colorScheme="dark"},n=()=>{window.matchMedia("(prefers-color-scheme: dark)").matches&&m()};(()=>{if(document.documentElement.matches(r)){const c=(()=>{try{return"localStorage"in window&&null!==window.localStorage}catch(e){return!1}})()?localStorage.getItem("scheme"):"",o=document.documentElement.getAttribute(a);switch(!0){case c===t:m();break;case c===e:n();break;case o===t:m();break;case o===e:n()}}})();

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
