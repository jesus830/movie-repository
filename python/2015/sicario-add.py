
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Sicario to the database
movies.insert(
    title="Sicario", 
    year=2015, 
    plot="An idealistic FBI agent is enlisted by a government task force to aid in the escalating war against drugs at the border area between the U.S. and Mexico.", 
    rating=7.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Sicario", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    