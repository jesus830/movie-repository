
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="13 Hours", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="13 Hours", 
        year=2016, 
        plot="During an attack on a U.S. compound in Libya, a security team struggles to make sense out of the chaos.", 
        rating=7.3
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    