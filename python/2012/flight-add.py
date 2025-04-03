
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Flight to the database
movies.insert(
    title="Flight", 
    year=2012, 
    plot="An airline pilot saves almost all his passengers on his malfunctioning airliner which eventually crashed, but an investigation into the accident reveals something troubling.", 
    rating=7.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Flight", 
    year=2012
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    