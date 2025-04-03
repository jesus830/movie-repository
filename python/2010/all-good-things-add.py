
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add All Good Things to the database
movies.insert(
    title="All Good Things", 
    year=2010, 
    plot="Mr. David Marks was suspected but never tried for killing his wife Katie who disappeared in 1982, but the truth is eventually revealed.", 
    rating=6.3
)

# Confirm that the movie was added
movie = movies.select(
    title="All Good Things", 
    year=2010
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    