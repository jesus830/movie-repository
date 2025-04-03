
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Boss", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Boss", 
        year=2016, 
        plot="A titan of industry is sent to prison after she's caught insider trading. When she emerges ready to rebrand herself as America's latest sweetheart, not everyone she screwed over is so quick to forgive and forget.", 
        rating=5.4
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    