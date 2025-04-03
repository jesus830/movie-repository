
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Oculus to the database
movies.insert(
    title="Oculus", 
    year=2013, 
    plot="A woman tries to exonerate her brother, who was convicted of murder, by proving that the crime was committed by a supernatural phenomenon.", 
    rating=6.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Oculus", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    