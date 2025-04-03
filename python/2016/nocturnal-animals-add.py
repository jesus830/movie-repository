
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Nocturnal Animals to the database
movies.insert(
    title="Nocturnal Animals", 
    year=2016, 
    plot="A wealthy art gallery owner is haunted by her ex-husband's novel, a violent thriller she interprets as a symbolic revenge tale.", 
    rating=7.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Nocturnal Animals", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    