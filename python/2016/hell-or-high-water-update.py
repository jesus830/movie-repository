
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Hell or High Water", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Hell or High Water", 
        year=2016, 
        plot="A divorced father and his ex-con older brother resort to a desperate scheme in order to save their family's ranch in West Texas.", 
        rating=7.7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    