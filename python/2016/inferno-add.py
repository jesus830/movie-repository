
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Inferno to the database
movies.insert(
    title="Inferno", 
    year=2016, 
    plot="When Robert Langdon wakes up in an Italian hospital with amnesia, he teams up with Dr. Sienna Brooks, and together they must race across Europe against the clock to foil a deadly global plot.", 
    rating=6.2
)

# Confirm that the movie was added
movie = movies.select(
    title="Inferno", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    