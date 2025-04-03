
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Underworld: Blood Wars to the database
movies.insert(
    title="Underworld: Blood Wars", 
    year=2016, 
    plot="Vampire death dealer, Selene (Kate Beckinsale) fights to end the eternal war between the Lycan clan and the Vampire faction that betrayed her.", 
    rating=5.8
)

# Confirm that the movie was added
movie = movies.select(
    title="Underworld: Blood Wars", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    