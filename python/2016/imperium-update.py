
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Imperium", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Imperium", 
        year=2016, 
        plot="A young FBI agent, eager to prove himself in the field, goes undercover as a white supremacist.", 
        rating=6.5
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    