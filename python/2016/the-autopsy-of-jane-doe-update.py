
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Autopsy of Jane Doe", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Autopsy of Jane Doe", 
        year=2016, 
        plot="A father and son, both coroners, are pulled into a complex mystery while attempting to identify the body of a young woman, who was apparently harboring dark secrets.", 
        rating=6.8
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    