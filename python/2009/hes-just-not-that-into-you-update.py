
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="He's Just Not That Into You", 
    year=2009
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="He's Just Not That Into You", 
        year=2009, 
        plot="The Baltimore-set movie of interconnecting story arcs deals with the challenges of reading or misreading human behavior.", 
        rating=6.4
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    