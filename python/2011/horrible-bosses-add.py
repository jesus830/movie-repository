
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Horrible Bosses to the database
movies.insert(
    title="Horrible Bosses", 
    year=2011, 
    plot="Three friends conspire to murder their awful bosses when they realize they are standing in the way of their happiness.", 
    rating=6.9
)

# Confirm that the movie was added
movie = movies.select(
    title="Horrible Bosses", 
    year=2011
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    