URL:
https://main--ds-gouv.netlify.app/example/component/header

Title:
En-tête - Système de design

Markdown:

En-tête - Système de design


DSFR v1.14.0


[Retour](../)


# En-tête (header)


L'en-tête permet aux utilisateurs d'identifier sur quel site ils se trouvent. Il peut donner accès à la recherche et à certaines pages ou fonctionnalités clés.
[Documentation](https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/en-tete)


#### Header minimal


[Intitulé

officiel](/)


Menu


Fermer


-


-


-


-


###
Extrait de code


<header role="banner" class="fr-header">
<div class="fr-header__body">
<div class="fr-container">
<div class="fr-header__body-row">
<div class="fr-header__brand fr-enlarge-link">
<div class="fr-header__brand-top">
<div class="fr-header__logo">
<a href="/" title="Accueil - Nom de l'entité (ministère, secrétariat d'état, gouvernement)">
<p class="fr-logo">
Intitulé
<br>officiel
</p>
</a>
</div>
<div class="fr-header__navbar">
<button data-fr-opened="false" aria-controls="modal-1845" title="Menu" type="button" id="button-1846" class="fr-btn--menu fr-btn">Menu</button>
</div>
</div>
</div>
</div>
</div>
</div>
<div class="fr-header__menu fr-modal" id="modal-1845" aria-labelledby="button-1846">
<div class="fr-container">
<button aria-controls="modal-1845" title="Fermer" type="button" id="button-1848" class="fr-btn--close fr-btn">Fermer</button>
<div class="fr-header__menu-links">
</div>
<nav class="fr-nav" id="navigation-1849" role="navigation" aria-label="Menu principal">
<ul class="fr-nav__list">
<li class="fr-nav__item">
<a id="nav-1850" type="link" href="#" class="fr-nav__link">accès direct nav-1850</a>
</li>
<li class="fr-nav__item">
<a id="nav-1851" type="link" href="#" class="fr-nav__link">accès direct nav-1851</a>
</li>
<li class="fr-nav__item">
<a id="nav-1852" type="link" href="#" class="fr-nav__link">accès direct nav-1852</a>
</li>
<li class="fr-nav__item">
<a id="nav-1853" type="link" href="#" class="fr-nav__link">accès direct nav-1853</a>
</li>
</ul>
</nav>
</div>
</div>
</header>


#### Header sans navigation


Intitulé

officiel


[Nom du site / service](/)


baseline - précisions sur l'organisation


###
Extrait de code


<header role="banner" class="fr-header">
<div class="fr-header__body">
<div class="fr-container">
<div class="fr-header__body-row">
<div class="fr-header__brand fr-enlarge-link">
<div class="fr-header__brand-top">
<div class="fr-header__logo">
<p class="fr-logo">
Intitulé
<br>officiel
</p>
</div>
</div>
<div class="fr-header__service">
<a href="/" title="Accueil - [À MODIFIER - Nom du site / service] - Nom de l'entité (ministère, secrétariat d'état, gouvernement)">
<p class="fr-header__service-title">
Nom du site / service
</p>
</a>
<p class="fr-header__service-tagline">baseline - précisions sur l'organisation</p>
</div>
</div>
</div>
</div>
</div>
</header>


#### Header sans navigation avec un seul raccourci


Intitulé

officiel


Menu


[Nom du site / service](/)


baseline - précisions sur l'organisation


[Espace particulier](%5Burl%20-%20%C3%A0%20modifier%5D)


Fermer


###
Extrait de code


<header role="banner" class="fr-header">
<div class="fr-header__body">
<div class="fr-container">
<div class="fr-header__body-row">
<div class="fr-header__brand fr-enlarge-link">
<div class="fr-header__brand-top">
<div class="fr-header__logo">
<p class="fr-logo">
Intitulé
<br>officiel
</p>
</div>
<div class="fr-header__navbar">
<button data-fr-opened="false" aria-controls="modal-1859" title="Menu" type="button" id="button-1860" class="fr-btn--menu fr-btn">Menu</button>
</div>
</div>
<div class="fr-header__service">
<a href="/" title="Accueil - [À MODIFIER - Nom du site / service] - Nom de l'entité (ministère, secrétariat d'état, gouvernement)">
<p class="fr-header__service-title">
Nom du site / service
</p>
</a>
<p class="fr-header__service-tagline">baseline - précisions sur l'organisation</p>
</div>
</div>
<div class="fr-header__tools">
<div class="fr-header__tools-links">
<a href="[url - à modifier]" class="fr-btn--account fr-btn fr-btn">Espace particulier</a>
</div>
</div>
</div>
</div>
</div>
<div class="fr-header__menu fr-modal" id="modal-1859" aria-labelledby="button-1860">
<div class="fr-container">
<button aria-controls="modal-1859" title="Fermer" type="button" id="button-1861" class="fr-btn--close fr-btn">Fermer</button>
<div class="fr-header__menu-links">
</div>
</div>
</div>
</header>


#### Header sans navigation avec une liste de raccourcis


Intitulé

officiel


Menu


[Nom du site / service](/)


baseline - précisions sur l'organisation


-
[Contact](%5Burl%20-%20%C3%A0%20modifier%5D)


-
[Espace recruteur](%5Burl%20-%20%C3%A0%20modifier%5D)


-
[Espace particulier](%5Burl%20-%20%C3%A0%20modifier%5D)


Fermer


###
Extrait de code


<header role="banner" class="fr-header">
<div class="fr-header__body">
<div class="fr-container">
<div class="fr-header__body-row">
<div class="fr-header__brand fr-enlarge-link">
<div class="fr-header__brand-top">
<div class="fr-header__logo">
<p class="fr-logo">
Intitulé
<br>officiel
</p>
</div>
<div class="fr-header__navbar">
<button data-fr-opened="false" aria-controls="modal-1866" title="Menu" type="button" id="button-1867" class="fr-btn--menu fr-btn">Menu</button>
</div>
</div>
<div class="fr-header__service">
<a href="/" title="Accueil - [À MODIFIER - Nom du site / service] - Nom de l'entité (ministère, secrétariat d'état, gouvernement)">
<p class="fr-header__service-title">
Nom du site / service
</p>
</a>
<p class="fr-header__service-tagline">baseline - précisions sur l'organisation</p>
</div>
</div>
<div class="fr-header__tools">
<div class="fr-header__tools-links">
<ul class="fr-btns-group">
<li>
<a href="[url - à modifier]" class="fr-btn--team fr-btn">Contact</a>
</li>
<li>
<a href="[url - à modifier]" class="fr-btn--briefcase fr-btn">Espace recruteur</a>
</li>
<li>
<a href="[url - à modifier]" class="fr-btn--account fr-btn">Espace particulier</a>
</li>
</ul>
</div>
</div>
</div>
</div>
</div>
<div class="fr-header__menu fr-modal" id="modal-1866" aria-labelledby="button-1867">
<div class="fr-container">
<button aria-controls="modal-1866" title="Fermer" type="button" id="button-1868" class="fr-btn--close fr-btn">Fermer</button>
<div class="fr-header__menu-links">
</div>
</div>
</div>
</header>


#### Header avec Navigation complète


Intitulé

officiel


Rechercher
Menu


[Nom du site / service](/)


baseline - précisions sur l'organisation


-
[Contact](%5Burl%20-%20%C3%A0%20modifier%5D)


-
[Espace recruteur](%5Burl%20-%20%C3%A0%20modifier%5D)


-
[Espace particulier](%5Burl%20-%20%C3%A0%20modifier%5D)


Fermer


Rechercher


Rechercher


Fermer


-
Entrée menu


-


-


-


-


-


-


-


-


-
Entrée mega menu


Fermer


#####


-


-


-


-


-


-


-


-


#####


-


-


-


-


-


-


-


-


#####


-


-


-


-


-


-


-


-


#####


-


-


-


-


-


-


-


-


-


-
Entrée menu


-


-


-


-


-


-


-


-


-
Entrée mega menu


Fermer


#### Titre éditorialisé


Lorem ipsum dolor sit amet, consectetur adipiscing, incididunt, ut labore et dolore magna aliqua. Vitae sapien pellentesque habitant morbi tristique senectus et. Diam maecenas sed enim ut. Accumsan lacus vel facilisis volutpat est. Ut aliquam purus sit amet luctus. Lorem ipsum dolor sit amet consectetur adipiscing elit ut.
[Voir toute la rubrique](%5Burl%20-%20%C3%A0%20modifier%5D)


#####


-


-


-


-


-


-


-


-


#####


-


-


-


-


-


-


-


-


#####


-


-


-


-


-


-


-


-


#####


-


-


-


-


-


-


-


-


-


-
Entrée mega menu


Fermer


#####


-


-


-


-


-


-


-


-


#####


-


-


-


-


-


-


-


-


#####


-


-


-


-


-


-


-


-


#####


-


-


-


-


-


-


-


-


-
Entrée menu


-


-


-


-


-


-


-


-


###
Extrait de code


