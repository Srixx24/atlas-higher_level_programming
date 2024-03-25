#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w < 1 || h < 1 || w === undefined || h === undefined) {
      this.width = w;
      this.height = h; 
    } else {
      this.width = 0;
      this.height = 0;
    }
  }
};
