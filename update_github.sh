#!/bin/bash

#################################################
# Mise à jour DSFR depuis GitHub officiel
# Source : https://github.com/GouvernementFR/dsfr
#################################################

# Couleurs
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${BLUE}╔════════════════════════════════════════════╗"
echo -e "║   📦 Mise à jour DSFR depuis GitHub        ║"
echo -e "╚════════════════════════════════════════════╝${NC}"
echo

echo -e "${YELLOW}Source : https://github.com/GouvernementFR/dsfr${NC}"
echo

# Lancer le script Python
python3 scripts/update_from_github.py

if [ $? -eq 0 ]; then
    echo
    echo -e "${GREEN}✅ Documentation mise à jour depuis GitHub !${NC}"
    
    # Afficher les fichiers générés
    echo
    echo -e "${BLUE}📄 Fichiers générés :${NC}"
    ls -lh docs/*GITHUB*.md 2>/dev/null | tail -1
    ls -lh docs/*GITHUB*.json 2>/dev/null | tail -1
else
    echo -e "❌ Erreur lors de l'extraction"
fi