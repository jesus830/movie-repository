
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Boyka: Undisputed IV", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Boyka: Undisputed IV", 
        year=2016, 
        plot="In the fourth installment of the fighting franchise, Boyka is shooting for the big leagues when an accidental death in the ring makes him question everything he stands for.", 
        rating=7.4
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    