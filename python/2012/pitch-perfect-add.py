
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Pitch Perfect to the database
movies.insert(
    title="Pitch Perfect", 
    year=2012, 
    plot="Beca, a freshman at Barden University, is cajoled into joining The Bellas, her school's all-girls singing group. Injecting some much needed energy into their repertoire, The Bellas take on their male rivals in a campus competition.", 
    rating=7.2
)

# Confirm that the movie was added
movie = movies.select(
    title="Pitch Perfect", 
    year=2012
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    