
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Florence Foster Jenkins", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Florence Foster Jenkins", 
        year=2016, 
        plot="The story of Florence Foster Jenkins, a New York heiress who dreamed of becoming an opera singer, despite having a terrible singing voice.", 
        rating=6.9
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    