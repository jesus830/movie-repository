
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Birth of the Dragon to the database
movies.insert(
    title="Birth of the Dragon", 
    year=2016, 
    plot="Young, up-and-coming martial artist, Bruce Lee, challenges legendary kung fu master Wong Jack Man to a no-holds-barred fight in Northern California.", 
    rating=3.9
)

# Confirm that the movie was added
movie = movies.select(
    title="Birth of the Dragon", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    