#!/usr/bin/node
let myNum = parseInt(process.argv[2]);

function factorial(num) {
	if (isNaN(num) === true || num === 1) {
		return 1;
	} else if (num === 0) {
		return;
	} else {
		return num * factorial(num - 1);
	}
}

let myFact = factorial(myNum);
console.log(myFact);
