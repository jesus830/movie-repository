
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Black Swan", 
    year=2010
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Black Swan", 
        year=2010, 
        plot="A committed dancer wins the lead role in a production of Tchaikovsky's "Swan Lake" only to find herself struggling to maintain her sanity.", 
        rating=8
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    