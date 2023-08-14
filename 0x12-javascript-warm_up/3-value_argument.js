#!/usr/bin/node
const myVar = process.argv.length;

if (myVar < 3) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
