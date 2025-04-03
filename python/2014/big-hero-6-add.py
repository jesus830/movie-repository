
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Big Hero 6 to the database
movies.insert(
    title="Big Hero 6", 
    year=2014, 
    plot="The special bond that develops between plus-sized inflatable robot Baymax, and prodigy Hiro Hamada, who team up with a group of friends to form a band of high-tech heroes.", 
    rating=7.8
)

# Confirm that the movie was added
movie = movies.select(
    title="Big Hero 6", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    