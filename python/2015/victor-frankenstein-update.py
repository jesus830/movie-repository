
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Victor Frankenstein", 
    year=2015
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Victor Frankenstein", 
        year=2015, 
        plot="Told from Igor's perspective, we see the troubled young assistant's dark origins, his redemptive friendship with the young medical student Viktor Von Frankenstein, and become eyewitnesses to the emergence of how Frankenstein became the man - and the legend - we know today.", 
        rating=6
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    