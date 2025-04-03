
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Blue Valentine", 
    year=2010
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Blue Valentine", 
        year=2010, 
        plot="The relationship of a contemporary married couple, charting their evolution over a span of years by cross-cutting between time periods.", 
        rating=7.4
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    