"""
Service des ressources design DSFR.
Fournit couleurs, icônes et thèmes officiels.
Clean Code : SOLID, DRY, KISS
"""

from typing import Dict, List, Optional, Any


class DesignService:
    """
    Service pour les ressources design DSFR.
    Responsabilité unique : Gérer couleurs, icônes et thèmes (S de SOLID).
    """
    
    def __init__(self):
        """Initialise le service avec les ressources design."""
        self.colors = self._init_colors()
        self.icons = self._init_icons()
        self.spacing = self._init_spacing()
        self.typography = self._init_typography()
    
    def _init_colors(self) -> Dict[str, Dict[str, str]]:
        """
        Initialise la palette de couleurs DSFR v1.14.
        Source: https://www.systeme-de-design.gouv.fr/elements-d-interface/fondamentaux-de-l-identite-de-l-etat/couleurs-palette
        """
        return {
            # Couleurs principales
            "primary": {
                "blue-france": "#000091",
                "blue-france-sun-113": "#000091",
                "blue-france-sun-113-hover": "#1212ff",
                "blue-france-975": "#f5f5fe",
                "blue-france-950": "#ececfe",
                "blue-france-925": "#e3e3fd",
                "blue-france-850": "#cacafb",
                "blue-france-750": "#a1a1f5",
                "blue-france-625": "#7575e8",
                "blue-france-425": "#4545d6",
                "blue-france-main-525": "#6a6af4"
            },
            
            # Couleurs système
            "system": {
                "success-425": "#18753c",
                "success-425-hover": "#1e9d4d",
                "success-950": "#b8fec9",
                "success-925": "#46fd89",
                "error-425": "#ce0500",
                "error-425-hover": "#ff0700",
                "error-950": "#ffe9e9",
                "error-925": "#ffbfbf",
                "warning-425": "#b34000",
                "warning-425-hover": "#ff5800",
                "warning-950": "#ffe9e5",
                "warning-925": "#ffb39a",
                "info-425": "#0063cb",
                "info-425-hover": "#0088ff",
                "info-950": "#e8edff",
                "info-925": "#b3c4ff"
            },
            
            # Gris
            "grey": {
                "grey-1000": "#161616",
                "grey-975": "#2a2a2a",
                "grey-950": "#3a3a3a",
                "grey-900": "#4d4d4d",
                "grey-850": "#5c5c5c",
                "grey-800": "#6a6a6a",
                "grey-750": "#777777",
                "grey-700": "#848484",
                "grey-625": "#999999",
                "grey-600": "#9e9e9e",
                "grey-500": "#adadad",
                "grey-425": "#c1c1c1",
                "grey-400": "#c5c5c5",
                "grey-300": "#d5d5d5",
                "grey-200": "#e5e5e5",
                "grey-100": "#f0f0f0",
                "grey-50": "#f8f8f8"
            },
            
            # Couleurs contextuelles
            "context": {
                "text-default": "#161616",
                "text-action": "#000091",
                "text-label": "#666666",
                "text-mention": "#666666",
                "text-inverted": "#f5f5fe",
                "text-title": "#161616",
                "background-default": "#ffffff",
                "background-alt": "#f6f6f6",
                "background-contrast": "#eeeeee",
                "background-disabled": "#e5e5e5",
                "background-raised": "#ffffff",
                "background-overlap": "#ffffff",
                "background-flat": "#e3e3fd",
                "background-action-low": "#e3e3fd",
                "background-action-high": "#000091"
            },
            
            # Bordures
            "border": {
                "default": "#dddddd",
                "disabled": "#e5e5e5",
                "plain": "#161616",
                "action": "#000091",
                "action-high": "#000091"
            }
        }
    
    def _init_icons(self) -> Dict[str, Dict[str, Any]]:
        """
        Initialise la bibliothèque d'icônes DSFR (Remix Icon).
        """
        return {
            # Navigation
            "navigation": {
                "arrow-left": {"class": "fr-icon-arrow-left-line", "category": "navigation"},
                "arrow-right": {"class": "fr-icon-arrow-right-line", "category": "navigation"},
                "arrow-up": {"class": "fr-icon-arrow-up-line", "category": "navigation"},
                "arrow-down": {"class": "fr-icon-arrow-down-line", "category": "navigation"},
                "arrow-go-back": {"class": "fr-icon-arrow-go-back-line", "category": "navigation"},
                "arrow-go-forward": {"class": "fr-icon-arrow-go-forward-line", "category": "navigation"},
                "close": {"class": "fr-icon-close-line", "category": "navigation"},
                "menu": {"class": "fr-icon-menu-line", "category": "navigation"},
                "home-4": {"class": "fr-icon-home-4-line", "category": "navigation"}
            },
            
            # Actions
            "action": {
                "add": {"class": "fr-icon-add-line", "category": "action"},
                "add-circle": {"class": "fr-icon-add-circle-line", "category": "action"},
                "check": {"class": "fr-icon-check-line", "category": "action"},
                "close-circle": {"class": "fr-icon-close-circle-line", "category": "action"},
                "delete": {"class": "fr-icon-delete-line", "category": "action"},
                "edit": {"class": "fr-icon-edit-line", "category": "action"},
                "refresh": {"class": "fr-icon-refresh-line", "category": "action"},
                "save": {"class": "fr-icon-save-line", "category": "action"},
                "search": {"class": "fr-icon-search-line", "category": "action"},
                "settings": {"class": "fr-icon-settings-5-line", "category": "action"},
                "share": {"class": "fr-icon-share-line", "category": "action"},
                "download": {"class": "fr-icon-download-line", "category": "action"},
                "upload": {"class": "fr-icon-upload-line", "category": "action"},
                "external-link": {"class": "fr-icon-external-link-line", "category": "action"},
                "link": {"class": "fr-icon-link", "category": "action"},
                "logout": {"class": "fr-icon-logout-box-r-line", "category": "action"},
                "lock": {"class": "fr-icon-lock-line", "category": "action"},
                "eye": {"class": "fr-icon-eye-line", "category": "action"},
                "eye-off": {"class": "fr-icon-eye-off-line", "category": "action"}
            },
            
            # Communication
            "communication": {
                "mail": {"class": "fr-icon-mail-line", "category": "communication"},
                "phone": {"class": "fr-icon-phone-line", "category": "communication"},
                "chat": {"class": "fr-icon-chat-3-line", "category": "communication"},
                "question": {"class": "fr-icon-question-line", "category": "communication"},
                "feedback": {"class": "fr-icon-feedback-line", "category": "communication"}
            },
            
            # Alertes
            "alert": {
                "info": {"class": "fr-icon-information-line", "category": "alert"},
                "success": {"class": "fr-icon-checkbox-circle-line", "category": "alert"},
                "warning": {"class": "fr-icon-warning-line", "category": "alert"},
                "error": {"class": "fr-icon-error-warning-line", "category": "alert"},
                "alert": {"class": "fr-icon-alert-line", "category": "alert"}
            },
            
            # Documents
            "document": {
                "file": {"class": "fr-icon-file-line", "category": "document"},
                "file-text": {"class": "fr-icon-file-text-line", "category": "document"},
                "file-pdf": {"class": "fr-icon-file-pdf-line", "category": "document"},
                "file-download": {"class": "fr-icon-file-download-line", "category": "document"},
                "folder": {"class": "fr-icon-folder-2-line", "category": "document"},
                "attachment": {"class": "fr-icon-attachment-line", "category": "document"}
            },
            
            # Utilisateur
            "user": {
                "user": {"class": "fr-icon-user-line", "category": "user"},
                "account": {"class": "fr-icon-account-line", "category": "user"},
                "team": {"class": "fr-icon-team-line", "category": "user"},
                "group": {"class": "fr-icon-group-line", "category": "user"}
            },
            
            # Système
            "system": {
                "calendar": {"class": "fr-icon-calendar-line", "category": "system"},
                "time": {"class": "fr-icon-time-line", "category": "system"},
                "timer": {"class": "fr-icon-timer-line", "category": "system"},
                "database": {"class": "fr-icon-database-line", "category": "system"},
                "clipboard": {"class": "fr-icon-clipboard-line", "category": "system"},
                "code": {"class": "fr-icon-code-s-slash-line", "category": "system"},
                "terminal": {"class": "fr-icon-terminal-box-line", "category": "system"},
                "bug": {"class": "fr-icon-bug-line", "category": "system"}
            },
            
            # Media
            "media": {
                "image": {"class": "fr-icon-image-line", "category": "media"},
                "video": {"class": "fr-icon-video-line", "category": "media"},
                "volume": {"class": "fr-icon-volume-up-line", "category": "media"},
                "fullscreen": {"class": "fr-icon-fullscreen-line", "category": "media"}
            },
            
            # Gouvernement
            "government": {
                "government": {"class": "fr-icon-government-line", "category": "government"},
                "france": {"class": "fr-icon-france-line", "category": "government"},
                "building": {"class": "fr-icon-building-line", "category": "government"}
            }
        }
    
    def _init_spacing(self) -> Dict[str, str]:
        """Initialise le système d'espacement DSFR."""
        return {
            "0": "0",
            "0v": "0",
            "0-5v": "0.125rem",
            "1v": "0.25rem", 
            "1w": "0.5rem",
            "1-5v": "0.375rem",
            "1-5w": "0.75rem",
            "2w": "1rem",
            "3w": "1.5rem",
            "4w": "2rem",
            "5w": "2.5rem",
            "6w": "3rem",
            "7w": "3.5rem",
            "8w": "4rem",
            "9w": "4.5rem",
            "10w": "5rem",
            "12w": "6rem",
            "15w": "7.5rem"
        }
    
    def _init_typography(self) -> Dict[str, Dict[str, str]]:
        """Initialise le système typographique DSFR."""
        return {
            "font-family": {
                "default": "Marianne, arial, sans-serif",
                "mono": "Courier New, Courier, monospace"
            },
            "font-size": {
                "xs": "0.75rem",    # 12px
                "sm": "0.875rem",   # 14px
                "md": "1rem",       # 16px
                "lg": "1.125rem",   # 18px
                "xl": "1.25rem",    # 20px
                "lead": "1.25rem"   # 20px
            },
            "line-height": {
                "xs": "1.125rem",   # 18px
                "sm": "1.25rem",    # 20px
                "md": "1.5rem",     # 24px
                "lg": "1.75rem",    # 28px
                "xl": "2rem"        # 32px
            },
            "font-weight": {
                "light": "300",
                "regular": "400",
                "medium": "500",
                "bold": "700"
            }
        }
    
    def get_colors(self, category: Optional[str] = None) -> Dict[str, Any]:
        """
        Récupère les couleurs DSFR.
        
        Args:
            category: Catégorie spécifique (primary, system, grey, etc.)
            
        Returns:
            Dictionnaire des couleurs
        """
        if category and category in self.colors:
            return self.colors[category]
        return self.colors
    
    def get_icons(self, category: Optional[str] = None, search: Optional[str] = None) -> Dict[str, Any]:
        """
        Récupère les icônes DSFR.
        
        Args:
            category: Catégorie spécifique
            search: Terme de recherche
            
        Returns:
            Dictionnaire des icônes
        """
        icons = {}
        
        # Filtrer par catégorie
        if category:
            for cat_name, cat_icons in self.icons.items():
                if cat_name == category:
                    icons.update(cat_icons)
        else:
            for cat_icons in self.icons.values():
                icons.update(cat_icons)
        
        # Recherche
        if search:
            search_lower = search.lower()
            icons = {
                name: data for name, data in icons.items()
                if search_lower in name.lower()
            }
        
        return icons
    
    def get_spacing(self) -> Dict[str, str]:
        """Récupère le système d'espacement."""
        return self.spacing
    
    def get_typography(self) -> Dict[str, Dict[str, str]]:
        """Récupère le système typographique."""
        return self.typography
    
    def create_theme(self, name: str, overrides: Dict[str, Any]) -> Dict[str, Any]:
        """
        Crée un thème personnalisé basé sur DSFR.
        
        Args:
            name: Nom du thème
            overrides: Surcharges de couleurs
            
        Returns:
            Configuration du thème
        """
        theme = {
            "name": name,
            "base": "dsfr",
            "colors": self.colors.copy(),
            "spacing": self.spacing.copy(),
            "typography": self.typography.copy()
        }
        
        # Appliquer les surcharges
        if "colors" in overrides:
            for category, colors in overrides["colors"].items():
                if category in theme["colors"]:
                    theme["colors"][category].update(colors)
        
        return theme


# Singleton
_instance: Optional[DesignService] = None

def get_design_service() -> DesignService:
    """Retourne l'instance singleton du DesignService."""
    global _instance
    if _instance is None:
        _instance = DesignService()
    return _instance