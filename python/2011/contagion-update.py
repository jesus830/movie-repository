
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Contagion", 
    year=2011
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Contagion", 
        year=2011, 
        plot="Healthcare professionals, government officials and everyday people find themselves in the midst of a worldwide epidemic as the CDC works to find a cure.", 
        rating=6.6
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    