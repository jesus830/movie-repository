
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="12 Years a Slave", 
    year=2013
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="12 Years a Slave", 
        year=2013, 
        plot="In the antebellum United States, Solomon Northup, a free black man from upstate New York, is abducted and sold into slavery.", 
        rating=8.1
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    