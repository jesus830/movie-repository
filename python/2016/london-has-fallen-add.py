
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add London Has Fallen to the database
movies.insert(
    title="London Has Fallen", 
    year=2016, 
    plot="In London for the Prime Minister's funeral, Mike Banning discovers a plot to assassinate all the attending world leaders.", 
    rating=5.9
)

# Confirm that the movie was added
movie = movies.select(
    title="London Has Fallen", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    