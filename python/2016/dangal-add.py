
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Dangal to the database
movies.insert(
    title="Dangal", 
    year=2016, 
    plot="Former wrestler Mahavir Singh Phogat and his two wrestler daughters struggle towards glory at the Commonwealth Games in the face of societal oppression.", 
    rating=8.8
)

# Confirm that the movie was added
movie = movies.select(
    title="Dangal", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    