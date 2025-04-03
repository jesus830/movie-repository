
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Horns to the database
movies.insert(
    title="Horns", 
    year=2013, 
    plot="In the aftermath of his girlfriend's mysterious death, a young man awakens to find strange horns sprouting from his temples.", 
    rating=6.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Horns", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    