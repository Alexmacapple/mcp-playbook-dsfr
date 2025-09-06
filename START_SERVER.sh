#!/bin/bash
# Script de démarrage du serveur MCP DSFR

echo "🚀 Démarrage du serveur MCP DSFR..."
echo "=================================="

# Activer l'environnement virtuel
source venv/bin/activate

# Vérifier les dépendances
echo "📦 Vérification des dépendances..."
python3 -c "import bs4, lxml, mcp, pydantic; print('✅ Dépendances OK')" || {
    echo "❌ Dépendances manquantes. Installation..."
    pip install -r requirements.txt
}

# Tester le serveur
echo ""
echo "🧪 Test du serveur..."
python3 mcp_local/dsfr_server_simple.py --test

echo ""
echo "✅ Serveur prêt!"
echo ""
echo "📋 Pour utiliser avec Claude Desktop, copiez cette config dans:"
echo "   ~/Library/Application Support/Claude/claude_desktop_config.json"
echo ""
cat claude_desktop_config_correct.json
echo ""
echo "Puis redémarrez Claude Desktop."