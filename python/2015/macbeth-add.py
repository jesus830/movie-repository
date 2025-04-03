
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Macbeth to the database
movies.insert(
    title="Macbeth", 
    year=2015, 
    plot="Macbeth, the Thane of Glamis, receives a prophecy from a trio of witches that one day he will become King of Scotland. Consumed by ambition and spurred to action by his wife, Macbeth murders his king and takes the throne for himself.", 
    rating=6.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Macbeth", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    