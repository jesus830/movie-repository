
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The VVitch: A New-England Folktale to the database
movies.insert(
    title="The VVitch: A New-England Folktale", 
    year=2015, 
    plot="A family in 1630s New England is torn apart by the forces of witchcraft, black magic and possession.", 
    rating=6.8
)

# Confirm that the movie was added
movie = movies.select(
    title="The VVitch: A New-England Folktale", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    