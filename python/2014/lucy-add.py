
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Lucy to the database
movies.insert(
    title="Lucy", 
    year=2014, 
    plot="A woman, accidentally caught in a dark deal, turns the tables on her captors and transforms into a merciless warrior evolved beyond human logic.", 
    rating=6.4
)

# Confirm that the movie was added
movie = movies.select(
    title="Lucy", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    