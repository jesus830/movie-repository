
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Whisky Galore to the database
movies.insert(
    title="Whisky Galore", 
    year=2016, 
    plot="Scottish islanders try to plunder cases of whisky from a stranded ship.", 
    rating=5
)

# Confirm that the movie was added
movie = movies.select(
    title="Whisky Galore", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    