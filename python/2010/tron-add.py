
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Tron to the database
movies.insert(
    title="Tron", 
    year=2010, 
    plot="The son of a virtual world designer goes looking for his father and ends up inside the digital world that his father designed. He meets his father's corrupted creation and a unique ally who was born inside the digital world.", 
    rating=6.8
)

# Confirm that the movie was added
movie = movies.select(
    title="Tron", 
    year=2010
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    