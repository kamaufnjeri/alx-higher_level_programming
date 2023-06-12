#!/usr/bin/node
const myArg = process.argv[2];
if (myArg === undefined) {
  console.log('Missing size');
} else if (isNaN(Number(myArg)) === true) {
  console.log('Missing size');
} else {
  let width = '';
  for (let i = 0; i < Number(myArg); i++) {
    width += 'X';
  }
  for (let j = 0; j < Number(myArg); j++) {
    console.log(width);
  }
}
