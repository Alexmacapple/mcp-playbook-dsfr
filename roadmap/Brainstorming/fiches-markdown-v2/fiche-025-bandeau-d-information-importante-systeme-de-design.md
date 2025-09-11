URL:
https://main--ds-gouv.netlify.app/example/component/notice

Title:
Bandeau d'information importante - Système de design

Markdown:

Bandeau d'information importante - Système de design


DSFR v1.14.0


[Retour](../)


# Bandeau d'information importante (notice)


Le bandeau d'information importante permet aux utilisateurs de voir ou d'accéder à une information importante et temporaire.
[Documentation](https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/bandeau-d-information-importante)


## Contenu des Bandeaux d'information importante


Le bandeau doit être placé sur toutes les pages du site.

La balise <p> peut être remplacée par un niveau de titre hx suivant le contexte.


#### Bandeau d'information minimum


Titre du bandeau d'information


###
Extrait de code


<div class="fr-notice fr-notice--info">
<div class="fr-container">
<div class="fr-notice__body">
<p>
<span class="fr-notice__title">Titre du bandeau d'information</span>
</p>
</div>
</div>
</div>


#### Bandeau d'information avec bouton fermer


Titre du bandeau

Masquer le message


###
Extrait de code


<div class="fr-notice fr-notice--info">
<div class="fr-container">
<div class="fr-notice__body">
<p>
<span class="fr-notice__title">Titre du bandeau</span>
</p>
<button title="Masquer le message" onclick="const notice = this.parentNode.parentNode.parentNode; notice.parentNode.removeChild(notice)" type="button" class="fr-btn--close fr-btn">Masquer le message</button>
</div>
</div>
</div>


#### Bandeau d'information sans icône


Titre du bandeau

Masquer le message


###
Extrait de code


<div class="fr-notice fr-notice--info fr-notice--no-icon">
<div class="fr-container">
<div class="fr-notice__body">
<p>
<span class="fr-notice__title">Titre du bandeau</span>
</p>
<button title="Masquer le message" onclick="const notice = this.parentNode.parentNode.parentNode; notice.parentNode.removeChild(notice)" type="button" class="fr-btn--close fr-btn">Masquer le message</button>
</div>
</div>
</div>


#### Bandeau d'information avec icone personnalisée


Titre du bandeau

Masquer le message


###
Extrait de code


<div class="fr-notice fr-notice--info">
<div class="fr-container">
<div class="fr-notice__body">
<p>
<span class="fr-notice__title fr-icon-virus-fill">Titre du bandeau</span>
</p>
<button title="Masquer le message" onclick="const notice = this.parentNode.parentNode.parentNode; notice.parentNode.removeChild(notice)" type="button" class="fr-btn--close fr-btn">Masquer le message</button>
</div>
</div>
</div>


#### Bandeau d'information cas max


Titre du bandeau assez long
Texte de description plutot long lorem ipsum sit consectetur adipiscing elit. Sed


Masquer le message


###
Extrait de code


<div class="fr-notice fr-notice--info">
<div class="fr-container">
<div class="fr-notice__body">
<p>
<span class="fr-notice__title">Titre du bandeau assez long</span>
<span class="fr-notice__desc">Texte de description plutot long lorem ipsum sit consectetur adipiscing elit. Sed</span>
<a title="Lien de consultation - nouvelle fenêtre" href="#" target="_blank" rel="noopener external" class="fr-notice__link">Lien de consultation</a>
</p>
<button title="Masquer le message" onclick="const notice = this.parentNode.parentNode.parentNode; notice.parentNode.removeChild(notice)" type="button" class="fr-btn--close fr-btn">Masquer le message</button>
</div>
</div>
</div>


## Bandeaux génériques


Il existe 3 bandeaux génériques utilisables en fonction du niveau de gravité de l'information. L'icône peut être modifiée et seul le titre est obligatoire


#### Bandeau d'information


Titre du bandeau d'information
Texte de description lorem ipsum sit consectetur adipiscing.


Masquer le message


###
Extrait de code


