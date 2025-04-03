
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Human Centipede (First Sequence)", 
    year=2009
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Human Centipede (First Sequence)", 
        year=2009, 
        plot="A mad scientist kidnaps and mutilates a trio of tourists in order to reassemble them into a human centipede, created by stitching their mouths to each others' rectums.", 
        rating=4.4
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    