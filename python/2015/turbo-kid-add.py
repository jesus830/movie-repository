
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Turbo Kid to the database
movies.insert(
    title="Turbo Kid", 
    year=2015, 
    plot="In a post-apocalyptic wasteland in 1997, a comic book fan adopts the persona of his favourite hero to save his enthusiastic friend and fight a tyrannical overlord.", 
    rating=6.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Turbo Kid", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    