<header role="banner" class="fr-header">
<div class="fr-header__body">
<div class="fr-container">
<div class="fr-header__body-row">
<div class="fr-header__brand fr-enlarge-link">
<div class="fr-header__brand-top">
<div class="fr-header__logo">
<p class="fr-logo">
Intitulé
<br>officiel
</p>
</div>
<div class="fr-header__navbar">
<button data-fr-opened="false" aria-controls="modal-2031" title="Rechercher" type="button" id="button-2032" class="fr-btn--search fr-btn">Rechercher</button>
<button data-fr-opened="false" aria-controls="modal-2033" title="Menu" type="button" id="button-2034" class="fr-btn--menu fr-btn">Menu</button>
</div>
</div>
<div class="fr-header__service">
<a href="/" title="Accueil - [À MODIFIER - Nom du site / service] - Nom de l'entité (ministère, secrétariat d'état, gouvernement)">
<p class="fr-header__service-title">
Nom du site / service
</p>
</a>
<p class="fr-header__service-tagline">baseline - précisions sur l'organisation</p>
</div>
</div>
<div class="fr-header__tools">
<div class="fr-header__tools-links">
<ul class="fr-btns-group">
<li>
<a href="[url - à modifier]" class="fr-btn--team fr-btn">Contact</a>
</li>
<li>
<a href="[url - à modifier]" class="fr-btn--briefcase fr-btn">Espace recruteur</a>
</li>
<li>
<a href="[url - à modifier]" class="fr-btn--account fr-btn">Espace particulier</a>
</li>
</ul>
</div>
<div class="fr-header__search fr-modal" id="modal-2031" aria-labelledby="button-2032">
<div class="fr-container fr-container-lg--fluid">
<button aria-controls="modal-2031" title="Fermer" type="button" id="button-2036" class="fr-btn--close fr-btn">Fermer</button>
<div class="fr-search-bar" id="search-2030" role="search">
<label class="fr-label" for="search-2030-input">
Rechercher
</label>
<input class="fr-input" aria-describedby="search-2030-input-messages" placeholder="Rechercher" id="search-2030-input" type="search">
<div class="fr-messages-group" id="search-2030-input-messages" aria-live="polite">
</div>
<button title="Rechercher" type="button" id="search-btn-2038" class="fr-btn">Rechercher</button>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
<div class="fr-header__menu fr-modal" id="modal-2033" aria-labelledby="button-2034">
<div class="fr-container">
<button aria-controls="modal-2033" title="Fermer" type="button" id="button-2039" class="fr-btn--close fr-btn">Fermer</button>
<div class="fr-header__menu-links">
</div>
<nav class="fr-nav" id="navigation-2035" role="navigation" aria-label="Menu principal">
<ul class="fr-nav__list">
<li class="fr-nav__item">
<button id="menu-2040" aria-expanded="false" aria-controls="collapse-2041" type="button" class="fr-nav__btn">Entrée menu</button>
<div class="fr-collapse fr-menu" id="collapse-2041">
<ul class="fr-menu__list">
<li>
<a id="nav-2042" href="#" class="fr-nav__link">Lien de navigation nav-2042</a>
</li>
<li>
<a id="nav-2043" href="#" class="fr-nav__link">Lien de navigation nav-2043</a>
</li>
<li>
<a id="nav-2044" href="#" class="fr-nav__link">Lien de navigation nav-2044</a>
</li>
<li>
<a id="nav-2045" href="#" class="fr-nav__link">Lien de navigation nav-2045</a>
</li>
<li>
<a id="nav-2046" href="#" class="fr-nav__link">Lien de navigation nav-2046</a>
</li>
<li>
<a id="nav-2047" href="#" class="fr-nav__link">Lien de navigation nav-2047</a>
</li>
<li>
<a id="nav-2048" href="#" class="fr-nav__link">Lien de navigation nav-2048</a>
</li>
<li>
<a id="nav-2049" href="#" class="fr-nav__link">Lien de navigation nav-2049</a>
</li>
</ul>
</div>
</li>
<li class="fr-nav__item">
<button id="mega-menu-2050" aria-expanded="false" aria-controls="collapse-2051" type="button" class="fr-nav__btn">Entrée mega menu</button>
<div class="fr-collapse fr-mega-menu" id="collapse-2051">
<div class="fr-container fr-container--fluid fr-container-lg">
<div class="fr-grid-row fr-grid-row-lg--gutters">
<div class="fr-col-12 fr-mb-n3v">
<button aria-controls="collapse-2051" title="Fermer" type="button" id="button-2187" class="fr-btn--close fr-btn">Fermer</button>
</div>
<div class="fr-col-12 fr-col-lg-3">
<h5 class="fr-mega-menu__category">
<a id="category-2052" href="#" class="fr-nav__link">Nom de catégorie</a>
</h5>
<ul class="fr-mega-menu__list">
<li>
<a id="nav-2053" href="#" class="fr-nav__link">Lien de navigation nav-2053</a>
</li>
<li>
<a id="nav-2054" href="#" class="fr-nav__link">Lien de navigation nav-2054</a>
</li>
<li>
<a id="nav-2055" href="#" class="fr-nav__link">Lien de navigation nav-2055</a>
</li>
<li>
<a id="nav-2056" href="#" class="fr-nav__link">Lien de navigation nav-2056</a>
</li>
<li>
<a id="nav-2057" href="#" class="fr-nav__link">Lien de navigation nav-2057</a>
</li>
<li>
<a id="nav-2058" href="#" class="fr-nav__link">Lien de navigation nav-2058</a>
</li>
<li>
<a id="nav-2059" href="#" class="fr-nav__link">Lien de navigation nav-2059</a>
</li>
<li>
<a id="nav-2060" href="#" class="fr-nav__link">Lien de navigation nav-2060</a>
</li>
</ul>
</div>
<div class="fr-col-12 fr-col-lg-3">
<h5 class="fr-mega-menu__category">
<a id="category-2061" href="#" class="fr-nav__link">Nom de catégorie</a>
</h5>
<ul class="fr-mega-menu__list">
<li>
<a id="nav-2062" href="#" class="fr-nav__link">Lien de navigation nav-2062</a>
</li>
<li>
<a id="nav-2063" href="#" class="fr-nav__link">Lien de navigation nav-2063</a>
</li>
<li>
<a id="nav-2064" href="#" class="fr-nav__link">Lien de navigation nav-2064</a>
</li>
<li>
<a id="nav-2065" href="#" class="fr-nav__link">Lien de navigation nav-2065</a>
</li>
<li>
<a id="nav-2066" href="#" class="fr-nav__link">Lien de navigation nav-2066</a>
</li>
<li>
<a id="nav-2067" href="#" class="fr-nav__link">Lien de navigation nav-2067</a>
</li>
<li>
<a id="nav-2068" href="#" class="fr-nav__link">Lien de navigation nav-2068</a>
</li>
<li>
<a id="nav-2069" href="#" class="fr-nav__link">Lien de navigation nav-2069</a>
</li>
</ul>
</div>
<div class="fr-col-12 fr-col-lg-3">
<h5 class="fr-mega-menu__category">
<a id="category-2070" href="#" class="fr-nav__link">Nom de catégorie</a>
</h5>
<ul class="fr-mega-menu__list">
<li>
<a id="nav-2071" href="#" class="fr-nav__link">Lien de navigation nav-2071</a>
</li>
<li>
<a id="nav-2072" href="#" class="fr-nav__link">Lien de navigation nav-2072</a>
</li>
<li>
<a id="nav-2073" aria-current="page" href="#" class="fr-nav__link">Lien de navigation nav-2073</a>
</li>
<li>
<a id="nav-2074" href="#" class="fr-nav__link">Lien de navigation nav-2074</a>
</li>
<li>
<a id="nav-2075" href="#" class="fr-nav__link">Lien de navigation nav-2075</a>
</li>
<li>
<a id="nav-2076" href="#" class="fr-nav__link">Lien de navigation nav-2076</a>
</li>
<li>
<a id="nav-2077" href="#" class="fr-nav__link">Lien de navigation nav-2077</a>
</li>
<li>
<a id="nav-2078" href="#" class="fr-nav__link">Lien de navigation nav-2078</a>
</li>
</ul>
</div>
<div class="fr-col-12 fr-col-lg-3">
<h5 class="fr-mega-menu__category">
<a id="category-2079" href="#" class="fr-nav__link">Nom de catégorie</a>
</h5>
<ul class="fr-mega-menu__list">
<li>
<a id="nav-2080" href="#" class="fr-nav__link">Lien de navigation nav-2080</a>
</li>
<li>
<a id="nav-2081" href="#" class="fr-nav__link">Lien de navigation nav-2081</a>
</li>
<li>
<a id="nav-2082" href="#" class="fr-nav__link">Lien de navigation nav-2082</a>
</li>
<li>
<a id="nav-2083" href="#" class="fr-nav__link">Lien de navigation nav-2083</a>
</li>
<li>
<a id="nav-2084" href="#" class="fr-nav__link">Lien de navigation nav-2084</a>
</li>
<li>
<a id="nav-2085" href="#" class="fr-nav__link">Lien de navigation nav-2085</a>
</li>
<li>
<a id="nav-2086" href="#" class="fr-nav__link">Lien de navigation nav-2086</a>
</li>
<li>
<a id="nav-2087" href="#" class="fr-nav__link">Lien de navigation nav-2087</a>
</li>
</ul>
</div>
</div>
</div>
</div>
</li>
<li class="fr-nav__item">
<a id="nav-2088" type="link" href="#" class="fr-nav__link">accès direct nav-2088</a>
</li>
<li class="fr-nav__item">
<button id="menu-2089" aria-expanded="false" aria-controls="collapse-2090" aria-current="true" type="button" class="fr-nav__btn">Entrée menu</button>
<div class="fr-collapse fr-menu" id="collapse-2090">
<ul class="fr-menu__list">
<li>
<a id="nav-2091" href="#" class="fr-nav__link">Lien de navigation nav-2091</a>
</li>
<li>
<a id="nav-2092" href="#" class="fr-nav__link">Lien de navigation nav-2092</a>
</li>
<li>
<a id="nav-2093" aria-current="page" href="#" class="fr-nav__link">Lien de navigation nav-2093</a>
</li>
<li>
<a id="nav-2094" href="#" class="fr-nav__link">Lien de navigation nav-2094</a>
</li>
<li>
<a id="nav-2095" href="#" class="fr-nav__link">Lien de navigation nav-2095</a>
</li>
<li>
<a id="nav-2096" href="#" class="fr-nav__link">Lien de navigation nav-2096</a>
</li>
<li>
<a id="nav-2097" href="#" class="fr-nav__link">Lien de navigation nav-2097</a>
</li>
<li>
<a id="nav-2098" href="#" class="fr-nav__link">Lien de navigation nav-2098</a>
</li>
</ul>
</div>
</li>
<li class="fr-nav__item">
<button id="mega-menu-2099" aria-expanded="false" aria-controls="collapse-2100" type="button" class="fr-nav__btn">Entrée mega menu</button>
<div class="fr-collapse fr-mega-menu" id="collapse-2100">
<div class="fr-container fr-container--fluid fr-container-lg">
<div class="fr-grid-row fr-grid-row-lg--gutters">
<div class="fr-col-12 fr-mb-n3v">
<button aria-controls="collapse-2100" title="Fermer" type="button" id="button-2188" class="fr-btn--close fr-btn">Fermer</button>
</div>
<div class="fr-col-12 fr-col-lg-8 fr-col-offset-lg-4--right">
<div class="fr-mega-menu__leader">
<h4 class="fr-h4 fr-mb-2v">Titre éditorialisé</h4>
<p class="fr-hidden fr-unhidden-lg">Lorem [...] elit ut.</p>
<a id="link-2101" href="[url - à modifier]" class="fr-link fr-icon-arrow-right-line fr-link--icon-right">Voir toute la rubrique</a>
</div>
</div>
<div class="fr-col-12 fr-col-lg-3">
<h5 class="fr-mega-menu__category">
<a id="category-2102" href="#" class="fr-nav__link">Nom de catégorie</a>
</h5>
<ul class="fr-mega-menu__list">
<li>
<a id="nav-2103" href="#" class="fr-nav__link">Lien de navigation nav-2103</a>
</li>
<li>
<a id="nav-2104" href="#" class="fr-nav__link">Lien de navigation nav-2104</a>
</li>
<li>
<a id="nav-2105" href="#" class="fr-nav__link">Lien de navigation nav-2105</a>
</li>
<li>
<a id="nav-2106" href="#" class="fr-nav__link">Lien de navigation nav-2106</a>
</li>
<li>
<a id="nav-2107" href="#" class="fr-nav__link">Lien de navigation nav-2107</a>
</li>
<li>
<a id="nav-2108" href="#" class="fr-nav__link">Lien de navigation nav-2108</a>
</li>
<li>
<a id="nav-2109" href="#" class="fr-nav__link">Lien de navigation nav-2109</a>
</li>
<li>
<a id="nav-2110" href="#" class="fr-nav__link">Lien de navigation nav-2110</a>
</li>
</ul>
</div>
<div class="fr-col-12 fr-col-lg-3">
<h5 class="fr-mega-menu__category">
<a id="category-2111" href="#" class="fr-nav__link">Nom de catégorie</a>
</h5>
<ul class="fr-mega-menu__list">
<li>
<a id="nav-2112" href="#" class="fr-nav__link">Lien de navigation nav-2112</a>
</li>
<li>
<a id="nav-2113" href="#" class="fr-nav__link">Lien de navigation nav-2113</a>
</li>
<li>
<a id="nav-2114" href="#" class="fr-nav__link">Lien de navigation nav-2114</a>
</li>
<li>
<a id="nav-2115" href="#" class="fr-nav__link">Lien de navigation nav-2115</a>
</li>
<li>
<a id="nav-2116" href="#" class="fr-nav__link">Lien de navigation nav-2116</a>
</li>
<li>
<a id="nav-2117" href="#" class="fr-nav__link">Lien de navigation nav-2117</a>
</li>
<li>
<a id="nav-2118" href="#" class="fr-nav__link">Lien de navigation nav-2118</a>
</li>
<li>
<a id="nav-2119" href="#" class="fr-nav__link">Lien de navigation nav-2119</a>
</li>
</ul>
</div>
<div class="fr-col-12 fr-col-lg-3">
<h5 class="fr-mega-menu__category">
<a id="category-2120" href="#" class="fr-nav__link">Nom de catégorie</a>
</h5>
<ul class="fr-mega-menu__list">
<li>
<a id="nav-2121" href="#" class="fr-nav__link">Lien de navigation nav-2121</a>
</li>
<li>
<a id="nav-2122" href="#" class="fr-nav__link">Lien de navigation nav-2122</a>
</li>
<li>
<a id="nav-2123" aria-current="page" href="#" class="fr-nav__link">Lien de navigation nav-2123</a>
</li>
<li>
<a id="nav-2124" href="#" class="fr-nav__link">Lien de navigation nav-2124</a>
</li>
<li>
<a id="nav-2125" href="#" class="fr-nav__link">Lien de navigation nav-2125</a>
</li>
<li>
<a id="nav-2126" href="#" class="fr-nav__link">Lien de navigation nav-2126</a>
</li>
<li>
<a id="nav-2127" href="#" class="fr-nav__link">Lien de navigation nav-2127</a>
</li>
<li>
<a id="nav-2128" href="#" class="fr-nav__link">Lien de navigation nav-2128</a>
</li>
</ul>
</div>
<div class="fr-col-12 fr-col-lg-3">
<h5 class="fr-mega-menu__category">
<a id="category-2129" href="#" class="fr-nav__link">Nom de catégorie</a>
</h5>
<ul class="fr-mega-menu__list">
<li>
<a id="nav-2130" href="#" class="fr-nav__link">Lien de navigation nav-2130</a>
</li>
<li>
<a id="nav-2131" href="#" class="fr-nav__link">Lien de navigation nav-2131</a>
</li>
<li>
<a id="nav-2132" href="#" class="fr-nav__link">Lien de navigation nav-2132</a>
</li>
<li>
<a id="nav-2133" href="#" class="fr-nav__link">Lien de navigation nav-2133</a>
</li>
<li>
<a id="nav-2134" href="#" class="fr-nav__link">Lien de navigation nav-2134</a>
</li>
<li>
<a id="nav-2135" href="#" class="fr-nav__link">Lien de navigation nav-2135</a>
</li>
<li>
<a id="nav-2136" href="#" class="fr-nav__link">Lien de navigation nav-2136</a>
</li>
<li>
<a id="nav-2137" href="#" class="fr-nav__link">Lien de navigation nav-2137</a>
</li>
</ul>
</div>
</div>
</div>
</div>
</li>
<li class="fr-nav__item">
<a id="nav-2138" type="link" href="#" class="fr-nav__link">accès direct nav-2138</a>
</li>
<li class="fr-nav__item">
<button id="mega-menu-2139" aria-expanded="false" aria-controls="collapse-2140" type="button" class="fr-nav__btn">Entrée mega menu</button>
<div class="fr-collapse fr-mega-menu" id="collapse-2140">
<div class="fr-container fr-container--fluid fr-container-lg">
<div class="fr-grid-row fr-grid-row-lg--gutters">
<div class="fr-col-12 fr-mb-n3v">
<button aria-controls="collapse-2140" title="Fermer" type="button" id="button-2189" class="fr-btn--close fr-btn">Fermer</button>
</div>
<div class="fr-col-12 fr-col-lg-3">
<h5 class="fr-mega-menu__category">
<a id="category-2141" href="#" class="fr-nav__link">Nom de catégorie</a>
</h5>
<ul class="fr-mega-menu__list">
<li>
<a id="nav-2142" href="#" class="fr-nav__link">Lien de navigation nav-2142</a>
</li>
<li>
<a id="nav-2143" href="#" class="fr-nav__link">Lien de navigation nav-2143</a>
</li>
<li>
<a id="nav-2144" href="#" class="fr-nav__link">Lien de navigation nav-2144</a>
</li>
<li>
<a id="nav-2145" href="#" class="fr-nav__link">Lien de navigation nav-2145</a>
</li>
<li>
<a id="nav-2146" href="#" class="fr-nav__link">Lien de navigation nav-2146</a>
</li>
<li>
<a id="nav-2147" href="#" class="fr-nav__link">Lien de navigation nav-2147</a>
</li>
<li>
<a id="nav-2148" href="#" class="fr-nav__link">Lien de navigation nav-2148</a>
</li>
<li>
<a id="nav-2149" href="#" class="fr-nav__link">Lien de navigation nav-2149</a>
</li>
</ul>
</div>
<div class="fr-col-12 fr-col-lg-3">
<h5 class="fr-mega-menu__category">
<a id="category-2150" href="#" class="fr-nav__link">Nom de catégorie</a>
</h5>
<ul class="fr-mega-menu__list">
<li>
<a id="nav-2151" href="#" class="fr-nav__link">Lien de navigation nav-2151</a>
</li>
<li>
<a id="nav-2152" href="#" class="fr-nav__link">Lien de navigation nav-2152</a>
</li>
<li>
<a id="nav-2153" href="#" class="fr-nav__link">Lien de navigation nav-2153</a>
</li>
<li>
<a id="nav-2154" href="#" class="fr-nav__link">Lien de navigation nav-2154</a>
</li>
<li>
<a id="nav-2155" href="#" class="fr-nav__link">Lien de navigation nav-2155</a>
</li>
<li>
<a id="nav-2156" href="#" class="fr-nav__link">Lien de navigation nav-2156</a>
</li>
<li>
<a id="nav-2157" href="#" class="fr-nav__link">Lien de navigation nav-2157</a>
</li>
<li>
<a id="nav-2158" href="#" class="fr-nav__link">Lien de navigation nav-2158</a>
</li>
</ul>
</div>
<div class="fr-col-12 fr-col-lg-3">
<h5 class="fr-mega-menu__category">
<a id="category-2159" href="#" class="fr-nav__link">Nom de catégorie</a>
</h5>
<ul class="fr-mega-menu__list">
<li>
<a id="nav-2160" href="#" class="fr-nav__link">Lien de navigation nav-2160</a>
</li>
<li>
<a id="nav-2161" href="#" class="fr-nav__link">Lien de navigation nav-2161</a>
</li>
<li>
<a id="nav-2162" aria-current="page" href="#" class="fr-nav__link">Lien de navigation nav-2162</a>
</li>
<li>
<a id="nav-2163" href="#" class="fr-nav__link">Lien de navigation nav-2163</a>
</li>
<li>
<a id="nav-2164" href="#" class="fr-nav__link">Lien de navigation nav-2164</a>
</li>
<li>
<a id="nav-2165" href="#" class="fr-nav__link">Lien de navigation nav-2165</a>
</li>
<li>
<a id="nav-2166" href="#" class="fr-nav__link">Lien de navigation nav-2166</a>
</li>
<li>
<a id="nav-2167" href="#" class="fr-nav__link">Lien de navigation nav-2167</a>
</li>
</ul>
</div>
<div class="fr-col-12 fr-col-lg-3">
<h5 class="fr-mega-menu__category">
<a id="category-2168" href="#" class="fr-nav__link">Nom de catégorie</a>
</h5>
<ul class="fr-mega-menu__list">
<li>
<a id="nav-2169" href="#" class="fr-nav__link">Lien de navigation nav-2169</a>
</li>
<li>
<a id="nav-2170" href="#" class="fr-nav__link">Lien de navigation nav-2170</a>
</li>
<li>
<a id="nav-2171" href="#" class="fr-nav__link">Lien de navigation nav-2171</a>
</li>
<li>
<a id="nav-2172" href="#" class="fr-nav__link">Lien de navigation nav-2172</a>
</li>
<li>
<a id="nav-2173" href="#" class="fr-nav__link">Lien de navigation nav-2173</a>
</li>
<li>
<a id="nav-2174" href="#" class="fr-nav__link">Lien de navigation nav-2174</a>
</li>
<li>
<a id="nav-2175" href="#" class="fr-nav__link">Lien de navigation nav-2175</a>
</li>
<li>
<a id="nav-2176" href="#" class="fr-nav__link">Lien de navigation nav-2176</a>
</li>
</ul>
</div>
</div>
</div>
</div>
</li>
<li class="fr-nav__item">
<button id="menu-2177" aria-expanded="false" aria-controls="collapse-2178" type="button" class="fr-nav__btn">Entrée menu</button>
<div class="fr-collapse fr-menu" id="collapse-2178">
<ul class="fr-menu__list">
<li>
<a id="nav-2179" href="#" class="fr-nav__link">Lien de navigation nav-2179</a>
</li>
<li>
<a id="nav-2180" href="#" class="fr-nav__link">Lien de navigation nav-2180</a>
</li>
<li>
<a id="nav-2181" href="#" class="fr-nav__link">Lien de navigation nav-2181</a>
</li>
<li>
<a id="nav-2182" href="#" class="fr-nav__link">Lien de navigation nav-2182</a>
</li>
<li>
<a id="nav-2183" href="#" class="fr-nav__link">Lien de navigation nav-2183</a>
</li>
<li>
<a id="nav-2184" href="#" class="fr-nav__link">Lien de navigation nav-2184</a>
</li>
<li>
<a id="nav-2185" href="#" class="fr-nav__link">Lien de navigation nav-2185</a>
</li>
<li>
<a id="nav-2186" href="#" class="fr-nav__link">Lien de navigation nav-2186</a>
</li>
</ul>
</div>
</li>
</ul>
</nav>
</div>
</div>
</header>


#### Header avec selecteur de langues


Intitulé

officiel


Menu


[Nom du site / service](/)


baseline - précisions sur l'organisation


FR - Français


-
[FR - Français](lang=%22fr%22)


-
[EN - English](lang=%22en%22)


-
[ES - Español](lang=%22es%22)


-
[DE - Deutsch](lang=%22de%22)


-
[TR - Türkçe](lang=%22tr%22)


-
[RO - Română](lang=%22ro%22)


Fermer


-
Entrée menu


-


-


-


-


-


-


-


-


-
Entrée mega menu


Fermer


#####


-


-


-


-


-


-


-


-


#####


-


-


-


-


-


-


-


-


#####


-


-


-


-


-


-


-


-


#####


-


-


-


-


-


-


-


-


-


-
Entrée menu


-


-


-


-


-


-


-


-


-
Entrée mega menu


Fermer


#### Titre éditorialisé


Lorem ipsum dolor sit amet, consectetur adipiscing, incididunt, ut labore et dolore magna aliqua. Vitae sapien pellentesque habitant morbi tristique senectus et. Diam maecenas sed enim ut. Accumsan lacus vel facilisis volutpat est. Ut aliquam purus sit amet luctus. Lorem ipsum dolor sit amet consectetur adipiscing elit ut.
[Voir toute la rubrique](%5Burl%20-%20%C3%A0%20modifier%5D)


#####


-


-


-


-


-


-


-


-


#####


-


-


-


-


-


-


-


-


#####


-


-


-


-


-


-


-


-


#####


-


-


-


-


-


-


-


-


-


-
Entrée mega menu


Fermer


#####


-


-


-


-


-


-


-


-


#####


-


-


-


-


-


-


-


-


#####


-


-


-


-


-


-


-


-


#####


-


-


-


-


-


-


-


-


-
Entrée menu


-


-


-


-


-


-


-


-


###
Extrait de code


