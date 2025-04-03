
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Me and Earl and the Dying Girl", 
    year=2015
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Me and Earl and the Dying Girl", 
        year=2015, 
        plot="High schooler Greg, who spends most of his time making parodies of classic movies with his co-worker Earl, finds his outlook forever altered after befriending a classmate who has just been diagnosed with cancer.", 
        rating=7.8
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    