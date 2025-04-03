
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Midnight Meat Train", 
    year=2008
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Midnight Meat Train", 
        year=2008, 
        plot="A photographer's obsessive pursuit of dark subject matter leads him into the path of a serial killer who stalks late night commuters, ultimately butchering them in the most gruesome ways imaginable.", 
        rating=6.1
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    