
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Accountant to the database
movies.insert(
    title="The Accountant", 
    year=2016, 
    plot="As a math savant uncooks the books for a new client, the Treasury Department closes in on his activities and the body count starts to rise.", 
    rating=7.4
)

# Confirm that the movie was added
movie = movies.select(
    title="The Accountant", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    