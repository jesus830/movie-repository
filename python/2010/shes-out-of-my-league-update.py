
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="She's Out of My League", 
    year=2010
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="She's Out of My League", 
        year=2010, 
        plot="An average Joe meets the perfect woman, but his lack of confidence and the influence of his friends and family begin to pick away at the relationship.", 
        rating=6.4
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    