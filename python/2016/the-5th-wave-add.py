
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The 5th Wave to the database
movies.insert(
    title="The 5th Wave", 
    year=2016, 
    plot="Four waves of increasingly deadly alien attacks have left most of Earth decimated. Cassie is on the run, desperately trying to save her younger brother.", 
    rating=5.2
)

# Confirm that the movie was added
movie = movies.select(
    title="The 5th Wave", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    