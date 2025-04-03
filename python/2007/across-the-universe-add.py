
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Across the Universe to the database
movies.insert(
    title="Across the Universe", 
    year=2007, 
    plot="The music of the Beatles and the Vietnam War form the backdrop for the romance between an upper-class American girl and a poor Liverpudlian artist.", 
    rating=7.4
)

# Confirm that the movie was added
movie = movies.select(
    title="Across the Universe", 
    year=2007
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    