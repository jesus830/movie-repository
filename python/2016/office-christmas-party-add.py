
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Office Christmas Party to the database
movies.insert(
    title="Office Christmas Party", 
    year=2016, 
    plot="When his uptight CEO sister threatens to shut down his branch, the branch manager throws an epic Christmas party in order to land a big client and save the day, but the party gets way out of hand...", 
    rating=5.8
)

# Confirm that the movie was added
movie = movies.select(
    title="Office Christmas Party", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    