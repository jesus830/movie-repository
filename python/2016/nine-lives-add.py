
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Nine Lives to the database
movies.insert(
    title="Nine Lives", 
    year=2016, 
    plot="A stuffy businessman finds himself trapped inside the body of his family's cat.", 
    rating=5.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Nine Lives", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    