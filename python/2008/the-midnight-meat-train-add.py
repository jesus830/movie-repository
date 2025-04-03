
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Midnight Meat Train to the database
movies.insert(
    title="The Midnight Meat Train", 
    year=2008, 
    plot="A photographer's obsessive pursuit of dark subject matter leads him into the path of a serial killer who stalks late night commuters, ultimately butchering them in the most gruesome ways imaginable.", 
    rating=6.1
)

# Confirm that the movie was added
movie = movies.select(
    title="The Midnight Meat Train", 
    year=2008
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    