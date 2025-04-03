
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Freedom Writers", 
    year=2007
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Freedom Writers", 
        year=2007, 
        plot="A young teacher inspires her class of at-risk students to learn tolerance, apply themselves, and pursue education beyond high school.", 
        rating=7.5
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    