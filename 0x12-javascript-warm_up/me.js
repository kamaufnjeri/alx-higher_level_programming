#!/usr/bin/node
const k = process.argv;
console.log(k);
const j = k.length;
k.forEach((e, idx) => {
  console.log(`${e} ${idx}`);
});
