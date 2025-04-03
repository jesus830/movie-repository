
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Big Hero 6", 
    year=2014
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Big Hero 6", 
        year=2014, 
        plot="The special bond that develops between plus-sized inflatable robot Baymax, and prodigy Hiro Hamada, who team up with a group of friends to form a band of high-tech heroes.", 
        rating=7.8
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    