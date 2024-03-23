#!/usr/bin/node
const theJoke = 'C is fun';
const numb = parseInt(process.argv[2]);
if (isNaN(numb) === true) {
  console.log('Missing number of occurrences');
} else {
  for (const x = 0; x < numb; x++) {
    console.log(theJoke);
  }
}