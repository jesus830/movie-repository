
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add He's Just Not That Into You to the database
movies.insert(
    title="He's Just Not That Into You", 
    year=2009, 
    plot="The Baltimore-set movie of interconnecting story arcs deals with the challenges of reading or misreading human behavior.", 
    rating=6.4
)

# Confirm that the movie was added
movie = movies.select(
    title="He's Just Not That Into You", 
    year=2009
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    