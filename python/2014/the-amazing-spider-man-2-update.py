
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Amazing Spider-Man 2", 
    year=2014
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Amazing Spider-Man 2", 
        year=2014, 
        plot="When New York is put under siege by Oscorp, it is up to Spider-Man to save the city he swore to protect as well as his loved ones.", 
        rating=6.7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    