#!/usr/bin/node
exports.esrever = function (list) {
  const arr = [];
  for (let j = list.length - 1; j > -1; j--) {
    arr.push(list[j]);
  }
  return arr;
};
