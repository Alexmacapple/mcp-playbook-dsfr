#!/bin/bash
#################################################
#  Installation MCP Playbook DSFR              #
#  Script d'installation automatique           #
#################################################

set -e

# Couleurs
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${BLUE}================================================${NC}"
echo -e "${BLUE}   MCP Playbook DSFR - Installation${NC}"
echo -e "${BLUE}================================================${NC}"
echo ""

# 1. Vérifier Python
echo -e "${YELLOW}📋 Vérification de Python...${NC}"
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ Python 3 n'est pas installé${NC}"
    echo "Installez Python 3.13+ depuis https://python.org"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
echo -e "${GREEN}✅ Python $PYTHON_VERSION détecté${NC}"

# 2. Créer l'environnement virtuel et les dossiers nécessaires
echo ""
echo -e "${YELLOW}📦 Création de l'environnement virtuel...${NC}"
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo -e "${GREEN}✅ Environnement virtuel créé${NC}"
else
    echo -e "${GREEN}✅ Environnement virtuel existant${NC}"
fi

# Créer les dossiers qui seront gitignorés
mkdir -p cache logs tests/html_outputs
echo -e "${GREEN}✅ Dossiers cache/, logs/ et tests/html_outputs/ créés${NC}"

# 3. Activer l'environnement
echo ""
echo -e "${YELLOW}🔄 Activation de l'environnement...${NC}"
source venv/bin/activate

# 4. Installer les dépendances
echo ""
echo -e "${YELLOW}📥 Installation des dépendances...${NC}"
pip install --upgrade pip > /dev/null 2>&1
pip install -r requirements.txt

# 5. Vérifier l'installation
echo ""
echo -e "${YELLOW}🧪 Vérification de l'installation...${NC}"
python3 -c "
import sys
try:
    import mcp
    import bs4
    import pydantic
    print('✅ MCP SDK installé')
    print('✅ BeautifulSoup4 installé')
    print('✅ Pydantic installé')
except ImportError as e:
    print(f'❌ Erreur: {e}')
    sys.exit(1)
"

# 6. Tester le serveur
echo ""
echo -e "${YELLOW}🚀 Test du serveur MCP...${NC}"
python3 -c "
import sys
sys.path.insert(0, '.')
try:
    from mcp_local.server import app
    from src.services import get_generator
    # Test basique
    html = get_generator().generate('button', label='Test')
    if 'fr-btn' in html:
        print('✅ Serveur MCP fonctionnel')
    else:
        print('❌ Erreur: génération incorrecte')
        sys.exit(1)
except Exception as e:
    print(f'❌ Erreur serveur: {e}')
    sys.exit(1)
"

# 7. Créer un fichier .env exemple (optionnel)
if [ ! -f ".env" ]; then
    cat > .env.example <<EOF
# Configuration environnement MCP DSFR
ENV=development
LOG_LEVEL=INFO
DEFAULT_RGAA_LEVEL=AA
ENABLE_HTML_SANITIZATION=true
EOF
    echo -e "${GREEN}✅ Fichier .env.example créé${NC}"
    echo -e "${YELLOW}   Copiez .env.example vers .env pour personnaliser${NC}"
fi

# 8. Configuration Claude Desktop
echo ""
echo -e "${BLUE}================================================${NC}"
echo -e "${BLUE}   Configuration Claude Desktop${NC}"
echo -e "${BLUE}================================================${NC}"
echo ""
echo -e "${YELLOW}📋 Pour configurer Claude Desktop :${NC}"
echo ""
echo "1. Copiez cette configuration dans :"
echo "   ~/Library/Application Support/Claude/claude_desktop_config.json"
echo ""
echo -e "${BLUE}Configuration à copier :${NC}"
echo "----------------------------------------"
cat <<EOF
{
  "mcpServers": {
    "mcp-playbook-dsfr": {
      "command": "$(pwd)/venv/bin/python3",
      "args": ["$(pwd)/mcp_local/server.py"],
      "env": {
        "PYTHONPATH": "$(pwd)",
        "ENV": "production",
        "LOG_LEVEL": "INFO",
        "DEFAULT_RGAA_LEVEL": "AA",
        "ENABLE_HTML_SANITIZATION": "true"
      }
    }
  }
}
EOF
echo "----------------------------------------"
echo ""
echo "2. Redémarrez Claude Desktop"
echo "3. Vérifiez l'icône 🔌 dans Claude"
echo ""
echo -e "${GREEN}🎉 Installation terminée avec succès !${NC}"
echo ""
echo -e "${YELLOW}Pour démarrer le serveur manuellement :${NC}"
echo "  source venv/bin/activate"
echo "  python3 mcp_local/server.py"
echo ""