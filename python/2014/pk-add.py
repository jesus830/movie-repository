
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add PK to the database
movies.insert(
    title="PK", 
    year=2014, 
    plot="A stranger in the city asks questions no one has asked before. His childlike curiosity will take him on a journey of love, laughter, and letting go.", 
    rating=8.2
)

# Confirm that the movie was added
movie = movies.select(
    title="PK", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    