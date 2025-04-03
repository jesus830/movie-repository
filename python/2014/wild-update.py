
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Wild", 
    year=2014
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Wild", 
        year=2014, 
        plot="A chronicle of one woman's 1,100-mile solo hike undertaken as a way to recover from a recent personal tragedy.", 
        rating=7.1
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    