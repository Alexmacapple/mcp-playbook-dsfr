#!/bin/bash

#################################################
# Script de mise à jour de la documentation DSFR
# Extrait depuis Storybook + NPM
#################################################

# Couleurs
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${BLUE}╔════════════════════════════════════════════╗"
echo -e "║   Mise à jour Documentation DSFR          ║"
echo -e "╚════════════════════════════════════════════╝${NC}"
echo

# Vérifier Python
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ Python3 non installé${NC}"
    exit 1
fi

# Vérifier npm
if ! command -v npm &> /dev/null; then
    echo -e "${RED}❌ npm non installé${NC}"
    exit 1
fi

# 1. Vérifier la version actuelle
echo -e "${BLUE}📊 Vérification de la version actuelle...${NC}"
CURRENT_VERSION=$(grep -o "DSFR v[0-9.]*" docs/*.md 2>/dev/null | head -1 | cut -d'v' -f2)
echo -e "   Version locale : ${YELLOW}${CURRENT_VERSION:-Non trouvée}${NC}"

# 2. Vérifier la dernière version NPM
echo -e "${BLUE}📦 Vérification de la version NPM...${NC}"
LATEST_VERSION=$(npm view @gouvfr/dsfr version 2>/dev/null)
echo -e "   Version NPM : ${GREEN}${LATEST_VERSION}${NC}"

# 3. Comparer les versions
if [ "$CURRENT_VERSION" = "$LATEST_VERSION" ]; then
    echo -e "${GREEN}✅ Documentation déjà à jour${NC}"
    echo
    read -p "Voulez-vous forcer la mise à jour ? (o/n) : " force
    if [ "$force" != "o" ]; then
        exit 0
    fi
fi

# 4. Demander confirmation
echo
echo -e "${YELLOW}Une mise à jour est disponible !${NC}"
echo -e "  ${CURRENT_VERSION:-?} → ${LATEST_VERSION}"
echo
read -p "Voulez-vous mettre à jour ? (o/n) : " confirm

if [ "$confirm" != "o" ]; then
    echo -e "${YELLOW}Mise à jour annulée${NC}"
    exit 0
fi

# 5. Installer/mettre à jour le package NPM
echo
echo -e "${BLUE}📥 Installation du package DSFR...${NC}"
npm install @gouvfr/dsfr@latest --save 2>/dev/null

if [ $? -ne 0 ]; then
    echo -e "${RED}❌ Erreur lors de l'installation NPM${NC}"
    exit 1
fi

# 6. Lancer le script Python de mise à jour
echo
echo -e "${BLUE}🔄 Extraction de la documentation...${NC}"
echo -e "${YELLOW}Cela peut prendre quelques minutes...${NC}"
echo

cd "$(dirname "$0")"

# Créer le dossier scripts s'il n'existe pas
mkdir -p scripts

# Vérifier que le script Python existe
if [ ! -f "scripts/update_from_storybook.py" ]; then
    echo -e "${RED}❌ Script Python non trouvé${NC}"
    echo "   Attendu : scripts/update_from_storybook.py"
    exit 1
fi

# Lancer l'extraction
python3 scripts/update_from_storybook.py

if [ $? -eq 0 ]; then
    echo
    echo -e "${GREEN}╔════════════════════════════════════════════╗${NC}"
    echo -e "${GREEN}║   ✅ Mise à jour terminée avec succès !    ║${NC}"
    echo -e "${GREEN}╚════════════════════════════════════════════╝${NC}"
    echo
    
    # Afficher les nouveaux fichiers
    echo -e "${BLUE}📄 Fichiers générés :${NC}"
    ls -lh docs/*UPDATED*.md 2>/dev/null | tail -1
    ls -lh docs/*DATA*.json 2>/dev/null | tail -1
    
    echo
    echo -e "${BLUE}Pour utiliser la nouvelle documentation :${NC}"
    echo "  ./dsfr-agent"
    
    # Proposer de supprimer les anciennes versions
    echo
    read -p "Voulez-vous archiver les anciennes versions ? (o/n) : " archive
    if [ "$archive" = "o" ]; then
        mkdir -p docs/archives
        mv docs/*_UPDATED_*.md docs/archives/ 2>/dev/null
        mv docs/*_DATA_*.json docs/archives/ 2>/dev/null
        echo -e "${GREEN}✅ Anciennes versions archivées dans docs/archives/${NC}"
    fi
    
else
    echo
    echo -e "${RED}❌ Erreur lors de la mise à jour${NC}"
    echo "   Consultez les logs ci-dessus pour plus de détails"
    exit 1
fi

# 7. Nettoyer node_modules si trop gros
NODE_SIZE=$(du -sh node_modules 2>/dev/null | cut -f1)
echo
echo -e "${BLUE}📊 Taille de node_modules : ${NODE_SIZE:-0}${NC}"

if [ -d "node_modules" ]; then
    read -p "Voulez-vous supprimer node_modules pour économiser l'espace ? (o/n) : " clean
    if [ "$clean" = "o" ]; then
        rm -rf node_modules
        echo -e "${GREEN}✅ node_modules supprimé${NC}"
    fi
fi

echo
echo -e "${GREEN}✨ Tout est prêt !${NC}"