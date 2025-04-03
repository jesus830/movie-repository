
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Seven Pounds to the database
movies.insert(
    title="Seven Pounds", 
    year=2008, 
    plot="A man with a fateful secret embarks on an extraordinary journey of redemption by forever changing the lives of seven strangers.", 
    rating=7.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Seven Pounds", 
    year=2008
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    