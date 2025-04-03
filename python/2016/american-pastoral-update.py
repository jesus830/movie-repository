
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="American Pastoral", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="American Pastoral", 
        year=2016, 
        plot="An All-American college star and his beauty queen wife watch their seemingly perfect life fall apart as their daughter joins the turmoil of '60s America.", 
        rating=6.1
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    