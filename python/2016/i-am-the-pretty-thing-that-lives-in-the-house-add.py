
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add I Am the Pretty Thing That Lives in the House to the database
movies.insert(
    title="I Am the Pretty Thing That Lives in the House", 
    year=2016, 
    plot="A young nurse takes care of elderly author who lives in a haunted house.", 
    rating=4.7
)

# Confirm that the movie was added
movie = movies.select(
    title="I Am the Pretty Thing That Lives in the House", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    