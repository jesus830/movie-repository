
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Oblivion", 
    year=2013
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Oblivion", 
        year=2013, 
        plot="A veteran assigned to extract Earth's remaining resources begins to question what he knows about his mission and himself.", 
        rating=7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    