
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Iris", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Iris", 
        year=2016, 
        plot="Iris, young wife of a businessman, disappears in Paris. Maybe a mechanic with many debts is involved in the strange affair. A really complicated job for the police.", 
        rating=6.1
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    