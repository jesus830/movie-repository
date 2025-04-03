
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Couples Retreat to the database
movies.insert(
    title="Couples Retreat", 
    year=2009, 
    plot="A comedy centered around four couples who settle into a tropical-island resort for a vacation. While one of the couples is there to work on the marriage, the others fail to realize that participation in the resort's therapy sessions is not optional.", 
    rating=5.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Couples Retreat", 
    year=2009
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    