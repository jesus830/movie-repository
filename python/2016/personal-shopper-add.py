
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Personal Shopper to the database
movies.insert(
    title="Personal Shopper", 
    year=2016, 
    plot="A personal shopper in Paris refuses to leave the city until she makes contact with her twin brother who previously died there. Her life becomes more complicated when a mysterious person contacts her via text message.", 
    rating=6.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Personal Shopper", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    