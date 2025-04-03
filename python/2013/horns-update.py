
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Horns", 
    year=2013
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Horns", 
        year=2013, 
        plot="In the aftermath of his girlfriend's mysterious death, a young man awakens to find strange horns sprouting from his temples.", 
        rating=6.5
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    