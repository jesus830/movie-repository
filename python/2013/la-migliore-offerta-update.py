
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="La migliore offerta", 
    year=2013
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="La migliore offerta", 
        year=2013, 
        plot="In the world of high-end art auctions and antiques, Virgil Oldman is an elderly and esteemed but eccentric genius art-expert, known and appreciated by the world. Oldman is hired by a ... See full summary »", 
        rating=7.8
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    