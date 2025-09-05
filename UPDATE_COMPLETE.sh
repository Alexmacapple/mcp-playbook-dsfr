#!/bin/bash

#################################################
# MISE À JOUR ULTRA COMPLÈTE DSFR
# Combine : GitHub + Storybook + NPM
#################################################

# Couleurs
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
MAGENTA='\033[0;35m'
NC='\033[0m'

echo -e "${MAGENTA}╔════════════════════════════════════════════════════╗"
echo -e "║     📚 MISE À JOUR ULTRA COMPLÈTE DSFR            ║"
echo -e "║     GitHub + Storybook + NPM                      ║"
echo -e "╚════════════════════════════════════════════════════╝${NC}"
echo

# Vérifier les dépendances
echo -e "${BLUE}🔍 Vérification des dépendances...${NC}"

# Git
if ! command -v git &> /dev/null; then
    echo -e "${RED}❌ Git non installé${NC}"
    echo "   Installer avec : brew install git"
    exit 1
fi
echo -e "   ✅ Git"

# Python3
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ Python3 non installé${NC}"
    exit 1
fi
echo -e "   ✅ Python3"

# NPM
if ! command -v npm &> /dev/null; then
    echo -e "${RED}❌ npm non installé${NC}"
    exit 1
fi
echo -e "   ✅ NPM"

echo
echo -e "${CYAN}📊 Cette mise à jour va :${NC}"
echo "   1. Cloner le dépôt GitHub DSFR"
echo "   2. Extraire le code source (SCSS, JS, Templates)"
echo "   3. Récupérer la documentation Storybook"
echo "   4. Fusionner toutes les sources"
echo "   5. Générer une documentation ULTRA COMPLÈTE"
echo
echo -e "${YELLOW}⏱️  Durée estimée : 2-3 minutes${NC}"
echo

read -p "Voulez-vous continuer ? (o/n) : " confirm

if [ "$confirm" != "o" ]; then
    echo -e "${YELLOW}Mise à jour annulée${NC}"
    exit 0
fi

echo
echo -e "${BLUE}🚀 Lancement de la mise à jour...${NC}"
echo

# Créer le dossier docs si nécessaire
mkdir -p docs

# Lancer le script Python
python3 scripts/update_complete.py

if [ $? -eq 0 ]; then
    echo
    echo -e "${GREEN}╔════════════════════════════════════════════════════╗${NC}"
    echo -e "${GREEN}║     ✅ MISE À JOUR TERMINÉE AVEC SUCCÈS !         ║${NC}"
    echo -e "${GREEN}╚════════════════════════════════════════════════════╝${NC}"
    echo
    
    # Afficher le dernier fichier créé
    LATEST_FILE=$(ls -t docs/*ULTRA_COMPLETE*.md 2>/dev/null | head -1)
    if [ -n "$LATEST_FILE" ]; then
        SIZE=$(du -h "$LATEST_FILE" | cut -f1)
        echo -e "${CYAN}📄 Documentation générée :${NC}"
        echo "   $LATEST_FILE"
        echo "   Taille : $SIZE"
        
        # Compter les composants
        COMP_COUNT=$(grep -c "^## 🔹" "$LATEST_FILE" 2>/dev/null || echo "?")
        echo "   Composants : $COMP_COUNT"
    fi
    
    echo
    echo -e "${BLUE}✨ La documentation contient :${NC}"
    echo "   • Code source complet (SCSS, JS)"
    echo "   • Templates HTML"
    echo "   • Documentation Storybook interactive"
    echo "   • Exemples d'utilisation"
    echo "   • Variables CSS et API JavaScript"
    echo "   • Liens vers GitHub et Storybook"
    
    echo
    echo -e "${CYAN}📖 Pour consulter :${NC}"
    echo "   cat $LATEST_FILE | less"
    
else
    echo
    echo -e "${RED}❌ Erreur lors de la mise à jour${NC}"
    echo "   Consultez les logs ci-dessus"
    exit 1
fi