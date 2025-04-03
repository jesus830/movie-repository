
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Ridiculous 6 to the database
movies.insert(
    title="The Ridiculous 6", 
    year=2015, 
    plot="An outlaw who was raised by Native Americans discovers that he has five half-brothers; together the men go on a mission to find their wayward, deadbeat dad.", 
    rating=4.8
)

# Confirm that the movie was added
movie = movies.select(
    title="The Ridiculous 6", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    