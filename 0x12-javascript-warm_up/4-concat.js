#!/usr/bin/node
const myArg = process.argv;
if (myArg[2] === undefined) {
  console.log('undefined is undefined');
} else if (myArg[3] === undefined) {
  const word = myArg[2] + ' is undefined';
  console.log(word);
} else {
  const word = myArg[2] + ' is ' + myArg[3];
  console.log(word);
}
