
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Predestination to the database
movies.insert(
    title="Predestination", 
    year=2014, 
    plot="For his final assignment, a top temporal agent must pursue the one criminal that has eluded him throughout time. The chase turns into a unique, surprising and mind-bending exploration of love, fate, identity and time travel taboos.", 
    rating=7.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Predestination", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    