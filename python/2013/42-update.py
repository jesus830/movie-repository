
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="42", 
    year=2013
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="42", 
        year=2013, 
        plot="This movie is about Jackie Robinson and his journey to becoming a Brooklyn Dodger and his life during that time.", 
        rating=7.5
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    