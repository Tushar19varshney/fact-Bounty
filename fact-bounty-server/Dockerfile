FROM node

RUN mkdir -p /usr/fact-bounty/fact-bounty-server
WORKDIR /usr/fact-bounty/fact-bounty-server

COPY package.json ./
RUN npm install
COPY . .
EXPOSE 7000
CMD ["npm", "start"]