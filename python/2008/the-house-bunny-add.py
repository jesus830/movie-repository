
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The House Bunny to the database
movies.insert(
    title="The House Bunny", 
    year=2008, 
    plot="After Playboy bunny Shelley is kicked out of the playboy mansion, she finds a job as the house mother for a sorority full of socially awkward girls.", 
    rating=5.5
)

# Confirm that the movie was added
movie = movies.select(
    title="The House Bunny", 
    year=2008
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    