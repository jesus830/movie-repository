
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Captain Fantastic", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Captain Fantastic", 
        year=2016, 
        plot="In the forests of the Pacific Northwest, a father devoted to raising his six kids with a rigorous physical and intellectual education is forced to leave his paradise and enter the world, challenging his idea of what it means to be a parent.", 
        rating=7.9
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    