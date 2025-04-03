
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Void to the database
movies.insert(
    title="The Void", 
    year=2016, 
    plot="Shortly after delivering a patient to an understaffed hospital, a police officer experiences strange and violent occurrences seemingly linked to a group of mysterious hooded figures.", 
    rating=5.8
)

# Confirm that the movie was added
movie = movies.select(
    title="The Void", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    