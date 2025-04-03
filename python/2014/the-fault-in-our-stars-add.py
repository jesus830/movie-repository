
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Fault in Our Stars to the database
movies.insert(
    title="The Fault in Our Stars", 
    year=2014, 
    plot="Two teenage cancer patients begin a life-affirming journey to visit a reclusive author in Amsterdam.", 
    rating=7.8
)

# Confirm that the movie was added
movie = movies.select(
    title="The Fault in Our Stars", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    