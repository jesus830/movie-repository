
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Paint It Black to the database
movies.insert(
    title="Paint It Black", 
    year=2016, 
    plot="A young woman attempts to deal with the death of her boyfriend while continuously confronted by his mentally unstable mother.", 
    rating=8.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Paint It Black", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    