
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Jack Ryan: Shadow Recruit", 
    year=2014
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Jack Ryan: Shadow Recruit", 
        year=2014, 
        plot="Jack Ryan, as a young covert CIA analyst, uncovers a Russian plot to crash the U.S. economy with a terrorist attack.", 
        rating=6.2
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    