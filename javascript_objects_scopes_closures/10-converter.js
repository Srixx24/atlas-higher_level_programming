#!/usr/bin/node
exports.converter = function (base) {
  function toBase (numb) {
    return numb.toString(base);
  }
  return toBase;
};
