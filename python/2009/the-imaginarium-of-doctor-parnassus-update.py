
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Imaginarium of Doctor Parnassus", 
    year=2009
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Imaginarium of Doctor Parnassus", 
        year=2009, 
        plot="A traveling theater company gives its audience much more than they were expecting.", 
        rating=6.8
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    