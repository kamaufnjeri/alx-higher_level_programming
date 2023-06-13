#!/usr/bin/node
const list = require('./100-data.js').list;
const arr = list.map((elem, index) => elem * index);
console.log(list);
console.log(arr);
