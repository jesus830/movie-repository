
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Dictator", 
    year=2012
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Dictator", 
        year=2012, 
        plot="The heroic story of a dictator who risked his life to ensure that democracy would never come to the country he so lovingly oppressed.", 
        rating=6.4
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    