
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Kickboxer: Vengeance", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Kickboxer: Vengeance", 
        year=2016, 
        plot="A kick boxer is out to avenge his brother.", 
        rating=4.9
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    