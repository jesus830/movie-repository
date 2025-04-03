
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Vicky Cristina Barcelona to the database
movies.insert(
    title="Vicky Cristina Barcelona", 
    year=2008, 
    plot="Two girlfriends on a summer holiday in Spain become enamored with the same painter, unaware that his ex-wife, with whom he has a tempestuous relationship, is about to re-enter the picture.", 
    rating=7.1
)

# Confirm that the movie was added
movie = movies.select(
    title="Vicky Cristina Barcelona", 
    year=2008
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    