<div class="fr-notice fr-notice--info">
<div class="fr-container">
<div class="fr-notice__body">
<p>
<span class="fr-notice__title">Titre du bandeau d'information</span>
<span class="fr-notice__desc">Texte de description lorem ipsum sit consectetur adipiscing.</span>
<a title="Lien de consultation - nouvelle fenêtre" href="#" target="_blank" rel="noopener external" class="fr-notice__link">Lien de consultation</a>
</p>
<button title="Masquer le message" onclick="const notice = this.parentNode.parentNode.parentNode; notice.parentNode.removeChild(notice)" type="button" class="fr-btn--close fr-btn">Masquer le message</button>
</div>
</div>
</div>


#### Bandeau d'avertissement


Titre du bandeau d'avertissement
Texte de description lorem ipsum sit consectetur adipiscing.


Masquer le message


###
Extrait de code


<div class="fr-notice fr-notice--warning">
<div class="fr-container">
<div class="fr-notice__body">
<p>
<span class="fr-notice__title">Titre du bandeau d'avertissement</span>
<span class="fr-notice__desc">Texte de description lorem ipsum sit consectetur adipiscing.</span>
<a title="Lien de consultation - nouvelle fenêtre" href="#" target="_blank" rel="noopener external" class="fr-notice__link">Lien de consultation</a>
</p>
<button title="Masquer le message" onclick="const notice = this.parentNode.parentNode.parentNode; notice.parentNode.removeChild(notice)" type="button" class="fr-btn--close fr-btn">Masquer le message</button>
</div>
</div>
</div>


#### Bandeau d'alerte


Titre du bandeau d'alerte
Texte de description lorem ipsum sit consectetur adipiscing.


Masquer le message


###
Extrait de code


<div class="fr-notice fr-notice--alert">
<div class="fr-container">
<div class="fr-notice__body">
<p>
<span class="fr-notice__title">Titre du bandeau d'alerte</span>
<span class="fr-notice__desc">Texte de description lorem ipsum sit consectetur adipiscing.</span>
<a title="Lien de consultation - nouvelle fenêtre" href="#" target="_blank" rel="noopener external" class="fr-notice__link">Lien de consultation</a>
</p>
<button title="Masquer le message" onclick="const notice = this.parentNode.parentNode.parentNode; notice.parentNode.removeChild(notice)" type="button" class="fr-btn--close fr-btn">Masquer le message</button>
</div>
</div>
</div>


## Bandeaux vigilance météo


Il existe 3 bandeaux météo utilisables en fonction du niveau d'alerte météo. L'icône peut être modifiée et seul le titre est obligatoire


#### Vigilance météo orange


Vigilance météo orange
Texte de description lorem ipsum sit consectetur adipiscing.


Masquer le message


###
Extrait de code


<div class="fr-notice fr-notice--weather-orange">
<div class="fr-container">
<div class="fr-notice__body">
<p>
<span class="fr-notice__title">Vigilance météo orange</span>
<span class="fr-notice__desc">Texte de description lorem ipsum sit consectetur adipiscing.</span>
<a title="Lien de consultation - nouvelle fenêtre" href="#" target="_blank" rel="noopener external" class="fr-notice__link">Lien de consultation</a>
</p>
<button title="Masquer le message" onclick="const notice = this.parentNode.parentNode.parentNode; notice.parentNode.removeChild(notice)" type="button" class="fr-btn--close fr-btn">Masquer le message</button>
</div>
</div>
</div>


#### Vigilance météo rouge


Vigilance météo rouge
Texte de description lorem ipsum sit consectetur adipiscing.


Masquer le message


###
Extrait de code


<div class="fr-notice fr-notice--weather-red">
<div class="fr-container">
<div class="fr-notice__body">
<p>
<span class="fr-notice__title">Vigilance météo rouge</span>
<span class="fr-notice__desc">Texte de description lorem ipsum sit consectetur adipiscing.</span>
<a title="Lien de consultation - nouvelle fenêtre" href="#" target="_blank" rel="noopener external" class="fr-notice__link">Lien de consultation</a>
</p>
<button title="Masquer le message" onclick="const notice = this.parentNode.parentNode.parentNode; notice.parentNode.removeChild(notice)" type="button" class="fr-btn--close fr-btn">Masquer le message</button>
</div>
</div>
</div>


#### Vigilance météo violette


Vigilance météo violette
Texte de description lorem ipsum sit consectetur adipiscing.


Masquer le message


###
Extrait de code


