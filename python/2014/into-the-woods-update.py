
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Into the Woods", 
    year=2014
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Into the Woods", 
        year=2014, 
        plot="A witch tasks a childless baker and his wife with procuring magical items from classic fairy tales to reverse the curse put on their family tree.", 
        rating=6
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    