
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Only for One Night", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Only for One Night", 
        year=2016, 
        plot="A married womans husband with a perfect life cheats with her sister with extreme consequences befalling them all.", 
        rating=4.6
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    