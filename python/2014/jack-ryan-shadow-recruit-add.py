
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Jack Ryan: Shadow Recruit to the database
movies.insert(
    title="Jack Ryan: Shadow Recruit", 
    year=2014, 
    plot="Jack Ryan, as a young covert CIA analyst, uncovers a Russian plot to crash the U.S. economy with a terrorist attack.", 
    rating=6.2
)

# Confirm that the movie was added
movie = movies.select(
    title="Jack Ryan: Shadow Recruit", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    