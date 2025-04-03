
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Total Recall to the database
movies.insert(
    title="Total Recall", 
    year=2012, 
    plot="A factory worker, Douglas Quaid, begins to suspect that he is a spy after visiting Rekall - a company that provides its clients with implanted fake memories of a life they would like to have led - goes wrong and he finds himself on the run.", 
    rating=6.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Total Recall", 
    year=2012
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    