<header role="banner" class="fr-header">
<div class="fr-header__body">
<div class="fr-container">
<div class="fr-header__body-row">
<div class="fr-header__brand fr-enlarge-link">
<div class="fr-header__brand-top">
<div class="fr-header__logo">
<p class="fr-logo">
Intitulé
<br>officiel
</p>
</div>
<div class="fr-header__navbar">
<button data-fr-opened="false" aria-controls="modal-2354" title="Menu" type="button" id="button-2355" class="fr-btn--menu fr-btn">Menu</button>
</div>
</div>
<div class="fr-header__service">
<a href="/" title="Accueil - [À MODIFIER - Nom du site / service] - Nom de l'entité (ministère, secrétariat d'état, gouvernement)">
<p class="fr-header__service-title">
Nom du site / service
</p>
</a>
<p class="fr-header__service-tagline">baseline - précisions sur l'organisation</p>
</div>
</div>
<div class="fr-header__tools">
<div class="fr-header__tools-links">
<nav role="navigation" class="fr-translate fr-nav" id="translate-2357">
<div class="fr-nav__item">
<button aria-controls="translate-2353" aria-expanded="false" type="button" class="fr-translate__btn fr-btn">FR<span class="fr-hidden-lg"> - Français</span>
</button>
<div class="fr-collapse fr-translate__menu fr-menu" id="translate-2353">
<ul class="fr-menu__list">
<li>
<a class="fr-translate__language fr-nav__link" hreflang="fr" lang="fr" href="/fr/" id="language-2358" aria-current="true">FR - Français</a>
</li>
<li>
<a class="fr-translate__language fr-nav__link" hreflang="en" lang="en" href="/en/" id="language-2359">EN - English</a>
</li>
<li>
<a class="fr-translate__language fr-nav__link" hreflang="es" lang="es" href="/es/" id="language-2360">ES - Español</a>
</li>
<li>
<a class="fr-translate__language fr-nav__link" hreflang="de" lang="de" href="/de/" id="language-2361">DE - Deutsch</a>
</li>
<li>
<a class="fr-translate__language fr-nav__link" hreflang="tr" lang="tr" href="/tr/" id="language-2362">TR - Türkçe</a>
</li>
<li>
<a class="fr-translate__language fr-nav__link" hreflang="ro" lang="ro" href="/ro/" id="language-2363">RO - Română</a>
</li>
</ul>
</div>
</div>
</nav>
</div>
</div>
</div>
</div>
</div>
<div class="fr-header__menu fr-modal" id="modal-2354" aria-labelledby="button-2355">
<div class="fr-container">
<button aria-controls="modal-2354" title="Fermer" type="button" id="button-2364" class="fr-btn--close fr-btn">Fermer</button>
<div class="fr-header__menu-links">
</div>
<nav class="fr-nav" id="navigation-2356" role="navigation" aria-label="Menu principal">
<ul class="fr-nav__list">
<li class="fr-nav__item">
<button id="menu-2365" aria-expanded="false" aria-controls="collapse-2366" type="button" class="fr-nav__btn">Entrée menu</button>
<div class="fr-collapse fr-menu" id="collapse-2366">
<ul class="fr-menu__list">
<li>
<a id="nav-2367" href="#" class="fr-nav__link">Lien de navigation nav-2367</a>
</li>
<li>
<a id="nav-2368" href="#" class="fr-nav__link">Lien de navigation nav-2368</a>
</li>
<li>
<a id="nav-2369" href="#" class="fr-nav__link">Lien de navigation nav-2369</a>
</li>
<li>
<a id="nav-2370" href="#" class="fr-nav__link">Lien de navigation nav-2370</a>
</li>
<li>
<a id="nav-2371" href="#" class="fr-nav__link">Lien de navigation nav-2371</a>
</li>
<li>
<a id="nav-2372" href="#" class="fr-nav__link">Lien de navigation nav-2372</a>
</li>
<li>
<a id="nav-2373" href="#" class="fr-nav__link">Lien de navigation nav-2373</a>
</li>
<li>
<a id="nav-2374" href="#" class="fr-nav__link">Lien de navigation nav-2374</a>
</li>
</ul>
</div>
</li>
<li class="fr-nav__item">
<button id="mega-menu-2375" aria-expanded="false" aria-controls="collapse-2376" type="button" class="fr-nav__btn">Entrée mega menu</button>
<div class="fr-collapse fr-mega-menu" id="collapse-2376">
<div class="fr-container fr-container--fluid fr-container-lg">
<div class="fr-grid-row fr-grid-row-lg--gutters">
<div class="fr-col-12 fr-mb-n3v">
<button aria-controls="collapse-2376" title="Fermer" type="button" id="button-2512" class="fr-btn--close fr-btn">Fermer</button>
</div>
<div class="fr-col-12 fr-col-lg-3">
<h5 class="fr-mega-menu__category">
<a id="category-2377" href="#" class="fr-nav__link">Nom de catégorie</a>
</h5>
<ul class="fr-mega-menu__list">
<li>
<a id="nav-2378" href="#" class="fr-nav__link">Lien de navigation nav-2378</a>
</li>
<li>
<a id="nav-2379" href="#" class="fr-nav__link">Lien de navigation nav-2379</a>
</li>
<li>
<a id="nav-2380" href="#" class="fr-nav__link">Lien de navigation nav-2380</a>
</li>
<li>
<a id="nav-2381" href="#" class="fr-nav__link">Lien de navigation nav-2381</a>
</li>
<li>
<a id="nav-2382" href="#" class="fr-nav__link">Lien de navigation nav-2382</a>
</li>
<li>
<a id="nav-2383" href="#" class="fr-nav__link">Lien de navigation nav-2383</a>
</li>
<li>
<a id="nav-2384" href="#" class="fr-nav__link">Lien de navigation nav-2384</a>
</li>
<li>
<a id="nav-2385" href="#" class="fr-nav__link">Lien de navigation nav-2385</a>
</li>
</ul>
</div>
<div class="fr-col-12 fr-col-lg-3">
<h5 class="fr-mega-menu__category">
<a id="category-2386" href="#" class="fr-nav__link">Nom de catégorie</a>
</h5>
<ul class="fr-mega-menu__list">
<li>
<a id="nav-2387" href="#" class="fr-nav__link">Lien de navigation nav-2387</a>
</li>
<li>
<a id="nav-2388" href="#" class="fr-nav__link">Lien de navigation nav-2388</a>
</li>
<li>
<a id="nav-2389" href="#" class="fr-nav__link">Lien de navigation nav-2389</a>
</li>
<li>
<a id="nav-2390" href="#" class="fr-nav__link">Lien de navigation nav-2390</a>
</li>
<li>
<a id="nav-2391" href="#" class="fr-nav__link">Lien de navigation nav-2391</a>
</li>
<li>
<a id="nav-2392" href="#" class="fr-nav__link">Lien de navigation nav-2392</a>
</li>
<li>
<a id="nav-2393" href="#" class="fr-nav__link">Lien de navigation nav-2393</a>
</li>
<li>
<a id="nav-2394" href="#" class="fr-nav__link">Lien de navigation nav-2394</a>
</li>
</ul>
</div>
<div class="fr-col-12 fr-col-lg-3">
<h5 class="fr-mega-menu__category">
<a id="category-2395" href="#" class="fr-nav__link">Nom de catégorie</a>
</h5>
<ul class="fr-mega-menu__list">
<li>
<a id="nav-2396" href="#" class="fr-nav__link">Lien de navigation nav-2396</a>
</li>
<li>
<a id="nav-2397" href="#" class="fr-nav__link">Lien de navigation nav-2397</a>
</li>
<li>
<a id="nav-2398" aria-current="page" href="#" class="fr-nav__link">Lien de navigation nav-2398</a>
</li>
<li>
<a id="nav-2399" href="#" class="fr-nav__link">Lien de navigation nav-2399</a>
</li>
<li>
<a id="nav-2400" href="#" class="fr-nav__link">Lien de navigation nav-2400</a>
</li>
<li>
<a id="nav-2401" href="#" class="fr-nav__link">Lien de navigation nav-2401</a>
</li>
<li>
<a id="nav-2402" href="#" class="fr-nav__link">Lien de navigation nav-2402</a>
</li>
<li>
<a id="nav-2403" href="#" class="fr-nav__link">Lien de navigation nav-2403</a>
</li>
</ul>
</div>
<div class="fr-col-12 fr-col-lg-3">
<h5 class="fr-mega-menu__category">
<a id="category-2404" href="#" class="fr-nav__link">Nom de catégorie</a>
</h5>
<ul class="fr-mega-menu__list">
<li>
<a id="nav-2405" href="#" class="fr-nav__link">Lien de navigation nav-2405</a>
</li>
<li>
<a id="nav-2406" href="#" class="fr-nav__link">Lien de navigation nav-2406</a>
</li>
<li>
<a id="nav-2407" href="#" class="fr-nav__link">Lien de navigation nav-2407</a>
</li>
<li>
<a id="nav-2408" href="#" class="fr-nav__link">Lien de navigation nav-2408</a>
</li>
<li>
<a id="nav-2409" href="#" class="fr-nav__link">Lien de navigation nav-2409</a>
</li>
<li>
<a id="nav-2410" href="#" class="fr-nav__link">Lien de navigation nav-2410</a>
</li>
<li>
<a id="nav-2411" href="#" class="fr-nav__link">Lien de navigation nav-2411</a>
</li>
<li>
<a id="nav-2412" href="#" class="fr-nav__link">Lien de navigation nav-2412</a>
</li>
</ul>
</div>
</div>
</div>
</div>
</li>
<li class="fr-nav__item">
<a id="nav-2413" type="link" href="#" class="fr-nav__link">accès direct nav-2413</a>
</li>
<li class="fr-nav__item">
<button id="menu-2414" aria-expanded="false" aria-controls="collapse-2415" aria-current="true" type="button" class="fr-nav__btn">Entrée menu</button>
<div class="fr-collapse fr-menu" id="collapse-2415">
<ul class="fr-menu__list">
<li>
<a id="nav-2416" href="#" class="fr-nav__link">Lien de navigation nav-2416</a>
</li>
<li>
<a id="nav-2417" href="#" class="fr-nav__link">Lien de navigation nav-2417</a>
</li>
<li>
<a id="nav-2418" aria-current="page" href="#" class="fr-nav__link">Lien de navigation nav-2418</a>
</li>
<li>
<a id="nav-2419" href="#" class="fr-nav__link">Lien de navigation nav-2419</a>
</li>
<li>
<a id="nav-2420" href="#" class="fr-nav__link">Lien de navigation nav-2420</a>
</li>
<li>
<a id="nav-2421" href="#" class="fr-nav__link">Lien de navigation nav-2421</a>
</li>
<li>
<a id="nav-2422" href="#" class="fr-nav__link">Lien de navigation nav-2422</a>
</li>
<li>
<a id="nav-2423" href="#" class="fr-nav__link">Lien de navigation nav-2423</a>
</li>
</ul>
</div>
</li>
<li class="fr-nav__item">
<button id="mega-menu-2424" aria-expanded="false" aria-controls="collapse-2425" type="button" class="fr-nav__btn">Entrée mega menu</button>
<div class="fr-collapse fr-mega-menu" id="collapse-2425">
<div class="fr-container fr-container--fluid fr-container-lg">
<div class="fr-grid-row fr-grid-row-lg--gutters">
<div class="fr-col-12 fr-mb-n3v">
<button aria-controls="collapse-2425" title="Fermer" type="button" id="button-2513" class="fr-btn--close fr-btn">Fermer</button>
</div>
<div class="fr-col-12 fr-col-lg-8 fr-col-offset-lg-4--right">
<div class="fr-mega-menu__leader">
<h4 class="fr-h4 fr-mb-2v">Titre éditorialisé</h4>
<p class="fr-hidden fr-unhidden-lg">Lorem [...] elit ut.</p>
<a id="link-2426" href="[url - à modifier]" class="fr-link fr-icon-arrow-right-line fr-link--icon-right">Voir toute la rubrique</a>
</div>
</div>
<div class="fr-col-12 fr-col-lg-3">
<h5 class="fr-mega-menu__category">
<a id="category-2427" href="#" class="fr-nav__link">Nom de catégorie</a>
</h5>
<ul class="fr-mega-menu__list">
<li>
<a id="nav-2428" href="#" class="fr-nav__link">Lien de navigation nav-2428</a>
</li>
<li>
<a id="nav-2429" href="#" class="fr-nav__link">Lien de navigation nav-2429</a>
</li>
<li>
<a id="nav-2430" href="#" class="fr-nav__link">Lien de navigation nav-2430</a>
</li>
<li>
<a id="nav-2431" href="#" class="fr-nav__link">Lien de navigation nav-2431</a>
</li>
<li>
<a id="nav-2432" href="#" class="fr-nav__link">Lien de navigation nav-2432</a>
</li>
<li>
<a id="nav-2433" href="#" class="fr-nav__link">Lien de navigation nav-2433</a>
</li>
<li>
<a id="nav-2434" href="#" class="fr-nav__link">Lien de navigation nav-2434</a>
</li>
<li>
<a id="nav-2435" href="#" class="fr-nav__link">Lien de navigation nav-2435</a>
</li>
</ul>
</div>
<div class="fr-col-12 fr-col-lg-3">
<h5 class="fr-mega-menu__category">
<a id="category-2436" href="#" class="fr-nav__link">Nom de catégorie</a>
</h5>
<ul class="fr-mega-menu__list">
<li>
<a id="nav-2437" href="#" class="fr-nav__link">Lien de navigation nav-2437</a>
</li>
<li>
<a id="nav-2438" href="#" class="fr-nav__link">Lien de navigation nav-2438</a>
</li>
<li>
<a id="nav-2439" href="#" class="fr-nav__link">Lien de navigation nav-2439</a>
</li>
<li>
<a id="nav-2440" href="#" class="fr-nav__link">Lien de navigation nav-2440</a>
</li>
<li>
<a id="nav-2441" href="#" class="fr-nav__link">Lien de navigation nav-2441</a>
</li>
<li>
<a id="nav-2442" href="#" class="fr-nav__link">Lien de navigation nav-2442</a>
</li>
<li>
<a id="nav-2443" href="#" class="fr-nav__link">Lien de navigation nav-2443</a>
</li>
<li>
<a id="nav-2444" href="#" class="fr-nav__link">Lien de navigation nav-2444</a>
</li>
</ul>
</div>
<div class="fr-col-12 fr-col-lg-3">
<h5 class="fr-mega-menu__category">
<a id="category-2445" href="#" class="fr-nav__link">Nom de catégorie</a>
</h5>
<ul class="fr-mega-menu__list">
<li>
<a id="nav-2446" href="#" class="fr-nav__link">Lien de navigation nav-2446</a>
</li>
<li>
<a id="nav-2447" href="#" class="fr-nav__link">Lien de navigation nav-2447</a>
</li>
<li>
<a id="nav-2448" aria-current="page" href="#" class="fr-nav__link">Lien de navigation nav-2448</a>
</li>
<li>
<a id="nav-2449" href="#" class="fr-nav__link">Lien de navigation nav-2449</a>
</li>
<li>
<a id="nav-2450" href="#" class="fr-nav__link">Lien de navigation nav-2450</a>
</li>
<li>
<a id="nav-2451" href="#" class="fr-nav__link">Lien de navigation nav-2451</a>
</li>
<li>
<a id="nav-2452" href="#" class="fr-nav__link">Lien de navigation nav-2452</a>
</li>
<li>
<a id="nav-2453" href="#" class="fr-nav__link">Lien de navigation nav-2453</a>
</li>
</ul>
</div>
<div class="fr-col-12 fr-col-lg-3">
<h5 class="fr-mega-menu__category">
<a id="category-2454" href="#" class="fr-nav__link">Nom de catégorie</a>
</h5>
<ul class="fr-mega-menu__list">
<li>
<a id="nav-2455" href="#" class="fr-nav__link">Lien de navigation nav-2455</a>
</li>
<li>
<a id="nav-2456" href="#" class="fr-nav__link">Lien de navigation nav-2456</a>
</li>
<li>
<a id="nav-2457" href="#" class="fr-nav__link">Lien de navigation nav-2457</a>
</li>
<li>
<a id="nav-2458" href="#" class="fr-nav__link">Lien de navigation nav-2458</a>
</li>
<li>
<a id="nav-2459" href="#" class="fr-nav__link">Lien de navigation nav-2459</a>
</li>
<li>
<a id="nav-2460" href="#" class="fr-nav__link">Lien de navigation nav-2460</a>
</li>
<li>
<a id="nav-2461" href="#" class="fr-nav__link">Lien de navigation nav-2461</a>
</li>
<li>
<a id="nav-2462" href="#" class="fr-nav__link">Lien de navigation nav-2462</a>
</li>
</ul>
</div>
</div>
</div>
</div>
</li>
<li class="fr-nav__item">
<a id="nav-2463" type="link" href="#" class="fr-nav__link">accès direct nav-2463</a>
</li>
<li class="fr-nav__item">
<button id="mega-menu-2464" aria-expanded="false" aria-controls="collapse-2465" type="button" class="fr-nav__btn">Entrée mega menu</button>
<div class="fr-collapse fr-mega-menu" id="collapse-2465">
<div class="fr-container fr-container--fluid fr-container-lg">
<div class="fr-grid-row fr-grid-row-lg--gutters">
<div class="fr-col-12 fr-mb-n3v">
<button aria-controls="collapse-2465" title="Fermer" type="button" id="button-2514" class="fr-btn--close fr-btn">Fermer</button>
</div>
<div class="fr-col-12 fr-col-lg-3">
<h5 class="fr-mega-menu__category">
<a id="category-2466" href="#" class="fr-nav__link">Nom de catégorie</a>
</h5>
<ul class="fr-mega-menu__list">
<li>
<a id="nav-2467" href="#" class="fr-nav__link">Lien de navigation nav-2467</a>
</li>
<li>
<a id="nav-2468" href="#" class="fr-nav__link">Lien de navigation nav-2468</a>
</li>
<li>
<a id="nav-2469" href="#" class="fr-nav__link">Lien de navigation nav-2469</a>
</li>
<li>
<a id="nav-2470" href="#" class="fr-nav__link">Lien de navigation nav-2470</a>
</li>
<li>
<a id="nav-2471" href="#" class="fr-nav__link">Lien de navigation nav-2471</a>
</li>
<li>
<a id="nav-2472" href="#" class="fr-nav__link">Lien de navigation nav-2472</a>
</li>
<li>
<a id="nav-2473" href="#" class="fr-nav__link">Lien de navigation nav-2473</a>
</li>
<li>
<a id="nav-2474" href="#" class="fr-nav__link">Lien de navigation nav-2474</a>
</li>
</ul>
</div>
<div class="fr-col-12 fr-col-lg-3">
<h5 class="fr-mega-menu__category">
<a id="category-2475" href="#" class="fr-nav__link">Nom de catégorie</a>
</h5>
<ul class="fr-mega-menu__list">
<li>
<a id="nav-2476" href="#" class="fr-nav__link">Lien de navigation nav-2476</a>
</li>
<li>
<a id="nav-2477" href="#" class="fr-nav__link">Lien de navigation nav-2477</a>
</li>
<li>
<a id="nav-2478" href="#" class="fr-nav__link">Lien de navigation nav-2478</a>
</li>
<li>
<a id="nav-2479" href="#" class="fr-nav__link">Lien de navigation nav-2479</a>
</li>
<li>
<a id="nav-2480" href="#" class="fr-nav__link">Lien de navigation nav-2480</a>
</li>
<li>
<a id="nav-2481" href="#" class="fr-nav__link">Lien de navigation nav-2481</a>
</li>
<li>
<a id="nav-2482" href="#" class="fr-nav__link">Lien de navigation nav-2482</a>
</li>
<li>
<a id="nav-2483" href="#" class="fr-nav__link">Lien de navigation nav-2483</a>
</li>
</ul>
</div>
<div class="fr-col-12 fr-col-lg-3">
<h5 class="fr-mega-menu__category">
<a id="category-2484" href="#" class="fr-nav__link">Nom de catégorie</a>
</h5>
<ul class="fr-mega-menu__list">
<li>
<a id="nav-2485" href="#" class="fr-nav__link">Lien de navigation nav-2485</a>
</li>
<li>
<a id="nav-2486" href="#" class="fr-nav__link">Lien de navigation nav-2486</a>
</li>
<li>
<a id="nav-2487" aria-current="page" href="#" class="fr-nav__link">Lien de navigation nav-2487</a>
</li>
<li>
<a id="nav-2488" href="#" class="fr-nav__link">Lien de navigation nav-2488</a>
</li>
<li>
<a id="nav-2489" href="#" class="fr-nav__link">Lien de navigation nav-2489</a>
</li>
<li>
<a id="nav-2490" href="#" class="fr-nav__link">Lien de navigation nav-2490</a>
</li>
<li>
<a id="nav-2491" href="#" class="fr-nav__link">Lien de navigation nav-2491</a>
</li>
<li>
<a id="nav-2492" href="#" class="fr-nav__link">Lien de navigation nav-2492</a>
</li>
</ul>
</div>
<div class="fr-col-12 fr-col-lg-3">
<h5 class="fr-mega-menu__category">
<a id="category-2493" href="#" class="fr-nav__link">Nom de catégorie</a>
</h5>
<ul class="fr-mega-menu__list">
<li>
<a id="nav-2494" href="#" class="fr-nav__link">Lien de navigation nav-2494</a>
</li>
<li>
<a id="nav-2495" href="#" class="fr-nav__link">Lien de navigation nav-2495</a>
</li>
<li>
<a id="nav-2496" href="#" class="fr-nav__link">Lien de navigation nav-2496</a>
</li>
<li>
<a id="nav-2497" href="#" class="fr-nav__link">Lien de navigation nav-2497</a>
</li>
<li>
<a id="nav-2498" href="#" class="fr-nav__link">Lien de navigation nav-2498</a>
</li>
<li>
<a id="nav-2499" href="#" class="fr-nav__link">Lien de navigation nav-2499</a>
</li>
<li>
<a id="nav-2500" href="#" class="fr-nav__link">Lien de navigation nav-2500</a>
</li>
<li>
<a id="nav-2501" href="#" class="fr-nav__link">Lien de navigation nav-2501</a>
</li>
</ul>
</div>
</div>
</div>
</div>
</li>
<li class="fr-nav__item">
<button id="menu-2502" aria-expanded="false" aria-controls="collapse-2503" type="button" class="fr-nav__btn">Entrée menu</button>
<div class="fr-collapse fr-menu" id="collapse-2503">
<ul class="fr-menu__list">
<li>
<a id="nav-2504" href="#" class="fr-nav__link">Lien de navigation nav-2504</a>
</li>
<li>
<a id="nav-2505" href="#" class="fr-nav__link">Lien de navigation nav-2505</a>
</li>
<li>
<a id="nav-2506" href="#" class="fr-nav__link">Lien de navigation nav-2506</a>
</li>
<li>
<a id="nav-2507" href="#" class="fr-nav__link">Lien de navigation nav-2507</a>
</li>
<li>
<a id="nav-2508" href="#" class="fr-nav__link">Lien de navigation nav-2508</a>
</li>
<li>
<a id="nav-2509" href="#" class="fr-nav__link">Lien de navigation nav-2509</a>
</li>
<li>
<a id="nav-2510" href="#" class="fr-nav__link">Lien de navigation nav-2510</a>
</li>
<li>
<a id="nav-2511" href="#" class="fr-nav__link">Lien de navigation nav-2511</a>
</li>
</ul>
</div>
</li>
</ul>
</nav>
</div>
</div>
</header>


#### Header avec selecteur de langues et raccourcis


Intitulé

officiel


Menu


[Nom du site / service](/)


baseline - précisions sur l'organisation


-
[Contact](%5Burl%20-%20%C3%A0%20modifier%5D)


-
[Espace recruteur](%5Burl%20-%20%C3%A0%20modifier%5D)


FR - Français


-
[FR - Français](lang=%22fr%22)


-
[EN - English](lang=%22en%22)


-
[ES - Español](lang=%22es%22)


-
[DE - Deutsch](lang=%22de%22)


-
[TR - Türkçe](lang=%22tr%22)


-
[RO - Română](lang=%22ro%22)


Fermer


-
Entrée menu


-


-


-


-


-


-


-


-


-
Entrée mega menu


Fermer


#####


-


-


-


-


-


-


-


-


#####


-


-


-


-


-


-


-


-


#####


-


-


-


-


-


-


-


-


#####


-


-


-


-


-


-


-


-


-


-
Entrée menu


-


-


-


-


-


-


-


-


-
Entrée mega menu


Fermer


#### Titre éditorialisé


Lorem ipsum dolor sit amet, consectetur adipiscing, incididunt, ut labore et dolore magna aliqua. Vitae sapien pellentesque habitant morbi tristique senectus et. Diam maecenas sed enim ut. Accumsan lacus vel facilisis volutpat est. Ut aliquam purus sit amet luctus. Lorem ipsum dolor sit amet consectetur adipiscing elit ut.
[Voir toute la rubrique](%5Burl%20-%20%C3%A0%20modifier%5D)


#####


-


-


-


-


-


-


-


-


#####


-


-


-


-


-


-


-


-


#####


-


-


-


-


-


-


-


-


#####


-


-


-


-


-


-


-


-


-


-
Entrée mega menu


Fermer


#####


-


-


-


-


-


-


-


-


#####


-


-


-


-


-


-


-


-


#####


-


-


-


-


-


-


-


-


#####


-


-


-


-


-


-


-


-


-
Entrée menu


-


-


-


-


-


-


-


-


###
Extrait de code


