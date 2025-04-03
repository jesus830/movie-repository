
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Free State of Jones", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Free State of Jones", 
        year=2016, 
        plot="A disillusioned Confederate army deserter returns to Mississippi and leads a militia of fellow deserters, runaway slaves, and women in an uprising against the corrupt local Confederate government.", 
        rating=6.9
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    