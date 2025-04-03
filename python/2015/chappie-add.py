
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Chappie to the database
movies.insert(
    title="Chappie", 
    year=2015, 
    plot="In the near future, crime is patrolled by a mechanized police force. When one police droid, Chappie, is stolen and given new programming, he becomes the first robot with the ability to think and feel for himself.", 
    rating=6.9
)

# Confirm that the movie was added
movie = movies.select(
    title="Chappie", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    