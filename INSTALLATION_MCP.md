# 🚀 Installation MCP DSFR dans Claude Desktop

## Installation en 3 étapes (2 minutes chrono !)

### 1️⃣ Installer le package MCP (si pas déjà fait)
```bash
pip3 install mcp
```

### 2️⃣ Configurer Claude Desktop

Ouvrir le fichier de config Claude :
```bash
# macOS
open ~/Library/Application\ Support/Claude/claude_desktop_config.json

# Windows
# %APPDATA%\Claude\claude_desktop_config.json

# Linux
# ~/.config/Claude/claude_desktop_config.json
```

Ajouter cette configuration :
```json
{
  "mcpServers": {
    "mcp-playbook-dsfr": {
      "command": "python3",
      "args": ["/Users/alex/Desktop/mcp-playbook-dsfr/mcp/server.py"]
    }
  }
}
```

### 3️⃣ Redémarrer Claude Desktop

Fermer complètement et rouvrir Claude Desktop.

## ✅ Vérification

Dans Claude, taper :
```
Liste les composants DSFR disponibles
```

Si Claude répond avec la liste des composants, c'est bon ! 🎉

## 🎮 Commandes disponibles

### Générer un composant
```
Génère un bouton DSFR primaire avec le label "Valider"
```

### Lister les composants
```
Quels sont les composants DSFR disponibles ?
```

### Voir les variantes
```
Montre-moi les variantes du composant alert
```

### Valider du HTML
```
Valide ce HTML DSFR : <button class="fr-btn">Test</button>
```

### Analyser un besoin
```
J'ai besoin d'un formulaire de contact accessible
```

### Créer une page complète
```
Crée une page avec un header, un formulaire et un footer
```

## 🐛 Troubleshooting

### Claude ne trouve pas les commandes
1. Vérifier que le chemin dans la config est correct
2. Vérifier que Python 3 est installé : `python3 --version`
3. Vérifier que le package mcp est installé : `pip3 list | grep mcp`

### Erreur au démarrage
Tester manuellement :
```bash
cd /Users/alex/Desktop/mcp-playbook-dsfr
python3 mcp/server.py
```

Si une erreur apparaît, l'installer :
```bash
pip3 install -r requirements.txt
```

## 📊 Ce que Claude peut faire maintenant

- ✅ Générer n'importe quel composant DSFR
- ✅ Personnaliser avec toutes les options
- ✅ Valider l'accessibilité RGAA
- ✅ Créer des pages complètes
- ✅ Analyser les besoins et suggérer
- ✅ 48 composants, 131 variantes

## 🎯 Exemples concrets

```
Claude, génère un formulaire de connexion DSFR accessible
```

```
Claude, crée une page d'accueil avec navigation, hero banner et cards
```

```
Claude, valide cette page HTML et vérifie la conformité RGAA
```

## 💡 Pro Tips

1. **Demander des variantes** : Claude connaît toutes les variantes
2. **Validation automatique** : Toujours demander validation RGAA
3. **Pages complètes** : Claude peut générer des pages entières
4. **Analyse de besoins** : Décrivez votre besoin, Claude suggère

---

**Support** : En cas de problème, vérifier les logs dans `mcp.log`