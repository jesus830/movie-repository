
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Snowpiercer to the database
movies.insert(
    title="Snowpiercer", 
    year=2013, 
    plot="Set in a future where a failed climate-change experiment kills all life on the planet except for a lucky few who boarded the Snowpiercer, a train that travels around the globe, where a class system emerges.", 
    rating=7
)

# Confirm that the movie was added
movie = movies.select(
    title="Snowpiercer", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    