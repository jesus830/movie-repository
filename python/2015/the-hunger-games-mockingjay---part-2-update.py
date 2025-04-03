
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Hunger Games: Mockingjay - Part 2", 
    year=2015
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Hunger Games: Mockingjay - Part 2", 
        year=2015, 
        plot="As the war of Panem escalates to the destruction of other districts, Katniss Everdeen, the reluctant leader of the rebellion, must bring together an army against President Snow, while all she holds dear hangs in the balance.", 
        rating=6.6
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    