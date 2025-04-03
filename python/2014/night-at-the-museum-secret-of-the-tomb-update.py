
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Night at the Museum: Secret of the Tomb", 
    year=2014
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Night at the Museum: Secret of the Tomb", 
        year=2014, 
        plot="Larry spans the globe, uniting favorite and new characters while embarking on an epic quest to save the magic before it is gone forever.", 
        rating=6.2
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    