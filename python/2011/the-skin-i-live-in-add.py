
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Skin I Live In to the database
movies.insert(
    title="The Skin I Live In", 
    year=2011, 
    plot="A brilliant plastic surgeon, haunted by past tragedies, creates a type of synthetic skin that withstands any kind of damage. His guinea pig: a mysterious and volatile woman who holds the key to his obsession.", 
    rating=7.6
)

# Confirm that the movie was added
movie = movies.select(
    title="The Skin I Live In", 
    year=2011
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    