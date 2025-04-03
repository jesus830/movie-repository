
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Moonrise Kingdom", 
    year=2012
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Moonrise Kingdom", 
        year=2012, 
        plot="A pair of young lovers flee their New England town, which causes a local search party to fan out to find them.", 
        rating=7.8
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    