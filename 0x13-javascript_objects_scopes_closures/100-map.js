#!/usr/bin/node
const list = require('./100-data.js').list;
const data = list.map((el, idx) => el * idx);
console.log(list);
console.log(data);
