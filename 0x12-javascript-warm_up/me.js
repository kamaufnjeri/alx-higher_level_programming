#!/usr/bin/node
const k = process.argv;
if (k[2] === undefined) {
  console.log('undefined');
} else {
  console.log(k[2]);
}
const j = k.length;
