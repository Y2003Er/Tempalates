# Deployment
1. cp .env.example .env
2. docker compose -f docker/docker-compose.yml up -d
3. psql -f database/01_schema.sql && psql -f database/02_seed.sql
4. n8n import workflows
Backups: pg_basebackup daily S3, DR RPO 5m RTO 30m
