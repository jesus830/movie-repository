
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Lone Ranger to the database
movies.insert(
    title="The Lone Ranger", 
    year=2013, 
    plot="Native American warrior Tonto recounts the untold tales that transformed John Reid, a man of the law, into a legend of justice.", 
    rating=6.5
)

# Confirm that the movie was added
movie = movies.select(
    title="The Lone Ranger", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    