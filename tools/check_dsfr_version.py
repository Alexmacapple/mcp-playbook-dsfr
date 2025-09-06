#!/usr/bin/env python3
"""
Script simple pour vérifier si une nouvelle version DSFR est disponible
"""

import json
import sys

def check_dsfr_version():
    """Vérifie la dernière version DSFR sur GitHub"""
    
    # Version actuelle dans votre projet
    CURRENT_VERSION = "v1.14.1"
    
    try:
        import urllib.request
        
        # Récupérer la dernière release depuis GitHub API
        url = "https://api.github.com/repos/GouvernementFR/dsfr/releases/latest"
        
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            latest_version = data.get("tag_name", "unknown")
            release_date = data.get("published_at", "").split("T")[0]
            release_url = data.get("html_url", "")
        
        print("=" * 50)
        print("   Vérification de version DSFR")
        print("=" * 50)
        print()
        print(f"Version actuelle du projet : {CURRENT_VERSION}")
        print(f"Dernière version disponible : {latest_version}")
        
        if latest_version != CURRENT_VERSION:
            print()
            print("[ATTENTION] Une nouvelle version est disponible !")
            print(f"Date de sortie : {release_date}")
            print(f"Voir les changements : {release_url}")
            print()
            print("Pour mettre à jour :")
            print("1. Consultez les notes de version")
            print("2. Téléchargez les nouveaux composants si nécessaire")
            print("3. Testez avec votre projet MCP")
            return 1
        else:
            print()
            print("[OK] Votre projet utilise la dernière version DSFR")
            return 0
            
    except Exception as e:
        print(f"[ERREUR] Impossible de vérifier la version : {e}")
        print("Vérifiez manuellement sur : https://github.com/GouvernementFR/dsfr/releases")
        return 2

if __name__ == "__main__":
    sys.exit(check_dsfr_version())