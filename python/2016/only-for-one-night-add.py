
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Only for One Night to the database
movies.insert(
    title="Only for One Night", 
    year=2016, 
    plot="A married womans husband with a perfect life cheats with her sister with extreme consequences befalling them all.", 
    rating=4.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Only for One Night", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    