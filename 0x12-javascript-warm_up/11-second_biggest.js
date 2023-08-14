#!/usr/bin/node
const myArray = [];

for (let i = 0; i < process.argv.length - 2; i++) {
  myArray.push(Number(process.argv[i + 2]));
}
const mySortedArray = myArray.sort();
if (mySortedArray.length <= 1) {
  console.log(0);
} else {
  console.log(mySortedArray[mySortedArray.length - 2]);
}
