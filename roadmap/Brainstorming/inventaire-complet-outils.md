# Inventaire Complet des Outils du Projet Ecosystème

## 🔍 Scanners d'Analyse (6 scanners)

### 1. **Scanner d'Accessibilité** (`accessibility-scanner.js`)
- **Fonction** : Analyse RGAA et conformité accessibilité
- **Vérifications** : Images alt, titres H1-H6, formulaires, liens, langue, skip links
- **Score** : 0-100% basé sur critères RGAA 4.1
- **API** : `POST /api/scan/accessibility`

### 2. **Scanner de Certificats SSL** (`certificate/`)
- **Fonction** : Analyse des certificats SSL/TLS
- **Vérifications** : Validité, expiration, chaîne, autorité, domaines SAN
- **Alertes** : Certificats expirant sous 30 jours
- **API** : `POST /api/scan/certificate`

### 3. **Scanner DNS** (`dns/`)
- **Fonction** : Analyse des enregistrements DNS
- **Vérifications** : A, AAAA, MX, TXT, NS, CNAME
- **Détection** : SPF, DMARC, DKIM
- **API** : `POST /api/scan/dns`

### 4. **Scanner DSFR** (`dsfr/`)
- **Fonction** : Conformité au Design System Français
- **Vérifications** : CSS DSFR, composants, couleurs, typographie
- **Score** : Niveau de conformité (totale, partielle, non conforme)
- **API** : `POST /api/scan/dsfr`

### 5. **Scanner Lighthouse** (`lighthouse/`)
- **Fonction** : Performance et qualité web
- **Métriques** : Performance, accessibilité, SEO, bonnes pratiques
- **Moteur** : Google Lighthouse avec axe-core
- **API** : `POST /api/scan/lighthouse`

### 6. **Scanner Wappalyzer** (`wappalyzer/`)
- **Fonction** : Détection des technologies web
- **Catégories** : CMS, frameworks, analytics, serveurs
- **Cache** : Optimisé avec cache local
- **API** : `POST /api/scan/wappalyzer`

## 🛠️ Scripts Utilitaires

### Scripts de Maintenance Base de Données

#### `backup-database.sh`
```bash
./scripts/backup-database.sh [nom_backup]
```
- Sauvegarde SQLite avec vérification d'intégrité
- Métadonnées et statistiques
- Rotation automatique (garde 10 derniers)

#### `analyze-certificate-duplicates.js`
```bash
node scripts/analyze-certificate-duplicates.js
```
- Analyse les certificats dupliqués
- Génère rapports JSON et Markdown
- Identifie les certificats multi-domaines

#### `migrate-certificate-deduplication.js`
```bash
node scripts/migrate-certificate-deduplication.js
```
- Migration pour dédupliquer les certificats
- Mise à jour des relations Many-to-Many
- Rapport de migration détaillé

## 🧪 Tests et Validation

### Tests Unitaires et d'Intégration
- `dsfr-scanner.test.js` - Tests du scanner DSFR
- `test-integration-complete.js` - Tests d'intégration complets
- `test-rate-limiter.js` - Tests du rate limiting
- `test-wappalyzer-cache.js` - Tests du cache Wappalyzer
- `test-wappalyzer-offline.js` - Tests mode offline
- `test-mcp.js` - Tests du serveur MCP

### Scripts de Test
- `run-tests.js` - Lance tous les tests
- `run-dsfr.js` - Lance tests DSFR spécifiques

## 🐳 Outils Docker et Infrastructure

### Makefile - Commandes principales
```bash
# Production
make build         # Construire les images
make up           # Démarrer en production
make down         # Arrêter les services
make logs         # Voir les logs

# Développement
make dev          # Mode développement
make dev-logs     # Logs développement
make dev-restart  # Redémarrer dev

# Base de données
make db-backup    # Sauvegarder BDD
make db-restore   # Restaurer BDD

# Spécifiques
make backend-logs # Logs backend seul
make frontend-logs # Logs frontend seul
make mcp          # Avec serveur MCP
make tools        # Avec outils dev (Adminer)
```

### Docker Compose
- `docker-compose.yml` - Configuration production
- `docker-compose.dev.yml` - Configuration développement
- Services : backend, frontend, nginx, adminer

### Scripts Shell
- `start.sh` - Script de démarrage principal
- `setup-claude.sh` - Configuration Claude Desktop

