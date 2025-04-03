
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Diary of a Wimpy Kid to the database
movies.insert(
    title="Diary of a Wimpy Kid", 
    year=2010, 
    plot="The adventures of a teenager who is fresh out of elementary and transitions to middle school, where he has to learn the consequences and responsibility to survive the year.", 
    rating=6.2
)

# Confirm that the movie was added
movie = movies.select(
    title="Diary of a Wimpy Kid", 
    year=2010
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    