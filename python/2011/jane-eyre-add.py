
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Jane Eyre to the database
movies.insert(
    title="Jane Eyre", 
    year=2011, 
    plot="A mousy governess who softens the heart of her employer soon discovers that he's hiding a terrible secret.", 
    rating=7.4
)

# Confirm that the movie was added
movie = movies.select(
    title="Jane Eyre", 
    year=2011
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    