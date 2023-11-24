FROM node:18.0.0-alpine3.14

WORKDIR /app

COPY app/package.json /app

RUN npm install -g pnpm 

RUN pnpm install 

COPY app /app

RUN pnpm run build
