
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Jason Bourne", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Jason Bourne", 
        year=2016, 
        plot="The CIA's most dangerous former operative is drawn out of hiding to uncover more explosive truths about his past.", 
        rating=6.7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    