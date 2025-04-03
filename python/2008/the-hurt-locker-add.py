
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Hurt Locker to the database
movies.insert(
    title="The Hurt Locker", 
    year=2008, 
    plot="During the Iraq War, a Sergeant recently assigned to an army bomb squad is put at odds with his squad mates due to his maverick way of handling his work.", 
    rating=7.6
)

# Confirm that the movie was added
movie = movies.select(
    title="The Hurt Locker", 
    year=2008
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    