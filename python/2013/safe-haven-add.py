
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Safe Haven to the database
movies.insert(
    title="Safe Haven", 
    year=2013, 
    plot="A young woman with a mysterious past lands in Southport, North Carolina where her bond with a widower forces her to confront the dark secret that haunts her.", 
    rating=6.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Safe Haven", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    