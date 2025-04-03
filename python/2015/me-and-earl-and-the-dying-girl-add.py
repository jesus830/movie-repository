
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Me and Earl and the Dying Girl to the database
movies.insert(
    title="Me and Earl and the Dying Girl", 
    year=2015, 
    plot="High schooler Greg, who spends most of his time making parodies of classic movies with his co-worker Earl, finds his outlook forever altered after befriending a classmate who has just been diagnosed with cancer.", 
    rating=7.8
)

# Confirm that the movie was added
movie = movies.select(
    title="Me and Earl and the Dying Girl", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    