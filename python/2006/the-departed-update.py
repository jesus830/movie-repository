
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Departed", 
    year=2006
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Departed", 
        year=2006, 
        plot="An undercover cop and a mole in the police attempt to identify each other while infiltrating an Irish gang in South Boston.", 
        rating=8.5
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    