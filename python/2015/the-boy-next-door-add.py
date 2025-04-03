
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Boy Next Door to the database
movies.insert(
    title="The Boy Next Door", 
    year=2015, 
    plot="A woman, separated from her unfaithful husband, falls for a younger man who has moved in next door, but their torrid affair soon takes a dangerous turn.", 
    rating=4.6
)

# Confirm that the movie was added
movie = movies.select(
    title="The Boy Next Door", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    