<header role="banner" class="fr-header">
<div class="fr-header__body">
<div class="fr-container">
<div class="fr-header__body-row">
<div class="fr-header__brand fr-enlarge-link">
<div class="fr-header__brand-top">
<div class="fr-header__logo">
<p class="fr-logo">
Intitulé
<br>officiel
</p>
</div>
<div class="fr-header__navbar">
<button data-fr-opened="false" aria-controls="modal-2679" title="Menu" type="button" id="button-2680" class="fr-btn--menu fr-btn">Menu</button>
</div>
</div>
<div class="fr-header__service">
<a href="/" title="Accueil - [À MODIFIER - Nom du site / service] - Nom de l'entité (ministère, secrétariat d'état, gouvernement)">
<p class="fr-header__service-title">
Nom du site / service
</p>
</a>
<p class="fr-header__service-tagline">baseline - précisions sur l'organisation</p>
</div>
</div>
<div class="fr-header__tools">
<div class="fr-header__tools-links">
<ul class="fr-btns-group">
<li>
<a href="[url - à modifier]" class="fr-btn--team fr-btn fr-btn">Contact</a>
</li>
<li>
<a href="[url - à modifier]" class="fr-btn--briefcase fr-btn fr-btn">Espace recruteur</a>
</li>
</ul>
<nav role="navigation" class="fr-translate fr-nav" id="translate-2682">
<div class="fr-nav__item">
<button aria-controls="translate-2678" aria-expanded="false" type="button" class="fr-translate__btn fr-btn">FR<span class="fr-hidden-lg"> - Français</span>
</button>
<div class="fr-collapse fr-translate__menu fr-menu" id="translate-2678">
<ul class="fr-menu__list">
<li>
<a class="fr-translate__language fr-nav__link" hreflang="fr" lang="fr" href="/fr/" id="language-2683" aria-current="true">FR - Français</a>
</li>
<li>
<a class="fr-translate__language fr-nav__link" hreflang="en" lang="en" href="/en/" id="language-2684">EN - English</a>
</li>
<li>
<a class="fr-translate__language fr-nav__link" hreflang="es" lang="es" href="/es/" id="language-2685">ES - Español</a>
</li>
<li>
<a class="fr-translate__language fr-nav__link" hreflang="de" lang="de" href="/de/" id="language-2686">DE - Deutsch</a>
</li>
<li>
<a class="fr-translate__language fr-nav__link" hreflang="tr" lang="tr" href="/tr/" id="language-2687">TR - Türkçe</a>
</li>
<li>
<a class="fr-translate__language fr-nav__link" hreflang="ro" lang="ro" href="/ro/" id="language-2688">RO - Română</a>
</li>
</ul>
</div>
</div>
</nav>
</div>
</div>
</div>
</div>
</div>
<div class="fr-header__menu fr-modal" id="modal-2679" aria-labelledby="button-2680">
<div class="fr-container">
<button aria-controls="modal-2679" title="Fermer" type="button" id="button-2689" class="fr-btn--close fr-btn">Fermer</button>
<div class="fr-header__menu-links">
</div>
<nav class="fr-nav" id="navigation-2681" role="navigation" aria-label="Menu principal">
<ul class="fr-nav__list">
<li class="fr-nav__item">
<button id="menu-2690" aria-expanded="false" aria-controls="collapse-2691" type="button" class="fr-nav__btn">Entrée menu</button>
<div class="fr-collapse fr-menu" id="collapse-2691">
<ul class="fr-menu__list">
<li>
<a id="nav-2692" href="#" class="fr-nav__link">Lien de navigation nav-2692</a>
</li>
<li>
<a id="nav-2693" href="#" class="fr-nav__link">Lien de navigation nav-2693</a>
</li>
<li>
<a id="nav-2694" href="#" class="fr-nav__link">Lien de navigation nav-2694</a>
</li>
<li>
<a id="nav-2695" href="#" class="fr-nav__link">Lien de navigation nav-2695</a>
</li>
<li>
<a id="nav-2696" href="#" class="fr-nav__link">Lien de navigation nav-2696</a>
</li>
<li>
<a id="nav-2697" href="#" class="fr-nav__link">Lien de navigation nav-2697</a>
</li>
<li>
<a id="nav-2698" href="#" class="fr-nav__link">Lien de navigation nav-2698</a>
</li>
<li>
<a id="nav-2699" href="#" class="fr-nav__link">Lien de navigation nav-2699</a>
</li>
</ul>
</div>
</li>
<li class="fr-nav__item">
<button id="mega-menu-2700" aria-expanded="false" aria-controls="collapse-2701" type="button" class="fr-nav__btn">Entrée mega menu</button>
<div class="fr-collapse fr-mega-menu" id="collapse-2701">
<div class="fr-container fr-container--fluid fr-container-lg">
<div class="fr-grid-row fr-grid-row-lg--gutters">
<div class="fr-col-12 fr-mb-n3v">
<button aria-controls="collapse-2701" title="Fermer" type="button" id="button-2837" class="fr-btn--close fr-btn">Fermer</button>
</div>
<div class="fr-col-12 fr-col-lg-3">
<h5 class="fr-mega-menu__category">
<a id="category-2702" href="#" class="fr-nav__link">Nom de catégorie</a>
</h5>
<ul class="fr-mega-menu__list">
<li>
<a id="nav-2703" href="#" class="fr-nav__link">Lien de navigation nav-2703</a>
</li>
<li>
<a id="nav-2704" href="#" class="fr-nav__link">Lien de navigation nav-2704</a>
</li>
<li>
<a id="nav-2705" href="#" class="fr-nav__link">Lien de navigation nav-2705</a>
</li>
<li>
<a id="nav-2706" href="#" class="fr-nav__link">Lien de navigation nav-2706</a>
</li>
<li>
<a id="nav-2707" href="#" class="fr-nav__link">Lien de navigation nav-2707</a>
</li>
<li>
<a id="nav-2708" href="#" class="fr-nav__link">Lien de navigation nav-2708</a>
</li>
<li>
<a id="nav-2709" href="#" class="fr-nav__link">Lien de navigation nav-2709</a>
</li>
<li>
<a id="nav-2710" href="#" class="fr-nav__link">Lien de navigation nav-2710</a>
</li>
</ul>
</div>
<div class="fr-col-12 fr-col-lg-3">
<h5 class="fr-mega-menu__category">
<a id="category-2711" href="#" class="fr-nav__link">Nom de catégorie</a>
</h5>
<ul class="fr-mega-menu__list">
<li>
<a id="nav-2712" href="#" class="fr-nav__link">Lien de navigation nav-2712</a>
</li>
<li>
<a id="nav-2713" href="#" class="fr-nav__link">Lien de navigation nav-2713</a>
</li>
<li>
<a id="nav-2714" href="#" class="fr-nav__link">Lien de navigation nav-2714</a>
</li>
<li>
<a id="nav-2715" href="#" class="fr-nav__link">Lien de navigation nav-2715</a>
</li>
<li>
<a id="nav-2716" href="#" class="fr-nav__link">Lien de navigation nav-2716</a>
</li>
<li>
<a id="nav-2717" href="#" class="fr-nav__link">Lien de navigation nav-2717</a>
</li>
<li>
<a id="nav-2718" href="#" class="fr-nav__link">Lien de navigation nav-2718</a>
</li>
<li>
<a id="nav-2719" href="#" class="fr-nav__link">Lien de navigation nav-2719</a>
</li>
</ul>
</div>
<div class="fr-col-12 fr-col-lg-3">
<h5 class="fr-mega-menu__category">
<a id="category-2720" href="#" class="fr-nav__link">Nom de catégorie</a>
</h5>
<ul class="fr-mega-menu__list">
<li>
<a id="nav-2721" href="#" class="fr-nav__link">Lien de navigation nav-2721</a>
</li>
<li>
<a id="nav-2722" href="#" class="fr-nav__link">Lien de navigation nav-2722</a>
</li>
<li>
<a id="nav-2723" aria-current="page" href="#" class="fr-nav__link">Lien de navigation nav-2723</a>
</li>
<li>
<a id="nav-2724" href="#" class="fr-nav__link">Lien de navigation nav-2724</a>
</li>
<li>
<a id="nav-2725" href="#" class="fr-nav__link">Lien de navigation nav-2725</a>
</li>
<li>
<a id="nav-2726" href="#" class="fr-nav__link">Lien de navigation nav-2726</a>
</li>
<li>
<a id="nav-2727" href="#" class="fr-nav__link">Lien de navigation nav-2727</a>
</li>
<li>
<a id="nav-2728" href="#" class="fr-nav__link">Lien de navigation nav-2728</a>
</li>
</ul>
</div>
<div class="fr-col-12 fr-col-lg-3">
<h5 class="fr-mega-menu__category">
<a id="category-2729" href="#" class="fr-nav__link">Nom de catégorie</a>
</h5>
<ul class="fr-mega-menu__list">
<li>
<a id="nav-2730" href="#" class="fr-nav__link">Lien de navigation nav-2730</a>
</li>
<li>
<a id="nav-2731" href="#" class="fr-nav__link">Lien de navigation nav-2731</a>
</li>
<li>
<a id="nav-2732" href="#" class="fr-nav__link">Lien de navigation nav-2732</a>
</li>
<li>
<a id="nav-2733" href="#" class="fr-nav__link">Lien de navigation nav-2733</a>
</li>
<li>
<a id="nav-2734" href="#" class="fr-nav__link">Lien de navigation nav-2734</a>
</li>
<li>
<a id="nav-2735" href="#" class="fr-nav__link">Lien de navigation nav-2735</a>
</li>
<li>
<a id="nav-2736" href="#" class="fr-nav__link">Lien de navigation nav-2736</a>
</li>
<li>
<a id="nav-2737" href="#" class="fr-nav__link">Lien de navigation nav-2737</a>
</li>
</ul>
</div>
</div>
</div>
</div>
</li>
<li class="fr-nav__item">
<a id="nav-2738" type="link" href="#" class="fr-nav__link">accès direct nav-2738</a>
</li>
<li class="fr-nav__item">
<button id="menu-2739" aria-expanded="false" aria-controls="collapse-2740" aria-current="true" type="button" class="fr-nav__btn">Entrée menu</button>
<div class="fr-collapse fr-menu" id="collapse-2740">
<ul class="fr-menu__list">
<li>
<a id="nav-2741" href="#" class="fr-nav__link">Lien de navigation nav-2741</a>
</li>
<li>
<a id="nav-2742" href="#" class="fr-nav__link">Lien de navigation nav-2742</a>
</li>
<li>
<a id="nav-2743" aria-current="page" href="#" class="fr-nav__link">Lien de navigation nav-2743</a>
</li>
<li>
<a id="nav-2744" href="#" class="fr-nav__link">Lien de navigation nav-2744</a>
</li>
<li>
<a id="nav-2745" href="#" class="fr-nav__link">Lien de navigation nav-2745</a>
</li>
<li>
<a id="nav-2746" href="#" class="fr-nav__link">Lien de navigation nav-2746</a>
</li>
<li>
<a id="nav-2747" href="#" class="fr-nav__link">Lien de navigation nav-2747</a>
</li>
<li>
<a id="nav-2748" href="#" class="fr-nav__link">Lien de navigation nav-2748</a>
</li>
</ul>
</div>
</li>
<li class="fr-nav__item">
<button id="mega-menu-2749" aria-expanded="false" aria-controls="collapse-2750" type="button" class="fr-nav__btn">Entrée mega menu</button>
<div class="fr-collapse fr-mega-menu" id="collapse-2750">
<div class="fr-container fr-container--fluid fr-container-lg">
<div class="fr-grid-row fr-grid-row-lg--gutters">
<div class="fr-col-12 fr-mb-n3v">
<button aria-controls="collapse-2750" title="Fermer" type="button" id="button-2838" class="fr-btn--close fr-btn">Fermer</button>
</div>
<div class="fr-col-12 fr-col-lg-8 fr-col-offset-lg-4--right">
<div class="fr-mega-menu__leader">
<h4 class="fr-h4 fr-mb-2v">Titre éditorialisé</h4>
<p class="fr-hidden fr-unhidden-lg">Lorem [...] elit ut.</p>
<a id="link-2751" href="[url - à modifier]" class="fr-link fr-icon-arrow-right-line fr-link--icon-right">Voir toute la rubrique</a>
</div>
</div>
<div class="fr-col-12 fr-col-lg-3">
<h5 class="fr-mega-menu__category">
<a id="category-2752" href="#" class="fr-nav__link">Nom de catégorie</a>
</h5>
<ul class="fr-mega-menu__list">
<li>
<a id="nav-2753" href="#" class="fr-nav__link">Lien de navigation nav-2753</a>
</li>
<li>
<a id="nav-2754" href="#" class="fr-nav__link">Lien de navigation nav-2754</a>
</li>
<li>
<a id="nav-2755" href="#" class="fr-nav__link">Lien de navigation nav-2755</a>
</li>
<li>
<a id="nav-2756" href="#" class="fr-nav__link">Lien de navigation nav-2756</a>
</li>
<li>
<a id="nav-2757" href="#" class="fr-nav__link">Lien de navigation nav-2757</a>
</li>
<li>
<a id="nav-2758" href="#" class="fr-nav__link">Lien de navigation nav-2758</a>
</li>
<li>
<a id="nav-2759" href="#" class="fr-nav__link">Lien de navigation nav-2759</a>
</li>
<li>
<a id="nav-2760" href="#" class="fr-nav__link">Lien de navigation nav-2760</a>
</li>
</ul>
</div>
<div class="fr-col-12 fr-col-lg-3">
<h5 class="fr-mega-menu__category">
<a id="category-2761" href="#" class="fr-nav__link">Nom de catégorie</a>
</h5>
<ul class="fr-mega-menu__list">
<li>
<a id="nav-2762" href="#" class="fr-nav__link">Lien de navigation nav-2762</a>
</li>
<li>
<a id="nav-2763" href="#" class="fr-nav__link">Lien de navigation nav-2763</a>
</li>
<li>
<a id="nav-2764" href="#" class="fr-nav__link">Lien de navigation nav-2764</a>
</li>
<li>
<a id="nav-2765" href="#" class="fr-nav__link">Lien de navigation nav-2765</a>
</li>
<li>
<a id="nav-2766" href="#" class="fr-nav__link">Lien de navigation nav-2766</a>
</li>
<li>
<a id="nav-2767" href="#" class="fr-nav__link">Lien de navigation nav-2767</a>
</li>
<li>
<a id="nav-2768" href="#" class="fr-nav__link">Lien de navigation nav-2768</a>
</li>
<li>
<a id="nav-2769" href="#" class="fr-nav__link">Lien de navigation nav-2769</a>
</li>
</ul>
</div>
<div class="fr-col-12 fr-col-lg-3">
<h5 class="fr-mega-menu__category">
<a id="category-2770" href="#" class="fr-nav__link">Nom de catégorie</a>
</h5>
<ul class="fr-mega-menu__list">
<li>
<a id="nav-2771" href="#" class="fr-nav__link">Lien de navigation nav-2771</a>
</li>
<li>
<a id="nav-2772" href="#" class="fr-nav__link">Lien de navigation nav-2772</a>
</li>
<li>
<a id="nav-2773" aria-current="page" href="#" class="fr-nav__link">Lien de navigation nav-2773</a>
</li>
<li>
<a id="nav-2774" href="#" class="fr-nav__link">Lien de navigation nav-2774</a>
</li>
<li>
<a id="nav-2775" href="#" class="fr-nav__link">Lien de navigation nav-2775</a>
</li>
<li>
<a id="nav-2776" href="#" class="fr-nav__link">Lien de navigation nav-2776</a>
</li>
<li>
<a id="nav-2777" href="#" class="fr-nav__link">Lien de navigation nav-2777</a>
</li>
<li>
<a id="nav-2778" href="#" class="fr-nav__link">Lien de navigation nav-2778</a>
</li>
</ul>
</div>
<div class="fr-col-12 fr-col-lg-3">
<h5 class="fr-mega-menu__category">
<a id="category-2779" href="#" class="fr-nav__link">Nom de catégorie</a>
</h5>
<ul class="fr-mega-menu__list">
<li>
<a id="nav-2780" href="#" class="fr-nav__link">Lien de navigation nav-2780</a>
</li>
<li>
<a id="nav-2781" href="#" class="fr-nav__link">Lien de navigation nav-2781</a>
</li>
<li>
<a id="nav-2782" href="#" class="fr-nav__link">Lien de navigation nav-2782</a>
</li>
<li>
<a id="nav-2783" href="#" class="fr-nav__link">Lien de navigation nav-2783</a>
</li>
<li>
<a id="nav-2784" href="#" class="fr-nav__link">Lien de navigation nav-2784</a>
</li>
<li>
<a id="nav-2785" href="#" class="fr-nav__link">Lien de navigation nav-2785</a>
</li>
<li>
<a id="nav-2786" href="#" class="fr-nav__link">Lien de navigation nav-2786</a>
</li>
<li>
<a id="nav-2787" href="#" class="fr-nav__link">Lien de navigation nav-2787</a>
</li>
</ul>
</div>
</div>
</div>
</div>
</li>
<li class="fr-nav__item">
<a id="nav-2788" type="link" href="#" class="fr-nav__link">accès direct nav-2788</a>
</li>
<li class="fr-nav__item">
<button id="mega-menu-2789" aria-expanded="false" aria-controls="collapse-2790" type="button" class="fr-nav__btn">Entrée mega menu</button>
<div class="fr-collapse fr-mega-menu" id="collapse-2790">
<div class="fr-container fr-container--fluid fr-container-lg">
<div class="fr-grid-row fr-grid-row-lg--gutters">
<div class="fr-col-12 fr-mb-n3v">
<button aria-controls="collapse-2790" title="Fermer" type="button" id="button-2839" class="fr-btn--close fr-btn">Fermer</button>
</div>
<div class="fr-col-12 fr-col-lg-3">
<h5 class="fr-mega-menu__category">
<a id="category-2791" href="#" class="fr-nav__link">Nom de catégorie</a>
</h5>
<ul class="fr-mega-menu__list">
<li>
<a id="nav-2792" href="#" class="fr-nav__link">Lien de navigation nav-2792</a>
</li>
<li>
<a id="nav-2793" href="#" class="fr-nav__link">Lien de navigation nav-2793</a>
</li>
<li>
<a id="nav-2794" href="#" class="fr-nav__link">Lien de navigation nav-2794</a>
</li>
<li>
<a id="nav-2795" href="#" class="fr-nav__link">Lien de navigation nav-2795</a>
</li>
<li>
<a id="nav-2796" href="#" class="fr-nav__link">Lien de navigation nav-2796</a>
</li>
<li>
<a id="nav-2797" href="#" class="fr-nav__link">Lien de navigation nav-2797</a>
</li>
<li>
<a id="nav-2798" href="#" class="fr-nav__link">Lien de navigation nav-2798</a>
</li>
<li>
<a id="nav-2799" href="#" class="fr-nav__link">Lien de navigation nav-2799</a>
</li>
</ul>
</div>
<div class="fr-col-12 fr-col-lg-3">
<h5 class="fr-mega-menu__category">
<a id="category-2800" href="#" class="fr-nav__link">Nom de catégorie</a>
</h5>
<ul class="fr-mega-menu__list">
<li>
<a id="nav-2801" href="#" class="fr-nav__link">Lien de navigation nav-2801</a>
</li>
<li>
<a id="nav-2802" href="#" class="fr-nav__link">Lien de navigation nav-2802</a>
</li>
<li>
<a id="nav-2803" href="#" class="fr-nav__link">Lien de navigation nav-2803</a>
</li>
<li>
<a id="nav-2804" href="#" class="fr-nav__link">Lien de navigation nav-2804</a>
</li>
<li>
<a id="nav-2805" href="#" class="fr-nav__link">Lien de navigation nav-2805</a>
</li>
<li>
<a id="nav-2806" href="#" class="fr-nav__link">Lien de navigation nav-2806</a>
</li>
<li>
<a id="nav-2807" href="#" class="fr-nav__link">Lien de navigation nav-2807</a>
</li>
<li>
<a id="nav-2808" href="#" class="fr-nav__link">Lien de navigation nav-2808</a>
</li>
</ul>
</div>
<div class="fr-col-12 fr-col-lg-3">
<h5 class="fr-mega-menu__category">
<a id="category-2809" href="#" class="fr-nav__link">Nom de catégorie</a>
</h5>
<ul class="fr-mega-menu__list">
<li>
<a id="nav-2810" href="#" class="fr-nav__link">Lien de navigation nav-2810</a>
</li>
<li>
<a id="nav-2811" href="#" class="fr-nav__link">Lien de navigation nav-2811</a>
</li>
<li>
<a id="nav-2812" aria-current="page" href="#" class="fr-nav__link">Lien de navigation nav-2812</a>
</li>
<li>
<a id="nav-2813" href="#" class="fr-nav__link">Lien de navigation nav-2813</a>
</li>
<li>
<a id="nav-2814" href="#" class="fr-nav__link">Lien de navigation nav-2814</a>
</li>
<li>
<a id="nav-2815" href="#" class="fr-nav__link">Lien de navigation nav-2815</a>
</li>
<li>
<a id="nav-2816" href="#" class="fr-nav__link">Lien de navigation nav-2816</a>
</li>
<li>
<a id="nav-2817" href="#" class="fr-nav__link">Lien de navigation nav-2817</a>
</li>
</ul>
</div>
<div class="fr-col-12 fr-col-lg-3">
<h5 class="fr-mega-menu__category">
<a id="category-2818" href="#" class="fr-nav__link">Nom de catégorie</a>
</h5>
<ul class="fr-mega-menu__list">
<li>
<a id="nav-2819" href="#" class="fr-nav__link">Lien de navigation nav-2819</a>
</li>
<li>
<a id="nav-2820" href="#" class="fr-nav__link">Lien de navigation nav-2820</a>
</li>
<li>
<a id="nav-2821" href="#" class="fr-nav__link">Lien de navigation nav-2821</a>
</li>
<li>
<a id="nav-2822" href="#" class="fr-nav__link">Lien de navigation nav-2822</a>
</li>
<li>
<a id="nav-2823" href="#" class="fr-nav__link">Lien de navigation nav-2823</a>
</li>
<li>
<a id="nav-2824" href="#" class="fr-nav__link">Lien de navigation nav-2824</a>
</li>
<li>
<a id="nav-2825" href="#" class="fr-nav__link">Lien de navigation nav-2825</a>
</li>
<li>
<a id="nav-2826" href="#" class="fr-nav__link">Lien de navigation nav-2826</a>
</li>
</ul>
</div>
</div>
</div>
</div>
</li>
<li class="fr-nav__item">
<button id="menu-2827" aria-expanded="false" aria-controls="collapse-2828" type="button" class="fr-nav__btn">Entrée menu</button>
<div class="fr-collapse fr-menu" id="collapse-2828">
<ul class="fr-menu__list">
<li>
<a id="nav-2829" href="#" class="fr-nav__link">Lien de navigation nav-2829</a>
</li>
<li>
<a id="nav-2830" href="#" class="fr-nav__link">Lien de navigation nav-2830</a>
</li>
<li>
<a id="nav-2831" href="#" class="fr-nav__link">Lien de navigation nav-2831</a>
</li>
<li>
<a id="nav-2832" href="#" class="fr-nav__link">Lien de navigation nav-2832</a>
</li>
<li>
<a id="nav-2833" href="#" class="fr-nav__link">Lien de navigation nav-2833</a>
</li>
<li>
<a id="nav-2834" href="#" class="fr-nav__link">Lien de navigation nav-2834</a>
</li>
<li>
<a id="nav-2835" href="#" class="fr-nav__link">Lien de navigation nav-2835</a>
</li>
<li>
<a id="nav-2836" href="#" class="fr-nav__link">Lien de navigation nav-2836</a>
</li>
</ul>
</div>
</li>
</ul>
</nav>
</div>
</div>
</header>


