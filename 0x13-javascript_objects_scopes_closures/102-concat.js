#!/usr/bin/node
const fs = require('fs');

const a = fs.readFileSync(process.argv[2], 'utf8');
const b = fs.readFileSync(process.argv[3], 'utf8');
const data = a + b;
fs.writeFileSync(process.argv[4], data);
