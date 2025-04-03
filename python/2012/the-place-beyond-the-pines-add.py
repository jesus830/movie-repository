
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Place Beyond the Pines to the database
movies.insert(
    title="The Place Beyond the Pines", 
    year=2012, 
    plot="A motorcycle stunt rider turns to robbing banks as a way to provide for his lover and their newborn child, a decision that puts him on a collision course with an ambitious rookie cop navigating a department ruled by a corrupt detective.", 
    rating=7.3
)

# Confirm that the movie was added
movie = movies.select(
    title="The Place Beyond the Pines", 
    year=2012
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    