
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Hunger Games: Mockingjay - Part 1", 
    year=2014
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Hunger Games: Mockingjay - Part 1", 
        year=2014, 
        plot="Katniss Everdeen is in District 13 after she shatters the games forever. Under the leadership of President Coin and the advice of her trusted friends, Katniss spreads her wings as she fights to save Peeta and a nation moved by her courage.", 
        rating=6.7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    