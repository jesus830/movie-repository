
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Human Centipede (First Sequence) to the database
movies.insert(
    title="The Human Centipede (First Sequence)", 
    year=2009, 
    plot="A mad scientist kidnaps and mutilates a trio of tourists in order to reassemble them into a human centipede, created by stitching their mouths to each others' rectums.", 
    rating=4.4
)

# Confirm that the movie was added
movie = movies.select(
    title="The Human Centipede (First Sequence)", 
    year=2009
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    