#!/usr/bin/node
exports.converter = function (base) {
  function num (number) {
    return number.toString(base);
  }
  return num;
};
