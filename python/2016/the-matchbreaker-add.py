
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Matchbreaker to the database
movies.insert(
    title="The Matchbreaker", 
    year=2016, 
    plot="When an idealistic romantic gets fired from his day job, he is offered a "one-time gig" to break up a girl's relationship for her disapproving parents. This "one-time" gig spreads through ... See full summary »", 
    rating=5.5
)

# Confirm that the movie was added
movie = movies.select(
    title="The Matchbreaker", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    