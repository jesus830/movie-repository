
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Insurgent to the database
movies.insert(
    title="Insurgent", 
    year=2015, 
    plot="Beatrice Prior must confront her inner demons and continue her fight against a powerful alliance which threatens to tear her society apart with the help from others on her side.", 
    rating=6.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Insurgent", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    