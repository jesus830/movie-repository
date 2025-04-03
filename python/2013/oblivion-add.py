
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Oblivion to the database
movies.insert(
    title="Oblivion", 
    year=2013, 
    plot="A veteran assigned to extract Earth's remaining resources begins to question what he knows about his mission and himself.", 
    rating=7
)

# Confirm that the movie was added
movie = movies.select(
    title="Oblivion", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    