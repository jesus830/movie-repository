
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Love Witch to the database
movies.insert(
    title="The Love Witch", 
    year=2016, 
    plot="A modern-day witch uses spells and magic to get men to fall in love with her.", 
    rating=6.2
)

# Confirm that the movie was added
movie = movies.select(
    title="The Love Witch", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    