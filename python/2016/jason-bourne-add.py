
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Jason Bourne to the database
movies.insert(
    title="Jason Bourne", 
    year=2016, 
    plot="The CIA's most dangerous former operative is drawn out of hiding to uncover more explosive truths about his past.", 
    rating=6.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Jason Bourne", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    