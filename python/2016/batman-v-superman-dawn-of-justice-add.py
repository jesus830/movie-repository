
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Batman v Superman: Dawn of Justice to the database
movies.insert(
    title="Batman v Superman: Dawn of Justice", 
    year=2016, 
    plot="Fearing that the actions of Superman are left unchecked, Batman takes on the Man of Steel, while the world wrestles with what kind of a hero it really needs.", 
    rating=6.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Batman v Superman: Dawn of Justice", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    