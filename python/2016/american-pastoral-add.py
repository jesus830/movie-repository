
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add American Pastoral to the database
movies.insert(
    title="American Pastoral", 
    year=2016, 
    plot="An All-American college star and his beauty queen wife watch their seemingly perfect life fall apart as their daughter joins the turmoil of '60s America.", 
    rating=6.1
)

# Confirm that the movie was added
movie = movies.select(
    title="American Pastoral", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    