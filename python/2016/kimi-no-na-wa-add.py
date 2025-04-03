
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Kimi no na wa to the database
movies.insert(
    title="Kimi no na wa", 
    year=2016, 
    plot="Two strangers find themselves linked in a bizarre way. When a connection forms, will distance be the only thing to keep them apart?", 
    rating=8.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Kimi no na wa", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    