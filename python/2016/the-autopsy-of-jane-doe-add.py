
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Autopsy of Jane Doe to the database
movies.insert(
    title="The Autopsy of Jane Doe", 
    year=2016, 
    plot="A father and son, both coroners, are pulled into a complex mystery while attempting to identify the body of a young woman, who was apparently harboring dark secrets.", 
    rating=6.8
)

# Confirm that the movie was added
movie = movies.select(
    title="The Autopsy of Jane Doe", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    