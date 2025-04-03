
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="3 Idiots", 
    year=2009
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="3 Idiots", 
        year=2009, 
        plot="Two friends are searching for their long lost companion. They revisit their college days and recall the memories of their friend who inspired them to think differently, even as the rest of the world called them "idiots".", 
        rating=8.4
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    