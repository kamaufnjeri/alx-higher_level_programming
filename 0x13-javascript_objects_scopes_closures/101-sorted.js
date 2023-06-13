#!/usr/bin/node
const dict = require('./101-data.js').dict;
let newDict = {};
for (const key in dict) {
  if (newDict[dict[key]] === undefined) {
    newDict[dict[key]] = [];
  } else {
    newDict[dict[key]].push(key);
  }
}
console.log(newDict);
