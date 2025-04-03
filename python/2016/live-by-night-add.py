
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Live by Night to the database
movies.insert(
    title="Live by Night", 
    year=2016, 
    plot="A group of Boston-bred gangsters set up shop in balmy Florida during the Prohibition era, facing off against the competition and the Ku Klux Klan.", 
    rating=6.4
)

# Confirm that the movie was added
movie = movies.select(
    title="Live by Night", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    