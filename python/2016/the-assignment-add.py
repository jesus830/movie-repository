
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Assignment to the database
movies.insert(
    title="The Assignment", 
    year=2016, 
    plot="After waking up and discovering that he has undergone gender reassignment surgery, an assassin seeks to find the doctor responsible.", 
    rating=4.5
)

# Confirm that the movie was added
movie = movies.select(
    title="The Assignment", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    