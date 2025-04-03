
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The imposible to the database
movies.insert(
    title="The imposible", 
    year=2012, 
    plot="The story of a tourist family in Thailand caught in the destruction and chaotic aftermath of the 2004 Indian Ocean tsunami.", 
    rating=7.6
)

# Confirm that the movie was added
movie = movies.select(
    title="The imposible", 
    year=2012
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    