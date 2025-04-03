
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Disaster Movie to the database
movies.insert(
    title="Disaster Movie", 
    year=2008, 
    plot="Over the course of one evening, an unsuspecting group of twenty-somethings find themselves bombarded by a series of natural disasters and catastrophic events.", 
    rating=1.9
)

# Confirm that the movie was added
movie = movies.select(
    title="Disaster Movie", 
    year=2008
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    