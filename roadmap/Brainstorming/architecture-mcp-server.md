# Architecture du serveur MCP Ecosystème

## Vue d'ensemble

Le serveur MCP (Model Context Protocol) permet à Claude Desktop d'interagir directement avec l'application Ecosystème via une interface standardisée. Il agit comme un pont entre Claude et l'API backend de la plateforme.

## 🏗️ Stack technique

| Technologie | Version | Rôle |
|------------|---------|------|
| `@modelcontextprotocol/sdk` | v0.6.0 | Framework officiel MCP d'Anthropic |
| `zod` | v3.22.4 | Validation des schémas de données |
| `node-fetch` | v3.3.2 | Client HTTP pour l'API backend |
| Node.js | ES6 modules | Runtime JavaScript moderne |

## 📐 Architecture en couches

### 1. Classe principale `EcosystemeServer`
- Encapsule toute la logique du serveur
- Initialise le serveur MCP avec métadonnées (nom, version)
- Configure les capacités (actuellement : tools uniquement)
- Gère les erreurs et signaux système (SIGINT)

### 2. Communication STDIO
- Utilise `StdioServerTransport` pour la communication stdin/stdout
- Permet l'intégration native avec Claude Desktop
- Format de communication : JSON-RPC over stdio

### 3. Gestionnaires de requêtes

#### `ListToolsRequestSchema`
- Déclare tous les outils disponibles
- Définit les schémas JSON pour chaque outil
- Fournit les descriptions et paramètres requis/optionnels

#### `CallToolRequestSchema`
- Route les appels d'outils vers les méthodes appropriées
- Gère les erreurs avec des codes MCP standardisés
- Switch/case pour dispatcher vers les 30+ méthodes

### 4. Méthode `apiRequest` centrale
```javascript
async apiRequest(endpoint, options = {})
```
- Abstraction pour tous les appels à l'API backend
- URL de base configurable via `ECOSYSTEME_API_BASE`
- Gestion automatique des headers JSON
- Traitement des erreurs HTTP et réponses vides (204)

## 🛠️ Outils disponibles (30+ outils)

### Scanning & Validation
| Outil | Description |
|-------|-------------|
| `scan_site` | Scanner avec certificat, DSFR, Lighthouse, Wappalyzer |
| `validate_url` | Vérifier l'accessibilité d'une URL |

### Gestion des Sites
| Outil | Description |
|-------|-------------|
| `list_sites` | Lister tous les sites avec recherche |
| `get_site` | Obtenir les détails d'un site |
| `create_site` | Créer un nouveau site |
| `delete_site` | Supprimer un site |

### Gestion des Domaines
| Outil | Description |
|-------|-------------|
| `list_domains` | Lister les domaines |
| `get_domain` | Détails d'un domaine |
| `create_domain` | Créer un domaine |
| `delete_domain` | Supprimer un domaine |

### Gestion des Organisations
| Outil | Description |
|-------|-------------|
| `list_organizations` | Lister les organisations |
| `get_organization` | Détails d'une organisation |
| `create_organization` | Créer une organisation |
| `delete_organization` | Supprimer une organisation |

### Gestion des Personnes
| Outil | Description |
|-------|-------------|
| `list_persons` | Lister les personnes |
| `get_person` | Détails d'une personne |
| `create_person` | Créer une personne |
| `delete_person` | Supprimer une personne |

### Monitoring & Statistiques
| Outil | Description |
|-------|-------------|
| `get_dashboard_stats` | Statistiques du dashboard |
| `get_site_evolution` | Évolution d'un site |
| `get_regressions` | Sites avec régressions |
| `get_certificate_alerts` | Alertes d'expiration SSL |
| `get_site_monitoring` | Données de monitoring |

### Gestion des Relations
| Outil | Description |
|-------|-------------|
| `add_site_organization` | Associer organisation à site |
| `add_site_responsible` | Ajouter responsable |
| `remove_site_organization` | Retirer organisation |
| `remove_site_responsible` | Retirer responsable |

### Homologation
| Outil | Description |
|-------|-------------|
| `get_sites_homologation` | État d'homologation |
| `update_site_homologation` | Mettre à jour homologation |

## 🔄 Flux de données

