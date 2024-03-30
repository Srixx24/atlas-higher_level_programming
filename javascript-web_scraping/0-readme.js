#!/usr/bin/node
const fs = require('fs');
fs.readFile(process.argv[2], 'utf-8', (error, file) => {
  if (error) return console.log(error);
  console.log(file);
});
