#!/usr/bin/node
const dic = require('./101-data.js').dict;
const object = {};

for (const key in dic) {
  if (object[dic[key]] === undefined) object[dic[key]] = [key];
  else {
    object[dic[key]] = object[dic[key]].concat(key);
  }
}
console.log(object);
