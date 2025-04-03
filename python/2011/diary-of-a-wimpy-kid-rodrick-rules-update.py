
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Diary of a Wimpy Kid: Rodrick Rules", 
    year=2011
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Diary of a Wimpy Kid: Rodrick Rules", 
        year=2011, 
        plot="Back in middle school after summer vacation, Greg Heffley and his older brother Rodrick must deal with their parents' misguided attempts to have them bond.", 
        rating=6.6
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    