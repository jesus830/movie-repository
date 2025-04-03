
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Black Room to the database
movies.insert(
    title="The Black Room", 
    year=2016, 
    plot="PAUL and JENNIFER HEMDALE have just moved into their dream house. But their happy marriage is about to be put to the test as they slowly discover the secret behind the black room in the ... See full summary »", 
    rating=3.9
)

# Confirm that the movie was added
movie = movies.select(
    title="The Black Room", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    