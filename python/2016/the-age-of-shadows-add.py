
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Age of Shadows to the database
movies.insert(
    title="The Age of Shadows", 
    year=2016, 
    plot="Japanese agents close in as members of the Korean resistance plan an attack in 1920's Seoul.", 
    rating=7.2
)

# Confirm that the movie was added
movie = movies.select(
    title="The Age of Shadows", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    