
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Allied to the database
movies.insert(
    title="Allied", 
    year=2016, 
    plot="In 1942, a Canadian intelligence officer in North Africa encounters a female French Resistance fighter on a deadly mission behind enemy lines. When they reunite in London, their relationship is tested by the pressures of war.", 
    rating=7.1
)

# Confirm that the movie was added
movie = movies.select(
    title="Allied", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    