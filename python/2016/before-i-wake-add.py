
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Before I Wake to the database
movies.insert(
    title="Before I Wake", 
    year=2016, 
    plot="A young couple adopt an orphaned child whose dreams - and nightmares - manifest physically as he sleeps.", 
    rating=6.1
)

# Confirm that the movie was added
movie = movies.select(
    title="Before I Wake", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    