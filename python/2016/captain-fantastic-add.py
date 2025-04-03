
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Captain Fantastic to the database
movies.insert(
    title="Captain Fantastic", 
    year=2016, 
    plot="In the forests of the Pacific Northwest, a father devoted to raising his six kids with a rigorous physical and intellectual education is forced to leave his paradise and enter the world, challenging his idea of what it means to be a parent.", 
    rating=7.9
)

# Confirm that the movie was added
movie = movies.select(
    title="Captain Fantastic", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    