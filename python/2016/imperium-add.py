
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Imperium to the database
movies.insert(
    title="Imperium", 
    year=2016, 
    plot="A young FBI agent, eager to prove himself in the field, goes undercover as a white supremacist.", 
    rating=6.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Imperium", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    