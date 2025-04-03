
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Fast Five to the database
movies.insert(
    title="Fast Five", 
    year=2011, 
    plot="Dominic Toretto and his crew of street racers plan a massive heist to buy their freedom while in the sights of a powerful Brazilian drug lord and a dangerous federal agent.", 
    rating=7.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Fast Five", 
    year=2011
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    