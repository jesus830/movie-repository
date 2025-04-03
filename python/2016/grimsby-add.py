
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Grimsby to the database
movies.insert(
    title="Grimsby", 
    year=2016, 
    plot="A new assignment forces a top spy to team up with his football hooligan brother.", 
    rating=6.2
)

# Confirm that the movie was added
movie = movies.select(
    title="Grimsby", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    