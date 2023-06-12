#!/usr/bin/node
const myArr = process.argv;
const numArr = myArr.slice(2, myArr.length);
const sortArr = numArr.sort((a, b) => a - b);
if (sortArr.length === 0) {
  console.log(0);
} else if (sortArr.length === 1) {
  console.log(0);
} else {
  const index = sortArr.length - 2;
  console.log(sortArr[index]);
}
