
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add If I Stay to the database
movies.insert(
    title="If I Stay", 
    year=2014, 
    plot="Life changes in an instant for young Mia Hall after a car accident puts her in a coma. During an out-of-body experience, she must decide whether to wake up and live a life far different than she had imagined. The choice is hers if she can go on.", 
    rating=6.8
)

# Confirm that the movie was added
movie = movies.select(
    title="If I Stay", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    