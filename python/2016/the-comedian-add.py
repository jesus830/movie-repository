
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Comedian to the database
movies.insert(
    title="The Comedian", 
    year=2016, 
    plot="A look at the life of an aging insult comic named Jack Burke.", 
    rating=5.4
)

# Confirm that the movie was added
movie = movies.select(
    title="The Comedian", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    