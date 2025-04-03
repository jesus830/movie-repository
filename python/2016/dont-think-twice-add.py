
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Don't Think Twice to the database
movies.insert(
    title="Don't Think Twice", 
    year=2016, 
    plot="When a member of a popular New York City improv troupe gets a huge break, the rest of the group - all best friends - start to realize that not everyone is going to make it after all.", 
    rating=6.8
)

# Confirm that the movie was added
movie = movies.select(
    title="Don't Think Twice", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    