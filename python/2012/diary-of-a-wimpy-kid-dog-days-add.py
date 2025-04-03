
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Diary of a Wimpy Kid: Dog Days to the database
movies.insert(
    title="Diary of a Wimpy Kid: Dog Days", 
    year=2012, 
    plot="School's out. Summer vacation is on. However, Greg may not have the best summer vacation ever. What could go wrong?", 
    rating=6.4
)

# Confirm that the movie was added
movie = movies.select(
    title="Diary of a Wimpy Kid: Dog Days", 
    year=2012
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    