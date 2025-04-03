
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Before I Wake", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Before I Wake", 
        year=2016, 
        plot="A young couple adopt an orphaned child whose dreams - and nightmares - manifest physically as he sleeps.", 
        rating=6.1
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    