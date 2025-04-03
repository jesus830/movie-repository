
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Matchbreaker", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Matchbreaker", 
        year=2016, 
        plot="When an idealistic romantic gets fired from his day job, he is offered a "one-time gig" to break up a girl's relationship for her disapproving parents. This "one-time" gig spreads through ... See full summary »", 
        rating=5.5
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    