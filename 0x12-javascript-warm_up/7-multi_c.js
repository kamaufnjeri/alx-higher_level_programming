#!/usr/bin/node
const myArg = process.argv[2];
if (myArg === undefined) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < Number(myArg); i++) {
    console.log('C is fun');
  }
}
