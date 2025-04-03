
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Demolition to the database
movies.insert(
    title="Demolition", 
    year=2015, 
    plot="A successful investment banker struggles after losing his wife in a tragic car crash. With the help of a customer service rep and her young son, he starts to rebuild, beginning with the demolition of the life he once knew.", 
    rating=7
)

# Confirm that the movie was added
movie = movies.select(
    title="Demolition", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    