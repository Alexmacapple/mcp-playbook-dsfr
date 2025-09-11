# Politique de sécurité

## Engagement sécurité

MCP Playbook DSFR s'engage à maintenir un niveau de sécurité élevé pour protéger les utilisateurs et leurs données.

## Versions supportées

| Version | Statut | Support sécurité | Fin de support |
|---------|--------|------------------|----------------|
| 2.0.x   | Actuelle | Actif | - |
| 1.x.x   | Obsolète | Critique uniquement | 2025-06-01 |
| < 1.0   | Non supportée | Aucun | Terminé |

## Signaler une vulnérabilité

### Process de signalement

Pour signaler une vulnérabilité de sécurité :

1. **NE PAS créer d'issue publique GitHub**
2. **Envoyer un email privé à** : alexandra.guiderdoni@gmail.com
3. **Sujet de l'email** : `[SECURITY] MCP DSFR - [Description courte]`

### Informations à fournir

Votre rapport doit inclure :

- **Description détaillée** de la vulnérabilité
- **Étapes pour reproduire** le problème
- **Version affectée** du serveur MCP
- **Impact potentiel** (exécution de code, fuite de données, déni de service, etc.)
- **Preuve de concept** (code ou commandes, si applicable)
- **Solution suggérée** ou mitigation temporaire
- **Votre contact** pour le suivi

### Délais de réponse

| Étape | Délai |
|-------|-------|
| Accusé de réception | 48 heures |
| Évaluation initiale | 7 jours |
| Plan de correction | 14 jours |
| Correctif publié | 30 jours* |
| Divulgation publique | 90 jours** |

*Selon la gravité et la complexité
**Ou après publication du correctif

## Pratiques de sécurité actuelles

### Validation et sanitization

- **HTML** : Sanitization via `bleach` pour prévenir XSS
- **Entrées utilisateur** : Validation stricte des paramètres
- **Templates** : Échappement automatique des variables

### Architecture sécurisée

- **Pas d'exécution de code arbitraire**
- **Pas de commandes système directes**
- **Isolation des services** (pattern SOLID)
- **Permissions minimales** requises

### Dépendances

- **Audit régulier** des dépendances
- **Versions minimales** spécifiées dans requirements.txt
- **7 dépendances seulement** en production

### Données

- **Aucun stockage persistant** de données utilisateur
- **Pas de cookies** ou tracking
- **Pas de données sensibles** en logs
- **Configuration locale** uniquement (.env ignoré par git)

## Hall of Fame

Nous remercions les chercheurs en sécurité qui ont contribué à améliorer MCP DSFR :

| Date | Contributeur | Vulnérabilité | Sévérité |
|------|--------------|---------------|----------|
| - | - | - | - |

## Ressources sécurité

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [CWE/SANS Top 25](https://cwe.mitre.org/top25/)
- [ANSSI - Guides](https://www.ssi.gouv.fr/guides/)
- [CERT-FR](https://www.cert.ssi.gouv.fr/)

## Checklist sécurité pour contributeurs

Avant de soumettre une PR :

- [ ] Pas de secrets dans le code (clés API, mots de passe)
- [ ] Validation des entrées utilisateur
- [ ] Échappement des sorties HTML
- [ ] Pas de `eval()` ou `exec()`
- [ ] Dépendances à jour
- [ ] Tests de sécurité passés

## Contact

**Email sécurité** : alexandra.guiderdoni@gmail.com
**PGP Key** : [À ajouter si disponible]

---

*Dernière mise à jour : 2025-09-11*