
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add No Country for Old Men to the database
movies.insert(
    title="No Country for Old Men", 
    year=2007, 
    plot="Violence and mayhem ensue after a hunter stumbles upon a drug deal gone wrong and more than two million dollars in cash near the Rio Grande.", 
    rating=8.1
)

# Confirm that the movie was added
movie = movies.select(
    title="No Country for Old Men", 
    year=2007
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    