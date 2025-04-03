
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Dead Awake", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Dead Awake", 
        year=2016, 
        plot="A young woman must save herself and her friends from an ancient evil that stalks its victims through the real-life phenomenon of sleep paralysis.", 
        rating=4.7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    