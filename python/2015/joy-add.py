
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Joy to the database
movies.insert(
    title="Joy", 
    year=2015, 
    plot="Joy is the story of the title character, who rose to become founder and matriarch of a powerful family business dynasty.", 
    rating=6.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Joy", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    