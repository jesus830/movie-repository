
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Pan's Labyrinth", 
    year=2006
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Pan's Labyrinth", 
        year=2006, 
        plot="In the falangist Spain of 1944, the bookish young stepdaughter of a sadistic army officer escapes into an eerie but captivating fantasy world.", 
        rating=8.2
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    