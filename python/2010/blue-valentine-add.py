
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Blue Valentine to the database
movies.insert(
    title="Blue Valentine", 
    year=2010, 
    plot="The relationship of a contemporary married couple, charting their evolution over a span of years by cross-cutting between time periods.", 
    rating=7.4
)

# Confirm that the movie was added
movie = movies.select(
    title="Blue Valentine", 
    year=2010
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    