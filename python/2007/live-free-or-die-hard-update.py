
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Live Free or Die Hard", 
    year=2007
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Live Free or Die Hard", 
        year=2007, 
        plot="John McClane and a young hacker join forces to take down master cyber-terrorist Thomas Gabriel in Washington D.C.", 
        rating=7.2
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    