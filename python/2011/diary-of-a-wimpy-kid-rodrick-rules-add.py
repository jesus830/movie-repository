
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Diary of a Wimpy Kid: Rodrick Rules to the database
movies.insert(
    title="Diary of a Wimpy Kid: Rodrick Rules", 
    year=2011, 
    plot="Back in middle school after summer vacation, Greg Heffley and his older brother Rodrick must deal with their parents' misguided attempts to have them bond.", 
    rating=6.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Diary of a Wimpy Kid: Rodrick Rules", 
    year=2011
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    