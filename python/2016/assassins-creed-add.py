
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Assassin's Creed to the database
movies.insert(
    title="Assassin's Creed", 
    year=2016, 
    plot="When Callum Lynch explores the memories of his ancestor Aguilar and gains the skills of a Master Assassin, he discovers he is a descendant of the secret Assassins society.", 
    rating=5.9
)

# Confirm that the movie was added
movie = movies.select(
    title="Assassin's Creed", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    