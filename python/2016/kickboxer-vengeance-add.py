
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Kickboxer: Vengeance to the database
movies.insert(
    title="Kickboxer: Vengeance", 
    year=2016, 
    plot="A kick boxer is out to avenge his brother.", 
    rating=4.9
)

# Confirm that the movie was added
movie = movies.select(
    title="Kickboxer: Vengeance", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    