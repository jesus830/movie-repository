
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Girl on the Train to the database
movies.insert(
    title="The Girl on the Train", 
    year=2016, 
    plot="A divorcee becomes entangled in a missing persons investigation that promises to send shockwaves throughout her life.", 
    rating=6.5
)

# Confirm that the movie was added
movie = movies.select(
    title="The Girl on the Train", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    