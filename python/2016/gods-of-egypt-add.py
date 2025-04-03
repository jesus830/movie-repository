
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Gods of Egypt to the database
movies.insert(
    title="Gods of Egypt", 
    year=2016, 
    plot="Mortal hero Bek teams with the god Horus in an alliance against Set, the merciless god of darkness, who has usurped Egypt's throne, plunging the once peaceful and prosperous empire into chaos and conflict.", 
    rating=5.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Gods of Egypt", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    