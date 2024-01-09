#!/usr/bin/node
const fs = require('fs');
const argv = process.argv.slice(2);

const f1 = fs.readFileSync(argv[0], 'utf-8');
const f2 = fs.readFileSync(argv[1], 'utf-8');
const newFile = f1 + f2;

fs.writeFileSync(argv[2], newFile, 'utf-8');
