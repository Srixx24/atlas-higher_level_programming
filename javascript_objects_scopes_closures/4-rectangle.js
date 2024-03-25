#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w < 1 || h < 1 || w === undefined || h === undefined) {
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let x = 0; x < this.height; ++x) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const temp = this.height;
    this.height = this.width;
    this.width = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
