
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Whisky Galore", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Whisky Galore", 
        year=2016, 
        plot="Scottish islanders try to plunder cases of whisky from a stranded ship.", 
        rating=5
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    