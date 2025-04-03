
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Dear Zindagi to the database
movies.insert(
    title="Dear Zindagi", 
    year=2016, 
    plot="Kaira is a budding cinematographer in search of a perfect life. Her encounter with Jug, an unconventional thinker, helps her gain a new perspective on life. She discovers that happiness is all about finding comfort in life's imperfections.", 
    rating=7.8
)

# Confirm that the movie was added
movie = movies.select(
    title="Dear Zindagi", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    