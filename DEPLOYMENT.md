# 🚀 Guide de Déploiement Production - MCP DSFR

## 📋 Prérequis

- Python 3.9+ ou Docker
- 512MB RAM minimum
- 1GB espace disque
- Accès réseau pour Claude Desktop

## 🐳 Déploiement avec Docker (Recommandé)

### 1. Build de l'image

```bash
# Clone du repository
git clone https://github.com/your-org/mcp-playbook-dsfr.git
cd mcp-playbook-dsfr

# Build de l'image
docker build -t mcp-playbook-dsfr:latest .

# Ou avec docker-compose
docker-compose build
```

### 2. Configuration production

```bash
# Copier le fichier d'environnement
cp .env.example .env

# Éditer les variables pour production
nano .env
```

Variables importantes pour production :
```env
ENV=production
LOG_LEVEL=WARNING
ENABLE_HTML_SANITIZATION=true
RATE_LIMIT_PER_MINUTE=30
ENABLE_METRICS=true
DEBUG=false
PRETTY_LOGS=false
```

### 3. Lancement

```bash
# Avec docker-compose
docker-compose up -d

# Ou directement avec Docker
docker run -d \
  --name mcp-dsfr \
  --restart unless-stopped \
  -e ENV=production \
  -e LOG_LEVEL=WARNING \
  -v $(pwd)/gabarits:/app/gabarits:ro \
  -v logs:/app/logs \
  -p 9090:9090 \
  mcp-playbook-dsfr:latest
```

### 4. Vérification

```bash
# Logs
docker logs mcp-dsfr

# Santé
docker exec mcp-dsfr python3 -c "from mcp.server import DSFRMCPServer; print('✅ OK')"

# Métriques (si activées)
curl http://localhost:9090/metrics
```

## 🖥️ Déploiement sans Docker

### 1. Installation système

```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install -y python3-pip python3-venv libxml2-dev libxslt1-dev

# RHEL/CentOS
sudo yum install -y python3 python3-pip libxml2-devel libxslt-devel
```

### 2. Environnement Python

```bash
# Créer environnement virtuel
python3 -m venv venv
source venv/bin/activate

# Installer dépendances
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Configuration systemd

Créer `/etc/systemd/system/mcp-dsfr.service` :

```ini
[Unit]
Description=MCP DSFR Server
After=network.target

[Service]
Type=simple
User=mcp
Group=mcp
WorkingDirectory=/opt/mcp-playbook-dsfr
Environment="ENV=production"
Environment="LOG_LEVEL=WARNING"
Environment="PATH=/opt/mcp-playbook-dsfr/venv/bin"
ExecStart=/opt/mcp-playbook-dsfr/venv/bin/python3 /opt/mcp-playbook-dsfr/mcp/server.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

### 4. Démarrage

```bash
# Recharger systemd
sudo systemctl daemon-reload

# Démarrer le service
sudo systemctl start mcp-dsfr
sudo systemctl enable mcp-dsfr

# Vérifier le statut
sudo systemctl status mcp-dsfr
```

## 🔒 Sécurité Production

### 1. Utilisateur dédié

```bash
# Créer utilisateur système
sudo useradd -r -s /bin/false mcp
sudo chown -R mcp:mcp /opt/mcp-playbook-dsfr
```

### 2. Permissions fichiers

```bash
# Lecture seule pour le code
chmod -R 644 /opt/mcp-playbook-dsfr/src
chmod -R 644 /opt/mcp-playbook-dsfr/gabarits
chmod -R 755 /opt/mcp-playbook-dsfr/src  # Dossiers

# Écriture pour logs
chmod 755 /opt/mcp-playbook-dsfr/logs
```

### 3. Reverse Proxy (Nginx)

```nginx
server {
    listen 443 ssl http2;
    server_name mcp-dsfr.example.com;
    
    ssl_certificate /etc/ssl/certs/mcp-dsfr.crt;
    ssl_certificate_key /etc/ssl/private/mcp-dsfr.key;
    
    # Sécurité headers
    add_header X-Content-Type-Options nosniff;
    add_header X-Frame-Options DENY;
    add_header X-XSS-Protection "1; mode=block";
    
    # Rate limiting
    limit_req_zone $binary_remote_addr zone=mcp:10m rate=10r/s;
    limit_req zone=mcp burst=20 nodelay;
    
    location /metrics {
        proxy_pass http://localhost:9090;
        allow 10.0.0.0/8;  # Réseau interne uniquement
        deny all;
    }
}
```

## 📊 Monitoring

### 1. Health Check

```bash
# Script de health check
cat > /opt/mcp-playbook-dsfr/health_check.sh << 'EOF'
#!/bin/bash
python3 -c "
from mcp.server import DSFRMCPServer
import sys
try:
    server = DSFRMCPServer()
    print('HEALTHY')
    sys.exit(0)
except:
    print('UNHEALTHY')
    sys.exit(1)
"
EOF

chmod +x /opt/mcp-playbook-dsfr/health_check.sh
```

### 2. Prometheus Metrics

Si `ENABLE_METRICS=true`, les métriques sont disponibles sur :
```
http://localhost:9090/metrics
```

Métriques exposées :
- `mcp_requests_total` : Nombre total de requêtes
- `mcp_request_duration_seconds` : Durée des requêtes
- `mcp_errors_total` : Nombre d'erreurs
- `mcp_rgaa_audits_total` : Audits RGAA effectués

### 3. Logs

```bash
# Suivre les logs en temps réel
tail -f /opt/mcp-playbook-dsfr/logs/mcp.log

# Avec Docker
docker logs -f mcp-dsfr

# Parser les logs JSON
cat logs/mcp.log | jq '.level == "ERROR"'
```

## 🔄 Mise à jour

### Avec Docker

```bash
# Pull nouvelle version
git pull origin main

# Rebuild
docker-compose build

# Redémarrer avec zero-downtime
docker-compose up -d --no-deps --build mcp-dsfr
```

### Sans Docker

```bash
# Backup
cp -r /opt/mcp-playbook-dsfr /opt/mcp-playbook-dsfr.backup

# Update
cd /opt/mcp-playbook-dsfr
git pull origin main
source venv/bin/activate
pip install -r requirements.txt

# Redémarrer
sudo systemctl restart mcp-dsfr
```

## 🆘 Troubleshooting

### Problème : Service ne démarre pas

```bash
# Vérifier les logs
journalctl -u mcp-dsfr -n 50

# Tester manuellement
cd /opt/mcp-playbook-dsfr
source venv/bin/activate
python3 mcp/server.py
```

### Problème : Erreurs de dépendances

```bash
# Réinstaller complètement
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install --no-cache-dir -r requirements.txt
```

### Problème : Performance dégradée

```bash
# Vérifier ressources
docker stats mcp-dsfr

# Augmenter limites dans docker-compose.yml
# Ou ajuster MAX_CACHE_SIZE dans .env
```

## 📞 Support

En cas de problème :
1. Consulter les logs : `docker logs mcp-dsfr`
2. Vérifier la configuration : `docker exec mcp-dsfr python3 -c "from mcp.config import MCPConfig; print(MCPConfig.to_dict())"`
3. Ouvrir une issue sur GitHub avec les logs

## ✅ Checklist Production

- [ ] Variables d'environnement configurées
- [ ] HTTPS activé (reverse proxy)
- [ ] Rate limiting configuré
- [ ] Monitoring en place
- [ ] Logs centralisés
- [ ] Backups automatiques
- [ ] Health checks configurés
- [ ] Utilisateur dédié (non-root)
- [ ] Firewall configuré
- [ ] Documentation à jour