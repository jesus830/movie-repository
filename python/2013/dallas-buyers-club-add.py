
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Dallas Buyers Club to the database
movies.insert(
    title="Dallas Buyers Club", 
    year=2013, 
    plot="In 1985 Dallas, electrician and hustler Ron Woodroof works around the system to help AIDS patients get the medication they need after he is diagnosed with the disease.", 
    rating=8
)

# Confirm that the movie was added
movie = movies.select(
    title="Dallas Buyers Club", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    