
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Green Room", 
    year=2015
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Green Room", 
        year=2015, 
        plot="A punk rock band is forced to fight for survival after witnessing a murder at a neo-Nazi skinhead bar.", 
        rating=7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    