
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Watchmen to the database
movies.insert(
    title="Watchmen", 
    year=2009, 
    plot="In 1985 where former superheroes exist, the murder of a colleague sends active vigilante Rorschach into his own sprawling investigation, uncovering something that could completely change the course of history as we know it.", 
    rating=7.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Watchmen", 
    year=2009
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    