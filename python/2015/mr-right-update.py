
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Mr. Right", 
    year=2015
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Mr. Right", 
        year=2015, 
        plot="A girl falls for the "perfect" guy, who happens to have a very fatal flaw: he's a hitman on the run from the crime cartels who employ him.", 
        rating=6.3
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    