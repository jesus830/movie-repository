
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Edge of Seventeen", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Edge of Seventeen", 
        year=2016, 
        plot="High-school life gets even more unbearable for Nadine when her best friend, Krista, starts dating her older brother.", 
        rating=7.4
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    