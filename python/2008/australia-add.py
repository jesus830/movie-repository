
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Australia to the database
movies.insert(
    title="Australia", 
    year=2008, 
    plot="Set in northern Australia before World War II, an English aristocrat who inherits a sprawling ranch reluctantly pacts with a stock-man in order to protect her new property from a takeover plot. As the pair drive 2,000 head of cattle over unforgiving landscape, they experience the bombing of Darwin, Australia, by Japanese forces firsthand.", 
    rating=6.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Australia", 
    year=2008
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    