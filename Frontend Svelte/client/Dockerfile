FROM node:18 as build

WORKDIR /app

COPY package.json ./
COPY package-lock.json ./

RUN npm install

COPY . ./

RUN npm run build

FROM nginx:1.19-alpine
COPY nginx.conf /etc/nginx/conf.d/
COPY nginx.conf /etc/nginx/conf.d/default.conf

COPY --from=build /app/dist  /usr/share/nginx/html