
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Immortals to the database
movies.insert(
    title="Immortals", 
    year=2011, 
    plot="Theseus is a mortal man chosen by Zeus to lead the fight against the ruthless King Hyperion, who is on a rampage across Greece to obtain a weapon that can destroy humanity.", 
    rating=6
)

# Confirm that the movie was added
movie = movies.select(
    title="Immortals", 
    year=2011
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    