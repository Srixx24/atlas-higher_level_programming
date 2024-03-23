#!/usr/bin/node
const square = process.argv[2];
if (isNaN(parseInt(square))) {
  console.log('Missing size');
} else {
  for (let x = 0; square > x; ++x) {
    console.log('x'.repeat(square));
  }
}
