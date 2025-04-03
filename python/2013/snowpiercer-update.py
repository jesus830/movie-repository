
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Snowpiercer", 
    year=2013
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Snowpiercer", 
        year=2013, 
        plot="Set in a future where a failed climate-change experiment kills all life on the planet except for a lucky few who boarded the Snowpiercer, a train that travels around the globe, where a class system emerges.", 
        rating=7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    