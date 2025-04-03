
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Couples Retreat", 
    year=2009
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Couples Retreat", 
        year=2009, 
        plot="A comedy centered around four couples who settle into a tropical-island resort for a vacation. While one of the couples is there to work on the marriage, the others fail to realize that participation in the resort's therapy sessions is not optional.", 
        rating=5.5
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    