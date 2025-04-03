
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add La migliore offerta to the database
movies.insert(
    title="La migliore offerta", 
    year=2013, 
    plot="In the world of high-end art auctions and antiques, Virgil Oldman is an elderly and esteemed but eccentric genius art-expert, known and appreciated by the world. Oldman is hired by a ... See full summary »", 
    rating=7.8
)

# Confirm that the movie was added
movie = movies.select(
    title="La migliore offerta", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    