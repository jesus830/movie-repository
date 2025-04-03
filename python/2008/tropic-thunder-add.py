
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Tropic Thunder to the database
movies.insert(
    title="Tropic Thunder", 
    year=2008, 
    plot="Through a series of freak occurrences, a group of actors shooting a big-budget war movie are forced to become the soldiers they are portraying.", 
    rating=7
)

# Confirm that the movie was added
movie = movies.select(
    title="Tropic Thunder", 
    year=2008
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    