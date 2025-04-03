
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="We Are Your Friends", 
    year=2015
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="We Are Your Friends", 
        year=2015, 
        plot="Caught between a forbidden romance and the expectations of his friends, aspiring DJ Cole Carter attempts to find the path in life that leads to fame and fortune.", 
        rating=6.2
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    