
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Loft to the database
movies.insert(
    title="The Loft", 
    year=2014, 
    plot="Five married guys conspire to secretly share a penthouse loft in the city--a place where they can carry out hidden affairs and indulge in their deepest fantasies. But the fantasy becomes a nightmare when they discover the dead body of an unknown woman in the loft, and they realize one of the group must be involved.", 
    rating=6.3
)

# Confirm that the movie was added
movie = movies.select(
    title="The Loft", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    