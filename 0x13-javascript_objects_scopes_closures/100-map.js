#!/usr/bin/node
const values = require('./100-data.js').list;
const data = values.map((el, idx) => el * idx);
console.log(values);
console.log(data);
