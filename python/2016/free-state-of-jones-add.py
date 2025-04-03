
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Free State of Jones to the database
movies.insert(
    title="Free State of Jones", 
    year=2016, 
    plot="A disillusioned Confederate army deserter returns to Mississippi and leads a militia of fellow deserters, runaway slaves, and women in an uprising against the corrupt local Confederate government.", 
    rating=6.9
)

# Confirm that the movie was added
movie = movies.select(
    title="Free State of Jones", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    