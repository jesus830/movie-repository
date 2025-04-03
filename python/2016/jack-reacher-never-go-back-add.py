
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Jack Reacher: Never Go Back to the database
movies.insert(
    title="Jack Reacher: Never Go Back", 
    year=2016, 
    plot="Jack Reacher must uncover the truth behind a major government conspiracy in order to clear his name. On the run as a fugitive from the law, Reacher uncovers a potential secret from his past that could change his life forever.", 
    rating=6.1
)

# Confirm that the movie was added
movie = movies.select(
    title="Jack Reacher: Never Go Back", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    