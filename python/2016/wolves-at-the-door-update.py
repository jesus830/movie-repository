
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Wolves at the Door", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Wolves at the Door", 
        year=2016, 
        plot="Four friends gather at an elegant home during the Summer of Love, 1969. Unbeknownst to them, deadly visitors are waiting outside. What begins as a simple farewell party turns to a night of ... See full summary »", 
        rating=4.6
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    