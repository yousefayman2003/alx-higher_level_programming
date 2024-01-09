#!/usr/bin/node
let argN = 0;

exports.logMe = function (item) {
  console.log(`${argN}: ${item}`);
  argN++;
};
