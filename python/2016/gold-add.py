
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Gold to the database
movies.insert(
    title="Gold", 
    year=2016, 
    plot="Kenny Wells, a prospector desperate for a lucky break, teams up with a similarly eager geologist and sets off on a journey to find gold in the uncharted jungle of Indonesia.", 
    rating=6.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Gold", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    