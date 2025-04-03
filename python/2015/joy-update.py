
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Joy", 
    year=2015
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Joy", 
        year=2015, 
        plot="Joy is the story of the title character, who rose to become founder and matriarch of a powerful family business dynasty.", 
        rating=6.6
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    