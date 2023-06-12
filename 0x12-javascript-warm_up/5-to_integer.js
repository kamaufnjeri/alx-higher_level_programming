#!/usr/bin/node
const myArg = process.argv;
if (typeof (myArg[2]) === 'string') {
  const num = Number(myArg[2]);
  if (num === num) {
    console.log(num);
  } else {
    console.log('Not a number');
  }
} else {
  console.log('Not a number');
}
