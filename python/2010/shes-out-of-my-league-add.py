
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add She's Out of My League to the database
movies.insert(
    title="She's Out of My League", 
    year=2010, 
    plot="An average Joe meets the perfect woman, but his lack of confidence and the influence of his friends and family begin to pick away at the relationship.", 
    rating=6.4
)

# Confirm that the movie was added
movie = movies.select(
    title="She's Out of My League", 
    year=2010
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    