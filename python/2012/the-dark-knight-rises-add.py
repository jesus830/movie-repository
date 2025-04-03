
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Dark Knight Rises to the database
movies.insert(
    title="The Dark Knight Rises", 
    year=2012, 
    plot="Eight years after the Joker's reign of anarchy, the Dark Knight, with the help of the enigmatic Selina, is forced from his imposed exile to save Gotham City, now on the edge of total annihilation, from the brutal guerrilla terrorist Bane.", 
    rating=8.5
)

# Confirm that the movie was added
movie = movies.select(
    title="The Dark Knight Rises", 
    year=2012
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    