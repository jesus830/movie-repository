
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Dracula Untold to the database
movies.insert(
    title="Dracula Untold", 
    year=2014, 
    plot="As his kingdom is being threatened by the Turks, young prince Vlad Tepes must become a monster feared by his own people in order to obtain the power needed to protect his own family, and the families of his kingdom.", 
    rating=6.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Dracula Untold", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    