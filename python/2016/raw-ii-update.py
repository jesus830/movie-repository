
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Raw (II)", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Raw (II)", 
        year=2016, 
        plot="When a young vegetarian undergoes a carnivorous hazing ritual at vet school, an unbidden taste for meat begins to grow in her.", 
        rating=7.5
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    