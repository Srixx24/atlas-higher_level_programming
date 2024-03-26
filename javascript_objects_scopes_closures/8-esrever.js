#!/usr/bin/node
exports.esrever = function (list) {
  const R = list.length - 1;
  const L = 0;

  while (R > L) {
    const temp = list[L];
    list[L] = list[R];
    list[R] = temp;
    L++;
    R--;
  }
  return list;
};
