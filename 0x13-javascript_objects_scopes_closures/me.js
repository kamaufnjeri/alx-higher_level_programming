#!/usr/bin/node
function myfunction () {
  const x = 1;
  var y = 2; // var is a global variable
  if (x) {
    const x = 3;
    var y = 4;
    console.log(x); // will be 3
    console.log(y); // will be 4
  }
  console.log(x); // will be 1
  console.log(y); // will be 4
}
myfunction();
