
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Iron Man 2 to the database
movies.insert(
    title="Iron Man 2", 
    year=2010, 
    plot="With the world now aware of his identity as Iron Man, Tony Stark must contend with both his declining health and a vengeful mad man with ties to his father's legacy.", 
    rating=7
)

# Confirm that the movie was added
movie = movies.select(
    title="Iron Man 2", 
    year=2010
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    