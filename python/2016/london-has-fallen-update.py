
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="London Has Fallen", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="London Has Fallen", 
        year=2016, 
        plot="In London for the Prime Minister's funeral, Mike Banning discovers a plot to assassinate all the attending world leaders.", 
        rating=5.9
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    