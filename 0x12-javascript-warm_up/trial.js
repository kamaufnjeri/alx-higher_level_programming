#!/usr/bin/node
const myArray = [];

for (let i = 0; i < process.argv.length - 2; i++) {
  myArray.push(Number(process.argv[i + 2]));
}

function secondBiggest (arr) {
  const arrSort = arr.sort();
  if (arrSort.length < 2) {
    return 0;
  } else {
    for (let i = arrSort.length - 1; i >= 0; i--) {
      if (arrSort[arrSort.length - 1] !== arrSort[i]) {
        return arrSort[i];
      }
    }
  }
}

const secondBig = secondBiggest(myArray);
console.log(secondBig);
