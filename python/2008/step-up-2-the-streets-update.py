
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Step Up 2: The Streets", 
    year=2008
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Step Up 2: The Streets", 
        year=2008, 
        plot="Romantic sparks occur between two dance students from different backgrounds at the Maryland School of the Arts.", 
        rating=6.2
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    