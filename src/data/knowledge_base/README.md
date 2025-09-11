# Knowledge Base DSFR

Ce répertoire contient les données extraites des 213 fiches DSFR officielles.

## Fichiers

### components.json (1.3 MB)
- **88 fiches** de composants avec HTML
- **65 composants uniques** DSFR
- **775 variantes** HTML extraites
- Source : fiches avec "Extrait de code"

### documentation.json (290 KB)
- **125 fiches** de documentation
- **16 fondamentaux** (typographie, grille, couleurs)
- **69 utilitaires** (classes CSS, outils)
- **15 templates** (pages erreur, connexion)
- **25 autres** (pictogrammes, icônes)

## Utilisation

Ces fichiers sont automatiquement chargés par les services :
- `GeneratorService` : Utilise components.json
- `DesignService` : Utilise documentation.json
- `TemplateService` : Utilise documentation.json
- `ComponentRegistry` : Fusionne components.json avec gabarits/

## Source

Données extraites de `/roadmap/Brainstorming/fiches-markdown-v2/` (213 fichiers)
- Extraction : `extract_components_kb_v2.py`
- Documentation : `extract_documentation_kb.py`

## Mise à jour

Pour mettre à jour avec de nouvelles fiches DSFR :
1. Placer les nouvelles fiches markdown dans un répertoire
2. Adapter les scripts d'extraction
3. Remplacer les fichiers JSON ici
4. Les services chargeront automatiquement les nouvelles données au redémarrage