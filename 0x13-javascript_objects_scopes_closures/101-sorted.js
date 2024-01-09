#!/usr/bin/node
const dict = require('./101-data.js').dict;
const object = {};

for (const key of dict) {
  if (object[dict[key]] === undefined) object[dict[key]] = [key];
  else {
    object[dict[key]] = object[dict[key]].concat(key);
  }
}
console.log(object);