## 🤖 Serveur MCP (Model Context Protocol)

### Serveur MCP (`backend/mcp-server/`)
- **30+ outils** disponibles via protocole MCP
- Communication STDIO avec Claude Desktop
- Validation Zod sur tous les inputs
- Accès complet à l'API backend

### Outils MCP disponibles
- Scanning (tous les scanners)
- CRUD sites, domaines, organisations, personnes
- Monitoring et statistiques
- Gestion des certificats
- Relations et associations

## 📊 Outils de Monitoring

### Dashboard Frontend
- Statistiques en temps réel
- Graphiques Recharts et D3.js
- Visualisation réseau avec Sigma.js
- Exports CSV des données

### API de Statistiques
- `GET /api/sites/stats` - Stats globales
- `GET /api/sites/evolution` - Evolution temporelle
- `GET /api/certificates/alerts` - Alertes certificats
- `GET /api/sites/regressions` - Sites avec régressions

## 🔧 Outils de Développement

### Backend
- **Nodemon** - Hot reload développement
- **Swagger** - Documentation API (`/api-docs`)
- **Helmet** - Sécurité headers HTTP
- **Morgan** - Logging HTTP
- **Express Rate Limit** - Protection DDoS

### Frontend
- **Vite** - Build tool ultra-rapide
- **ESLint** - Linting code
- **TypeScript** - Type checking
- **React DevTools** - Debug React

## 📚 Documentation et Génération

### Documentation Automatique
- Swagger UI sur `/api-docs`
- JSDoc dans le code
- README par module

### Génération de Rapports
- Rapports de migration JSON/Markdown
- Exports CSV depuis le dashboard
- Logs structurés avec timestamps

## 🔐 Outils de Sécurité

### Sécurité Backend
- **Helmet.js** - Headers sécurisés
- **CORS** - Configuration stricte
- **Rate Limiting** - 100 req/15min
- **Validation** - Entrées sanitisées

### Sécurité Frontend
- **HTTPS** obligatoire en production
- **CSP** via headers Helmet
- **XSS Protection** via React
- **CSRF** tokens (à implémenter)

## 📦 Gestionnaires de Paquets

### NPM Scripts Backend
```json
"scripts": {
  "start": "node server.js",
  "dev": "nodemon server.js",
  "test": "node tests/run-tests.js",
  "test:dsfr": "node tests/dsfr-scanner.test.js",
  "test:smoke": "node tests/test-integration-complete.js",
  "docs:swagger": "node src/utils/swagger-generator.js"
}
```

### NPM Scripts Frontend
```json
"scripts": {
  "dev": "vite",
  "build": "tsc -b && vite build",
  "lint": "eslint .",
  "preview": "vite preview"
}
```

## 🌐 Outils d'API

### Routes API principales
- `/api/sites` - Gestion des sites
- `/api/domains` - Gestion des domaines
- `/api/certificates` - Certificats SSL
- `/api/scan/*` - Tous les scanners
- `/api/technologies` - Stack technologique
- `/api/organizations` - Organisations
- `/api/network` - Visualisation réseau

### Middleware
- Authentication (à implémenter)
- Error handling global
- Request logging
- Response compression

## 📈 Outils d'Analyse

### Analyse de Performance
- Lighthouse scores
- Métriques Core Web Vitals
- Temps de chargement

### Analyse de Conformité
- Score DSFR
- Score RGAA accessibilité
- Conformité légale (mentions, CGU)

### Analyse de Sécurité
- Certificats SSL/TLS
- Headers de sécurité
- Vulnérabilités connues

## 🔄 Outils de Migration

### Migrations Base de Données
- Scripts SQL dans `backend/src/database/migrations/`
- Versioning des schémas
- Rollback possible

### Import/Export
- Export CSV depuis dashboard
- Import bulk (à implémenter)
- Backup/restore SQLite

---

## Résumé Statistique

- **6 Scanners** spécialisés
- **11 Tests** automatisés
- **30+ Outils MCP** disponibles
- **20+ Commandes Make** pour Docker
- **10+ Scripts** utilitaires
- **50+ Routes API** REST
- **100% Dockerisé** avec dev/prod
- **3 Frameworks** : Express, React, MCP SDK

---

*Inventaire réalisé le 11 septembre 2025*  
*Projet Ecosystème v1.0.0*