
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add 12 Years a Slave to the database
movies.insert(
    title="12 Years a Slave", 
    year=2013, 
    plot="In the antebellum United States, Solomon Northup, a free black man from upstate New York, is abducted and sold into slavery.", 
    rating=8.1
)

# Confirm that the movie was added
movie = movies.select(
    title="12 Years a Slave", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    