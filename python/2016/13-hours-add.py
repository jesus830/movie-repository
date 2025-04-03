
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add 13 Hours to the database
movies.insert(
    title="13 Hours", 
    year=2016, 
    plot="During an attack on a U.S. compound in Libya, a security team struggles to make sense out of the chaos.", 
    rating=7.3
)

# Confirm that the movie was added
movie = movies.select(
    title="13 Hours", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    