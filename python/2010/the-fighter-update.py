
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Fighter", 
    year=2010
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Fighter", 
        year=2010, 
        plot="A look at the early years of boxer "Irish" Micky Ward and his brother who helped train him before going pro in the mid 1980s.", 
        rating=7.8
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    