
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Furious 6 to the database
movies.insert(
    title="Furious 6", 
    year=2013, 
    plot="Hobbs has Dominic and Brian reassemble their crew to take down a team of mercenaries: Dominic unexpectedly gets convoluted also facing his presumed deceased girlfriend, Letty.", 
    rating=7.1
)

# Confirm that the movie was added
movie = movies.select(
    title="Furious 6", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    