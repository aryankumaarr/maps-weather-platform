-- Runs automatically on first container start (docker-entrypoint-initdb.d).
-- postgis is useful for a maps/geo project; drop it if it turns out unneeded.
CREATE EXTENSION IF NOT EXISTS postgis;
