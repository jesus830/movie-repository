
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Kings of Summer to the database
movies.insert(
    title="The Kings of Summer", 
    year=2013, 
    plot="Three teenage friends, in the ultimate act of independence, decide to spend their summer building a house in the woods and living off the land.", 
    rating=7.2
)

# Confirm that the movie was added
movie = movies.select(
    title="The Kings of Summer", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    