
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="This Means War", 
    year=2012
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="This Means War", 
        year=2012, 
        plot="Two top CIA operatives wage an epic battle against one another after they discover they are dating the same woman.", 
        rating=6.3
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    