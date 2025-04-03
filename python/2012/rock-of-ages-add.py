
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Rock of Ages to the database
movies.insert(
    title="Rock of Ages", 
    year=2012, 
    plot="A small town girl and a city boy meet on the Sunset Strip, while pursuing their Hollywood dreams.", 
    rating=5.9
)

# Confirm that the movie was added
movie = movies.select(
    title="Rock of Ages", 
    year=2012
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    