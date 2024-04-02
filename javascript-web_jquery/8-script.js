$.get('https://swapi-api.hbtn.io/api/films/?format=json', (data) => {
  $.each(data.results, (value) => {
    $('UL#list_movies').append($('<LI></LI>').text(value.title));
  });
});
