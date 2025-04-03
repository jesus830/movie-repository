
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Tomorrowland to the database
movies.insert(
    title="Tomorrowland", 
    year=2015, 
    plot="Bound by a shared destiny, a teen bursting with scientific curiosity and a former boy-genius inventor embark on a mission to unearth the secrets of a place somewhere in time and space that exists in their collective memory.", 
    rating=6.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Tomorrowland", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    