#!/usr/bin/node
function add (a, b) {
  return a + b;
}
const num1 = Number(process.argv[2]);
const num2 = Number(process.argv[3]);
const sum = add(num1, num2);
console.log(sum);
