
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Trainwreck to the database
movies.insert(
    title="Trainwreck", 
    year=2015, 
    plot="Having thought that monogamy was never possible, a commitment-phobic career woman may have to face her fears when she meets a good guy.", 
    rating=6.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Trainwreck", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    