#### Header avec selecteur de langues et paramètre d'affichage


Intitulé

officiel


Menu


[Nom du site / service](/)


baseline - précisions sur l'organisation


Paramètres d'affichage


FR - Français


-
[FR - Français](lang=%22fr%22)


-
[EN - English](lang=%22en%22)


-
[ES - Español](lang=%22es%22)


-
[DE - Deutsch](lang=%22de%22)


-
[TR - Türkçe](lang=%22tr%22)


-
[RO - Română](lang=%22ro%22)


Fermer


-
Entrée menu


-


-


-


-


-


-


-


-


-
Entrée mega menu


Fermer


#####


-


-


-


-


-


-


-


-


#####


-


-


-


-


-


-


-


-


#####


-


-


-


-


-


-


-


-


#####


-


-


-


-


-


-


-


-


-


-
Entrée menu


-


-


-


-


-


-


-


-


-
Entrée mega menu


Fermer


#### Titre éditorialisé


Lorem ipsum dolor sit amet, consectetur adipiscing, incididunt, ut labore et dolore magna aliqua. Vitae sapien pellentesque habitant morbi tristique senectus et. Diam maecenas sed enim ut. Accumsan lacus vel facilisis volutpat est. Ut aliquam purus sit amet luctus. Lorem ipsum dolor sit amet consectetur adipiscing elit ut.
[Voir toute la rubrique](%5Burl%20-%20%C3%A0%20modifier%5D)


#####


-


-


-


-


-


-


-


-


#####


-


-


-


-


-


-


-


-


#####


-


-


-


-


-


-


-


-


#####


-


-


-


-


-


-


-


-


-


-
Entrée mega menu


Fermer


#####


-


-


-


-


-


-


-


-


#####


-


-


-


-


-


-


-


-


#####


-


-


-


-


-


-


-


-


#####


-


-


-


-


-


-


-


-


-
Entrée menu


-


-


-


-


-


-


-


-


###
Extrait de code


<header role="banner" class="fr-header">
<div class="fr-header__body">
<div class="fr-container">
<div class="fr-header__body-row">
<div class="fr-header__brand fr-enlarge-link">
<div class="fr-header__brand-top">
<div class="fr-header__logo">
<p class="fr-logo">
Intitulé
<br>officiel
</p>
</div>
<div class="fr-header__navbar">
<button data-fr-opened="false" aria-controls="modal-3004" title="Menu" type="button" id="button-3005" class="fr-btn--menu fr-btn">Menu</button>
</div>
</div>
<div class="fr-header__service">
<a href="/" title="Accueil - [À MODIFIER - Nom du site / service] - Nom de l'entité (ministère, secrétariat d'état, gouvernement)">
<p class="fr-header__service-title">
Nom du site / service
</p>
</a>
<p class="fr-header__service-tagline">baseline - précisions sur l'organisation</p>
</div>
</div>
<div class="fr-header__tools">
<div class="fr-header__tools-links">
<button aria-controls="fr-theme-modal" data-fr-opened="false" type="button" class="fr-icon-theme-fill fr-btn--icon-left fr-btn fr-btn">Paramètres d'affichage</button>
<nav role="navigation" class="fr-translate fr-nav" id="translate-3007">
<div class="fr-nav__item">
<button aria-controls="translate-3003" aria-expanded="false" type="button" class="fr-translate__btn fr-btn">FR<span class="fr-hidden-lg"> - Français</span>
</button>
<div class="fr-collapse fr-translate__menu fr-menu" id="translate-3003">
<ul class="fr-menu__list">
<li>
<a class="fr-translate__language fr-nav__link" hreflang="fr" lang="fr" href="/fr/" id="language-3008" aria-current="true">FR - Français</a>
</li>
<li>
<a class="fr-translate__language fr-nav__link" hreflang="en" lang="en" href="/en/" id="language-3009">EN - English</a>
</li>
<li>
<a class="fr-translate__language fr-nav__link" hreflang="es" lang="es" href="/es/" id="language-3010">ES - Español</a>
</li>
<li>
<a class="fr-translate__language fr-nav__link" hreflang="de" lang="de" href="/de/" id="language-3011">DE - Deutsch</a>
</li>
<li>
<a class="fr-translate__language fr-nav__link" hreflang="tr" lang="tr" href="/tr/" id="language-3012">TR - Türkçe</a>
</li>
<li>
<a class="fr-translate__language fr-nav__link" hreflang="ro" lang="ro" href="/ro/" id="language-3013">RO - Română</a>
</li>
</ul>
</div>
</div>
</nav>
</div>
</div>
</div>
</div>
</div>
<div class="fr-header__menu fr-modal" id="modal-3004" aria-labelledby="button-3005">
<div class="fr-container">
<button aria-controls="modal-3004" title="Fermer" type="button" id="button-3014" class="fr-btn--close fr-btn">Fermer</button>
<div class="fr-header__menu-links">
</div>
<nav class="fr-nav" id="navigation-3006" role="navigation" aria-label="Menu principal">
<ul class="fr-nav__list">
<li class="fr-nav__item">
<button id="menu-3015" aria-expanded="false" aria-controls="collapse-3016" type="button" class="fr-nav__btn">Entrée menu</button>
<div class="fr-collapse fr-menu" id="collapse-3016">
<ul class="fr-menu__list">
<li>
<a id="nav-3017" href="#" class="fr-nav__link">Lien de navigation nav-3017</a>
</li>
<li>
<a id="nav-3018" href="#" class="fr-nav__link">Lien de navigation nav-3018</a>
</li>
<li>
<a id="nav-3019" href="#" class="fr-nav__link">Lien de navigation nav-3019</a>
</li>
<li>
<a id="nav-3020" href="#" class="fr-nav__link">Lien de navigation nav-3020</a>
</li>
<li>
<a id="nav-3021" href="#" class="fr-nav__link">Lien de navigation nav-3021</a>
</li>
<li>
<a id="nav-3022" href="#" class="fr-nav__link">Lien de navigation nav-3022</a>
</li>
<li>
<a id="nav-3023" href="#" class="fr-nav__link">Lien de navigation nav-3023</a>
</li>
<li>
<a id="nav-3024" href="#" class="fr-nav__link">Lien de navigation nav-3024</a>
</li>
</ul>
</div>
</li>
<li class="fr-nav__item">
<button id="mega-menu-3025" aria-expanded="false" aria-controls="collapse-3026" type="button" class="fr-nav__btn">Entrée mega menu</button>
<div class="fr-collapse fr-mega-menu" id="collapse-3026">
<div class="fr-container fr-container--fluid fr-container-lg">
<div class="fr-grid-row fr-grid-row-lg--gutters">
<div class="fr-col-12 fr-mb-n3v">
<button aria-controls="collapse-3026" title="Fermer" type="button" id="button-3162" class="fr-btn--close fr-btn">Fermer</button>
</div>
<div class="fr-col-12 fr-col-lg-3">
<h5 class="fr-mega-menu__category">
<a id="category-3027" href="#" class="fr-nav__link">Nom de catégorie</a>
</h5>
<ul class="fr-mega-menu__list">
<li>
<a id="nav-3028" href="#" class="fr-nav__link">Lien de navigation nav-3028</a>
</li>
<li>
<a id="nav-3029" href="#" class="fr-nav__link">Lien de navigation nav-3029</a>
</li>
<li>
<a id="nav-3030" href="#" class="fr-nav__link">Lien de navigation nav-3030</a>
</li>
<li>
<a id="nav-3031" href="#" class="fr-nav__link">Lien de navigation nav-3031</a>
</li>
<li>
<a id="nav-3032" href="#" class="fr-nav__link">Lien de navigation nav-3032</a>
</li>
<li>
<a id="nav-3033" href="#" class="fr-nav__link">Lien de navigation nav-3033</a>
</li>
<li>
<a id="nav-3034" href="#" class="fr-nav__link">Lien de navigation nav-3034</a>
</li>
<li>
<a id="nav-3035" href="#" class="fr-nav__link">Lien de navigation nav-3035</a>
</li>
</ul>
</div>
<div class="fr-col-12 fr-col-lg-3">
<h5 class="fr-mega-menu__category">
<a id="category-3036" href="#" class="fr-nav__link">Nom de catégorie</a>
</h5>
<ul class="fr-mega-menu__list">
<li>
<a id="nav-3037" href="#" class="fr-nav__link">Lien de navigation nav-3037</a>
</li>
<li>
<a id="nav-3038" href="#" class="fr-nav__link">Lien de navigation nav-3038</a>
</li>
<li>
<a id="nav-3039" href="#" class="fr-nav__link">Lien de navigation nav-3039</a>
</li>
<li>
<a id="nav-3040" href="#" class="fr-nav__link">Lien de navigation nav-3040</a>
</li>
<li>
<a id="nav-3041" href="#" class="fr-nav__link">Lien de navigation nav-3041</a>
</li>
<li>
<a id="nav-3042" href="#" class="fr-nav__link">Lien de navigation nav-3042</a>
</li>
<li>
<a id="nav-3043" href="#" class="fr-nav__link">Lien de navigation nav-3043</a>
</li>
<li>
<a id="nav-3044" href="#" class="fr-nav__link">Lien de navigation nav-3044</a>
</li>
</ul>
</div>
<div class="fr-col-12 fr-col-lg-3">
<h5 class="fr-mega-menu__category">
<a id="category-3045" href="#" class="fr-nav__link">Nom de catégorie</a>
</h5>
<ul class="fr-mega-menu__list">
<li>
<a id="nav-3046" href="#" class="fr-nav__link">Lien de navigation nav-3046</a>
</li>
<li>
<a id="nav-3047" href="#" class="fr-nav__link">Lien de navigation nav-3047</a>
</li>
<li>
<a id="nav-3048" aria-current="page" href="#" class="fr-nav__link">Lien de navigation nav-3048</a>
</li>
<li>
<a id="nav-3049" href="#" class="fr-nav__link">Lien de navigation nav-3049</a>
</li>
<li>
<a id="nav-3050" href="#" class="fr-nav__link">Lien de navigation nav-3050</a>
</li>
<li>
<a id="nav-3051" href="#" class="fr-nav__link">Lien de navigation nav-3051</a>
</li>
<li>
<a id="nav-3052" href="#" class="fr-nav__link">Lien de navigation nav-3052</a>
</li>
<li>
<a id="nav-3053" href="#" class="fr-nav__link">Lien de navigation nav-3053</a>
</li>
</ul>
</div>
<div class="fr-col-12 fr-col-lg-3">
<h5 class="fr-mega-menu__category">
<a id="category-3054" href="#" class="fr-nav__link">Nom de catégorie</a>
</h5>
<ul class="fr-mega-menu__list">
<li>
<a id="nav-3055" href="#" class="fr-nav__link">Lien de navigation nav-3055</a>
</li>
<li>
<a id="nav-3056" href="#" class="fr-nav__link">Lien de navigation nav-3056</a>
</li>
<li>
<a id="nav-3057" href="#" class="fr-nav__link">Lien de navigation nav-3057</a>
</li>
<li>
<a id="nav-3058" href="#" class="fr-nav__link">Lien de navigation nav-3058</a>
</li>
<li>
<a id="nav-3059" href="#" class="fr-nav__link">Lien de navigation nav-3059</a>
</li>
<li>
<a id="nav-3060" href="#" class="fr-nav__link">Lien de navigation nav-3060</a>
</li>
<li>
<a id="nav-3061" href="#" class="fr-nav__link">Lien de navigation nav-3061</a>
</li>
<li>
<a id="nav-3062" href="#" class="fr-nav__link">Lien de navigation nav-3062</a>
</li>
</ul>
</div>
</div>
</div>
</div>
</li>
<li class="fr-nav__item">
<a id="nav-3063" type="link" href="#" class="fr-nav__link">accès direct nav-3063</a>
</li>
<li class="fr-nav__item">
<button id="menu-3064" aria-expanded="false" aria-controls="collapse-3065" aria-current="true" type="button" class="fr-nav__btn">Entrée menu</button>
<div class="fr-collapse fr-menu" id="collapse-3065">
<ul class="fr-menu__list">
<li>
<a id="nav-3066" href="#" class="fr-nav__link">Lien de navigation nav-3066</a>
</li>
<li>
<a id="nav-3067" href="#" class="fr-nav__link">Lien de navigation nav-3067</a>
</li>
<li>
<a id="nav-3068" aria-current="page" href="#" class="fr-nav__link">Lien de navigation nav-3068</a>
</li>
<li>
<a id="nav-3069" href="#" class="fr-nav__link">Lien de navigation nav-3069</a>
</li>
<li>
<a id="nav-3070" href="#" class="fr-nav__link">Lien de navigation nav-3070</a>
</li>
<li>
<a id="nav-3071" href="#" class="fr-nav__link">Lien de navigation nav-3071</a>
</li>
<li>
<a id="nav-3072" href="#" class="fr-nav__link">Lien de navigation nav-3072</a>
</li>
<li>
<a id="nav-3073" href="#" class="fr-nav__link">Lien de navigation nav-3073</a>
</li>
</ul>
</div>
</li>
<li class="fr-nav__item">
<button id="mega-menu-3074" aria-expanded="false" aria-controls="collapse-3075" type="button" class="fr-nav__btn">Entrée mega menu</button>
<div class="fr-collapse fr-mega-menu" id="collapse-3075">
<div class="fr-container fr-container--fluid fr-container-lg">
<div class="fr-grid-row fr-grid-row-lg--gutters">
<div class="fr-col-12 fr-mb-n3v">
<button aria-controls="collapse-3075" title="Fermer" type="button" id="button-3163" class="fr-btn--close fr-btn">Fermer</button>
</div>
<div class="fr-col-12 fr-col-lg-8 fr-col-offset-lg-4--right">
<div class="fr-mega-menu__leader">
<h4 class="fr-h4 fr-mb-2v">Titre éditorialisé</h4>
<p class="fr-hidden fr-unhidden-lg">Lorem [...] elit ut.</p>
<a id="link-3076" href="[url - à modifier]" class="fr-link fr-icon-arrow-right-line fr-link--icon-right">Voir toute la rubrique</a>
</div>
</div>
<div class="fr-col-12 fr-col-lg-3">
<h5 class="fr-mega-menu__category">
<a id="category-3077" href="#" class="fr-nav__link">Nom de catégorie</a>
</h5>
<ul class="fr-mega-menu__list">
<li>
<a id="nav-3078" href="#" class="fr-nav__link">Lien de navigation nav-3078</a>
</li>
<li>
<a id="nav-3079" href="#" class="fr-nav__link">Lien de navigation nav-3079</a>
</li>
<li>
<a id="nav-3080" href="#" class="fr-nav__link">Lien de navigation nav-3080</a>
</li>
<li>
<a id="nav-3081" href="#" class="fr-nav__link">Lien de navigation nav-3081</a>
</li>
<li>
<a id="nav-3082" href="#" class="fr-nav__link">Lien de navigation nav-3082</a>
</li>
<li>
<a id="nav-3083" href="#" class="fr-nav__link">Lien de navigation nav-3083</a>
</li>
<li>
<a id="nav-3084" href="#" class="fr-nav__link">Lien de navigation nav-3084</a>
</li>
<li>
<a id="nav-3085" href="#" class="fr-nav__link">Lien de navigation nav-3085</a>
</li>
</ul>
</div>
<div class="fr-col-12 fr-col-lg-3">
<h5 class="fr-mega-menu__category">
<a id="category-3086" href="#" class="fr-nav__link">Nom de catégorie</a>
</h5>
<ul class="fr-mega-menu__list">
<li>
<a id="nav-3087" href="#" class="fr-nav__link">Lien de navigation nav-3087</a>
</li>
<li>
<a id="nav-3088" href="#" class="fr-nav__link">Lien de navigation nav-3088</a>
</li>
<li>
<a id="nav-3089" href="#" class="fr-nav__link">Lien de navigation nav-3089</a>
</li>
<li>
<a id="nav-3090" href="#" class="fr-nav__link">Lien de navigation nav-3090</a>
</li>
<li>
<a id="nav-3091" href="#" class="fr-nav__link">Lien de navigation nav-3091</a>
</li>
<li>
<a id="nav-3092" href="#" class="fr-nav__link">Lien de navigation nav-3092</a>
</li>
<li>
<a id="nav-3093" href="#" class="fr-nav__link">Lien de navigation nav-3093</a>
</li>
<li>
<a id="nav-3094" href="#" class="fr-nav__link">Lien de navigation nav-3094</a>
</li>
</ul>
</div>
<div class="fr-col-12 fr-col-lg-3">
<h5 class="fr-mega-menu__category">
<a id="category-3095" href="#" class="fr-nav__link">Nom de catégorie</a>
</h5>
<ul class="fr-mega-menu__list">
<li>
<a id="nav-3096" href="#" class="fr-nav__link">Lien de navigation nav-3096</a>
</li>
<li>
<a id="nav-3097" href="#" class="fr-nav__link">Lien de navigation nav-3097</a>
</li>
<li>
<a id="nav-3098" aria-current="page" href="#" class="fr-nav__link">Lien de navigation nav-3098</a>
</li>
<li>
<a id="nav-3099" href="#" class="fr-nav__link">Lien de navigation nav-3099</a>
</li>
<li>
<a id="nav-3100" href="#" class="fr-nav__link">Lien de navigation nav-3100</a>
</li>
<li>
<a id="nav-3101" href="#" class="fr-nav__link">Lien de navigation nav-3101</a>
</li>
<li>
<a id="nav-3102" href="#" class="fr-nav__link">Lien de navigation nav-3102</a>
</li>
<li>
<a id="nav-3103" href="#" class="fr-nav__link">Lien de navigation nav-3103</a>
</li>
</ul>
</div>
<div class="fr-col-12 fr-col-lg-3">
<h5 class="fr-mega-menu__category">
<a id="category-3104" href="#" class="fr-nav__link">Nom de catégorie</a>
</h5>
<ul class="fr-mega-menu__list">
<li>
<a id="nav-3105" href="#" class="fr-nav__link">Lien de navigation nav-3105</a>
</li>
<li>
<a id="nav-3106" href="#" class="fr-nav__link">Lien de navigation nav-3106</a>
</li>
<li>
<a id="nav-3107" href="#" class="fr-nav__link">Lien de navigation nav-3107</a>
</li>
<li>
<a id="nav-3108" href="#" class="fr-nav__link">Lien de navigation nav-3108</a>
</li>
<li>
<a id="nav-3109" href="#" class="fr-nav__link">Lien de navigation nav-3109</a>
</li>
<li>
<a id="nav-3110" href="#" class="fr-nav__link">Lien de navigation nav-3110</a>
</li>
<li>
<a id="nav-3111" href="#" class="fr-nav__link">Lien de navigation nav-3111</a>
</li>
<li>
<a id="nav-3112" href="#" class="fr-nav__link">Lien de navigation nav-3112</a>
</li>
</ul>
</div>
</div>
</div>
</div>
</li>
<li class="fr-nav__item">
<a id="nav-3113" type="link" href="#" class="fr-nav__link">accès direct nav-3113</a>
</li>
<li class="fr-nav__item">
<button id="mega-menu-3114" aria-expanded="false" aria-controls="collapse-3115" type="button" class="fr-nav__btn">Entrée mega menu</button>
<div class="fr-collapse fr-mega-menu" id="collapse-3115">
<div class="fr-container fr-container--fluid fr-container-lg">
<div class="fr-grid-row fr-grid-row-lg--gutters">
<div class="fr-col-12 fr-mb-n3v">
<button aria-controls="collapse-3115" title="Fermer" type="button" id="button-3164" class="fr-btn--close fr-btn">Fermer</button>
</div>
<div class="fr-col-12 fr-col-lg-3">
<h5 class="fr-mega-menu__category">
<a id="category-3116" href="#" class="fr-nav__link">Nom de catégorie</a>
</h5>
<ul class="fr-mega-menu__list">
<li>
<a id="nav-3117" href="#" class="fr-nav__link">Lien de navigation nav-3117</a>
</li>
<li>
<a id="nav-3118" href="#" class="fr-nav__link">Lien de navigation nav-3118</a>
</li>
<li>
<a id="nav-3119" href="#" class="fr-nav__link">Lien de navigation nav-3119</a>
</li>
<li>
<a id="nav-3120" href="#" class="fr-nav__link">Lien de navigation nav-3120</a>
</li>
<li>
<a id="nav-3121" href="#" class="fr-nav__link">Lien de navigation nav-3121</a>
</li>
<li>
<a id="nav-3122" href="#" class="fr-nav__link">Lien de navigation nav-3122</a>
</li>
<li>
<a id="nav-3123" href="#" class="fr-nav__link">Lien de navigation nav-3123</a>
</li>
<li>
<a id="nav-3124" href="#" class="fr-nav__link">Lien de navigation nav-3124</a>
</li>
</ul>
</div>
<div class="fr-col-12 fr-col-lg-3">
<h5 class="fr-mega-menu__category">
<a id="category-3125" href="#" class="fr-nav__link">Nom de catégorie</a>
</h5>
<ul class="fr-mega-menu__list">
<li>
<a id="nav-3126" href="#" class="fr-nav__link">Lien de navigation nav-3126</a>
</li>
<li>
<a id="nav-3127" href="#" class="fr-nav__link">Lien de navigation nav-3127</a>
</li>
<li>
<a id="nav-3128" href="#" class="fr-nav__link">Lien de navigation nav-3128</a>
</li>
<li>
<a id="nav-3129" href="#" class="fr-nav__link">Lien de navigation nav-3129</a>
</li>
<li>
<a id="nav-3130" href="#" class="fr-nav__link">Lien de navigation nav-3130</a>
</li>
<li>
<a id="nav-3131" href="#" class="fr-nav__link">Lien de navigation nav-3131</a>
</li>
<li>
<a id="nav-3132" href="#" class="fr-nav__link">Lien de navigation nav-3132</a>
</li>
<li>
<a id="nav-3133" href="#" class="fr-nav__link">Lien de navigation nav-3133</a>
</li>
</ul>
</div>
<div class="fr-col-12 fr-col-lg-3">
<h5 class="fr-mega-menu__category">
<a id="category-3134" href="#" class="fr-nav__link">Nom de catégorie</a>
</h5>
<ul class="fr-mega-menu__list">
<li>
<a id="nav-3135" href="#" class="fr-nav__link">Lien de navigation nav-3135</a>
</li>
<li>
<a id="nav-3136" href="#" class="fr-nav__link">Lien de navigation nav-3136</a>
</li>
<li>
<a id="nav-3137" aria-current="page" href="#" class="fr-nav__link">Lien de navigation nav-3137</a>
</li>
<li>
<a id="nav-3138" href="#" class="fr-nav__link">Lien de navigation nav-3138</a>
</li>
<li>
<a id="nav-3139" href="#" class="fr-nav__link">Lien de navigation nav-3139</a>
</li>
<li>
<a id="nav-3140" href="#" class="fr-nav__link">Lien de navigation nav-3140</a>
</li>
<li>
<a id="nav-3141" href="#" class="fr-nav__link">Lien de navigation nav-3141</a>
</li>
<li>
<a id="nav-3142" href="#" class="fr-nav__link">Lien de navigation nav-3142</a>
</li>
</ul>
</div>
<div class="fr-col-12 fr-col-lg-3">
<h5 class="fr-mega-menu__category">
<a id="category-3143" href="#" class="fr-nav__link">Nom de catégorie</a>
</h5>
<ul class="fr-mega-menu__list">
<li>
<a id="nav-3144" href="#" class="fr-nav__link">Lien de navigation nav-3144</a>
</li>
<li>
<a id="nav-3145" href="#" class="fr-nav__link">Lien de navigation nav-3145</a>
</li>
<li>
<a id="nav-3146" href="#" class="fr-nav__link">Lien de navigation nav-3146</a>
</li>
<li>
<a id="nav-3147" href="#" class="fr-nav__link">Lien de navigation nav-3147</a>
</li>
<li>
<a id="nav-3148" href="#" class="fr-nav__link">Lien de navigation nav-3148</a>
</li>
<li>
<a id="nav-3149" href="#" class="fr-nav__link">Lien de navigation nav-3149</a>
</li>
<li>
<a id="nav-3150" href="#" class="fr-nav__link">Lien de navigation nav-3150</a>
</li>
<li>
<a id="nav-3151" href="#" class="fr-nav__link">Lien de navigation nav-3151</a>
</li>
</ul>
</div>
</div>
</div>
</div>
</li>
<li class="fr-nav__item">
<button id="menu-3152" aria-expanded="false" aria-controls="collapse-3153" type="button" class="fr-nav__btn">Entrée menu</button>
<div class="fr-collapse fr-menu" id="collapse-3153">
<ul class="fr-menu__list">
<li>
<a id="nav-3154" href="#" class="fr-nav__link">Lien de navigation nav-3154</a>
</li>
<li>
<a id="nav-3155" href="#" class="fr-nav__link">Lien de navigation nav-3155</a>
</li>
<li>
<a id="nav-3156" href="#" class="fr-nav__link">Lien de navigation nav-3156</a>
</li>
<li>
<a id="nav-3157" href="#" class="fr-nav__link">Lien de navigation nav-3157</a>
</li>
<li>
<a id="nav-3158" href="#" class="fr-nav__link">Lien de navigation nav-3158</a>
</li>
<li>
<a id="nav-3159" href="#" class="fr-nav__link">Lien de navigation nav-3159</a>
</li>
<li>
<a id="nav-3160" href="#" class="fr-nav__link">Lien de navigation nav-3160</a>
</li>
<li>
<a id="nav-3161" href="#" class="fr-nav__link">Lien de navigation nav-3161</a>
</li>
</ul>
</div>
</li>
</ul>
</nav>
</div>
</div>
</header>


