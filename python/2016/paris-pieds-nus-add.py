
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Paris pieds nus to the database
movies.insert(
    title="Paris pieds nus", 
    year=2016, 
    plot="Fiona visits Paris for the first time to assist her myopic Aunt Martha. Catastrophes ensue, mainly involving Dom, a homeless man who has yet to have an emotion or thought he was afraid of expressing.", 
    rating=6.8
)

# Confirm that the movie was added
movie = movies.select(
    title="Paris pieds nus", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    