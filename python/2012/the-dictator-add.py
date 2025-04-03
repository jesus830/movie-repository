
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Dictator to the database
movies.insert(
    title="The Dictator", 
    year=2012, 
    plot="The heroic story of a dictator who risked his life to ensure that democracy would never come to the country he so lovingly oppressed.", 
    rating=6.4
)

# Confirm that the movie was added
movie = movies.select(
    title="The Dictator", 
    year=2012
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    