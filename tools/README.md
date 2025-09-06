# Outils de maintenance MCP DSFR

Ce répertoire contient les outils de maintenance et d'administration du serveur MCP DSFR.

## Outils disponibles

### check_dsfr_version.py

Script de vérification des mises à jour DSFR disponibles sur GitHub.

**Usage :**
```bash
python3 tools/check_dsfr_version.py
```

**Fonctionnalités :**
- Vérifie la version actuelle du projet (v1.14.1)
- Interroge l'API GitHub pour la dernière version
- Affiche les informations de mise à jour si disponible
- Retourne un code de sortie approprié (0=ok, 1=update, 2=erreur)

## Organisation

```
tools/
├── README.md               # Cette documentation
└── check_dsfr_version.py   # Vérificateur de version DSFR
```

## Notes

- Ces outils ne sont pas nécessaires au fonctionnement du serveur MCP
- Ils sont utiles pour la maintenance et les mises à jour
- Pour les tests, voir le répertoire `/tests/`