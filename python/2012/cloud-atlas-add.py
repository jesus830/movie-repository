
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Cloud Atlas to the database
movies.insert(
    title="Cloud Atlas", 
    year=2012, 
    plot="An exploration of how the actions of individual lives impact one another in the past, present and future, as one soul is shaped from a killer into a hero, and an act of kindness ripples across centuries to inspire a revolution.", 
    rating=7.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Cloud Atlas", 
    year=2012
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    