
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Chalk It Up to the database
movies.insert(
    title="Chalk It Up", 
    year=2016, 
    plot="When a super girly-girl is dumped by her boyfriend; she decides to do everything she can to get him back by building a college gymnastics team, quickly learning that she is capable of a lot more than just getting an MRS degree.", 
    rating=4.8
)

# Confirm that the movie was added
movie = movies.select(
    title="Chalk It Up", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    