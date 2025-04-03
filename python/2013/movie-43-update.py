
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Movie 43", 
    year=2013
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Movie 43", 
        year=2013, 
        plot="A series of interconnected short films follows a washed-up producer as he pitches insane story lines featuring some of the biggest stars in Hollywood.", 
        rating=4.3
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    