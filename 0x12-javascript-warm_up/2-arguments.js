#!/usr/bin/node
let myArg = process.argv;
let argLen = myArg.length;
if (argLen == 2) {
	console.log('No argument');
} else if (argLen == 3) {
	console.log('Argument found');
} else {
	console.log('Arguments found');
}
