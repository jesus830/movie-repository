
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Hunger Games: Catching Fire", 
    year=2013
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Hunger Games: Catching Fire", 
        year=2013, 
        plot="Katniss Everdeen and Peeta Mellark become targets of the Capitol after their victory in the 74th Hunger Games sparks a rebellion in the Districts of Panem.", 
        rating=7.6
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    