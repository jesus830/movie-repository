
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Love Witch", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Love Witch", 
        year=2016, 
        plot="A modern-day witch uses spells and magic to get men to fall in love with her.", 
        rating=6.2
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    