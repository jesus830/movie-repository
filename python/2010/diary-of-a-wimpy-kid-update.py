
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Diary of a Wimpy Kid", 
    year=2010
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Diary of a Wimpy Kid", 
        year=2010, 
        plot="The adventures of a teenager who is fresh out of elementary and transitions to middle school, where he has to learn the consequences and responsibility to survive the year.", 
        rating=6.2
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    