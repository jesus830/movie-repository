
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Moonrise Kingdom to the database
movies.insert(
    title="Moonrise Kingdom", 
    year=2012, 
    plot="A pair of young lovers flee their New England town, which causes a local search party to fan out to find them.", 
    rating=7.8
)

# Confirm that the movie was added
movie = movies.select(
    title="Moonrise Kingdom", 
    year=2012
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    