
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Lobster to the database
movies.insert(
    title="The Lobster", 
    year=2015, 
    plot="In a dystopian near future, single people, according to the laws of The City, are taken to The Hotel, where they are obliged to find a romantic partner in forty-five days or are transformed into beasts and sent off into The Woods.", 
    rating=7.1
)

# Confirm that the movie was added
movie = movies.select(
    title="The Lobster", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    