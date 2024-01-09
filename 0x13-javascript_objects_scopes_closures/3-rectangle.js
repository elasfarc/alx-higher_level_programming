#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ([w, h].every(ele => ele > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let width = '';
      for (let j = 0; j < this.width; j++) {
        width += 'X';
      }
      console.log(width);
    }
  }
}

module.exports = Rectangle;
