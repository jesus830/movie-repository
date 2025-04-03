
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add This Means War to the database
movies.insert(
    title="This Means War", 
    year=2012, 
    plot="Two top CIA operatives wage an epic battle against one another after they discover they are dating the same woman.", 
    rating=6.3
)

# Confirm that the movie was added
movie = movies.select(
    title="This Means War", 
    year=2012
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    