
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Gone Baby Gone", 
    year=2007
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Gone Baby Gone", 
        year=2007, 
        plot="Two Boston area detectives investigate a little girl's kidnapping, which ultimately turns into a crisis both professionally and personally.", 
        rating=7.7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    