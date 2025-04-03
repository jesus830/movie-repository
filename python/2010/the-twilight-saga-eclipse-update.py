
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Twilight Saga: Eclipse", 
    year=2010
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Twilight Saga: Eclipse", 
        year=2010, 
        plot="As a string of mysterious killings grips Seattle, Bella, whose high school graduation is fast approaching, is forced to choose between her love for vampire Edward and her friendship with werewolf Jacob.", 
        rating=4.9
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    