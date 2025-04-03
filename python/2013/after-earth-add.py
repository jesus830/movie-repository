
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add After Earth to the database
movies.insert(
    title="After Earth", 
    year=2013, 
    plot="A crash landing leaves Kitai Raige and his father Cypher stranded on Earth, a millennium after events forced humanity's escape. With Cypher injured, Kitai must embark on a perilous journey to signal for help.", 
    rating=4.9
)

# Confirm that the movie was added
movie = movies.select(
    title="After Earth", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    