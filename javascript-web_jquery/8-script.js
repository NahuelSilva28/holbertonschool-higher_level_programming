$(function() {
    $.get("https://swapi-api.hbtn.io/api/films/?format=json", function(data) {
      var movies = data.results;
      var listMovies = $("#list_movies");
  
      $.each(movies, function(index, movie) {
        $("<li>").text(movie.title).appendTo(listMovies);
      });
    });
  });
  