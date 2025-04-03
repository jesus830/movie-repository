
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The 9th Life of Louis Drax", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The 9th Life of Louis Drax", 
        year=2016, 
        plot="A psychologist who begins working with a young boy who has suffered a near-fatal fall finds himself drawn into a mystery that tests the boundaries of fantasy and reality.", 
        rating=6.3
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    