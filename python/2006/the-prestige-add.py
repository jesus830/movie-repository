
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Prestige to the database
movies.insert(
    title="The Prestige", 
    year=2006, 
    plot="Two stage magicians engage in competitive one-upmanship in an attempt to create the ultimate stage illusion.", 
    rating=8.5
)

# Confirm that the movie was added
movie = movies.select(
    title="The Prestige", 
    year=2006
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    