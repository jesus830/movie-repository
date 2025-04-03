
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Hangover to the database
movies.insert(
    title="The Hangover", 
    year=2009, 
    plot="Three buddies wake up from a bachelor party in Las Vegas, with no memory of the previous night and the bachelor missing. They make their way around the city in order to find their friend before his wedding.", 
    rating=7.8
)

# Confirm that the movie was added
movie = movies.select(
    title="The Hangover", 
    year=2009
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    