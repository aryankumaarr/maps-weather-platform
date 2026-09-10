# maps-weather-platform
A weather map plugin that allows you to redirect traffic based off of weather conditions and more

## Team

- **Frontend** — Next.js, TypeScript, Google Maps UI
- **Backend** — FastAPI, Python, REST APIs, weather API integration
- **Infrastructure / Data** — PostgreSQL (PostGIS), Redis, Docker, AWS, CI/CD, monitoring

## Getting started

Everything runs locally via Docker Compose — free/open-source images only, no paid services
required. Each person runs their own full stack on their own laptop; nothing here needs to be
reachable from the internet.

### Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running
  (Rancher Desktop or Colima work too, if you'd rather avoid Docker Desktop's licensing terms)
- Git

### First time only

```bash
git clone <repo-url>
cd maps-weather-platform
cp .env.example .env
docker compose up --build
```

`.env` is gitignored on purpose (so nobody commits real secrets/API keys) — `git pull` will
never touch it, so this `cp` only needs to happen once. If you want different ports or
credentials, edit your own `.env` after copying it.

Once it's up:

- Frontend: http://localhost:3000
- Backend: http://localhost:8000
- Postgres (PostGIS): localhost:5432
- Redis: localhost:6379

### Every time you pull new changes

```bash
git pull
docker compose up --build
```

Always include `--build`. Without it, Docker may reuse an old image even after
`docker-compose.yml`, a `Dockerfile`, `requirements.txt`, or `package.json` changed — `--build`
is a fast no-op if nothing actually changed, so it's safe to always include.

### Stopping

```bash
docker compose down
```

Stops the containers but keeps your database data. Only add `-v` (`docker compose down -v`) if
you actually want to wipe your local database — e.g. the schema got into a broken state and you
want a clean slate.

### Troubleshooting

**"port is already allocated"** — something else on your machine is already using that port
(often a locally-installed Postgres competing for 5432). Open your `.env`, change the matching
`*_PORT` value (e.g. `POSTGRES_PORT=15432`), and re-run `docker compose up --build`.

### Optional extras

Not needed day-to-day, but available:

```bash
# pgAdmin (database GUI) at http://localhost:5050
docker compose --profile tools up

# Prometheus (http://localhost:9090) + Grafana (http://localhost:3001)
docker compose --profile monitoring up
```

See [infrastructure/README.md](infrastructure/README.md) for what's actually running under the
hood and why.
