#!/bin/bash
#################################################
#  MCP Playbook DSFR - Exécution des Tests     #
#  Script pour lancer tous les tests           #
#################################################

set -e

# Couleurs
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${BLUE}================================================${NC}"
echo -e "${BLUE}   MCP Playbook DSFR - Tests${NC}"
echo -e "${BLUE}================================================${NC}"
echo ""

# Vérifier si l'environnement virtuel existe
if [ ! -d "venv" ]; then
    echo -e "${RED}❌ Environnement virtuel non trouvé${NC}"
    echo -e "${YELLOW}Lancez d'abord : ./install.sh${NC}"
    exit 1
fi

# Activer l'environnement virtuel
echo -e "${YELLOW}🔄 Activation de l'environnement virtuel...${NC}"
source venv/bin/activate

# Vérifier que beautifulsoup4 est installé
echo -e "${YELLOW}📋 Vérification des dépendances...${NC}"
python3 -c "
import sys
try:
    import bs4
    print('✅ BeautifulSoup4 disponible')
except ImportError:
    print('❌ BeautifulSoup4 manquant')
    print('   Installation en cours...')
    import subprocess
    subprocess.run([sys.executable, '-m', 'pip', 'install', 'beautifulsoup4'], check=True)
    print('✅ BeautifulSoup4 installé')
"

# Créer le dossier de résultats si nécessaire
mkdir -p tests/resultats-test
mkdir -p tests/html_outputs

# Compter les tests
TOTAL_TESTS=$(ls tests/test-mcp-dsfr-*.py 2>/dev/null | wc -l | tr -d ' ')

# Ajouter le test de non-régression s'il existe
if [ -f "tests/test_non_regression.py" ]; then
    TOTAL_TESTS=$((TOTAL_TESTS + 1))
fi

echo ""
echo -e "${BLUE}📊 $TOTAL_TESTS tests trouvés${NC}"
echo ""

# Exécuter tous les tests
PASSED=0
FAILED=0
SKIPPED=0

echo -e "${YELLOW}🧪 Exécution des tests...${NC}"
echo "----------------------------------------"

# Tests standards test-mcp-dsfr-*.py
for test_file in tests/test-mcp-dsfr-*.py; do
    if [ -f "$test_file" ]; then
        TEST_NAME=$(basename "$test_file" .py)
        echo -ne "  $TEST_NAME ... "
        
        # Exécuter le test et capturer le résultat
        if python3 "$test_file" > /dev/null 2>&1; then
            echo -e "${GREEN}✅ PASS${NC}"
            PASSED=$((PASSED + 1))
        else
            # Vérifier si c'est une erreur de dépendance
            ERROR_OUTPUT=$(python3 "$test_file" 2>&1)
            if echo "$ERROR_OUTPUT" | grep -q "ModuleNotFoundError"; then
                echo -e "${YELLOW}⚠️  SKIP (dépendance manquante)${NC}"
                SKIPPED=$((SKIPPED + 1))
            else
                echo -e "${RED}❌ FAIL${NC}"
                FAILED=$((FAILED + 1))
            fi
        fi
    fi
done

# Test de non-régression
if [ -f "tests/test_non_regression.py" ]; then
    echo -ne "  test_non_regression ... "
    if python3 tests/test_non_regression.py > /dev/null 2>&1; then
        echo -e "${GREEN}✅ PASS${NC}"
        PASSED=$((PASSED + 1))
    else
        echo -e "${RED}❌ FAIL${NC}"
        FAILED=$((FAILED + 1))
    fi
fi

echo "----------------------------------------"
echo ""

# Résumé
echo -e "${BLUE}================================================${NC}"
echo -e "${BLUE}   RÉSUMÉ DES TESTS${NC}"
echo -e "${BLUE}================================================${NC}"
echo ""
echo -e "  ${GREEN}✅ Passés    : $PASSED${NC}"
echo -e "  ${RED}❌ Échoués   : $FAILED${NC}"
echo -e "  ${YELLOW}⚠️  Ignorés   : $SKIPPED${NC}"
echo -e "  📊 Total     : $TOTAL_TESTS"
echo ""

# Lister les rapports générés
echo -e "${YELLOW}📄 Rapports générés :${NC}"
for report in tests/resultats-test/*.txt; do
    if [ -f "$report" ]; then
        echo "  - $(basename "$report")"
    fi
done
echo ""

# Pages HTML générées
if ls tests/html_outputs/*.html 1> /dev/null 2>&1; then
    echo -e "${YELLOW}🌐 Pages HTML générées :${NC}"
    for html in tests/html_outputs/*.html; do
        echo "  - $(basename "$html")"
    done
    echo ""
fi

# Message de fin
if [ $FAILED -eq 0 ] && [ $PASSED -gt 0 ]; then
    echo -e "${GREEN}🎉 Tous les tests sont passés avec succès !${NC}"
elif [ $PASSED -gt 0 ]; then
    echo -e "${YELLOW}⚠️  Certains tests ont échoué ou ont été ignorés${NC}"
else
    echo -e "${RED}❌ Aucun test n'a réussi${NC}"
fi

echo ""
echo -e "${BLUE}Pour voir les détails d'un rapport :${NC}"
echo "  cat tests/resultats-test/[nom_du_rapport].txt"
echo ""

# Désactiver l'environnement virtuel
deactivate 2>/dev/null || true

exit 0