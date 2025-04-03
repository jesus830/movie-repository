
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Kimi no na wa", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Kimi no na wa", 
        year=2016, 
        plot="Two strangers find themselves linked in a bizarre way. When a connection forms, will distance be the only thing to keep them apart?", 
        rating=8.6
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    