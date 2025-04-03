
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Edge of Seventeen to the database
movies.insert(
    title="The Edge of Seventeen", 
    year=2016, 
    plot="High-school life gets even more unbearable for Nadine when her best friend, Krista, starts dating her older brother.", 
    rating=7.4
)

# Confirm that the movie was added
movie = movies.select(
    title="The Edge of Seventeen", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    