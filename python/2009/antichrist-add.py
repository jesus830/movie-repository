
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Antichrist to the database
movies.insert(
    title="Antichrist", 
    year=2009, 
    plot="A grieving couple retreat to their cabin in the woods, hoping to repair their broken hearts and troubled marriage. But nature takes its course and things go from bad to worse.", 
    rating=6.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Antichrist", 
    year=2009
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    