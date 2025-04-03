
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add 20th Century Women to the database
movies.insert(
    title="20th Century Women", 
    year=2016, 
    plot="The story of a teenage boy, his mother, and two other women who help raise him among the love and freedom of Southern California of 1979.", 
    rating=7.4
)

# Confirm that the movie was added
movie = movies.select(
    title="20th Century Women", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    