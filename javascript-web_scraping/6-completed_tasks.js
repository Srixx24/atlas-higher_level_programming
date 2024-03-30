#!/usr/bin/node
const request = require('request');
request(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const parseResp = JSON.parse(body);
    const completed = {};
    parseResp.forEach((todo) => {
      if (todo.completed === true) {
        if (completed[todo.userId] === undefined){
          completed[todo.userId] = 1;
        } else {
          completed[todo.userId]++;
        } 
      }
    });
    console.log(JSON.stringify(completed));
  }
});
