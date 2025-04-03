
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Yoga Hosers to the database
movies.insert(
    title="Yoga Hosers", 
    year=2016, 
    plot="Two teenage yoga enthusiasts team up with a legendary man-hunter to battle with an ancient evil presence that is threatening their major party plans.", 
    rating=4.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Yoga Hosers", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    