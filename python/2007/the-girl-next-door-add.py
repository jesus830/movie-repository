
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Girl Next Door to the database
movies.insert(
    title="The Girl Next Door", 
    year=2007, 
    plot="Based on the Jack Ketchum novel of the same name, The Girl Next Door follows the unspeakable torture and abuses committed on a teenage girl in the care of her aunt...and the boys who witness and fail to report the crime.", 
    rating=6.7
)

# Confirm that the movie was added
movie = movies.select(
    title="The Girl Next Door", 
    year=2007
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    