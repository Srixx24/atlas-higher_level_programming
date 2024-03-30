#!/usr/bin/node
const request = require('request');
const url = `https://swapi-api.hbtn.io/api/films/`;
const charID = 18;
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const parsResp = JSON.parse(body);
    const filtered = parsResp.results.filter(film =>
      film.characters.includes(`https://swapi-api.hbtn.io/api/people/${charID}/`)
        );
    console.log(filtered.length);
  }
});
