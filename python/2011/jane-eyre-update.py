
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Jane Eyre", 
    year=2011
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Jane Eyre", 
        year=2011, 
        plot="A mousy governess who softens the heart of her employer soon discovers that he's hiding a terrible secret.", 
        rating=7.4
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    