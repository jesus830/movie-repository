
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add She's the Man to the database
movies.insert(
    title="She's the Man", 
    year=2006, 
    plot="When her brother decides to ditch for a couple weeks, Viola heads over to his elite boarding school, disguised as him, and proceeds to fall for one of his soccer teammates, and soon learns she's not the only one with romantic troubles.", 
    rating=6.4
)

# Confirm that the movie was added
movie = movies.select(
    title="She's the Man", 
    year=2006
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    