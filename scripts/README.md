# Scripts MCP DSFR

Ce répertoire contient les scripts utilitaires pour le projet MCP DSFR.

## Structure

### 📁 extraction/
Scripts pour extraire les données des fiches DSFR :
- `extract_components_kb_v2.py` - Extraction des 775 variantes de composants
- `extract_documentation_kb.py` - Extraction de la documentation (125 fiches)
- `analyze_all_fiches.py` - Analyse des 213 fiches markdown
- `analyze_components_only.py` - Analyse des composants uniquement
- `test_extraction_button.py` - Test du parser sur le fichier bouton

### 📁 validation/
Scripts de validation et conformité :
- `validate_conformity.py` - Validation de conformité DSFR (score 87%)

## Utilisation

### Extraction des Knowledge Bases
```bash
# Extraire les composants (si nouvelles fiches)
python3 scripts/extraction/extract_components_kb_v2.py

# Extraire la documentation
python3 scripts/extraction/extract_documentation_kb.py
```

### Validation
```bash
# Valider la conformité DSFR
python3 scripts/validation/validate_conformity.py
```

## Résultats

Les données extraites sont stockées dans :
- `src/data/knowledge_base/components.json` - 775 variantes
- `src/data/knowledge_base/documentation.json` - Documentation complète
- `src/data/analysis/` - Fichiers d'analyse

## Notes

Ces scripts ont été utilisés pour l'extraction initiale des 213 fiches DSFR.
Ils peuvent être réutilisés si de nouvelles fiches DSFR sont disponibles.