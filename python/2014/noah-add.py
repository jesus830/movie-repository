
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Noah to the database
movies.insert(
    title="Noah", 
    year=2014, 
    plot="A man is chosen by his world's creator to undertake a momentous mission before an apocalyptic flood cleanses the world.", 
    rating=5.8
)

# Confirm that the movie was added
movie = movies.select(
    title="Noah", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    