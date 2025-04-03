
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Other Woman", 
    year=2014
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Other Woman", 
        year=2014, 
        plot="After discovering her boyfriend is married, Carly soon meets the wife he's been betraying. And when yet another love affair is discovered, all three women team up to plot revenge on the three-timing S.O.B.", 
        rating=6
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    