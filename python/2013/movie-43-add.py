
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Movie 43 to the database
movies.insert(
    title="Movie 43", 
    year=2013, 
    plot="A series of interconnected short films follows a washed-up producer as he pitches insane story lines featuring some of the biggest stars in Hollywood.", 
    rating=4.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Movie 43", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    