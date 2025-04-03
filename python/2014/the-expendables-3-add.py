
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Expendables 3 to the database
movies.insert(
    title="The Expendables 3", 
    year=2014, 
    plot="Barney augments his team with new blood for a personal battle: to take down Conrad Stonebanks, the Expendables co-founder and notorious arms trader who is hell bent on wiping out Barney and every single one of his associates.", 
    rating=6.1
)

# Confirm that the movie was added
movie = movies.select(
    title="The Expendables 3", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    