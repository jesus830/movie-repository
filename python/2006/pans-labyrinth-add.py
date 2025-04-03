
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Pan's Labyrinth to the database
movies.insert(
    title="Pan's Labyrinth", 
    year=2006, 
    plot="In the falangist Spain of 1944, the bookish young stepdaughter of a sadistic army officer escapes into an eerie but captivating fantasy world.", 
    rating=8.2
)

# Confirm that the movie was added
movie = movies.select(
    title="Pan's Labyrinth", 
    year=2006
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    