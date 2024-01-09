#!/usr/bin/node

const BaseSquare = require('./5-square');

class Square extends BaseSquare {
  charPrint (c) {
    const printedSquare = Array(this.height).fill('');
    printedSquare.forEach((line) => {
      for (let i = 0; i < this.width; i++) {
        line += c ?? 'X';
      }
      console.log(line);
    });
  }
}
module.exports = Square;
