
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Kick-Ass 2", 
    year=2013
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Kick-Ass 2", 
        year=2013, 
        plot="Following Kick-Ass' heroics, other citizens are inspired to become masked crusaders. But the Red Mist leads his own group of evil supervillains to kill Kick-Ass and destroy everything for which he stands.", 
        rating=6.6
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    