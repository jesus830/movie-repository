
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Rise of the Planet of the Apes to the database
movies.insert(
    title="Rise of the Planet of the Apes", 
    year=2011, 
    plot="A substance, designed to help the brain repair itself, gives rise to a super-intelligent chimp who leads an ape uprising.", 
    rating=7.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Rise of the Planet of the Apes", 
    year=2011
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    