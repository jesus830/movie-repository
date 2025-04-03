
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Paterson to the database
movies.insert(
    title="Paterson", 
    year=2016, 
    plot="A quiet observation of the triumphs and defeats of daily life, along with the poetry evident in its smallest details.", 
    rating=7.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Paterson", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    