#!/usr/bin/node
const dict = require('./101-data.js').dict;
const arr1 = [];
const arr2 = [];
const arr3 = [];
for (const key in dict) {
  if (dict[key] === 1) {
    arr1.push(key);
  } else if (dict[key] === 2) {
    arr2.push(key);
  } else if (dict[key] === 3) {
    arr3.push(key);
  } else {
    const newDict = {};
  }
}
const newDict = {
  1: arr1,
  2: arr2,
  3: arr3
};
console.log(newDict);
