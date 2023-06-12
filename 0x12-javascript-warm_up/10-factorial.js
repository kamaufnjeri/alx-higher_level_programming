#!/usr/bin/node
function fact(number) {
 if (number === 1) {
  return number;
 } else {
  return number * fact(number - 1);
 }
}
const num = Number(process.argv[2]);
if (isNaN(num) === true) {
 console.log(1);
} else {
 let factorial = fact(num);
 console.log(factorial);
}
