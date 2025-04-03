
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Ma vie de Courgette to the database
movies.insert(
    title="Ma vie de Courgette", 
    year=2016, 
    plot="After losing his mother, a young boy is sent to a foster home with other orphans his age where he begins to learn the meaning of trust and true love.", 
    rating=7.8
)

# Confirm that the movie was added
movie = movies.select(
    title="Ma vie de Courgette", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    