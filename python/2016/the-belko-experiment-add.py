
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Belko Experiment to the database
movies.insert(
    title="The Belko Experiment", 
    year=2016, 
    plot="In a twisted social experiment, 80 Americans are locked in their high-rise corporate office in Bogotá, Colombia and ordered by an unknown voice coming from the company's intercom system to participate in a deadly game of kill or be killed.", 
    rating=6.3
)

# Confirm that the movie was added
movie = movies.select(
    title="The Belko Experiment", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    