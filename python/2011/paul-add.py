
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Paul to the database
movies.insert(
    title="Paul", 
    year=2011, 
    plot="Two British comic-book geeks traveling across the U.S. encounter an alien outside Area 51.", 
    rating=7
)

# Confirm that the movie was added
movie = movies.select(
    title="Paul", 
    year=2011
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    