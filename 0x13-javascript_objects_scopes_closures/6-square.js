#!/usr/bin/node

const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      let length = '';
      for (let i = 0; i < this.width; i++) {
        length += c;
      }
      for (let i = 0; i < this.height; i++) {
        console.log(length);
      }
    }
  }
};
