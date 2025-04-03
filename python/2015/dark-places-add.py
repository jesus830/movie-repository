
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Dark Places to the database
movies.insert(
    title="Dark Places", 
    year=2015, 
    plot="Libby Day was only eight years old when her family was brutally murdered in their rural Kansas farmhouse. Almost thirty years later, she reluctantly agrees to revisit the crime and uncovers the wrenching truths that led up to that tragic night.", 
    rating=6.2
)

# Confirm that the movie was added
movie = movies.select(
    title="Dark Places", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    