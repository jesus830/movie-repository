
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="In Dubious Battle", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="In Dubious Battle", 
        year=2016, 
        plot="An activist gets caught up in the labor movement for farm workers in California during the 1930s.", 
        rating=6.2
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    