
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Silence to the database
movies.insert(
    title="Silence", 
    year=2016, 
    plot="In the 17th century, two Portuguese Jesuit priests travel to Japan in an attempt to locate their mentor, who is rumored to have committed apostasy, and to propagate Catholicism.", 
    rating=7.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Silence", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    