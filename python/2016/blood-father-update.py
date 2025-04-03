
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Blood Father", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Blood Father", 
        year=2016, 
        plot="An ex-con reunites with his estranged wayward 17-year old daughter to protect her from drug dealers who are trying to kill her.", 
        rating=6.4
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    