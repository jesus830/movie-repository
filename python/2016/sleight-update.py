
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Sleight", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Sleight", 
        year=2016, 
        plot="A young street magician (Jacob Latimore) is left to care for his little sister after their parents passing, and turns to illegal activities to keep a roof over their heads. When he gets in ... See full summary »", 
        rating=6
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    