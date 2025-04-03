
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Snow White and the Huntsman to the database
movies.insert(
    title="Snow White and the Huntsman", 
    year=2012, 
    plot="In a twist to the fairy tale, the Huntsman ordered to take Snow White into the woods to be killed winds up becoming her protector and mentor in a quest to vanquish the Evil Queen.", 
    rating=6.1
)

# Confirm that the movie was added
movie = movies.select(
    title="Snow White and the Huntsman", 
    year=2012
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    