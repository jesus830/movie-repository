
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Conan the Barbarian to the database
movies.insert(
    title="Conan the Barbarian", 
    year=2011, 
    plot="A vengeful barbarian warrior sets off to get his revenge on the evil warlord who attacked his village and murdered his father when he was a boy.", 
    rating=5.2
)

# Confirm that the movie was added
movie = movies.select(
    title="Conan the Barbarian", 
    year=2011
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    