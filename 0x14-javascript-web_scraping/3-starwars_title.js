#!/usr/bin/node

const request = require('request');
const starWarsUrl = 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]);

request(starWarsUrl, (_, __, body) => {
  body = JSON.parse(body);
  console.log(body.title);
});
