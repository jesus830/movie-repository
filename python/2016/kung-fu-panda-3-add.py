
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Kung Fu Panda 3 to the database
movies.insert(
    title="Kung Fu Panda 3", 
    year=2016, 
    plot="Continuing his "legendary adventures of awesomeness", Po must face two hugely epic, but different threats: one supernatural and the other a little closer to his home.", 
    rating=7.2
)

# Confirm that the movie was added
movie = movies.select(
    title="Kung Fu Panda 3", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    