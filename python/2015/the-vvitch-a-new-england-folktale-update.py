
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The VVitch: A New-England Folktale", 
    year=2015
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The VVitch: A New-England Folktale", 
        year=2015, 
        plot="A family in 1630s New England is torn apart by the forces of witchcraft, black magic and possession.", 
        rating=6.8
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    