#!/usr/bin/node
const count = process.argv[2];

if (count > 0) {
  for (let i = 0; i < count; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
