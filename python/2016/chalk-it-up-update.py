
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Chalk It Up", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Chalk It Up", 
        year=2016, 
        plot="When a super girly-girl is dumped by her boyfriend; she decides to do everything she can to get him back by building a college gymnastics team, quickly learning that she is capable of a lot more than just getting an MRS degree.", 
        rating=4.8
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    