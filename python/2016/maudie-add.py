
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Maudie to the database
movies.insert(
    title="Maudie", 
    year=2016, 
    plot="An arthritic Nova Scotia woman works as a housekeeper while she hones her skills as an artist and eventually becomes a beloved figure in the community.", 
    rating=7.8
)

# Confirm that the movie was added
movie = movies.select(
    title="Maudie", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    