#### Header avec nom de service, lien d'accès


Intitulé

officiel


Menu


[Nom du site / service](/)


baseline - précisions sur l'organisation


-
[Contact](%5Burl%20-%20%C3%A0%20modifier%5D)


-
[Espace recruteur](%5Burl%20-%20%C3%A0%20modifier%5D)


-
[Espace particulier](%5Burl%20-%20%C3%A0%20modifier%5D)


Fermer


-


-


-


-


###
Extrait de code


<header role="banner" class="fr-header">
<div class="fr-header__body">
<div class="fr-container">
<div class="fr-header__body-row">
<div class="fr-header__brand fr-enlarge-link">
<div class="fr-header__brand-top">
<div class="fr-header__logo">
<p class="fr-logo">
Intitulé
<br>officiel
</p>
</div>
<div class="fr-header__navbar">
<button data-fr-opened="false" aria-controls="modal-3175" title="Menu" type="button" id="button-3176" class="fr-btn--menu fr-btn">Menu</button>
</div>
</div>
<div class="fr-header__service">
<a href="/" title="Accueil - [À MODIFIER - Nom du site / service] - Nom de l'entité (ministère, secrétariat d'état, gouvernement)">
<p class="fr-header__service-title">
Nom du site / service
</p>
</a>
<p class="fr-header__service-tagline">baseline - précisions sur l'organisation</p>
</div>
</div>
<div class="fr-header__tools">
<div class="fr-header__tools-links">
<ul class="fr-btns-group">
<li>
<a href="[url - à modifier]" class="fr-btn--team fr-btn">Contact</a>
</li>
<li>
<a href="[url - à modifier]" class="fr-btn--briefcase fr-btn">Espace recruteur</a>
</li>
<li>
<a href="[url - à modifier]" class="fr-btn--account fr-btn">Espace particulier</a>
</li>
</ul>
</div>
</div>
</div>
</div>
</div>
<div class="fr-header__menu fr-modal" id="modal-3175" aria-labelledby="button-3176">
<div class="fr-container">
<button aria-controls="modal-3175" title="Fermer" type="button" id="button-3178" class="fr-btn--close fr-btn">Fermer</button>
<div class="fr-header__menu-links">
</div>
<nav class="fr-nav" id="navigation-3179" role="navigation" aria-label="Menu principal">
<ul class="fr-nav__list">
<li class="fr-nav__item">
<a id="nav-3180" type="link" href="#" class="fr-nav__link">accès direct nav-3180</a>
</li>
<li class="fr-nav__item">
<a id="nav-3181" type="link" href="#" class="fr-nav__link">accès direct nav-3181</a>
</li>
<li class="fr-nav__item">
<a id="nav-3182" type="link" href="#" class="fr-nav__link">accès direct nav-3182</a>
</li>
<li class="fr-nav__item">
<a id="nav-3183" type="link" href="#" class="fr-nav__link">accès direct nav-3183</a>
</li>
</ul>
</nav>
</div>
</div>
</header>


#### Header avec nom de service, recherche


Intitulé

officiel


Rechercher
Menu


[Nom du site / service](/)


Fermer


Rechercher


Rechercher


Fermer


-


-


-


-


###
Extrait de code


<header role="banner" class="fr-header">
<div class="fr-header__body">
<div class="fr-container">
<div class="fr-header__body-row">
<div class="fr-header__brand fr-enlarge-link">
<div class="fr-header__brand-top">
<div class="fr-header__logo">
<p class="fr-logo">
Intitulé
<br>officiel
</p>
</div>
<div class="fr-header__navbar">
<button data-fr-opened="false" aria-controls="modal-3201" title="Rechercher" type="button" id="button-3202" class="fr-btn--search fr-btn">Rechercher</button>
<button data-fr-opened="false" aria-controls="modal-3203" title="Menu" type="button" id="button-3204" class="fr-btn--menu fr-btn">Menu</button>
</div>
</div>
<div class="fr-header__service">
<a href="/" title="Accueil - [À MODIFIER - Nom du site / service] - Nom de l'entité (ministère, secrétariat d'état, gouvernement)">
<p class="fr-header__service-title">
Nom du site / service
</p>
</a>
</div>
</div>
<div class="fr-header__tools">
<div class="fr-header__search fr-modal" id="modal-3201" aria-labelledby="button-3202">
<div class="fr-container fr-container-lg--fluid">
<button aria-controls="modal-3201" title="Fermer" type="button" id="button-3206" class="fr-btn--close fr-btn">Fermer</button>
<div class="fr-search-bar" id="search-3200" role="search">
<label class="fr-label" for="search-3200-input">
Rechercher
</label>
<input class="fr-input" aria-describedby="search-3200-input-messages" placeholder="Rechercher" id="search-3200-input" type="search">
<div class="fr-messages-group" id="search-3200-input-messages" aria-live="polite">
</div>
<button title="Rechercher" type="button" id="search-btn-3208" class="fr-btn">Rechercher</button>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
<div class="fr-header__menu fr-modal" id="modal-3203" aria-labelledby="button-3204">
<div class="fr-container">
<button aria-controls="modal-3203" title="Fermer" type="button" id="button-3209" class="fr-btn--close fr-btn">Fermer</button>
<div class="fr-header__menu-links">
</div>
<nav class="fr-nav" id="navigation-3210" role="navigation" aria-label="Menu principal">
<ul class="fr-nav__list">
<li class="fr-nav__item">
<a id="nav-3211" type="link" href="#" class="fr-nav__link">accès direct nav-3211</a>
</li>
<li class="fr-nav__item">
<a id="nav-3212" type="link" href="#" class="fr-nav__link">accès direct nav-3212</a>
</li>
<li class="fr-nav__item">
<a id="nav-3213" type="link" href="#" class="fr-nav__link">accès direct nav-3213</a>
</li>
<li class="fr-nav__item">
<a id="nav-3214" type="link" href="#" class="fr-nav__link">accès direct nav-3214</a>
</li>
</ul>
</nav>
</div>
</div>
</header>


#### Header avec logo opérateur vertical, recherche


République

Française


