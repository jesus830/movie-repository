
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Inception to the database
movies.insert(
    title="Inception", 
    year=2010, 
    plot="A thief, who steals corporate secrets through use of dream-sharing technology, is given the inverse task of planting an idea into the mind of a CEO.", 
    rating=8.8
)

# Confirm that the movie was added
movie = movies.select(
    title="Inception", 
    year=2010
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    