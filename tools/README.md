# Outils de Développement

## RÉPERTOIRE EXCLU DE LA PRODUCTION

Ce répertoire contient des outils de développement et de maintenance. **Il n'est PAS nécessaire au fonctionnement du serveur MCP**.

## Structure

```
tools/
└── maintenance/     # Scripts de maintenance des gabarits DSFR
    ├── build_*.py   # Génération de gabarits
    └── update_*.py  # Synchronisation avec DSFR officiel
```

## Utilisation

### En développement

Ces outils peuvent être utilisés pour :
- Mettre à jour les gabarits DSFR
- Synchroniser avec les dernières versions officielles
- Regénérer la documentation

### En production

**NE PAS DÉPLOYER** ce répertoire en production. Le serveur MCP n'en a pas besoin.

## Exclusion du déploiement

### Docker

Dans le `.dockerignore` :
```
tools/
```

### Déploiement manuel

Ne pas copier le répertoire `/tools/` sur le serveur de production.

## Documentation

Consultez le README spécifique de chaque sous-répertoire pour plus de détails.