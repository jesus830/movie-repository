
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Suite Française to the database
movies.insert(
    title="Suite Française", 
    year=2014, 
    plot="During the early years of Nazi occupation of France in World War II, romance blooms between Lucile Angellier (Michelle Williams), a French villager, and Bruno von Falk (Matthias Schoenaerts), a German soldier.", 
    rating=6.9
)

# Confirm that the movie was added
movie = movies.select(
    title="Suite Française", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    