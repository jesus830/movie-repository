
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Manchester by the Sea to the database
movies.insert(
    title="Manchester by the Sea", 
    year=2016, 
    plot="A depressed uncle is asked to take care of his teenage nephew after the boy's father dies.", 
    rating=7.9
)

# Confirm that the movie was added
movie = movies.select(
    title="Manchester by the Sea", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    