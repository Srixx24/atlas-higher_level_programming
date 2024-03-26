#!/usr/bin/node
const square6 = require('./5-square.js');
module.exports = class Square extends square6 {
  charPrint(c) {
      let boop = c;  
      if (c === undefined){
        boop = 'X';
      }
      for (const x = 0; this.height < x; ++x) {
      console.log (c.repeat(this.width));
      }
    }
};
