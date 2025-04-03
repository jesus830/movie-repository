
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Masterminds", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Masterminds", 
        year=2016, 
        plot="A guard at an armored car company in the Southern U.S. organizes one of the biggest bank heists in American history. Based on the October 1997 Loomis Fargo robbery.", 
        rating=5.8
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    