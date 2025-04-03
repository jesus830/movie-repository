
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add X-Men: Apocalypse to the database
movies.insert(
    title="X-Men: Apocalypse", 
    year=2016, 
    plot="After the re-emergence of the world's first mutant, world-destroyer Apocalypse, the X-Men must unite to defeat his extinction level plan.", 
    rating=7.1
)

# Confirm that the movie was added
movie = movies.select(
    title="X-Men: Apocalypse", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    