
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Conjuring 2 to the database
movies.insert(
    title="The Conjuring 2", 
    year=2016, 
    plot="Lorraine and Ed Warren travel to north London to help a single mother raising four children alone in a house plagued by a malicious spirit.", 
    rating=7.4
)

# Confirm that the movie was added
movie = movies.select(
    title="The Conjuring 2", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    