
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Belko Experiment", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Belko Experiment", 
        year=2016, 
        plot="In a twisted social experiment, 80 Americans are locked in their high-rise corporate office in Bogotá, Colombia and ordered by an unknown voice coming from the company's intercom system to participate in a deadly game of kill or be killed.", 
        rating=6.3
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    