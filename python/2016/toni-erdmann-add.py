
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Toni Erdmann to the database
movies.insert(
    title="Toni Erdmann", 
    year=2016, 
    plot="A practical joking father tries to reconnect with his hard working daughter by creating an outrageous alter ego and posing as her CEO's life coach.", 
    rating=7.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Toni Erdmann", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    