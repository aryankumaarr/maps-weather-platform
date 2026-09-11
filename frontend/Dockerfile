# Dev-mode Dockerfile for the Next.js frontend (hot-reload via bind mount).
# Frontend owner: add a production multi-stage build when this is ready to deploy.
FROM node:20-alpine

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm ci

COPY . .

EXPOSE 3000

CMD ["npm", "run", "dev"]
