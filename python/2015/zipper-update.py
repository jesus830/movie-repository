
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Zipper", 
    year=2015
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Zipper", 
        year=2015, 
        plot="A successful family man with a blossoming political career loses all sense of morality when he becomes addicted to using an escort agency.", 
        rating=5.7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    