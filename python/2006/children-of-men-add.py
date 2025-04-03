
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Children of Men to the database
movies.insert(
    title="Children of Men", 
    year=2006, 
    plot="In 2027, in a chaotic world in which women have become somehow infertile, a former activist agrees to help transport a miraculously pregnant woman to a sanctuary at sea.", 
    rating=7.9
)

# Confirm that the movie was added
movie = movies.select(
    title="Children of Men", 
    year=2006
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    