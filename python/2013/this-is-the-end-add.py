
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add This Is the End to the database
movies.insert(
    title="This Is the End", 
    year=2013, 
    plot="While attending a party at James Franco's house, Seth Rogen, Jay Baruchel and many other celebrities are faced with the Biblical Apocalypse.", 
    rating=6.6
)

# Confirm that the movie was added
movie = movies.select(
    title="This Is the End", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    