
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="G.I. Joe: The Rise of Cobra", 
    year=2009
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="G.I. Joe: The Rise of Cobra", 
        year=2009, 
        plot="An elite military unit comprised of special operatives known as G.I. Joe, operating out of The Pit, takes on an evil organization led by a notorious arms dealer.", 
        rating=5.8
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    