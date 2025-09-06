# ROADMAP - Tests MCP DSFR

## État actuel (Janvier 2025)

### Couverture des tests
- **92%** des outils MCP testés (12/13)
- **100%** des services testés (7/7)
- **11 scripts de test actifs** avec nomenclature cohérente
- **100% des tests passent** (objectif atteint)
- **Rapports générés** dans `/tests/resultats-test/`

## Améliorations à venir

### Priorité HAUTE

#### 1. Test approfondi pour `accessibility_audit`
**Statut actuel :** Tests basiques uniquement dans `test-mcp-dsfr-integration.py`

**Objectif :** Créer `test-mcp-dsfr-accessibility.py`

**Fonctionnalités à tester :**
- [ ] Tests niveau A (basique)
- [ ] Tests niveau AA (intermédiaire)
- [ ] Tests niveau AAA (avancé)
- [ ] Génération de rapports HTML détaillés
- [ ] Suggestions de corrections automatiques
- [ ] Validation RGAA 4.1 complète
- [ ] Tests de contraste de couleurs
- [ ] Tests de navigation au clavier
- [ ] Tests avec lecteurs d'écran simulés
- [ ] Validation des attributs ARIA
- [ ] Tests de structure sémantique HTML5

**Estimation :** 2-3 jours de développement

---

#### 2. Amélioration de la couverture pour `search_components`
**Statut actuel :** Tests partiels dans `test-mcp-dsfr-design.py`

**Objectif :** Étendre les tests existants

**Fonctionnalités à tester :**
- [ ] Recherche par mot-clé simple
- [ ] Recherche avec filtres multiples
- [ ] Recherche par catégorie
- [ ] Recherche floue (fuzzy search)
- [ ] Recherche avec expressions régulières
- [ ] Recherche dans les métadonnées
- [ ] Recherche dans les variantes
- [ ] Tests de performance (temps de réponse)
- [ ] Gestion des résultats vides
- [ ] Pagination des résultats
- [ ] Tri des résultats (pertinence, alphabétique)

**Estimation :** 1-2 jours de développement

---

### Priorité MOYENNE

#### 3. Tests de performance
**Objectif :** Créer `test-mcp-dsfr-performance.py`

**Métriques à mesurer :**
- [ ] Temps de génération par composant
- [ ] Utilisation mémoire
- [ ] Efficacité du cache
- [ ] Tests de charge (100, 1000, 10000 requêtes)
- [ ] Temps de réponse moyen/médian/P95
- [ ] Détection de fuites mémoire

---

#### 4. Tests de sécurité
**Objectif :** Créer `test-mcp-dsfr-security.py`

**Tests à implémenter :**
- [ ] Validation des entrées (XSS, injection)
- [ ] Échappement HTML
- [ ] Sanitization des données
- [ ] Tests OWASP Top 10
- [ ] Validation CSP (Content Security Policy)

---

### Priorité BASSE

#### 5. Tests d'intégration avec frameworks
**Objectif :** Tester l'intégration avec React, Vue, Angular

- [ ] Test avec React
- [ ] Test avec Vue.js
- [ ] Test avec Angular
- [ ] Test avec Svelte

---

## Planning prévisionnel

### Q1 2025 (Janvier - Mars)
- [x] Janvier : Mise en place de la nomenclature cohérente (FAIT)
- [ ] Février : Test approfondi accessibility_audit
- [ ] Mars : Amélioration search_components

### Q2 2025 (Avril - Juin)
- [ ] Avril : Tests de performance
- [ ] Mai : Tests de sécurité
- [ ] Juin : Documentation et exemples

### Q3 2025 (Juillet - Septembre)
- [ ] Tests d'intégration frameworks
- [ ] Automatisation CI/CD
- [ ] Benchmarks

## Métriques de succès

### Court terme (Q1 2025)
- [ ] **95%** de couverture des outils MCP
- [ ] Tous les tests passent sans beautifulsoup4
- [ ] Temps d'exécution < 30 secondes pour la suite complète

### Moyen terme (Q2 2025)
- [ ] **100%** de couverture des outils MCP
- [ ] Tests de performance automatisés
- [ ] Intégration CI/CD complète

### Long terme (2025)
- [ ] Certification RGAA complète
- [ ] Tests multi-navigateurs
- [ ] Tests multi-plateformes
- [ ] Documentation interactive

## Contribution

Pour contribuer aux tests :
1. Choisir un item de la roadmap
2. Créer une branche feature
3. Suivre la nomenclature `test-mcp-dsfr-*.py`
4. Sans émojis, en français
5. Générer un rapport dans `/tests/resultats-test/`
6. Soumettre une PR

## Notes techniques

### Dépendances à éviter
- pytest (utiliser des tests autonomes)
- Émojis dans le code
- Dépendances externes non nécessaires

### Standards à respecter
- Nomenclature : `test-mcp-dsfr-[fonction].py`
- Rapports : `/tests/resultats-test/[nom]_report.txt`
- Code en français
- Compatible Python 3.9+
- Aligné avec MCP DSFR v2.0.0
- Sans émojis dans tout le code

## Contact

Pour questions ou suggestions :
- Ouvrir une issue sur le repository
- Tag : `tests`, `roadmap`, `amélioration`

---

*Dernière mise à jour : Janvier 2025*
*Version : 1.0.0*