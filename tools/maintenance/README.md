# Outils de Maintenance DSFR

## IMPORTANT : DÉVELOPPEMENT UNIQUEMENT

Ces scripts sont des **outils de maintenance** pour les développeurs. Ils ne sont **PAS nécessaires** au fonctionnement du serveur MCP en production.

## Présentation

Ce répertoire contient des scripts utilitaires pour maintenir et mettre à jour la documentation DSFR et les gabarits HTML.

### Scripts disponibles

| Script | Fonction | Utilisation |
|--------|----------|-------------|
| `build_complete_library.py` | Génère les gabarits HTML pour 51 composants DSFR | Reconstruction complète des gabarits |
| `build_html_library.py` | Génère des gabarits HTML de production | Version alternative de génération |
| `update_complete.py` | Met à jour depuis toutes les sources (GitHub, Storybook, NPM) | Synchronisation complète |
| `update_from_github.py` | Synchronise avec le repo DSFR officiel | Mise à jour depuis GitHub |
| `update_from_storybook.py` | Synchronise avec Storybook DSFR | Mise à jour de la documentation |

## Prérequis

### Dépendances supplémentaires

Ces scripts nécessitent des dépendances **NON incluses** dans `requirements.txt` :

```bash
# Installation des dépendances de maintenance
pip install requests beautifulsoup4 lxml
```

### Accès requis

- Accès Internet pour GitHub API
- Accès à https://www.systeme-de-design.gouv.fr
- Permissions d'écriture dans `/tmp/` pour les fichiers temporaires

## Utilisation

### 1. Générer/Regénérer les gabarits

Si vous devez reconstruire les gabarits dans `/gabarits/` :

```bash
cd tools/maintenance
python3 build_complete_library.py
```

Cela créera/mettra à jour tous les gabarits HTML dans le répertoire `/gabarits/`.

### 2. Mettre à jour la documentation

Pour synchroniser avec la dernière version DSFR officielle :

```bash
# Mise à jour complète (recommandé)
python3 update_complete.py

# OU mise à jour depuis une source spécifique
python3 update_from_github.py    # Depuis le repo GitHub
python3 update_from_storybook.py  # Depuis Storybook
```

### 3. Vérifier les gabarits existants

```bash
# Lister tous les composants avec gabarits
ls -la ../../gabarits/

# Compter les composants
ls ../../gabarits/ | wc -l
```

## Structure des gabarits générés

Les scripts génèrent la structure suivante dans `/gabarits/` :

```
gabarits/
├── accordion/
│   ├── basic.html
│   └── bordered.html
├── alert/
│   ├── info.html
│   ├── success.html
│   ├── warning.html
│   └── error.html
├── button/
│   ├── primary.html
│   ├── secondary.html
│   └── tertiary.html
└── ... (48 composants au total)
```

## Avertissements

### NE PAS utiliser en production

- Ces scripts sont pour le **développement local uniquement**
- Ils contiennent des chemins codés en dur
- Ils effectuent des opérations système (clone, wget, etc.)
- Ils nécessitent des dépendances supplémentaires

### Sécurité

- Les scripts accèdent à des repos externes
- Vérifiez toujours le contenu généré avant utilisation
- N'exécutez pas avec des privilèges élevés (sudo)

### Problèmes connus

1. **Chemin codé en dur** : 
   - `MCP_PATH = "/Users/alex/Desktop/mcp-dsfr"` dans certains scripts
   - Modifiez selon votre environnement

2. **Dépendance requests** :
   - Non incluse dans requirements.txt principal
   - Installez manuellement si nécessaire

3. **Limite API GitHub** :
   - Sans token, limite de 60 requêtes/heure
   - Ajoutez un token GitHub si nécessaire

## Workflow de maintenance

### Mise à jour périodique (mensuelle)

1. Vérifier les nouvelles versions DSFR :
   ```bash
   curl -s https://api.github.com/repos/GouvernementFR/dsfr/releases/latest | grep tag_name
   ```

2. Si nouvelle version, exécuter la mise à jour :
   ```bash
   cd tools/maintenance
   python3 update_complete.py
   ```

3. Tester les nouveaux gabarits :
   ```bash
   cd ../..
   python3 tests/test-mcp-dsfr-all-components.py
   ```

4. Commiter les changements si tout est OK :
   ```bash
   git add gabarits/
   git commit -m "chore: Mise à jour gabarits DSFR vX.XX"
   ```

## Support

Ces scripts sont fournis "as is" pour faciliter la maintenance. Pour le fonctionnement du MCP :
- Consultez `/README.md` pour la documentation principale
- Les gabarits dans `/gabarits/` sont suffisants pour la production
- Le serveur MCP n'a pas besoin de ces scripts pour fonctionner

## Notes de développement

### Architecture

- **Scripts de build** : Génèrent des gabarits statiques HTML
- **Scripts d'update** : Synchronisent avec les sources officielles
- **Gabarits** : Fichiers HTML statiques utilisés par le MCP

### Pourquoi des gabarits statiques ?

1. **Performance** : Pas de génération à la volée
2. **Stabilité** : Version figée et testée
3. **Simplicité** : Pas de dépendances externes en production
4. **Conformité** : HTML validé et conforme DSFR

### Contribution

Si vous améliorez ces scripts :
1. Testez localement d'abord
2. Documentez les changements
3. Gardez la compatibilité avec la structure existante
4. N'ajoutez pas de dépendances au requirements.txt principal

---

**Rappel** : Le serveur MCP fonctionne parfaitement sans ces scripts. Ils sont uniquement là pour faciliter les mises à jour futures de la documentation DSFR.