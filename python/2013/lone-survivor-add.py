
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Lone Survivor to the database
movies.insert(
    title="Lone Survivor", 
    year=2013, 
    plot="Marcus Luttrell and his team set out on a mission to capture or kill notorious Taliban leader Ahmad Shah, in late June 2005. Marcus and his team are left to fight for their lives in one of the most valiant efforts of modern warfare.", 
    rating=7.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Lone Survivor", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    