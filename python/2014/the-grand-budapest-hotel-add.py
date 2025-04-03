
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Grand Budapest Hotel to the database
movies.insert(
    title="The Grand Budapest Hotel", 
    year=2014, 
    plot="The adventures of Gustave H, a legendary concierge at a famous hotel from the fictional Republic of Zubrowka between the first and second World Wars, and Zero Moustafa, the lobby boy who becomes his most trusted friend.", 
    rating=8.1
)

# Confirm that the movie was added
movie = movies.select(
    title="The Grand Budapest Hotel", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    