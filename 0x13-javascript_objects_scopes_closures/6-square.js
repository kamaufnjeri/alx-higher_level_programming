#!/usr/bin/node
const Squareb = require('./4-rectangle.js');
module.exports = class Square extends Squareb {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      let row = '';
      for (let i = 0; i < this.width; i++) {
        row += c;
      }
      for (let j = 0; j < this.height; j++) {
        console.log(row);
      }
    }
  }
};
