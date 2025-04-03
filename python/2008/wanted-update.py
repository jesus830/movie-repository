
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Wanted", 
    year=2008
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Wanted", 
        year=2008, 
        plot="A frustrated office worker learns that he is the son of a professional assassin, and that he shares his father's superhuman killing abilities.", 
        rating=6.7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    