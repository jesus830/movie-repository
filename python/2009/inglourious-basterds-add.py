
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Inglourious Basterds to the database
movies.insert(
    title="Inglourious Basterds", 
    year=2009, 
    plot="In Nazi-occupied France during World War II, a plan to assassinate Nazi leaders by a group of Jewish U.S. soldiers coincides with a theatre owner's vengeful plans for the same.", 
    rating=8.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Inglourious Basterds", 
    year=2009
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    