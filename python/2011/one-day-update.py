
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="One Day", 
    year=2011
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="One Day", 
        year=2011, 
        plot="After spending the night together on the night of their college graduation Dexter and Em are shown each year on the same date to see where they are in their lives. They are sometimes together, sometimes not, on that day.", 
        rating=7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    