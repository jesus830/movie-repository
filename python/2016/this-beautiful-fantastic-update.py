
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="This Beautiful Fantastic", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="This Beautiful Fantastic", 
        year=2016, 
        plot="A young woman who dreams of being a children's author makes an unlikely friendship with a cantankerous, rich old widower.", 
        rating=6.9
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    