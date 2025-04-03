
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Yoga Hosers", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Yoga Hosers", 
        year=2016, 
        plot="Two teenage yoga enthusiasts team up with a legendary man-hunter to battle with an ancient evil presence that is threatening their major party plans.", 
        rating=4.3
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    