#!/usr/bin/node
const request = require('request');
const url = `https://swapi-api.hbtn.io/api/films/`;
const charID = 18;
request(url, (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      const parsResp = JSON.parse(body);
      console.log(parsResp.films[charID]);
    }
});
