
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Step Up to the database
movies.insert(
    title="Step Up", 
    year=2006, 
    plot="Tyler Gage receives the opportunity of a lifetime after vandalizing a performing arts school, gaining him the chance to earn a scholarship and dance with an up and coming dancer, Nora.", 
    rating=6.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Step Up", 
    year=2006
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    