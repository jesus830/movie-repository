
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add RED to the database
movies.insert(
    title="RED", 
    year=2010, 
    plot="When his peaceful life is threatened by a high-tech assassin, former black-ops agent Frank Moses reassembles his old team in a last ditch effort to survive and uncover his assailants.", 
    rating=7.1
)

# Confirm that the movie was added
movie = movies.select(
    title="RED", 
    year=2010
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    