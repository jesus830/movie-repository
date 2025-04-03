
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Great Wall", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Great Wall", 
        year=2016, 
        plot="European mercenaries searching for black powder become embroiled in the defense of the Great Wall of China against a horde of monstrous creatures.", 
        rating=6.1
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    