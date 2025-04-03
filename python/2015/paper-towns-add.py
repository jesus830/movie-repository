
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Paper Towns to the database
movies.insert(
    title="Paper Towns", 
    year=2015, 
    plot="After an all night adventure, Quentin's life-long crush, Margo, disappears, leaving behind clues that Quentin and his friends follow on the journey of a lifetime.", 
    rating=6.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Paper Towns", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    