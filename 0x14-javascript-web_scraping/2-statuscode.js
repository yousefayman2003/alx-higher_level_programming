#!/usr/bin/node

const request = require('request');

request(process.argv[2], (_, res) => {
  console.log('code:', res.statusCode);
});
