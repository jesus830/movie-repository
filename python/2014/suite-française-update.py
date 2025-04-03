
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Suite Française", 
    year=2014
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Suite Française", 
        year=2014, 
        plot="During the early years of Nazi occupation of France in World War II, romance blooms between Lucile Angellier (Michelle Williams), a French villager, and Bruno von Falk (Matthias Schoenaerts), a German soldier.", 
        rating=6.9
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    