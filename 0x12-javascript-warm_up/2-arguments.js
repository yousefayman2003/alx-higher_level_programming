#!/usr/bin/node
const length = process.argv.slice(2).length;

if (length === 0) {
  console.log('No argument');
} else {
  console.log('Argument found');
}
