
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Mad Max: Fury Road to the database
movies.insert(
    title="Mad Max: Fury Road", 
    year=2015, 
    plot="A woman rebels against a tyrannical ruler in postapocalyptic Australia in search for her home-land with the help of a group of female prisoners, a psychotic worshipper, and a drifter named Max.", 
    rating=8.1
)

# Confirm that the movie was added
movie = movies.select(
    title="Mad Max: Fury Road", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    