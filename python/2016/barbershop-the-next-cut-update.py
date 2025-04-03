
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Barbershop: The Next Cut", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Barbershop: The Next Cut", 
        year=2016, 
        plot="As their surrounding community has taken a turn for the worse, the crew at Calvin's Barbershop come together to bring some much needed change to their neighborhood.", 
        rating=5.9
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    