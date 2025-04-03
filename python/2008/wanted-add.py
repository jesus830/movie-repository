
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Wanted to the database
movies.insert(
    title="Wanted", 
    year=2008, 
    plot="A frustrated office worker learns that he is the son of a professional assassin, and that he shares his father's superhuman killing abilities.", 
    rating=6.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Wanted", 
    year=2008
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    