
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Adjustment Bureau to the database
movies.insert(
    title="The Adjustment Bureau", 
    year=2011, 
    plot="The affair between a politician and a contemporary dancer is affected by mysterious forces keeping the lovers apart.", 
    rating=7.1
)

# Confirm that the movie was added
movie = movies.select(
    title="The Adjustment Bureau", 
    year=2011
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    