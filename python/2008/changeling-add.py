
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Changeling to the database
movies.insert(
    title="Changeling", 
    year=2008, 
    plot="A grief-stricken mother takes on the LAPD to her own detriment when it stubbornly tries to pass off an obvious impostor as her missing child, while also refusing to give up hope that she will find him one day.", 
    rating=7.8
)

# Confirm that the movie was added
movie = movies.select(
    title="Changeling", 
    year=2008
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    