```
┌─────────────┐     STDIO      ┌──────────────┐     HTTP      ┌─────────────┐     SQL      ┌──────────┐
│   Claude    │ ◄──────────► │  MCP Server  │ ◄──────────► │ API Backend │ ◄──────────► │ SQLite DB│
│   Desktop   │   JSON-RPC     │   (Node.js)  │   REST API    │  (Express)  │              │          │
└─────────────┘                └──────────────┘   Port 3001   └─────────────┘              └──────────┘
```

### Étapes d'exécution

1. **Requête Claude** : Envoi d'une commande tool via STDIO
2. **Validation MCP** : Parse et validation avec schémas Zod
3. **Transformation** : Conversion en appel API REST
4. **Appel Backend** : Requête HTTP vers Express (port 3001)
5. **Traitement** : Backend interroge SQLite et applique la logique métier
6. **Réponse** : Retour JSON formaté vers Claude

## 🔐 Validation et sécurité

### Validation Zod
Chaque outil utilise Zod pour valider strictement :
- **Types de données** : string, number, boolean, array
- **Formats spécifiques** : URL, email, dates ISO 8601
- **Enums** : Valeurs autorisées (statuts, types, rôles)
- **Contraintes** : required/optional, min/max length

### Gestion d'erreurs
```javascript
try {
  // Exécution de l'outil
} catch (error) {
  if (error instanceof McpError) {
    throw error; // Erreur MCP native
  }
  throw new McpError(
    ErrorCode.InternalError,
    `Tool execution failed: ${error.message}`
  );
}
```

## 🚀 Points forts de l'architecture

### Type-safety
- Validation stricte à l'entrée avec Zod
- Schémas JSON détaillés pour chaque paramètre
- Gestion explicite des types de retour

### Modularité
- Pattern switch/case pour le routing
- Une méthode par outil
- Facile d'ajouter de nouveaux outils

### Résilience
- Try/catch à tous les niveaux
- Codes d'erreur MCP standardisés
- Gestion des timeouts et erreurs réseau

### Documentation
- Chaque outil a une description claire
- Paramètres documentés avec types et contraintes
- Exemples d'utilisation dans le README

### Standards
- Suit le protocole MCP officiel d'Anthropic
- Compatible avec tous les clients MCP
- Utilise les schémas JSON standard

## 📦 Installation et configuration

### Prérequis
- Node.js 18+
- npm ou yarn
- Backend Ecosystème en cours d'exécution

### Installation
```bash
cd backend/mcp-server
npm install
```

### Configuration Claude Desktop
Ajouter dans `~/Library/Application Support/Claude/claude_desktop_config.json` :

```json
{
  "mcpServers": {
    "ecosysteme": {
      "command": "node",
      "args": ["/chemin/vers/ecosysteme/backend/mcp-server/index.js"],
      "env": {
        "ECOSYSTEME_API_BASE": "http://localhost:3001/api"
      }
    }
  }
}
```

### Démarrage
```bash
node index.js  # Production
npm run dev    # Développement avec nodemon
```

## 🔧 Extension du serveur

### Ajouter un nouvel outil

1. **Déclarer l'outil** dans `ListToolsRequestSchema` :
```javascript
{
  name: 'mon_outil',
  description: 'Description de l'outil',
  inputSchema: {
    type: 'object',
    properties: {
      param1: { type: 'string', description: 'Description' }
    },
    required: ['param1']
  }
}
```

2. **Ajouter le case** dans `CallToolRequestSchema` :
```javascript
case 'mon_outil':
  return await this.monOutil(args);
```

3. **Implémenter la méthode** :
```javascript
async monOutil(args) {
  const { param1 } = z.object({
    param1: z.string()
  }).parse(args);
  
  const result = await this.apiRequest('/endpoint', {
    method: 'POST',
    body: JSON.stringify({ param1 })
  });
  
  return {
    content: [{
      type: 'text',
      text: `Résultat: ${JSON.stringify(result, null, 2)}`
    }]
  };
}
```

## 📊 Métriques et monitoring

Le serveur peut être surveillé via :
- Logs console pour debug
- Statut des processus Node.js
- Monitoring des appels API backend
- Métriques de performance des scanners

## 🔮 Évolutions futures possibles

- Support des resources MCP (accès aux données)
- Support des prompts MCP (templates de requêtes)
- Cache local pour réduire les appels API
- WebSocket pour les mises à jour temps réel
- Authentification et autorisation
- Rate limiting et quotas
- Métriques Prometheus/Grafana
- Tests automatisés avec Jest

---

*Document généré le 11 septembre 2025*
*Serveur MCP v1.0.0 - Ecosystème*