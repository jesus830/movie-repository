
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Purge: Election Year to the database
movies.insert(
    title="The Purge: Election Year", 
    year=2016, 
    plot="Former Police Sergeant Barnes becomes head of security for Senator Charlie Roan, a Presidential candidate targeted for death on Purge night due to her vow to eliminate the Purge.", 
    rating=6
)

# Confirm that the movie was added
movie = movies.select(
    title="The Purge: Election Year", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    