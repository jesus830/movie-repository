
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Everest to the database
movies.insert(
    title="Everest", 
    year=2015, 
    plot="The story of New Zealand's Robert "Rob" Edwin Hall, who on May 10, 1996, together with Scott Fischer, teamed up on a joint expedition to ascend Mount Everest.", 
    rating=7.1
)

# Confirm that the movie was added
movie = movies.select(
    title="Everest", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    