
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Bridge to Terabithia to the database
movies.insert(
    title="Bridge to Terabithia", 
    year=2007, 
    plot="A preteen's life turns upside down when he befriends the new girl in school and they imagine a whole new fantasy world to escape reality.", 
    rating=7.2
)

# Confirm that the movie was added
movie = movies.select(
    title="Bridge to Terabithia", 
    year=2007
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    