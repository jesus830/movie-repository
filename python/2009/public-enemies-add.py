
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Public Enemies to the database
movies.insert(
    title="Public Enemies", 
    year=2009, 
    plot="The Feds try to take down notorious American gangsters John Dillinger, Baby Face Nelson and Pretty Boy Floyd during a booming crime wave in the 1930s.", 
    rating=7
)

# Confirm that the movie was added
movie = movies.select(
    title="Public Enemies", 
    year=2009
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    