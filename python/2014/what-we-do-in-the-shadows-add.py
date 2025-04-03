
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add What We Do in the Shadows to the database
movies.insert(
    title="What We Do in the Shadows", 
    year=2014, 
    plot="A documentary team films the lives of a group of vampires for a few months. The vampires share a house in Wellington, New Zealand. Turns out vampires have their own domestic problems too.", 
    rating=7.6
)

# Confirm that the movie was added
movie = movies.select(
    title="What We Do in the Shadows", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    