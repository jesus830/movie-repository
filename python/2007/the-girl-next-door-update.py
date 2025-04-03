
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Girl Next Door", 
    year=2007
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Girl Next Door", 
        year=2007, 
        plot="Based on the Jack Ketchum novel of the same name, The Girl Next Door follows the unspeakable torture and abuses committed on a teenage girl in the care of her aunt...and the boys who witness and fail to report the crime.", 
        rating=6.7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    