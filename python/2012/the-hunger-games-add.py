
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Hunger Games to the database
movies.insert(
    title="The Hunger Games", 
    year=2012, 
    plot="Katniss Everdeen voluntarily takes her younger sister's place in the Hunger Games: a televised competition in which two teenagers from each of the twelve Districts of Panem are chosen at random to fight to the death.", 
    rating=7.2
)

# Confirm that the movie was added
movie = movies.select(
    title="The Hunger Games", 
    year=2012
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    