
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add I Spit on Your Grave to the database
movies.insert(
    title="I Spit on Your Grave", 
    year=2010, 
    plot="A writer who is brutalized during her cabin retreat seeks revenge on her attackers, who left her for dead.", 
    rating=6.3
)

# Confirm that the movie was added
movie = movies.select(
    title="I Spit on Your Grave", 
    year=2010
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    