
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Paper Towns", 
    year=2015
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Paper Towns", 
        year=2015, 
        plot="After an all night adventure, Quentin's life-long crush, Margo, disappears, leaving behind clues that Quentin and his friends follow on the journey of a lifetime.", 
        rating=6.3
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    