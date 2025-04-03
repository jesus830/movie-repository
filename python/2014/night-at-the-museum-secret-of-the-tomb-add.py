
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Night at the Museum: Secret of the Tomb to the database
movies.insert(
    title="Night at the Museum: Secret of the Tomb", 
    year=2014, 
    plot="Larry spans the globe, uniting favorite and new characters while embarking on an epic quest to save the magic before it is gone forever.", 
    rating=6.2
)

# Confirm that the movie was added
movie = movies.select(
    title="Night at the Museum: Secret of the Tomb", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    