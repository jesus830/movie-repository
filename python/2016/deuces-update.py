
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Deuces", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Deuces", 
        year=2016, 
        plot="An agent infiltrates a crime ring ran by a charismatic boss.", 
        rating=6.6
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    