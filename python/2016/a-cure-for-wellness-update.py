
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="A Cure for Wellness", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="A Cure for Wellness", 
        year=2016, 
        plot="An ambitious young executive is sent to retrieve his company's CEO from an idyllic but mysterious "wellness center" at a remote location in the Swiss Alps, but soon suspects that the spa's treatments are not what they seem.", 
        rating=6.5
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    