
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Miracles from Heaven", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Miracles from Heaven", 
        year=2016, 
        plot="A young girl suffering from a rare digestive disorder finds herself miraculously cured after surviving a terrible accident.", 
        rating=7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    