
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Hunger Games: Mockingjay - Part 1 to the database
movies.insert(
    title="The Hunger Games: Mockingjay - Part 1", 
    year=2014, 
    plot="Katniss Everdeen is in District 13 after she shatters the games forever. Under the leadership of President Coin and the advice of her trusted friends, Katniss spreads her wings as she fights to save Peeta and a nation moved by her courage.", 
    rating=6.7
)

# Confirm that the movie was added
movie = movies.select(
    title="The Hunger Games: Mockingjay - Part 1", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    