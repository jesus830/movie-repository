
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Robin Hood to the database
movies.insert(
    title="Robin Hood", 
    year=2010, 
    plot="In 12th century England, Robin and his band of marauders confront corruption in a local village and lead an uprising against the crown that will forever alter the balance of world power.", 
    rating=6.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Robin Hood", 
    year=2010
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    