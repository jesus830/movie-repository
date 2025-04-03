
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Lowriders to the database
movies.insert(
    title="Lowriders", 
    year=2016, 
    plot="A young street artist in East Los Angeles is caught between his father's obsession with lowrider car culture, his ex-felon brother and his need for self-expression.", 
    rating=6.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Lowriders", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    