
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Devil Wears Prada to the database
movies.insert(
    title="The Devil Wears Prada", 
    year=2006, 
    plot="A smart but sensible new graduate lands a job as an assistant to Miranda Priestly, the demanding editor-in-chief of a high fashion magazine.", 
    rating=6.8
)

# Confirm that the movie was added
movie = movies.select(
    title="The Devil Wears Prada", 
    year=2006
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    