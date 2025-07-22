FROM node:18-alpine

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build

RUN npm install -g serve

ENV HOST 0.0.0.0
EXPOSE 8080

CMD ["serve", "-s", "dist", "-l", "8080", "-n"]
