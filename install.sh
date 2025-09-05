#!/bin/bash

#################################################
#  Installation DSFR Agent                     #
#  Script d'installation automatique           #
#################################################

set -e

# Couleurs
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Variables
INSTALL_DIR="$(pwd)"
AGENT_NAME="dsfr-agent"

echo -e "${BLUE}╔═══════════════════════════════════════════════════════╗"
echo -e "║          Installation DSFR Agent v1.0                 ║"
echo -e "╚═══════════════════════════════════════════════════════╝${NC}"
echo

# Vérification des prérequis
echo -e "${YELLOW}Vérification des prérequis...${NC}"

# Vérifier bash
if ! command -v bash &> /dev/null; then
    echo -e "${RED}❌ Bash n'est pas installé${NC}"
    exit 1
fi

# Vérifier les CLI optionnels
echo -e "${BLUE}Détection des CLI...${NC}"
if command -v claude &> /dev/null; then
    echo -e "${GREEN}✓ Claude CLI détecté${NC}"
    CLAUDE_INSTALLED=true
else
    echo -e "${YELLOW}⚠ Claude CLI non détecté (optionnel)${NC}"
    CLAUDE_INSTALLED=false
fi

if command -v gemini &> /dev/null; then
    echo -e "${GREEN}✓ Gemini CLI détecté${NC}"
    GEMINI_INSTALLED=true
else
    echo -e "${YELLOW}⚠ Gemini CLI non détecté (optionnel)${NC}"
    GEMINI_INSTALLED=false
fi

# Créer la structure de dossiers
echo -e "${BLUE}Création de la structure...${NC}"
mkdir -p config docs cache scripts

# Vérifier que les fichiers essentiels existent
if [ ! -f "$AGENT_NAME" ]; then
    echo -e "${RED}❌ Le fichier $AGENT_NAME n'existe pas${NC}"
    exit 1
fi

# Rendre le script exécutable
chmod +x "$AGENT_NAME"
echo -e "${GREEN}✓ Script principal configuré${NC}"

# Déplacer les fichiers de documentation s'ils existent
echo -e "${BLUE}Organisation des fichiers...${NC}"
for file in DSFR_v1.14_PLAYBOOK_ULTRA_COMPLET.md DSFR_v1.14_Playbook_Exhaustif.md DSFR_v1.14_ALL_URLs_Complete.md DSFR_v1.14_NPM_Documentation.md; do
    if [ -f "$file" ]; then
        mv "$file" "docs/" 2>/dev/null || cp "$file" "docs/"
        echo -e "${GREEN}✓ $file déplacé dans docs/${NC}"
    fi
done

# Déplacer les scripts Python s'ils existent
for script in extract_npm_documentation.py compile_final_playbook.py split_for_llm.py; do
    if [ -f "$script" ]; then
        mv "$script" "scripts/" 2>/dev/null || cp "$script" "scripts/"
        echo -e "${GREEN}✓ $script déplacé dans scripts/${NC}"
    fi
done

# Proposer d'installer un alias global
echo
echo -e "${YELLOW}Souhaitez-vous créer un alias global 'dsfr' ?${NC}"
echo -e "Cela permettra d'utiliser 'dsfr' depuis n'importe où"
read -p "Installer l'alias ? (o/N): " install_alias

if [[ "$install_alias" =~ ^[Oo]$ ]]; then
    SHELL_RC=""
    
    # Détecter le shell
    if [ -f "$HOME/.zshrc" ]; then
        SHELL_RC="$HOME/.zshrc"
    elif [ -f "$HOME/.bashrc" ]; then
        SHELL_RC="$HOME/.bashrc"
    fi
    
    if [ -n "$SHELL_RC" ]; then
        # Ajouter l'alias
        echo "" >> "$SHELL_RC"
        echo "# DSFR Agent alias" >> "$SHELL_RC"
        echo "alias dsfr='$INSTALL_DIR/$AGENT_NAME'" >> "$SHELL_RC"
        echo -e "${GREEN}✓ Alias 'dsfr' ajouté à $SHELL_RC${NC}"
        echo -e "${YELLOW}  Rechargez votre shell: source $SHELL_RC${NC}"
    else
        echo -e "${YELLOW}⚠ Fichier de configuration shell non trouvé${NC}"
        echo -e "  Ajoutez manuellement à votre .bashrc ou .zshrc:"
        echo -e "  ${BLUE}alias dsfr='$INSTALL_DIR/$AGENT_NAME'${NC}"
    fi
fi

# Installation des dépendances optionnelles
echo
if [ "$CLAUDE_INSTALLED" = false ] || [ "$GEMINI_INSTALLED" = false ]; then
    echo -e "${YELLOW}Installation des CLI (optionnel)${NC}"
    echo -e "Pour une expérience complète, vous pouvez installer :"
    
    if [ "$CLAUDE_INSTALLED" = false ]; then
        echo
        echo -e "${BLUE}Claude CLI:${NC}"
        echo "  pip install anthropic-cli"
        echo "  export ANTHROPIC_API_KEY='your-key'"
    fi
    
    if [ "$GEMINI_INSTALLED" = false ]; then
        echo
        echo -e "${BLUE}Gemini CLI:${NC}"
        echo "  pip install google-generativeai-cli"
        echo "  export GOOGLE_API_KEY='your-key'"
    fi
    echo
    echo -e "${YELLOW}Note: L'agent fonctionne aussi sans ces CLI${NC}"
fi

# Test de l'installation
echo
echo -e "${BLUE}Test de l'installation...${NC}"
if ./"$AGENT_NAME" --help &> /dev/null; then
    echo -e "${GREEN}✓ Installation réussie !${NC}"
else
    echo -e "${RED}❌ Erreur lors du test${NC}"
    exit 1
fi

# Résumé
echo
echo -e "${GREEN}╔═══════════════════════════════════════════════════════╗"
echo -e "║         Installation terminée avec succès !           ║"
echo -e "╚═══════════════════════════════════════════════════════╝${NC}"
echo
echo -e "${BLUE}Structure créée:${NC}"
echo "  $INSTALL_DIR/"
echo "  ├── dsfr-agent          ${GREEN}(script principal)${NC}"
echo "  ├── config/             ${GREEN}(configuration)${NC}"
echo "  ├── docs/               ${GREEN}(documentation DSFR)${NC}"
echo "  ├── cache/              ${GREEN}(cache des réponses)${NC}"
echo "  └── scripts/            ${GREEN}(scripts utilitaires)${NC}"
echo
echo -e "${BLUE}Utilisation:${NC}"
if [[ "$install_alias" =~ ^[Oo]$ ]]; then
    echo "  dsfr --help             ${GREEN}(après: source $SHELL_RC)${NC}"
    echo "  dsfr -i                 ${GREEN}(mode interactif)${NC}"
    echo "  dsfr \"votre question\"   ${GREEN}(requête directe)${NC}"
else
    echo "  ./dsfr-agent --help"
    echo "  ./dsfr-agent -i"
    echo "  ./dsfr-agent \"votre question\""
fi
echo
echo -e "${YELLOW}Documentation:${NC} Voir SHARE_WITH_TEAM.md"
echo -e "${YELLOW}Support:${NC} https://github.com/GouvernementFR/dsfr"
echo