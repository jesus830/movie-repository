
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Transformers to the database
movies.insert(
    title="Transformers", 
    year=2007, 
    plot="An ancient struggle between two Cybertronian races, the heroic Autobots and the evil Decepticons, comes to Earth, with a clue to the ultimate power held by a teenager.", 
    rating=7.1
)

# Confirm that the movie was added
movie = movies.select(
    title="Transformers", 
    year=2007
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    