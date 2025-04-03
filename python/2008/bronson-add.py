
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Bronson to the database
movies.insert(
    title="Bronson", 
    year=2008, 
    plot="A young man who was sentenced to seven years in prison for robbing a post office ends up spending three decades in solitary confinement. During this time, his own personality is supplanted by his alter-ego, Charles Bronson.", 
    rating=7.1
)

# Confirm that the movie was added
movie = movies.select(
    title="Bronson", 
    year=2008
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    