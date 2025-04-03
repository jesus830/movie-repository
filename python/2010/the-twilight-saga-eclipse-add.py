
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Twilight Saga: Eclipse to the database
movies.insert(
    title="The Twilight Saga: Eclipse", 
    year=2010, 
    plot="As a string of mysterious killings grips Seattle, Bella, whose high school graduation is fast approaching, is forced to choose between her love for vampire Edward and her friendship with werewolf Jacob.", 
    rating=4.9
)

# Confirm that the movie was added
movie = movies.select(
    title="The Twilight Saga: Eclipse", 
    year=2010
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    