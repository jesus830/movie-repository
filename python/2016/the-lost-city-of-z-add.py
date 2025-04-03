
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Lost City of Z to the database
movies.insert(
    title="The Lost City of Z", 
    year=2016, 
    plot="A true-life drama, centering on British explorer Col. Percival Fawcett, who disappeared while searching for a mysterious city in the Amazon in the 1920s.", 
    rating=7.1
)

# Confirm that the movie was added
movie = movies.select(
    title="The Lost City of Z", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    