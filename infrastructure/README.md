# Infrastructure

Everything here is free/open-source — no paid Docker or cloud tier is required to develop
or run this stack locally.

## Layout

- `docker/postgres/init/` — SQL run automatically on first Postgres container start.
- `docker/monitoring/` — Prometheus + Grafana config (optional `monitoring` profile).
- `aws/` — notes and (eventually) Terraform for deployment. Nothing is deployed yet.

## Running locally

Requires Docker Engine + Docker Compose v2 — both free and open-source (Apache 2.0). Docker
Desktop works too and is free for individuals/small teams; if licensing is ever a concern,
[Rancher Desktop](https://rancherdesktop.io/) or [Colima](https://github.com/abiosoft/colima)
are drop-in free alternatives that talk to the same `docker`/`docker compose` CLI.

```bash
cp .env.example .env
docker compose up --build
```

- Backend: http://localhost:8000
- Frontend: http://localhost:3000
- Postgres: localhost:5432 (with PostGIS)
- Redis: localhost:6379

### Optional profiles

```bash
# pgAdmin (DB admin UI) at http://localhost:5050
docker compose --profile tools up

# Prometheus (http://localhost:9090) + Grafana (http://localhost:3001)
docker compose --profile monitoring up
```

## CI/CD

GitHub Actions (free for this repo's tier) — see [.github/workflows/ci.yml](../.github/workflows/ci.yml).
Lints/tests the backend and frontend, and builds the Docker images on every push/PR.
