
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Mother's Day to the database
movies.insert(
    title="Mother's Day", 
    year=2016, 
    plot="Three generations come together in the week leading up to Mother's Day.", 
    rating=5.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Mother's Day", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    