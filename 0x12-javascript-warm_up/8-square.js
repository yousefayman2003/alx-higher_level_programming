#!/usr/bin/node
const args = process.argv.slice(2);
const length = args.length;
const n = parseInt(args[0]);

if (length === 0 || isNaN(n)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      process.stdout.write('X');
    }
    process.stdout.write('\n');
  }
}
