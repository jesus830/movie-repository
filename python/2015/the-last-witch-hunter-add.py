
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Last Witch Hunter to the database
movies.insert(
    title="The Last Witch Hunter", 
    year=2015, 
    plot="The last witch hunter is all that stands between humanity and the combined forces of the most horrifying witches in history.", 
    rating=6
)

# Confirm that the movie was added
movie = movies.select(
    title="The Last Witch Hunter", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    