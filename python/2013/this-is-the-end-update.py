
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="This Is the End", 
    year=2013
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="This Is the End", 
        year=2013, 
        plot="While attending a party at James Franco's house, Seth Rogen, Jay Baruchel and many other celebrities are faced with the Biblical Apocalypse.", 
        rating=6.6
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    