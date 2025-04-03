
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Gone Baby Gone to the database
movies.insert(
    title="Gone Baby Gone", 
    year=2007, 
    plot="Two Boston area detectives investigate a little girl's kidnapping, which ultimately turns into a crisis both professionally and personally.", 
    rating=7.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Gone Baby Gone", 
    year=2007
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    