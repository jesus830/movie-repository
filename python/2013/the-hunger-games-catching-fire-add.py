
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Hunger Games: Catching Fire to the database
movies.insert(
    title="The Hunger Games: Catching Fire", 
    year=2013, 
    plot="Katniss Everdeen and Peeta Mellark become targets of the Capitol after their victory in the 74th Hunger Games sparks a rebellion in the Districts of Panem.", 
    rating=7.6
)

# Confirm that the movie was added
movie = movies.select(
    title="The Hunger Games: Catching Fire", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    