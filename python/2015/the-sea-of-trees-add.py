
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Sea of Trees to the database
movies.insert(
    title="The Sea of Trees", 
    year=2015, 
    plot="A suicidal American befriends a Japanese man lost in a forest near Mt. Fuji and the two search for a way out.", 
    rating=5.9
)

# Confirm that the movie was added
movie = movies.select(
    title="The Sea of Trees", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    