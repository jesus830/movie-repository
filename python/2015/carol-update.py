
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Carol", 
    year=2015
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Carol", 
        year=2015, 
        plot="An aspiring photographer develops an intimate relationship with an older woman in 1950s New York.", 
        rating=7.2
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    