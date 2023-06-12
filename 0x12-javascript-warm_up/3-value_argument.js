#!/usr/bin/node
const myArg = process.argv;
if (myArg.push() < 3) {
  console.log('No argument');
} else {
  console.log(myArg[2]);
}
