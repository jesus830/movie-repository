
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Sherlock Holmes to the database
movies.insert(
    title="Sherlock Holmes", 
    year=2009, 
    plot="Detective Sherlock Holmes and his stalwart partner Watson engage in a battle of wits and brawn with a nemesis whose plot is a threat to all of England.", 
    rating=7.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Sherlock Holmes", 
    year=2009
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    