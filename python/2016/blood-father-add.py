
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Blood Father to the database
movies.insert(
    title="Blood Father", 
    year=2016, 
    plot="An ex-con reunites with his estranged wayward 17-year old daughter to protect her from drug dealers who are trying to kill her.", 
    rating=6.4
)

# Confirm that the movie was added
movie = movies.select(
    title="Blood Father", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    