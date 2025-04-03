
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Heartbreak Kid to the database
movies.insert(
    title="The Heartbreak Kid", 
    year=2007, 
    plot="A newly wed man who believes he's just gotten hitched to the perfect woman encounters another lady on his honeymoon.", 
    rating=5.8
)

# Confirm that the movie was added
movie = movies.select(
    title="The Heartbreak Kid", 
    year=2007
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    