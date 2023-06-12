#!/usr/bin/node
const myArg = process.argv;
const num = parseInt(myArg[2]);
if (num) {
  console.log(num);
} else {
  console.log('Not a number');
}
