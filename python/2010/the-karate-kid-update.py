
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Karate Kid", 
    year=2010
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Karate Kid", 
        year=2010, 
        plot="Work causes a single mother to move to China with her young son; in his new home, the boy embraces kung fu, taught to him by a master.", 
        rating=6.2
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    