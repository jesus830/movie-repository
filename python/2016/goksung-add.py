
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Goksung to the database
movies.insert(
    title="Goksung", 
    year=2016, 
    plot="A stranger arrives in a little village and soon after a mysterious sickness starts spreading. A policeman is drawn into the incident and is forced to solve the mystery in order to save his daughter.", 
    rating=7.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Goksung", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    