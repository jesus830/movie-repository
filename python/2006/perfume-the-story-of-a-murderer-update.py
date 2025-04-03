
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Perfume: The Story of a Murderer", 
    year=2006
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Perfume: The Story of a Murderer", 
        year=2006, 
        plot="Jean-Baptiste Grenouille, born with a superior olfactory sense, creates the world's finest perfume. His work, however, takes a dark turn as he searches for the ultimate scent.", 
        rating=7.5
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    