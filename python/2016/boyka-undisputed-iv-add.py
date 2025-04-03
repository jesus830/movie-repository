
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Boyka: Undisputed IV to the database
movies.insert(
    title="Boyka: Undisputed IV", 
    year=2016, 
    plot="In the fourth installment of the fighting franchise, Boyka is shooting for the big leagues when an accidental death in the ring makes him question everything he stands for.", 
    rating=7.4
)

# Confirm that the movie was added
movie = movies.select(
    title="Boyka: Undisputed IV", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    