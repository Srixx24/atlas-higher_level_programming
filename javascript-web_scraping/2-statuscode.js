#!/usr/bin/node
const request = require('request');
request(process.argv[2], (error, respo) => {
  if (respo) {
    console.log(`code: ${respo.statusCode}`);
  } else if (error) {
    console.log(error);
  }
});
