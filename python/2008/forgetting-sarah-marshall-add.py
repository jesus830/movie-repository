
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Forgetting Sarah Marshall to the database
movies.insert(
    title="Forgetting Sarah Marshall", 
    year=2008, 
    plot="Devastated Peter takes a Hawaiian vacation in order to deal with the recent break-up with his TV star girlfriend, Sarah. Little does he know, Sarah's traveling to the same resort as her ex - and she's bringing along her new boyfriend.", 
    rating=7.2
)

# Confirm that the movie was added
movie = movies.select(
    title="Forgetting Sarah Marshall", 
    year=2008
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    