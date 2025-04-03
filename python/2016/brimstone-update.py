
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Brimstone", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Brimstone", 
        year=2016, 
        plot="From the moment the new reverend climbs the pulpit, Liz knows she and her family are in great danger.", 
        rating=7.1
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    