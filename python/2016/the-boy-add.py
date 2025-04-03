
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Boy to the database
movies.insert(
    title="The Boy", 
    year=2016, 
    plot="An American nanny is shocked that her new English family's boy is actually a life-sized doll. After she violates a list of strict rules, disturbing events make her believe that the doll is really alive.", 
    rating=6
)

# Confirm that the movie was added
movie = movies.select(
    title="The Boy", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    