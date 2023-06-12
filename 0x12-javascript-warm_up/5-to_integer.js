#!/usr/bin/node
const myArg = process.argv;
if (typeof (myArg[2]) === 'string') {
  const num = Number(myArg[2]);
  if (isNaN(num) === true) {
    console.log('Not a number');
  } else {
    console.log('My number:', num);
  }
} else {
  console.log('Not a number');
}