[[À MODIFIER - texte alternatif de l'image]](/) [[À MODIFIER - texte alternatif de l'image](../../../example/img/placeholder.3x4.png)


Rechercher
Menu


Fermer


Rechercher


Rechercher


Fermer


-


-


-


-


###
Extrait de code


<header role="banner" class="fr-header">
<div class="fr-header__body">
<div class="fr-container">
<div class="fr-header__body-row">
<div class="fr-header__brand fr-enlarge-link">
<div class="fr-header__brand-top">
<div class="fr-header__logo">
<p class="fr-logo">
République
<br>Française
</p>
</div>
<div class="fr-header__operator">
<a href="/" title="Accueil - [À MODIFIER - texte alternatif de l'image : nom de l'opérateur ou du site serviciel] - République Française">
<img class="fr-responsive-img" style="max-width:3.5rem;" src="../../../example/img/placeholder.3x4.png" alt="[À MODIFIER - texte alternatif de l'image]" />
<!-- L'alternative de l'image (attribut alt) doit impérativement être renseignée et reprendre le texte visible dans l'image -->
</a>
</div>
<div class="fr-header__navbar">
<button data-fr-opened="false" aria-controls="modal-3232" title="Rechercher" type="button" id="button-3233" class="fr-btn--search fr-btn">Rechercher</button>
<button data-fr-opened="false" aria-controls="modal-3234" title="Menu" type="button" id="button-3235" class="fr-btn--menu fr-btn">Menu</button>
</div>
</div>
</div>
<div class="fr-header__tools">
<div class="fr-header__search fr-modal" id="modal-3232" aria-labelledby="button-3233">
<div class="fr-container fr-container-lg--fluid">
<button aria-controls="modal-3232" title="Fermer" type="button" id="button-3237" class="fr-btn--close fr-btn">Fermer</button>
<div class="fr-search-bar" id="search-3231" role="search">
<label class="fr-label" for="search-3231-input">
Rechercher
</label>
<input class="fr-input" aria-describedby="search-3231-input-messages" placeholder="Rechercher" id="search-3231-input" type="search">
<div class="fr-messages-group" id="search-3231-input-messages" aria-live="polite">
</div>
<button title="Rechercher" type="button" id="search-btn-3239" class="fr-btn">Rechercher</button>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
<div class="fr-header__menu fr-modal" id="modal-3234" aria-labelledby="button-3235">
<div class="fr-container">
<button aria-controls="modal-3234" title="Fermer" type="button" id="button-3240" class="fr-btn--close fr-btn">Fermer</button>
<div class="fr-header__menu-links">
</div>
<nav class="fr-nav" id="navigation-3241" role="navigation" aria-label="Menu principal">
<ul class="fr-nav__list">
<li class="fr-nav__item">
<a id="nav-3242" type="link" href="#" class="fr-nav__link">accès direct nav-3242</a>
</li>
<li class="fr-nav__item">
<a id="nav-3243" type="link" href="#" class="fr-nav__link">accès direct nav-3243</a>
</li>
<li class="fr-nav__item">
<a id="nav-3244" type="link" href="#" class="fr-nav__link">accès direct nav-3244</a>
</li>
<li class="fr-nav__item">
<a id="nav-3245" type="link" href="#" class="fr-nav__link">accès direct nav-3245</a>
</li>
</ul>
</nav>
</div>
</div>
</header>


#### Header avec logo opérateur horizontal, nom de service, lien d'accès, recherche


République

Française


![[À MODIFIER - texte alternatif de l'image]](../../../example/img/placeholder.16x9.png)


Rechercher
Menu


[Nom du site / service](/)


baseline - précisions sur l'organisation


-
[Contact](%5Burl%20-%20%C3%A0%20modifier%5D)


-
[Espace recruteur](%5Burl%20-%20%C3%A0%20modifier%5D)


-
[Espace particulier](%5Burl%20-%20%C3%A0%20modifier%5D)


Fermer


Rechercher


Rechercher


Fermer


-


-


-


-


###
Extrait de code


<header role="banner" class="fr-header">
<div class="fr-header__body">
<div class="fr-container">
<div class="fr-header__body-row">
<div class="fr-header__brand fr-enlarge-link">
<div class="fr-header__brand-top">
<div class="fr-header__logo">
<p class="fr-logo">
République
<br>Française
</p>
</div>
<div class="fr-header__operator">
<img class="fr-responsive-img" style="max-width:8rem;" src="../../../example/img/placeholder.16x9.png" alt="[À MODIFIER - texte alternatif de l'image]" />
<!-- L'alternative de l'image (attribut alt) doit impérativement être renseignée et reprendre le texte visible dans l'image -->
</div>
<div class="fr-header__navbar">
<button data-fr-opened="false" aria-controls="modal-3263" title="Rechercher" type="button" id="button-3264" class="fr-btn--search fr-btn">Rechercher</button>
<button data-fr-opened="false" aria-controls="modal-3265" title="Menu" type="button" id="button-3266" class="fr-btn--menu fr-btn">Menu</button>
</div>
</div>
<div class="fr-header__service">
<a href="/" title="Accueil - [À MODIFIER - Nom du site / service] - [À MODIFIER - texte alternatif de l'image : nom de l'opérateur ou du site serviciel] - République Française">
<p class="fr-header__service-title">
Nom du site / service
</p>
</a>
<p class="fr-header__service-tagline">baseline - précisions sur l'organisation</p>
</div>
</div>
<div class="fr-header__tools">
<div class="fr-header__tools-links">
<ul class="fr-btns-group">
<li>
<a href="[url - à modifier]" class="fr-btn--team fr-btn">Contact</a>
</li>
<li>
<a href="[url - à modifier]" class="fr-btn--briefcase fr-btn">Espace recruteur</a>
</li>
<li>
<a href="[url - à modifier]" class="fr-btn--account fr-btn">Espace particulier</a>
</li>
</ul>
</div>
<div class="fr-header__search fr-modal" id="modal-3263" aria-labelledby="button-3264">
<div class="fr-container fr-container-lg--fluid">
<button aria-controls="modal-3263" title="Fermer" type="button" id="button-3268" class="fr-btn--close fr-btn">Fermer</button>
<div class="fr-search-bar" id="search-3262" role="search">
<label class="fr-label" for="search-3262-input">
Rechercher
</label>
<input class="fr-input" aria-describedby="search-3262-input-messages" placeholder="Rechercher" id="search-3262-input" type="search">
<div class="fr-messages-group" id="search-3262-input-messages" aria-live="polite">
</div>
<button title="Rechercher" type="button" id="search-btn-3270" class="fr-btn">Rechercher</button>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
<div class="fr-header__menu fr-modal" id="modal-3265" aria-labelledby="button-3266">
<div class="fr-container">
<button aria-controls="modal-3265" title="Fermer" type="button" id="button-3271" class="fr-btn--close fr-btn">Fermer</button>
<div class="fr-header__menu-links">
</div>
<nav class="fr-nav" id="navigation-3272" role="navigation" aria-label="Menu principal">
<ul class="fr-nav__list">
<li class="fr-nav__item">
<a id="nav-3273" type="link" href="#" class="fr-nav__link">accès direct nav-3273</a>
</li>
<li class="fr-nav__item">
<a id="nav-3274" type="link" href="#" class="fr-nav__link">accès direct nav-3274</a>
</li>
<li class="fr-nav__item">
<a id="nav-3275" type="link" href="#" class="fr-nav__link">accès direct nav-3275</a>
</li>
<li class="fr-nav__item">
<a id="nav-3276" type="link" href="#" class="fr-nav__link">accès direct nav-3276</a>
</li>
</ul>
</nav>
</div>
</div>
</header>


#### Header avec raccourcis dupliqués, pour Angular, React et Vue


[Intitulé

officiel](/)


Menu


-
[Contact](%5Burl%20-%20%C3%A0%20modifier%5D)


-
[Espace recruteur](%5Burl%20-%20%C3%A0%20modifier%5D)


-
[Espace particulier](%5Burl%20-%20%C3%A0%20modifier%5D)


Fermer


-
[Contact](%5Burl%20-%20%C3%A0%20modifier%5D)


-
[Espace recruteur](%5Burl%20-%20%C3%A0%20modifier%5D)


-
[Espace particulier](%5Burl%20-%20%C3%A0%20modifier%5D)


###
Extrait de code


<header role="banner" class="fr-header">
<div class="fr-header__body">
<div class="fr-container">
<div class="fr-header__body-row">
<div class="fr-header__brand fr-enlarge-link">
<div class="fr-header__brand-top">
<div class="fr-header__logo">
<a href="/" title="Accueil - Nom de l'entité (ministère, secrétariat d'état, gouvernement)">
<p class="fr-logo">
Intitulé
<br>officiel
</p>
</a>
</div>
<div class="fr-header__navbar">
<button data-fr-opened="false" aria-controls="modal-3281" title="Menu" type="button" id="button-3282" class="fr-btn--menu fr-btn">Menu</button>
</div>
</div>
</div>
<div class="fr-header__tools">
<div class="fr-header__tools-links">
<ul class="fr-btns-group">
<li>
<a href="[url - à modifier]" class="fr-btn--team fr-btn">Contact</a>
</li>
<li>
<a href="[url - à modifier]" class="fr-btn--briefcase fr-btn">Espace recruteur</a>
</li>
<li>
<a href="[url - à modifier]" class="fr-btn--account fr-btn">Espace particulier</a>
</li>
</ul>
</div>
</div>
</div>
</div>
</div>
<div class="fr-header__menu fr-modal" id="modal-3281" aria-labelledby="button-3282">
<div class="fr-container">
<button aria-controls="modal-3281" title="Fermer" type="button" id="button-3283" class="fr-btn--close fr-btn">Fermer</button>
<div class="fr-header__menu-links">
<ul class="fr-btns-group">
<li>
<a href="[url - à modifier]" class="fr-btn--team fr-btn fr-btn">Contact</a>
</li>
<li>
<a href="[url - à modifier]" class="fr-btn--briefcase fr-btn fr-btn">Espace recruteur</a>
</li>
<li>
<a href="[url - à modifier]" class="fr-btn--account fr-btn fr-btn">Espace particulier</a>
</li>
</ul>
</div>
</div>
</div>
</header>


#### Header avec bandeau BETA


Intitulé

officiel


Rechercher
Menu


[Nom du site / service
BETA](/)


baseline - précisions sur l'organisation


-
[Contact](%5Burl%20-%20%C3%A0%20modifier%5D)


-
[Espace recruteur](%5Burl%20-%20%C3%A0%20modifier%5D)


-
[Espace particulier](%5Burl%20-%20%C3%A0%20modifier%5D)


Fermer


Rechercher


Rechercher


Fermer


-


-


-


-


###
Extrait de code


<header role="banner" class="fr-header">
<div class="fr-header__body">
<div class="fr-container">
<div class="fr-header__body-row">
<div class="fr-header__brand fr-enlarge-link">
<div class="fr-header__brand-top">
<div class="fr-header__logo">
<p class="fr-logo">
Intitulé
<br>officiel
</p>
</div>
<div class="fr-header__navbar">
<button data-fr-opened="false" aria-controls="modal-3301" title="Rechercher" type="button" id="button-3302" class="fr-btn--search fr-btn">Rechercher</button>
<button data-fr-opened="false" aria-controls="modal-3303" title="Menu" type="button" id="button-3304" class="fr-btn--menu fr-btn">Menu</button>
</div>
</div>
<div class="fr-header__service">
<a href="/" title="Accueil - [À MODIFIER - Nom du site / service] - Nom de l'entité (ministère, secrétariat d'état, gouvernement)">
<p class="fr-header__service-title">
Nom du site / service
<span class="fr-badge fr-badge--sm fr-badge--green-emeraude">BETA</span>
</p>
</a>
<p class="fr-header__service-tagline">baseline - précisions sur l'organisation</p>
</div>
</div>
<div class="fr-header__tools">
<div class="fr-header__tools-links">
<ul class="fr-btns-group">
<li>
<a href="[url - à modifier]" class="fr-btn--team fr-btn">Contact</a>
</li>
<li>
<a href="[url - à modifier]" class="fr-btn--briefcase fr-btn">Espace recruteur</a>
</li>
<li>
<a href="[url - à modifier]" class="fr-btn--account fr-btn">Espace particulier</a>
</li>
</ul>
</div>
<div class="fr-header__search fr-modal" id="modal-3301" aria-labelledby="button-3302">
<div class="fr-container fr-container-lg--fluid">
<button aria-controls="modal-3301" title="Fermer" type="button" id="button-3306" class="fr-btn--close fr-btn">Fermer</button>
<div class="fr-search-bar" id="search-3300" role="search">
<label class="fr-label" for="search-3300-input">
Rechercher
</label>
<input class="fr-input" aria-describedby="search-3300-input-messages" placeholder="Rechercher" id="search-3300-input" type="search">
<div class="fr-messages-group" id="search-3300-input-messages" aria-live="polite">
</div>
<button title="Rechercher" type="button" id="search-btn-3308" class="fr-btn">Rechercher</button>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
<div class="fr-header__menu fr-modal" id="modal-3303" aria-labelledby="button-3304">
<div class="fr-container">
<button aria-controls="modal-3303" title="Fermer" type="button" id="button-3309" class="fr-btn--close fr-btn">Fermer</button>
<div class="fr-header__menu-links">
</div>
<nav class="fr-nav" id="navigation-3310" role="navigation" aria-label="Menu principal">
<ul class="fr-nav__list">
<li class="fr-nav__item">
<a id="nav-3311" type="link" href="#" class="fr-nav__link">accès direct nav-3311</a>
</li>
<li class="fr-nav__item">
<a id="nav-3312" type="link" href="#" class="fr-nav__link">accès direct nav-3312</a>
</li>
<li class="fr-nav__item">
<a id="nav-3313" type="link" href="#" class="fr-nav__link">accès direct nav-3313</a>
</li>
<li class="fr-nav__item">
<a id="nav-3314" type="link" href="#" class="fr-nav__link">accès direct nav-3314</a>
</li>
</ul>
</nav>
</div>
</div>
</header>


#### Header logo opérateur + bandeau BETA


République

Française


![[À MODIFIER - texte alternatif de l'image]](../../../example/img/placeholder.16x9.png)


Rechercher
Menu


[Nom du site / service
BETA](/)


baseline - précisions sur l'organisation


-
[Contact](%5Burl%20-%20%C3%A0%20modifier%5D)


-
[Espace recruteur](%5Burl%20-%20%C3%A0%20modifier%5D)


-
[Espace particulier](%5Burl%20-%20%C3%A0%20modifier%5D)


Fermer


Rechercher


Rechercher


Fermer


-


-


-


-


###
Extrait de code


<header role="banner" class="fr-header">
<div class="fr-header__body">
<div class="fr-container">
<div class="fr-header__body-row">
<div class="fr-header__brand fr-enlarge-link">
<div class="fr-header__brand-top">
<div class="fr-header__logo">
<p class="fr-logo">
République
<br>Française
</p>
</div>
<div class="fr-header__operator">
<img class="fr-responsive-img" style="max-width:8rem;" src="../../../example/img/placeholder.16x9.png" alt="[À MODIFIER - texte alternatif de l'image]" />
<!-- L'alternative de l'image (attribut alt) doit impérativement être renseignée et reprendre le texte visible dans l'image -->
</div>
<div class="fr-header__navbar">
<button data-fr-opened="false" aria-controls="modal-3332" title="Rechercher" type="button" id="button-3333" class="fr-btn--search fr-btn">Rechercher</button>
<button data-fr-opened="false" aria-controls="modal-3334" title="Menu" type="button" id="button-3335" class="fr-btn--menu fr-btn">Menu</button>
</div>
</div>
<div class="fr-header__service">
<a href="/" title="Accueil - [À MODIFIER - Nom du site / service] - [À MODIFIER - texte alternatif de l'image : nom de l'opérateur ou du site serviciel] - République Française">
<p class="fr-header__service-title">
Nom du site / service
<span class="fr-badge fr-badge--sm fr-badge--green-emeraude">BETA</span>
</p>
</a>
<p class="fr-header__service-tagline">baseline - précisions sur l'organisation</p>
</div>
</div>
<div class="fr-header__tools">
<div class="fr-header__tools-links">
<ul class="fr-btns-group">
<li>
<a href="[url - à modifier]" class="fr-btn--team fr-btn">Contact</a>
</li>
<li>
<a href="[url - à modifier]" class="fr-btn--briefcase fr-btn">Espace recruteur</a>
</li>
<li>
<a href="[url - à modifier]" class="fr-btn--account fr-btn">Espace particulier</a>
</li>
</ul>
</div>
<div class="fr-header__search fr-modal" id="modal-3332" aria-labelledby="button-3333">
<div class="fr-container fr-container-lg--fluid">
<button aria-controls="modal-3332" title="Fermer" type="button" id="button-3337" class="fr-btn--close fr-btn">Fermer</button>
<div class="fr-search-bar" id="search-3331" role="search">
<label class="fr-label" for="search-3331-input">
Rechercher
</label>
<input class="fr-input" aria-describedby="search-3331-input-messages" placeholder="Rechercher" id="search-3331-input" type="search">
<div class="fr-messages-group" id="search-3331-input-messages" aria-live="polite">
</div>
<button title="Rechercher" type="button" id="search-btn-3339" class="fr-btn">Rechercher</button>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
<div class="fr-header__menu fr-modal" id="modal-3334" aria-labelledby="button-3335">
<div class="fr-container">
<button aria-controls="modal-3334" title="Fermer" type="button" id="button-3340" class="fr-btn--close fr-btn">Fermer</button>
<div class="fr-header__menu-links">
</div>
<nav class="fr-nav" id="navigation-3341" role="navigation" aria-label="Menu principal">
<ul class="fr-nav__list">
<li class="fr-nav__item">
<a id="nav-3342" type="link" href="#" class="fr-nav__link">accès direct nav-3342</a>
</li>
<li class="fr-nav__item">
<a id="nav-3343" type="link" href="#" class="fr-nav__link">accès direct nav-3343</a>
</li>
<li class="fr-nav__item">
<a id="nav-3344" type="link" href="#" class="fr-nav__link">accès direct nav-3344</a>
</li>
<li class="fr-nav__item">
<a id="nav-3345" type="link" href="#" class="fr-nav__link">accès direct nav-3345</a>
</li>
</ul>
</nav>
</div>
</div>
</header>


#### Header min avec bandeau BETA


[Intitulé

officiel](/)


Menu


BETA


Fermer


-


-


-


-


###
Extrait de code


<header role="banner" class="fr-header">
<div class="fr-header__body">
<div class="fr-container">
<div class="fr-header__body-row">
<div class="fr-header__brand fr-enlarge-link">
<div class="fr-header__brand-top">
<div class="fr-header__logo">
<a href="/" title="Accueil - Nom de l'entité (ministère, secrétariat d'état, gouvernement)">
<p class="fr-logo">
Intitulé
<br>officiel
</p>
</a>
</div>
<div class="fr-header__navbar">
<button data-fr-opened="false" aria-controls="modal-3356" title="Menu" type="button" id="button-3357" class="fr-btn--menu fr-btn">Menu</button>
</div>
</div>
<div class="fr-header__service">
<p class="fr-header__service-title">
<span class="fr-badge fr-badge--sm fr-badge--green-emeraude">BETA</span>
</p>
</div>
</div>
</div>
</div>
</div>
<div class="fr-header__menu fr-modal" id="modal-3356" aria-labelledby="button-3357">
<div class="fr-container">
<button aria-controls="modal-3356" title="Fermer" type="button" id="button-3359" class="fr-btn--close fr-btn">Fermer</button>
<div class="fr-header__menu-links">
</div>
<nav class="fr-nav" id="navigation-3360" role="navigation" aria-label="Menu principal">
<ul class="fr-nav__list">
<li class="fr-nav__item">
<a id="nav-3361" type="link" href="#" class="fr-nav__link">accès direct nav-3361</a>
</li>
<li class="fr-nav__item">
<a id="nav-3362" type="link" href="#" class="fr-nav__link">accès direct nav-3362</a>
</li>
<li class="fr-nav__item">
<a id="nav-3363" type="link" href="#" class="fr-nav__link">accès direct nav-3363</a>
</li>
<li class="fr-nav__item">
<a id="nav-3364" type="link" href="#" class="fr-nav__link">accès direct nav-3364</a>
</li>
</ul>
</nav>
</div>
</div>
</header>


## Dépréciation


Les exemples suivants sont dépréciés, ne pas utiliser comme référence

Pour support des versions précédentes


#### Header déprécié


Intitulé

officiel


Rechercher
Menu


[Nom du site / service](/)


baseline - précisions sur l'organisation


-
[Créer un espace](%5Burl%20-%20%C3%A0%20modifier%5D)


-
[Se connecter](%5Burl%20-%20%C3%A0%20modifier%5D)


-
[S'enregistrer](%5Burl%20-%20%C3%A0%20modifier%5D)


Fermer


Rechercher


Rechercher


Fermer


-
Entrée menu


-


-


-


-


-


-


-


-


-
Entrée mega menu


Fermer


#####


-


-


-


-


-


-


-


-


#####


-


-


-


-


-


-


-


-


#####


-


-


-


-


-


-


-


-


#####


-


-


-


-


-


-


-


-


-


-
Entrée menu


-


-


-


-


-


-


-


-


-
Entrée mega menu


Fermer


#### Titre éditorialisé


Lorem ipsum dolor sit amet, consectetur adipiscing, incididunt, ut labore et dolore magna aliqua. Vitae sapien pellentesque habitant morbi tristique senectus et. Diam maecenas sed enim ut. Accumsan lacus vel facilisis volutpat est. Ut aliquam purus sit amet luctus. Lorem ipsum dolor sit amet consectetur adipiscing elit ut.
[Voir toute la rubrique](%5Burl%20-%20%C3%A0%20modifier%5D)


#####


-


-


-


-


-


-


-


-


#####


-


-


-


-


-


-


-


-


#####


-


-


-


-


-


-


-


-


#####


-


-


-


-


-


-


-


-


-


-
Entrée mega menu


Fermer


#####


-


-


-


-


-


-


-


-


#####


-


-


-


-


-


-


-


-


#####


-


-


-


-


-


-


-


-


#####


-


-


-


-


-


-


-


-


-
Entrée menu


-


-


-


-


-


-


-


-


###
Extrait de code


<header role="banner" class="fr-header">
<div class="fr-header__body">
<div class="fr-container">
<div class="fr-header__body-row">
<div class="fr-header__brand fr-enlarge-link">
<div class="fr-header__brand-top">
<div class="fr-header__logo">
<p class="fr-logo">
Intitulé
<br>officiel
</p>
</div>
<div class="fr-header__navbar">
<button data-fr-opened="false" aria-controls="modal-3528" title="Rechercher" type="button" id="button-3529" class="fr-btn--search fr-btn">Rechercher</button>
<button data-fr-opened="false" aria-controls="modal-3530" title="Menu" type="button" id="button-3531" class="fr-btn--menu fr-btn">Menu</button>
</div>
</div>
<div class="fr-header__service">
<a href="/" title="Accueil - [À MODIFIER - Nom du site / service] - [À MODIFIER - nom de l'entité (ministère, secrétariat d'état, gouvernement)]">
<p class="fr-header__service-title">Nom du site / service</p>
</a>
<p class="fr-header__service-tagline">baseline - précisions sur l'organisation</p>
</div>
</div>
<div class="fr-header__tools">
<div class="fr-header__tools-links">
<ul class="fr-links-group">
<li>
<a id="link-3533" href="[url - à modifier]" class="fr-link fr-icon-add-circle-line">Créer un espace</a>
</li>
<li>
<a id="link-3534" href="[url - à modifier]" class="fr-link fr-icon-lock-line">Se connecter</a>
</li>
<li>
<a id="link-3535" href="[url - à modifier]" class="fr-link fr-icon-account-line">S'enregistrer</a>
</li>
</ul>
</div>
<div class="fr-header__search fr-modal" id="modal-3528" aria-labelledby="button-3529">
<div class="fr-container fr-container-lg--fluid">
<button class="fr-link--close fr-link" aria-controls="modal-3528">Fermer</button>
<div class="fr-search-bar" id="search-3527" role="search">
<label class="fr-label" for="search-3527-input">
Rechercher
</label>
<input class="fr-input" aria-describedby="search-3527-input-messages" placeholder="Rechercher" id="search-3527-input" type="search">
<div class="fr-messages-group" id="search-3527-input-messages" aria-live="polite">
</div>
<button title="Rechercher" type="button" id="search-btn-3537" class="fr-btn">Rechercher</button>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
<div class="fr-header__menu fr-modal" id="modal-3530" aria-labelledby="button-3531">
<div class="fr-container">
<button class="fr-link--close fr-link" aria-controls="modal-3530">Fermer</button>
<div class="fr-header__menu-links">
</div>
<nav class="fr-nav" id="navigation-3532" role="navigation" aria-label="Menu principal">
<ul class="fr-nav__list">
<li class="fr-nav__item">
<button id="menu-3538" aria-expanded="false" aria-controls="collapse-3539" type="button" class="fr-nav__btn">Entrée menu</button>
<div class="fr-collapse fr-menu" id="collapse-3539">
<ul class="fr-menu__list">
<li>
<a id="nav-3540" href="#" class="fr-nav__link">Lien de navigation nav-3540</a>
</li>
<li>
<a id="nav-3541" href="#" class="fr-nav__link">Lien de navigation nav-3541</a>
</li>
<li>
<a id="nav-3542" href="#" class="fr-nav__link">Lien de navigation nav-3542</a>
</li>
<li>
<a id="nav-3543" href="#" class="fr-nav__link">Lien de navigation nav-3543</a>
</li>
<li>
<a id="nav-3544" href="#" class="fr-nav__link">Lien de navigation nav-3544</a>
</li>
<li>
<a id="nav-3545" href="#" class="fr-nav__link">Lien de navigation nav-3545</a>
</li>
<li>
<a id="nav-3546" href="#" class="fr-nav__link">Lien de navigation nav-3546</a>
</li>
<li>
<a id="nav-3547" href="#" class="fr-nav__link">Lien de navigation nav-3547</a>
</li>
</ul>
</div>
</li>
<li class="fr-nav__item">
<button id="mega-menu-3548" aria-expanded="false" aria-controls="collapse-3549" type="button" class="fr-nav__btn">Entrée mega menu</button>
<div class="fr-collapse fr-mega-menu" id="collapse-3549">
<div class="fr-container fr-container--fluid fr-container-lg">
<div class="fr-grid-row fr-grid-row-lg--gutters">
<div class="fr-col-12 fr-mb-n3v">
<button aria-controls="collapse-3549" title="Fermer" type="button" id="button-3685" class="fr-btn--close fr-btn">Fermer</button>
</div>
<div class="fr-col-12 fr-col-lg-3">
<h5 class="fr-mega-menu__category">
<a id="category-3550" href="#" class="fr-nav__link">Nom de catégorie</a>
</h5>
<ul class="fr-mega-menu__list">
<li>
<a id="nav-3551" href="#" class="fr-nav__link">Lien de navigation nav-3551</a>
</li>
<li>
<a id="nav-3552" href="#" class="fr-nav__link">Lien de navigation nav-3552</a>
</li>
<li>
<a id="nav-3553" href="#" class="fr-nav__link">Lien de navigation nav-3553</a>
</li>
<li>
<a id="nav-3554" href="#" class="fr-nav__link">Lien de navigation nav-3554</a>
</li>
<li>
<a id="nav-3555" href="#" class="fr-nav__link">Lien de navigation nav-3555</a>
</li>
<li>
<a id="nav-3556" href="#" class="fr-nav__link">Lien de navigation nav-3556</a>
</li>
<li>
<a id="nav-3557" href="#" class="fr-nav__link">Lien de navigation nav-3557</a>
</li>
<li>
<a id="nav-3558" href="#" class="fr-nav__link">Lien de navigation nav-3558</a>
</li>
</ul>
</div>
<div class="fr-col-12 fr-col-lg-3">
<h5 class="fr-mega-menu__category">
<a id="category-3559" href="#" class="fr-nav__link">Nom de catégorie</a>
</h5>
<ul class="fr-mega-menu__list">
<li>
<a id="nav-3560" href="#" class="fr-nav__link">Lien de navigation nav-3560</a>
</li>
<li>
<a id="nav-3561" href="#" class="fr-nav__link">Lien de navigation nav-3561</a>
</li>
<li>
<a id="nav-3562" href="#" class="fr-nav__link">Lien de navigation nav-3562</a>
</li>
<li>
<a id="nav-3563" href="#" class="fr-nav__link">Lien de navigation nav-3563</a>
</li>
<li>
<a id="nav-3564" href="#" class="fr-nav__link">Lien de navigation nav-3564</a>
</li>
<li>
<a id="nav-3565" href="#" class="fr-nav__link">Lien de navigation nav-3565</a>
</li>
<li>
<a id="nav-3566" href="#" class="fr-nav__link">Lien de navigation nav-3566</a>
</li>
<li>
<a id="nav-3567" href="#" class="fr-nav__link">Lien de navigation nav-3567</a>
</li>
</ul>
</div>
<div class="fr-col-12 fr-col-lg-3">
<h5 class="fr-mega-menu__category">
<a id="category-3568" href="#" class="fr-nav__link">Nom de catégorie</a>
</h5>
<ul class="fr-mega-menu__list">
<li>
<a id="nav-3569" href="#" class="fr-nav__link">Lien de navigation nav-3569</a>
</li>
<li>
<a id="nav-3570" href="#" class="fr-nav__link">Lien de navigation nav-3570</a>
</li>
<li>
<a id="nav-3571" aria-current="page" href="#" class="fr-nav__link">Lien de navigation nav-3571</a>
</li>
<li>
<a id="nav-3572" href="#" class="fr-nav__link">Lien de navigation nav-3572</a>
</li>
<li>
<a id="nav-3573" href="#" class="fr-nav__link">Lien de navigation nav-3573</a>
</li>
<li>
<a id="nav-3574" href="#" class="fr-nav__link">Lien de navigation nav-3574</a>
</li>
<li>
<a id="nav-3575" href="#" class="fr-nav__link">Lien de navigation nav-3575</a>
</li>
<li>
<a id="nav-3576" href="#" class="fr-nav__link">Lien de navigation nav-3576</a>
</li>
</ul>
</div>
<div class="fr-col-12 fr-col-lg-3">
<h5 class="fr-mega-menu__category">
<a id="category-3577" href="#" class="fr-nav__link">Nom de catégorie</a>
</h5>
<ul class="fr-mega-menu__list">
<li>
<a id="nav-3578" href="#" class="fr-nav__link">Lien de navigation nav-3578</a>
</li>
<li>
<a id="nav-3579" href="#" class="fr-nav__link">Lien de navigation nav-3579</a>
</li>
<li>
<a id="nav-3580" href="#" class="fr-nav__link">Lien de navigation nav-3580</a>
</li>
<li>
<a id="nav-3581" href="#" class="fr-nav__link">Lien de navigation nav-3581</a>
</li>
<li>
<a id="nav-3582" href="#" class="fr-nav__link">Lien de navigation nav-3582</a>
</li>
<li>
<a id="nav-3583" href="#" class="fr-nav__link">Lien de navigation nav-3583</a>
</li>
<li>
<a id="nav-3584" href="#" class="fr-nav__link">Lien de navigation nav-3584</a>
</li>
<li>
<a id="nav-3585" href="#" class="fr-nav__link">Lien de navigation nav-3585</a>
</li>
</ul>
</div>
</div>
</div>
</div>
</li>
<li class="fr-nav__item">
<a id="nav-3586" type="link" href="#" class="fr-nav__link">accès direct nav-3586</a>
</li>
<li class="fr-nav__item">
<button id="menu-3587" aria-expanded="false" aria-controls="collapse-3588" aria-current="true" type="button" class="fr-nav__btn">Entrée menu</button>
<div class="fr-collapse fr-menu" id="collapse-3588">
<ul class="fr-menu__list">
<li>
<a id="nav-3589" href="#" class="fr-nav__link">Lien de navigation nav-3589</a>
</li>
<li>
<a id="nav-3590" href="#" class="fr-nav__link">Lien de navigation nav-3590</a>
</li>
<li>
<a id="nav-3591" aria-current="page" href="#" class="fr-nav__link">Lien de navigation nav-3591</a>
</li>
<li>
<a id="nav-3592" href="#" class="fr-nav__link">Lien de navigation nav-3592</a>
</li>
<li>
<a id="nav-3593" href="#" class="fr-nav__link">Lien de navigation nav-3593</a>
</li>
<li>
<a id="nav-3594" href="#" class="fr-nav__link">Lien de navigation nav-3594</a>
</li>
<li>
<a id="nav-3595" href="#" class="fr-nav__link">Lien de navigation nav-3595</a>
</li>
<li>
<a id="nav-3596" href="#" class="fr-nav__link">Lien de navigation nav-3596</a>
</li>
</ul>
</div>
</li>
<li class="fr-nav__item">
<button id="mega-menu-3597" aria-expanded="false" aria-controls="collapse-3598" type="button" class="fr-nav__btn">Entrée mega menu</button>
<div class="fr-collapse fr-mega-menu" id="collapse-3598">
<div class="fr-container fr-container--fluid fr-container-lg">
<div class="fr-grid-row fr-grid-row-lg--gutters">
<div class="fr-col-12 fr-mb-n3v">
<button aria-controls="collapse-3598" title="Fermer" type="button" id="button-3686" class="fr-btn--close fr-btn">Fermer</button>
</div>
<div class="fr-col-12 fr-col-lg-8 fr-col-offset-lg-4--right">
<div class="fr-mega-menu__leader">
<h4 class="fr-h4 fr-mb-2v">Titre éditorialisé</h4>
<p class="fr-hidden fr-unhidden-lg">Lorem [...] elit ut.</p>
<a id="link-3599" href="[url - à modifier]" class="fr-link fr-icon-arrow-right-line fr-link--icon-right">Voir toute la rubrique</a>
</div>
</div>
<div class="fr-col-12 fr-col-lg-3">
<h5 class="fr-mega-menu__category">
<a id="category-3600" href="#" class="fr-nav__link">Nom de catégorie</a>
</h5>
<ul class="fr-mega-menu__list">
<li>
<a id="nav-3601" href="#" class="fr-nav__link">Lien de navigation nav-3601</a>
</li>
<li>
<a id="nav-3602" href="#" class="fr-nav__link">Lien de navigation nav-3602</a>
</li>
<li>
<a id="nav-3603" href="#" class="fr-nav__link">Lien de navigation nav-3603</a>
</li>
<li>
<a id="nav-3604" href="#" class="fr-nav__link">Lien de navigation nav-3604</a>
</li>
<li>
<a id="nav-3605" href="#" class="fr-nav__link">Lien de navigation nav-3605</a>
</li>
<li>
<a id="nav-3606" href="#" class="fr-nav__link">Lien de navigation nav-3606</a>
</li>
<li>
<a id="nav-3607" href="#" class="fr-nav__link">Lien de navigation nav-3607</a>
</li>
<li>
<a id="nav-3608" href="#" class="fr-nav__link">Lien de navigation nav-3608</a>
</li>
</ul>
</div>
<div class="fr-col-12 fr-col-lg-3">
<h5 class="fr-mega-menu__category">
<a id="category-3609" href="#" class="fr-nav__link">Nom de catégorie</a>
</h5>
<ul class="fr-mega-menu__list">
<li>
<a id="nav-3610" href="#" class="fr-nav__link">Lien de navigation nav-3610</a>
</li>
<li>
<a id="nav-3611" href="#" class="fr-nav__link">Lien de navigation nav-3611</a>
</li>
<li>
<a id="nav-3612" href="#" class="fr-nav__link">Lien de navigation nav-3612</a>
</li>
<li>
<a id="nav-3613" href="#" class="fr-nav__link">Lien de navigation nav-3613</a>
</li>
<li>
<a id="nav-3614" href="#" class="fr-nav__link">Lien de navigation nav-3614</a>
</li>
<li>
<a id="nav-3615" href="#" class="fr-nav__link">Lien de navigation nav-3615</a>
</li>
<li>
<a id="nav-3616" href="#" class="fr-nav__link">Lien de navigation nav-3616</a>
</li>
<li>
<a id="nav-3617" href="#" class="fr-nav__link">Lien de navigation nav-3617</a>
</li>
</ul>
</div>
<div class="fr-col-12 fr-col-lg-3">
<h5 class="fr-mega-menu__category">
<a id="category-3618" href="#" class="fr-nav__link">Nom de catégorie</a>
</h5>
<ul class="fr-mega-menu__list">
<li>
<a id="nav-3619" href="#" class="fr-nav__link">Lien de navigation nav-3619</a>
</li>
<li>
<a id="nav-3620" href="#" class="fr-nav__link">Lien de navigation nav-3620</a>
</li>
<li>
<a id="nav-3621" aria-current="page" href="#" class="fr-nav__link">Lien de navigation nav-3621</a>
</li>
<li>
<a id="nav-3622" href="#" class="fr-nav__link">Lien de navigation nav-3622</a>
</li>
<li>
<a id="nav-3623" href="#" class="fr-nav__link">Lien de navigation nav-3623</a>
</li>
<li>
<a id="nav-3624" href="#" class="fr-nav__link">Lien de navigation nav-3624</a>
</li>
<li>
<a id="nav-3625" href="#" class="fr-nav__link">Lien de navigation nav-3625</a>
</li>
<li>
<a id="nav-3626" href="#" class="fr-nav__link">Lien de navigation nav-3626</a>
</li>
</ul>
</div>
<div class="fr-col-12 fr-col-lg-3">
<h5 class="fr-mega-menu__category">
<a id="category-3627" href="#" class="fr-nav__link">Nom de catégorie</a>
</h5>
<ul class="fr-mega-menu__list">
<li>
<a id="nav-3628" href="#" class="fr-nav__link">Lien de navigation nav-3628</a>
</li>
<li>
<a id="nav-3629" href="#" class="fr-nav__link">Lien de navigation nav-3629</a>
</li>
<li>
<a id="nav-3630" href="#" class="fr-nav__link">Lien de navigation nav-3630</a>
</li>
<li>
<a id="nav-3631" href="#" class="fr-nav__link">Lien de navigation nav-3631</a>
</li>
<li>
<a id="nav-3632" href="#" class="fr-nav__link">Lien de navigation nav-3632</a>
</li>
<li>
<a id="nav-3633" href="#" class="fr-nav__link">Lien de navigation nav-3633</a>
</li>
<li>
<a id="nav-3634" href="#" class="fr-nav__link">Lien de navigation nav-3634</a>
</li>
<li>
<a id="nav-3635" href="#" class="fr-nav__link">Lien de navigation nav-3635</a>
</li>
</ul>
</div>
</div>
</div>
</div>
</li>
<li class="fr-nav__item">
<a id="nav-3636" type="link" href="#" class="fr-nav__link">accès direct nav-3636</a>
</li>
<li class="fr-nav__item">
<button id="mega-menu-3637" aria-expanded="false" aria-controls="collapse-3638" type="button" class="fr-nav__btn">Entrée mega menu</button>
<div class="fr-collapse fr-mega-menu" id="collapse-3638">
<div class="fr-container fr-container--fluid fr-container-lg">
<div class="fr-grid-row fr-grid-row-lg--gutters">
<div class="fr-col-12 fr-mb-n3v">
<button aria-controls="collapse-3638" title="Fermer" type="button" id="button-3687" class="fr-btn--close fr-btn">Fermer</button>
</div>
<div class="fr-col-12 fr-col-lg-3">
<h5 class="fr-mega-menu__category">
<a id="category-3639" href="#" class="fr-nav__link">Nom de catégorie</a>
</h5>
<ul class="fr-mega-menu__list">
<li>
<a id="nav-3640" href="#" class="fr-nav__link">Lien de navigation nav-3640</a>
</li>
<li>
<a id="nav-3641" href="#" class="fr-nav__link">Lien de navigation nav-3641</a>
</li>
<li>
<a id="nav-3642" href="#" class="fr-nav__link">Lien de navigation nav-3642</a>
</li>
<li>
<a id="nav-3643" href="#" class="fr-nav__link">Lien de navigation nav-3643</a>
</li>
<li>
<a id="nav-3644" href="#" class="fr-nav__link">Lien de navigation nav-3644</a>
</li>
<li>
<a id="nav-3645" href="#" class="fr-nav__link">Lien de navigation nav-3645</a>
</li>
<li>
<a id="nav-3646" href="#" class="fr-nav__link">Lien de navigation nav-3646</a>
</li>
<li>
<a id="nav-3647" href="#" class="fr-nav__link">Lien de navigation nav-3647</a>
</li>
</ul>
</div>
<div class="fr-col-12 fr-col-lg-3">
<h5 class="fr-mega-menu__category">
<a id="category-3648" href="#" class="fr-nav__link">Nom de catégorie</a>
</h5>
<ul class="fr-mega-menu__list">
<li>
<a id="nav-3649" href="#" class="fr-nav__link">Lien de navigation nav-3649</a>
</li>
<li>
<a id="nav-3650" href="#" class="fr-nav__link">Lien de navigation nav-3650</a>
</li>
<li>
<a id="nav-3651" href="#" class="fr-nav__link">Lien de navigation nav-3651</a>
</li>
<li>
<a id="nav-3652" href="#" class="fr-nav__link">Lien de navigation nav-3652</a>
</li>
<li>
<a id="nav-3653" href="#" class="fr-nav__link">Lien de navigation nav-3653</a>
</li>
<li>
<a id="nav-3654" href="#" class="fr-nav__link">Lien de navigation nav-3654</a>
</li>
<li>
<a id="nav-3655" href="#" class="fr-nav__link">Lien de navigation nav-3655</a>
</li>
<li>
<a id="nav-3656" href="#" class="fr-nav__link">Lien de navigation nav-3656</a>
</li>
</ul>
</div>
<div class="fr-col-12 fr-col-lg-3">
<h5 class="fr-mega-menu__category">
<a id="category-3657" href="#" class="fr-nav__link">Nom de catégorie</a>
</h5>
<ul class="fr-mega-menu__list">
<li>
<a id="nav-3658" href="#" class="fr-nav__link">Lien de navigation nav-3658</a>
</li>
<li>
<a id="nav-3659" href="#" class="fr-nav__link">Lien de navigation nav-3659</a>
</li>
<li>
<a id="nav-3660" aria-current="page" href="#" class="fr-nav__link">Lien de navigation nav-3660</a>
</li>
<li>
<a id="nav-3661" href="#" class="fr-nav__link">Lien de navigation nav-3661</a>
</li>
<li>
<a id="nav-3662" href="#" class="fr-nav__link">Lien de navigation nav-3662</a>
</li>
<li>
<a id="nav-3663" href="#" class="fr-nav__link">Lien de navigation nav-3663</a>
</li>
<li>
<a id="nav-3664" href="#" class="fr-nav__link">Lien de navigation nav-3664</a>
</li>
<li>
<a id="nav-3665" href="#" class="fr-nav__link">Lien de navigation nav-3665</a>
</li>
</ul>
</div>
<div class="fr-col-12 fr-col-lg-3">
<h5 class="fr-mega-menu__category">
<a id="category-3666" href="#" class="fr-nav__link">Nom de catégorie</a>
</h5>
<ul class="fr-mega-menu__list">
<li>
<a id="nav-3667" href="#" class="fr-nav__link">Lien de navigation nav-3667</a>
</li>
<li>
<a id="nav-3668" href="#" class="fr-nav__link">Lien de navigation nav-3668</a>
</li>
<li>
<a id="nav-3669" href="#" class="fr-nav__link">Lien de navigation nav-3669</a>
</li>
<li>
<a id="nav-3670" href="#" class="fr-nav__link">Lien de navigation nav-3670</a>
</li>
<li>
<a id="nav-3671" href="#" class="fr-nav__link">Lien de navigation nav-3671</a>
</li>
<li>
<a id="nav-3672" href="#" class="fr-nav__link">Lien de navigation nav-3672</a>
</li>
<li>
<a id="nav-3673" href="#" class="fr-nav__link">Lien de navigation nav-3673</a>
</li>
<li>
<a id="nav-3674" href="#" class="fr-nav__link">Lien de navigation nav-3674</a>
</li>
</ul>
</div>
</div>
</div>
</div>
</li>
<li class="fr-nav__item">
<button id="menu-3675" aria-expanded="false" aria-controls="collapse-3676" type="button" class="fr-nav__btn">Entrée menu</button>
<div class="fr-collapse fr-menu" id="collapse-3676">
<ul class="fr-menu__list">
<li>
<a id="nav-3677" href="#" class="fr-nav__link">Lien de navigation nav-3677</a>
</li>
<li>
<a id="nav-3678" href="#" class="fr-nav__link">Lien de navigation nav-3678</a>
</li>
<li>
<a id="nav-3679" href="#" class="fr-nav__link">Lien de navigation nav-3679</a>
</li>
<li>
<a id="nav-3680" href="#" class="fr-nav__link">Lien de navigation nav-3680</a>
</li>
<li>
<a id="nav-3681" href="#" class="fr-nav__link">Lien de navigation nav-3681</a>
</li>
<li>
<a id="nav-3682" href="#" class="fr-nav__link">Lien de navigation nav-3682</a>
</li>
<li>
<a id="nav-3683" href="#" class="fr-nav__link">Lien de navigation nav-3683</a>
</li>
<li>
<a id="nav-3684" href="#" class="fr-nav__link">Lien de navigation nav-3684</a>
</li>
</ul>
</div>
</li>
</ul>
</nav>
</div>
</div>
</header>


Libellé bouton


Fermer


##
Paramètres d'affichage


Choisissez un thème pour personnaliser l'apparence du site.


Thème clair


Thème sombre


Système
Utilise les paramètres système
