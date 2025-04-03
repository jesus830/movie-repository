
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Brimstone to the database
movies.insert(
    title="Brimstone", 
    year=2016, 
    plot="From the moment the new reverend climbs the pulpit, Liz knows she and her family are in great danger.", 
    rating=7.1
)

# Confirm that the movie was added
movie = movies.select(
    title="Brimstone", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    