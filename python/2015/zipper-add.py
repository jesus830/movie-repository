
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Zipper to the database
movies.insert(
    title="Zipper", 
    year=2015, 
    plot="A successful family man with a blossoming political career loses all sense of morality when he becomes addicted to using an escort agency.", 
    rating=5.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Zipper", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    