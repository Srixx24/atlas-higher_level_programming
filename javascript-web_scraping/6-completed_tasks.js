#!/usr/bin/node
const request = require('request');
const url = `https://jsonplaceholder.typicode.com/todos`
request(url, (error, response, body) => {
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
  }
});
