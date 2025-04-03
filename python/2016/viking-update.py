
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Viking", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Viking", 
        year=2016, 
        plot="Kievan Rus, late 10th century. After the death of his father, the young Viking prince Vladimir of Novgorod is forced into exile across the frozen sea.", 
        rating=4.7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    