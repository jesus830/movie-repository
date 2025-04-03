
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Guest to the database
movies.insert(
    title="The Guest", 
    year=2014, 
    plot="A soldier introduces himself to the Peterson family, claiming to be a friend of their son who died in action. After the young man is welcomed into their home, a series of accidental deaths seem to be connected to his presence.", 
    rating=6.7
)

# Confirm that the movie was added
movie = movies.select(
    title="The Guest", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    