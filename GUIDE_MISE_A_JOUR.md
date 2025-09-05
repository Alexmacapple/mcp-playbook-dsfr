# 📚 Guide de Mise à Jour Documentation DSFR

## 🎯 Vue d'ensemble

Trois méthodes pour mettre à jour la documentation DSFR avec **playbook + composants + code** :

### 1. 🚀 **ULTRA COMPLÈTE** (Recommandé)
Combine TOUTES les sources : GitHub + Storybook + NPM

```bash
./UPDATE_COMPLETE.sh
```

**Ce que vous obtenez :**
- ✅ Code source complet (SCSS, JS)
- ✅ Templates HTML et exemples
- ✅ Documentation Storybook interactive
- ✅ Variables CSS et API JavaScript
- ✅ README de chaque composant
- ✅ Liens vers toutes les ressources

### 2. 📖 **Storybook** (Documentation interactive)
Extrait depuis le site officiel Storybook

```bash
./update_dsfr.sh
```

**Ce que vous obtenez :**
- ✅ Documentation interactive
- ✅ Descriptions détaillées
- ✅ Propriétés et variantes
- ✅ Exemples d'usage

### 3. 🐙 **GitHub** (Code source)
Extrait directement du dépôt officiel

```bash
./update_github.sh
```

**Ce que vous obtenez :**
- ✅ Code SCSS/JS
- ✅ Templates
- ✅ Structure des fichiers
- ⚠️ Limité par l'API GitHub (sans token)

## 📊 Comparaison des méthodes

| Méthode | Sources | Temps | Taille doc | Complétude |
|---------|---------|-------|------------|------------|
| **ULTRA COMPLÈTE** | GitHub + Storybook + NPM | 2-3 min | ~2-4 MB | ⭐⭐⭐⭐⭐ |
| **Storybook** | Site Storybook | 1-2 min | ~1 MB | ⭐⭐⭐⭐ |
| **GitHub** | API GitHub | 1 min | ~500 KB | ⭐⭐⭐ |

## 🔄 Workflow recommandé

### Pour une mise à jour complète :

1. **Vérifier la version actuelle**
   ```bash
   grep "DSFR v" docs/*.md | head -1
   ```

2. **Vérifier la dernière version NPM**
   ```bash
   npm view @gouvfr/dsfr version
   ```

3. **Lancer la mise à jour ULTRA COMPLÈTE**
   ```bash
   ./UPDATE_COMPLETE.sh
   ```

4. **Vérifier le résultat**
   ```bash
   ls -lh docs/*ULTRA_COMPLETE*.md | tail -1
   ```

## 📁 Structure des fichiers générés

```
docs/
├── DSFR_v1.14.1_ULTRA_COMPLETE_[DATE].md    # Documentation complète
├── DSFR_v1.14.1_COMPLETE_DATA_[DATE].json   # Métadonnées JSON
├── DSFR_v1.14.1_UPDATED_[DATE].md           # Depuis Storybook
└── DSFR_v1.14.1_GITHUB_[DATE].md            # Depuis GitHub
```

## 🛠️ Scripts disponibles

| Script | Description | Usage |
|--------|-------------|-------|
| `UPDATE_COMPLETE.sh` | Mise à jour ULTRA COMPLÈTE | `./UPDATE_COMPLETE.sh` |
| `update_dsfr.sh` | Mise à jour depuis Storybook | `./update_dsfr.sh` |
| `update_github.sh` | Mise à jour depuis GitHub | `./update_github.sh` |
| `scripts/update_complete.py` | Script Python complet | Python direct |
| `scripts/update_from_storybook.py` | Extraction Storybook | Python direct |
| `scripts/update_from_github.py` | Extraction GitHub | Python direct |

## 📋 Contenu de la documentation ULTRA COMPLÈTE

Pour chaque composant (51 au total) :

```markdown
## 🔹 BUTTON

### 📋 INFORMATIONS GÉNÉRALES
- Classe CSS : fr-btn
- Description
- Variantes disponibles

### 🎨 VARIABLES SCSS
- Liste des variables personnalisables

### 📝 CLASSES CSS
- Toutes les classes disponibles

### ⚙️ API JAVASCRIPT
- Méthodes disponibles
- Événements

### 📄 TEMPLATE HTML
- Code HTML complet
- Exemples d'utilisation

### 📚 DOCUMENTATION GITHUB
- README du composant

### 🔗 LIENS
- GitHub
- Storybook
- Site officiel
```

## 🚨 Dépannage

### Erreur "rate limit exceeded"
**Solution** : Utiliser `UPDATE_COMPLETE.sh` qui clone le dépôt localement

### Erreur "Module not found"
**Solution** : Le script utilise uniquement les modules Python standard

### Erreur "git not found"
**Solution** : Installer Git avec `brew install git`

## 🎯 Cas d'usage

### Je veux tout le code et la doc
```bash
./UPDATE_COMPLETE.sh
```

### Je veux juste la doc interactive
```bash
./update_dsfr.sh
```

### Je veux voir le code source
```bash
./update_github.sh
```

## 📝 Notes importantes

1. **Fréquence** : Mettre à jour mensuellement ou à chaque release DSFR
2. **Espace** : Prévoir ~10 MB temporaires pendant l'extraction
3. **Connexion** : Nécessite une connexion internet
4. **Durée** : 2-3 minutes pour la mise à jour complète

## 🔗 Ressources

- **DSFR officiel** : https://www.systeme-de-design.gouv.fr/
- **GitHub** : https://github.com/GouvernementFR/dsfr
- **NPM** : https://www.npmjs.com/package/@gouvfr/dsfr
- **Storybook** : https://www.systeme-de-design.gouv.fr/storybook/

---

*Pour une documentation toujours à jour avec playbook + composants + code complet*