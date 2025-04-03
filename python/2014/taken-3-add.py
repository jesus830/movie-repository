
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Taken 3 to the database
movies.insert(
    title="Taken 3", 
    year=2014, 
    plot="Ex-government operative Bryan Mills is accused of a ruthless murder he never committed or witnessed. As he is tracked and pursued, Mills brings out his particular set of skills to find the true killer and clear his name.", 
    rating=6
)

# Confirm that the movie was added
movie = movies.select(
    title="Taken 3", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    