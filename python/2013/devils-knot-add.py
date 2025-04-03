
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Devil's Knot to the database
movies.insert(
    title="Devil's Knot", 
    year=2013, 
    plot="The savage murders of three young children sparks a controversial trial of three teenagers accused of killing the kids as part of a satanic ritual.", 
    rating=6.1
)

# Confirm that the movie was added
movie = movies.select(
    title="Devil's Knot", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    