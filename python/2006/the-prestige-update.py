
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Prestige", 
    year=2006
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Prestige", 
        year=2006, 
        plot="Two stage magicians engage in competitive one-upmanship in an attempt to create the ultimate stage illusion.", 
        rating=8.5
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    