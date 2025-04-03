
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Da Vinci Code to the database
movies.insert(
    title="The Da Vinci Code", 
    year=2006, 
    plot="A murder inside the Louvre and clues in Da Vinci paintings lead to the discovery of a religious mystery protected by a secret society for two thousand years -- which could shake the foundations of Christianity.", 
    rating=6.6
)

# Confirm that the movie was added
movie = movies.select(
    title="The Da Vinci Code", 
    year=2006
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    