
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Closed Circuit to the database
movies.insert(
    title="Closed Circuit", 
    year=2013, 
    plot="A high-profile terrorism case unexpectedly binds together two ex-lovers on the defense team - testing the limits of their loyalties and placing their lives in jeopardy.", 
    rating=6.2
)

# Confirm that the movie was added
movie = movies.select(
    title="Closed Circuit", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    