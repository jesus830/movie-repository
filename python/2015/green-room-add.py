
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Green Room to the database
movies.insert(
    title="Green Room", 
    year=2015, 
    plot="A punk rock band is forced to fight for survival after witnessing a murder at a neo-Nazi skinhead bar.", 
    rating=7
)

# Confirm that the movie was added
movie = movies.select(
    title="Green Room", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    