<div class="fr-notice fr-notice--weather-purple">
<div class="fr-container">
<div class="fr-notice__body">
<p>
<span class="fr-notice__title">Vigilance météo violette</span>
<span class="fr-notice__desc">Texte de description lorem ipsum sit consectetur adipiscing.</span>
<a title="Lien de consultation - nouvelle fenêtre" href="#" target="_blank" rel="noopener external" class="fr-notice__link">Lien de consultation</a>
</p>
<button title="Masquer le message" onclick="const notice = this.parentNode.parentNode.parentNode; notice.parentNode.removeChild(notice)" type="button" class="fr-btn--close fr-btn">Masquer le message</button>
</div>
</div>
</div>


## Bandeaux d'alertes


Il existe 3 bandeaux d'alertes utilisables en fonction du type d'alerte. L'icône ne peut pas être modifiée et les intitulés officiels doivent être utilisés


#### Alerte attentat


Attentat en cours
Texte de description lorem ipsum sit consectetur adipiscing.


Masquer le message


###
Extrait de code


<div class="fr-notice fr-notice--attack">
<div class="fr-container">
<div class="fr-notice__body">
<p>
<span class="fr-notice__title">Attentat en cours</span>
<span class="fr-notice__desc">Texte de description lorem ipsum sit consectetur adipiscing.</span>
<a title="Lien de consultation - nouvelle fenêtre" href="#" target="_blank" rel="noopener external" class="fr-notice__link">Lien de consultation</a>
</p>
<button title="Masquer le message" onclick="const notice = this.parentNode.parentNode.parentNode; notice.parentNode.removeChild(notice)" type="button" class="fr-btn--close fr-btn">Masquer le message</button>
</div>
</div>
</div>


#### Appel à témoins


Appel à témoins
Texte de description lorem ipsum sit consectetur adipiscing.


Masquer le message


###
Extrait de code


<div class="fr-notice fr-notice--witness">
<div class="fr-container">
<div class="fr-notice__body">
<p>
<span class="fr-notice__title">Appel à témoins</span>
<span class="fr-notice__desc">Texte de description lorem ipsum sit consectetur adipiscing.</span>
<a title="Lien de consultation - nouvelle fenêtre" href="#" target="_blank" rel="noopener external" class="fr-notice__link">Lien de consultation</a>
</p>
<button title="Masquer le message" onclick="const notice = this.parentNode.parentNode.parentNode; notice.parentNode.removeChild(notice)" type="button" class="fr-btn--close fr-btn">Masquer le message</button>
</div>
</div>
</div>


#### Alerte technologique


Cyber-attaque
Texte de description lorem ipsum sit consectetur adipiscing.


Masquer le message


###
Extrait de code


<div class="fr-notice fr-notice--cyberattack">
<div class="fr-container">
<div class="fr-notice__body">
<p>
<span class="fr-notice__title">Cyber-attaque</span>
<span class="fr-notice__desc">Texte de description lorem ipsum sit consectetur adipiscing.</span>
<a title="Lien de consultation - nouvelle fenêtre" href="#" target="_blank" rel="noopener external" class="fr-notice__link">Lien de consultation</a>
</p>
<button title="Masquer le message" onclick="const notice = this.parentNode.parentNode.parentNode; notice.parentNode.removeChild(notice)" type="button" class="fr-btn--close fr-btn">Masquer le message</button>
</div>
</div>
</div>


## Mise en situation du placement du bandeau


Le bandeau doit être placé au début du contenu de la page, pour être le premier élément au clique sur le lien d'évitement "aller au contenu".


-
[Contenu](#content)


-
[Menu](#header-navigation)


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


Information importante


Voir le fil d'Ariane


1.
[Accueil](/)


2.
[Nom de la page](/segment-1/)


3.
[Nom de la page](/segment-1/segment-2/)


4.


## lorem, ipsum dolor sit amet


Lorem, ipsum dolor sit amet consectetur adipisicing elit. Inventore similique commodi sit eligendi, esse ab sapiente necessitatibus, consequatur delectus nobis doloribus rem libero, expedita blanditiis veritatis? Nobis doloribus possimus reprehenderit.


Libellé bouton


Fermer


##
Paramètres d'affichage


Choisissez un thème pour personnaliser l'apparence du site.


Thème clair


Thème sombre


Système
Utilise les paramètres système
