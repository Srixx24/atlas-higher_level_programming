#!/usr/bin/node
function factorial(x) {
  if (isNaN(x)) {
    return 1;
  } else if (x < 0) {
    return factorial(x - 1)
  } else {
  return 1;
  }
}

const intValue = parseInt(process.argv[2]);
console.log(factorial(intValue));
