
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Fault in Our Stars", 
    year=2014
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Fault in Our Stars", 
        year=2014, 
        plot="Two teenage cancer patients begin a life-affirming journey to visit a reclusive author in Amsterdam.", 
        rating=7.8
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    