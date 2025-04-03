
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Ghostbusters to the database
movies.insert(
    title="Ghostbusters", 
    year=2016, 
    plot="Following a ghost invasion of Manhattan, paranormal enthusiasts Erin Gilbert and Abby Yates, nuclear engineer Jillian Holtzmann, and subway worker Patty Tolan band together to stop the otherworldly threat.", 
    rating=5.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Ghostbusters", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    