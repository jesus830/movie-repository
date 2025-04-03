
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Now You See Me to the database
movies.insert(
    title="Now You See Me", 
    year=2013, 
    plot="An FBI agent and an Interpol detective track a team of illusionists who pull off bank heists during their performances and reward their audiences with the money.", 
    rating=7.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Now You See Me", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    