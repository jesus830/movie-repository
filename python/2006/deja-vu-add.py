
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Deja Vu to the database
movies.insert(
    title="Deja Vu", 
    year=2006, 
    plot="After a ferry is bombed in New Orleans, an A.T.F. agent joins a unique investigation using experimental surveillance technology to find the bomber, but soon finds himself becoming obsessed with one of the victims.", 
    rating=7
)

# Confirm that the movie was added
movie = movies.select(
    title="Deja Vu", 
    year=2006
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    