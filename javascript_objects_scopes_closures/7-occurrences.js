#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let total = 0;
  for (let x = 0; x < list.length; x++) {
    if (list[x] === searchElement) {
      total++;
    }
  }
  return total;
};
