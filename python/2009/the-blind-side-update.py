
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Blind Side", 
    year=2009
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Blind Side", 
        year=2009, 
        plot="The story of Michael Oher, a homeless and traumatized boy who became an All American football player and first round NFL draft pick with the help of a caring woman and her family.", 
        rating=7.7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    