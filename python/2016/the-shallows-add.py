
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Shallows to the database
movies.insert(
    title="The Shallows", 
    year=2016, 
    plot="A mere 200 yards from shore, surfer Nancy is attacked by a great white shark, with her short journey to safety becoming the ultimate contest of wills.", 
    rating=6.4
)

# Confirm that the movie was added
movie = movies.select(
    title="The Shallows", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    