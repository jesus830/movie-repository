
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Last Witch Hunter", 
    year=2015
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Last Witch Hunter", 
        year=2015, 
        plot="The last witch hunter is all that stands between humanity and the combined forces of the most horrifying witches in history.", 
        rating=6
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    