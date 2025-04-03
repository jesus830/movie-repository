
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Gambler", 
    year=2014
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Gambler", 
        year=2014, 
        plot="Lit professor and gambler Jim Bennett's debt causes him to borrow money from his mother and a loan shark. Further complicating his situation is his relationship with one of his students. Will Bennett risk his life for a second chance?", 
        rating=6
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    