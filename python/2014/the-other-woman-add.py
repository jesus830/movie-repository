
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Other Woman to the database
movies.insert(
    title="The Other Woman", 
    year=2014, 
    plot="After discovering her boyfriend is married, Carly soon meets the wife he's been betraying. And when yet another love affair is discovered, all three women team up to plot revenge on the three-timing S.O.B.", 
    rating=6
)

# Confirm that the movie was added
movie = movies.select(
    title="The Other Woman", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    