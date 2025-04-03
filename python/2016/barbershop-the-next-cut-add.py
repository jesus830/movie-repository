
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Barbershop: The Next Cut to the database
movies.insert(
    title="Barbershop: The Next Cut", 
    year=2016, 
    plot="As their surrounding community has taken a turn for the worse, the crew at Calvin's Barbershop come together to bring some much needed change to their neighborhood.", 
    rating=5.9
)

# Confirm that the movie was added
movie = movies.select(
    title="Barbershop: The Next Cut", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    